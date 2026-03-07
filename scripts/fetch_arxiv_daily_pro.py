#!/usr/bin/env python3
from __future__ import annotations

import datetime as dt
import html
import json
import os
import re
import sys
import textwrap
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable

ARXIV_API = "http://export.arxiv.org/api/query"
DEFAULT_TERMS = [
    '"document parsing"',
    '"document understanding"',
    '"optical character recognition"',
    'OCR',
    '"layout analysis"',
    '"document layout analysis"',
    '"text recognition"',
    '"table recognition"',
    '"form understanding"',
    '"document intelligence"',
    '"page understanding"',
    '"scene text recognition"',
    '"handwritten text recognition"',
    '"information extraction"',
]
DEFAULT_CATEGORIES = ["cs.CV", "cs.AI", "cs.CL", "eess.IV"]
NS = {"atom": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}

KEYWORD_WEIGHTS: list[tuple[str, int]] = [
    ("ocr", 6),
    ("optical character recognition", 7),
    ("text recognition", 5),
    ("scene text", 4),
    ("document", 4),
    ("layout", 4),
    ("table", 3),
    ("form", 3),
    ("receipt", 2),
    ("invoice", 2),
    ("pdf", 2),
    ("parsing", 5),
    ("reading order", 3),
    ("multimodal document", 5),
    ("document intelligence", 5),
    ("information extraction", 3),
    ("handwritten", 2),
    ("chart understanding", 2),
]

NEGATIVE_WEIGHTS: list[tuple[str, int]] = [
    ("speech recognition", -7),
    ("audio", -4),
    ("asr", -7),
    ("robot", -2),
    ("autonomous driving", -4),
    ("protein", -4),
    ("medical image segmentation", -3),
]


@dataclass
class Paper:
    title: str
    summary: str
    link: str
    pdf_url: str
    authors: list[str]
    published: str
    updated: str
    categories: list[str]
    arxiv_id: str
    score: int = 0
    topic_tags: list[str] | None = None
    zh_summary: str | None = None
    novelty: str | None = None
    innovation_points: list[str] | None = None
    limitations: str | None = None
    improvement_directions: list[str] | None = None
    engineering_value: str | None = None
    why_relevant: str | None = None


@dataclass
class DailySynthesis:
    executive_summary: str = ""
    trend_summary: str = ""
    common_innovations: list[str] | None = None
    future_directions: list[str] | None = None
    engineering_takeaways: list[str] | None = None
    watchlist: list[dict] | None = None


def getenv_bool(name: str, default: bool = False) -> bool:
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "y", "on"}


def normalize_text(text: str) -> str:
    text = html.unescape(text or "")
    text = re.sub(r"\s+", " ", text).strip()
    return text


def score_paper(title: str, summary: str, categories: Iterable[str]) -> int:
    text = f"{title} {summary} {' '.join(categories)}".lower()
    score = 0
    for key, weight in KEYWORD_WEIGHTS:
        if key in text:
            score += weight
    for key, weight in NEGATIVE_WEIGHTS:
        if key in text:
            score += weight
    return score


def build_query(terms: list[str], categories: list[str]) -> str:
    term_query = " OR ".join(f"all:{t}" for t in terms)
    cat_query = " OR ".join(f"cat:{c}" for c in categories)
    return f"({term_query}) AND ({cat_query})"


def fetch_arxiv(query: str, max_results: int, sort_by: str = "submittedDate") -> list[Paper]:
    params = {
        "search_query": query,
        "start": 0,
        "max_results": max_results,
        "sortBy": sort_by,
        "sortOrder": "descending",
    }
    url = f"{ARXIV_API}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "arxiv-ocr-daily-pro/1.0 (https://github.com/)"},
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = resp.read()

    root = ET.fromstring(data)
    entries = root.findall("atom:entry", NS)
    papers: list[Paper] = []
    for entry in entries:
        title = normalize_text(entry.findtext("atom:title", default="", namespaces=NS))
        summary = normalize_text(entry.findtext("atom:summary", default="", namespaces=NS))
        published = normalize_text(entry.findtext("atom:published", default="", namespaces=NS))
        updated = normalize_text(entry.findtext("atom:updated", default="", namespaces=NS))
        authors = [normalize_text(a.findtext("atom:name", default="", namespaces=NS)) for a in entry.findall("atom:author", NS)]
        categories = [c.attrib.get("term", "") for c in entry.findall("atom:category", NS)]
        link = ""
        pdf_url = ""
        for link_node in entry.findall("atom:link", NS):
            href = link_node.attrib.get("href", "")
            title_attr = link_node.attrib.get("title", "")
            rel = link_node.attrib.get("rel", "")
            type_ = link_node.attrib.get("type", "")
            if rel == "alternate":
                link = href
            if title_attr == "pdf" or type_ == "application/pdf":
                pdf_url = href
        id_text = normalize_text(entry.findtext("atom:id", default="", namespaces=NS))
        arxiv_id = id_text.rsplit("/", 1)[-1]
        papers.append(
            Paper(
                title=title,
                summary=summary,
                link=link,
                pdf_url=pdf_url,
                authors=authors,
                published=published,
                updated=updated,
                categories=categories,
                arxiv_id=arxiv_id,
                score=score_paper(title, summary, categories),
            )
        )
    return papers


def dedup_papers(papers: list[Paper]) -> list[Paper]:
    seen: set[str] = set()
    result: list[Paper] = []
    for p in papers:
        key = re.sub(r"\W+", "", p.title.lower())
        if key in seen:
            continue
        seen.add(key)
        result.append(p)
    return result


def parse_iso_date(s: str) -> dt.datetime:
    return dt.datetime.fromisoformat(s.replace("Z", "+00:00"))


def filter_recent(papers: list[Paper], days_back: int) -> list[Paper]:
    cutoff = dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=days_back)
    out: list[Paper] = []
    for p in papers:
        try:
            published = parse_iso_date(p.published)
        except Exception:
            continue
        if published >= cutoff:
            out.append(p)
    return out


def choose_top_papers(papers: list[Paper], limit: int) -> list[Paper]:
    papers = sorted(papers, key=lambda p: (p.score, p.published, p.updated), reverse=True)
    return papers[:limit]


def truncate(text: str, max_len: int = 2200) -> str:
    text = normalize_text(text)
    return text if len(text) <= max_len else text[: max_len - 3] + "..."


def _post_json(url: str, body: dict, api_key: str) -> dict:
    req = urllib.request.Request(
        url,
        data=json.dumps(body).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=240) as resp:
        return json.loads(resp.read().decode("utf-8"))


def call_deepseek_json(messages: list[dict], api_key: str, model: str, max_tokens: int = 5000) -> dict | list:
    body = {
        "model": model,
        "messages": messages,
        "response_format": {"type": "json_object"},
        "stream": False,
        "max_tokens": max_tokens,
    }
    response = _post_json("https://api.deepseek.com/chat/completions", body=body, api_key=api_key)
    content = response["choices"][0]["message"]["content"]
    parsed = json.loads(content)
    return parsed


def enrich_papers_with_deepseek(papers: list[Paper], api_key: str, model: str, batch_size: int = 6) -> None:
    for i in range(0, len(papers), batch_size):
        batch = papers[i : i + batch_size]
        payload_items = [
            {
                "idx": idx,
                "title": p.title,
                "summary": truncate(p.summary, 1600),
                "authors": p.authors[:8],
                "categories": p.categories,
            }
            for idx, p in enumerate(batch, start=1)
        ]
        system_prompt = (
            "你是一个严谨的 OCR / 文档解析学术情报助手。"
            "你需要阅读论文标题和摘要，输出中文技术情报。"
            "只返回 JSON，不要输出任何额外文字。"
            "JSON 顶层字段必须是 items，且 items 是数组。"
            "每篇论文返回字段：idx, zh_summary, novelty, innovation_points, limitations, improvement_directions, engineering_value, why_relevant, topic_tags。"
            "innovation_points 和 improvement_directions、topic_tags 必须是数组。"
            "创新点强调方法设计、训练范式、数据、架构、任务定义。"
            "改进方向强调后续 OCR 研究可继续推进的方向，避免空泛套话。"
            "表述要克制、专业、适合日报。"
        )
        user_prompt = "请基于下面论文信息输出 JSON：\n" + json.dumps(payload_items, ensure_ascii=False)
        parsed = call_deepseek_json(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            api_key=api_key,
            model=model,
            max_tokens=6000,
        )
        items = parsed["items"] if isinstance(parsed, dict) and isinstance(parsed.get("items"), list) else []
        mapping = {int(item["idx"]): item for item in items if isinstance(item, dict) and "idx" in item}
        for j, paper in enumerate(batch, start=1):
            item = mapping.get(j)
            if not item:
                continue
            paper.zh_summary = normalize_text(str(item.get("zh_summary", ""))) or None
            paper.novelty = normalize_text(str(item.get("novelty", ""))) or None
            paper.limitations = normalize_text(str(item.get("limitations", ""))) or None
            paper.engineering_value = normalize_text(str(item.get("engineering_value", ""))) or None
            paper.why_relevant = normalize_text(str(item.get("why_relevant", ""))) or None
            innovation_points = item.get("innovation_points", [])
            if isinstance(innovation_points, list):
                paper.innovation_points = [normalize_text(str(x)) for x in innovation_points if normalize_text(str(x))]
            future = item.get("improvement_directions", [])
            if isinstance(future, list):
                paper.improvement_directions = [normalize_text(str(x)) for x in future if normalize_text(str(x))]
            tags = item.get("topic_tags", [])
            if isinstance(tags, list):
                paper.topic_tags = [normalize_text(str(x)) for x in tags if normalize_text(str(x))]
        time.sleep(1.1)


def synthesize_daily_report(papers: list[Paper], api_key: str, model: str) -> DailySynthesis:
    payload = []
    for idx, p in enumerate(papers, start=1):
        payload.append(
            {
                "idx": idx,
                "title": p.title,
                "published": p.published,
                "tags": p.topic_tags or [],
                "zh_summary": p.zh_summary or "",
                "novelty": p.novelty or "",
                "innovation_points": p.innovation_points or [],
                "limitations": p.limitations or "",
                "improvement_directions": p.improvement_directions or [],
                "engineering_value": p.engineering_value or "",
            }
        )

    system_prompt = (
        "你是一个负责输出 OCR / 文档解析研究日报的资深研究经理。"
        "请基于给定论文清单，输出一份面向研究和工程团队的日报综合结论。"
        "只返回 JSON，不要附加解释。"
        "JSON 顶层字段包括：executive_summary, trend_summary, common_innovations, future_directions, engineering_takeaways, watchlist。"
        "common_innovations、future_directions、engineering_takeaways 是数组，每项一句话。"
        "watchlist 是数组，每项包含 title 和 watch_reason。"
        "future_directions 必须尽量具体，围绕 OCR 和文档解析下一步值得做的方向。"
        "避免空话，禁止夸张。"
    )
    user_prompt = "请根据以下论文情报，生成今天的完整 OCR / 文档解析研究日报结论：\n" + json.dumps(payload, ensure_ascii=False)
    parsed = call_deepseek_json(
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        api_key=api_key,
        model=model,
        max_tokens=5000,
    )
    if not isinstance(parsed, dict):
        raise RuntimeError("DeepSeek 综合日报输出不是 JSON 对象")
    return DailySynthesis(
        executive_summary=normalize_text(str(parsed.get("executive_summary", ""))),
        trend_summary=normalize_text(str(parsed.get("trend_summary", ""))),
        common_innovations=[normalize_text(str(x)) for x in parsed.get("common_innovations", []) if normalize_text(str(x))],
        future_directions=[normalize_text(str(x)) for x in parsed.get("future_directions", []) if normalize_text(str(x))],
        engineering_takeaways=[normalize_text(str(x)) for x in parsed.get("engineering_takeaways", []) if normalize_text(str(x))],
        watchlist=parsed.get("watchlist", []) if isinstance(parsed.get("watchlist"), list) else [],
    )


def safe_enrich_and_summarize(papers: list[Paper], api_key: str | None, model: str) -> tuple[bool, str | None, DailySynthesis | None]:
    if not api_key:
        return False, "未提供 DEEPSEEK_API_KEY，跳过大模型摘要和综合日报。", None
    try:
        enrich_papers_with_deepseek(papers, api_key=api_key, model=model)
        synthesis = synthesize_daily_report(papers, api_key=api_key, model=model)
        return True, None, synthesis
    except Exception as e:
        return False, f"DeepSeek 处理失败：{e}", None


def render_markdown(papers: list[Paper], synthesis: DailySynthesis | None, report_date: str, query: str, llm_enabled: bool, llm_note: str | None) -> str:
    lines: list[str] = []
    lines.append(f"# OCR / 文档解析研究日报（{report_date}）")
    lines.append("")
    lines.append("## 报告说明")
    lines.append("")
    lines.append("- 检索源：arXiv API")
    lines.append(f"- 检索查询：`{query}`")
    lines.append(f"- 生成时间（UTC）：`{dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%d %H:%M:%S')}`")
    lines.append(f"- 大模型综合分析：`{'开启' if llm_enabled else '关闭'}`")
    if llm_note:
        lines.append(f"- 备注：{llm_note}")
    lines.append("")

    if not papers:
        lines.append("今天没有筛到符合条件的新论文。")
        return "\n".join(lines).strip() + "\n"

    if synthesis and synthesis.executive_summary:
        lines.append("## 一、今日执行摘要")
        lines.append("")
        lines.append(f"> {synthesis.executive_summary}")
        lines.append("")

    if synthesis and synthesis.trend_summary:
        lines.append("## 二、今日趋势判断")
        lines.append("")
        lines.append(synthesis.trend_summary)
        lines.append("")

    lines.append("## 三、今日论文概览")
    lines.append("")
    for idx, p in enumerate(papers, start=1):
        tags = f" | 标签：{'、'.join(p.topic_tags)}" if p.topic_tags else ""
        lines.append(f"{idx}. **{p.title}**{tags}")
    lines.append("")

    if synthesis and synthesis.common_innovations:
        lines.append("## 四、今天 OCR / 文档解析论文里的主要创新点")
        lines.append("")
        for item in synthesis.common_innovations:
            lines.append(f"- {item}")
        lines.append("")

    if synthesis and synthesis.future_directions:
        lines.append("## 五、后续 OCR 领域值得推进的改进方向")
        lines.append("")
        for item in synthesis.future_directions:
            lines.append(f"- {item}")
        lines.append("")

    if synthesis and synthesis.engineering_takeaways:
        lines.append("## 六、工程落地启发")
        lines.append("")
        for item in synthesis.engineering_takeaways:
            lines.append(f"- {item}")
        lines.append("")

    if synthesis and synthesis.watchlist:
        lines.append("## 七、优先关注论文")
        lines.append("")
        for item in synthesis.watchlist:
            if not isinstance(item, dict):
                continue
            title = normalize_text(str(item.get("title", "")))
            reason = normalize_text(str(item.get("watch_reason", "")))
            if title:
                lines.append(f"- **{title}**：{reason}")
        lines.append("")

    lines.append("## 八、论文逐篇解析")
    lines.append("")
    for idx, p in enumerate(papers, start=1):
        lines.append(f"### {idx}. {p.title}")
        lines.append("")
        lines.append(f"- arXiv: [{p.arxiv_id}]({p.link})")
        if p.pdf_url:
            lines.append(f"- PDF: [下载链接]({p.pdf_url})")
        lines.append(f"- 作者: {', '.join(p.authors)}")
        lines.append(f"- 发布时间: {p.published}")
        lines.append(f"- 分类: {', '.join(p.categories)}")
        lines.append(f"- 相关性评分: {p.score}")
        if p.topic_tags:
            lines.append(f"- 主题标签: {'、'.join(p.topic_tags)}")
        lines.append("")
        if p.zh_summary:
            lines.append("**中文摘要**")
            lines.append("")
            lines.append(f"> {p.zh_summary}")
            lines.append("")
        if p.novelty:
            lines.append("**核心创新概述**")
            lines.append("")
            lines.append(f"> {p.novelty}")
            lines.append("")
        if p.innovation_points:
            lines.append("**创新点拆解**")
            lines.append("")
            for item in p.innovation_points:
                lines.append(f"- {item}")
            lines.append("")
        if p.limitations:
            lines.append("**当前局限**")
            lines.append("")
            lines.append(f"> {p.limitations}")
            lines.append("")
        if p.improvement_directions:
            lines.append("**后续可改进方向**")
            lines.append("")
            for item in p.improvement_directions:
                lines.append(f"- {item}")
            lines.append("")
        if p.engineering_value:
            lines.append("**工程启发**")
            lines.append("")
            lines.append(f"> {p.engineering_value}")
            lines.append("")
        if p.why_relevant:
            lines.append("**为什么值得关注**")
            lines.append("")
            lines.append(f"> {p.why_relevant}")
            lines.append("")
        lines.append("**原始摘要**")
        lines.append("")
        lines.append(textwrap.fill(p.summary, width=100))
        lines.append("")
        lines.append("---")
        lines.append("")

    return "\n".join(lines).strip() + "\n"


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def write_json(path: Path, papers: list[Paper], synthesis: DailySynthesis | None, meta: dict) -> None:
    data = {
        "meta": meta,
        "synthesis": asdict(synthesis) if synthesis else None,
        "papers": [asdict(p) for p in papers],
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    output_dir = root / "output"
    archive_dir = output_dir / "archive"
    report_date = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d")
    output_md = Path(os.getenv("OUTPUT_MD", output_dir / "daily_arxiv_docparse_ocr_pro.md"))
    output_json = Path(os.getenv("OUTPUT_JSON", output_dir / "daily_arxiv_docparse_ocr_pro.json"))

    terms = [x.strip() for x in os.getenv("ARXIV_TERMS", "").split("|") if x.strip()] or DEFAULT_TERMS
    categories = [x.strip() for x in os.getenv("ARXIV_CATEGORIES", "").split("|") if x.strip()] or DEFAULT_CATEGORIES
    max_results = int(os.getenv("ARXIV_MAX_RESULTS", "100"))
    days_back = int(os.getenv("ARXIV_DAYS_BACK", "3"))
    final_limit = int(os.getenv("ARXIV_FINAL_LIMIT", "12"))
    deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")
    deepseek_model = os.getenv("DEEPSEEK_MODEL", "deepseek-chat")
    fail_on_llm_error = getenv_bool("FAIL_ON_LLM_ERROR", default=False)

    query = build_query(terms, categories)
    papers = fetch_arxiv(query=query, max_results=max_results)
    papers = dedup_papers(papers)
    papers = filter_recent(papers, days_back=days_back)
    papers = [p for p in papers if p.score > 0]
    papers = choose_top_papers(papers, limit=final_limit)

    llm_enabled, llm_note, synthesis = safe_enrich_and_summarize(papers, api_key=deepseek_api_key, model=deepseek_model)
    if llm_note and fail_on_llm_error and deepseek_api_key:
        raise RuntimeError(llm_note)

    md = render_markdown(papers, synthesis, report_date, query, llm_enabled, llm_note)
    meta = {
        "report_date": report_date,
        "generated_at_utc": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M:%S"),
        "query": query,
        "llm_enabled": llm_enabled,
        "llm_note": llm_note,
        "count": len(papers),
    }
    write_file(output_md, md)
    write_json(output_json, papers, synthesis, meta)
    write_file(output_dir / "LATEST.md", md)
    write_file(archive_dir / f"{report_date}.md", md)

    print(f"Wrote markdown to: {output_md}")
    print(f"Wrote json to: {output_json}")
    print(f"Archived markdown to: {archive_dir / f'{report_date}.md'}")
    print(f"Papers selected: {len(papers)}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        print("Interrupted", file=sys.stderr)
        raise SystemExit(130)
