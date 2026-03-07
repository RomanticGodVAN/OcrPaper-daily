# OCR / 文档解析 arXiv 自动日报代理（Pro）

这是一个面向 **OCR、文档解析、版面分析、表格识别、表单理解、文档理解** 的自动化研究代理。

它每天会自动：

1. 从 arXiv 抓取最近几天的新论文
2. 通过规则筛选和相关性打分，保留 OCR / 文档解析方向的高相关论文
3. 调用 DeepSeek API 对每篇论文生成：
   - 中文摘要
   - 核心创新概述
   - 创新点拆解
   - 当前局限
   - 后续可改进方向
   - 工程启发
4. 再做一次**日报级综合总结**，输出：
   - 今日执行摘要
   - 今日趋势判断
   - 今天论文里的主要创新点
   - 后续 OCR 领域值得推进的改进方向
   - 工程落地启发
   - 优先关注论文
5. 自动生成 Markdown / JSON 并提交回 GitHub 仓库

---

## 目录结构

```text
.
├── .github/workflows/daily-arxiv-ocr-pro.yml
├── output/
│   ├── archive/
│   ├── daily_arxiv_docparse_ocr_pro.md
│   ├── daily_arxiv_docparse_ocr_pro.json
│   └── LATEST.md
├── requirements.txt
├── README.md
└── scripts/
    └── fetch_arxiv_daily_pro.py
```

---

## 这版比增强版多了什么

这版重点补上了你要的三个能力：

### 1. 自动总结每天 OCR 文章的创新点
不是只给单篇摘要，而是做两层总结：
- 单篇论文的创新点拆解
- 当天论文整体的共性创新总结

### 2. 自动推断 OCR 后续改进方向
不是泛泛说“模型更强、数据更多”，而是要求模型围绕：
- 复杂文档结构建模
- 跨页面 / 长文档建模
- 低资源文字与手写体
- 多语言、多模态、表格、公式、图文混排
- 效率、鲁棒性、数据构造、评测缺口
这些方向输出更具体的后续研究建议。

### 3. 每天给一个完整研究日报
日报顶部不再只是“论文列表”，而是完整结构：
- 今日执行摘要
- 今日趋势判断
- 主要创新点
- 后续值得推进方向
- 工程落地启发
- 重点论文 watchlist
- 逐篇解析

---

## 你需要准备的东西

### 1) GitHub 仓库
把本项目文件放进你的仓库。

### 2) DeepSeek API Key
在仓库中添加 Secret：

- `Settings` → `Secrets and variables` → `Actions`
- 新建：`DEEPSEEK_API_KEY`

---

## 使用方式

### 本地运行

```bash
export DEEPSEEK_API_KEY="你的key"
python scripts/fetch_arxiv_daily_pro.py
```

生成文件：

- `output/daily_arxiv_docparse_ocr_pro.md`
- `output/daily_arxiv_docparse_ocr_pro.json`
- `output/LATEST.md`
- `output/archive/YYYY-MM-DD.md`

### GitHub Actions 自动运行

工作流文件已经准备好：

```yaml
.github/workflows/daily-arxiv-ocr-pro.yml
```

它支持：
- `schedule`：每日自动执行
- `workflow_dispatch`：手动触发

---

## 环境变量

| 变量名 | 默认值 | 说明 |
|---|---:|---|
| `DEEPSEEK_API_KEY` | 空 | DeepSeek API Key |
| `DEEPSEEK_MODEL` | `deepseek-chat` | 使用的模型 |
| `ARXIV_MAX_RESULTS` | `100` | arXiv 候选论文数 |
| `ARXIV_DAYS_BACK` | `3` | 只看最近几天论文 |
| `ARXIV_FINAL_LIMIT` | `12` | 最终日报保留条数 |
| `FAIL_ON_LLM_ERROR` | `false` | DeepSeek 失败时是否让任务失败 |
| `ARXIV_TERMS` | 内置默认值 | 自定义关键词，使用 `|` 分隔 |
| `ARXIV_CATEGORIES` | 内置默认值 | 自定义分类，使用 `|` 分隔 |

示例：

```bash
export ARXIV_TERMS='"document parsing"|"optical character recognition"|OCR|"table recognition"|"handwritten text recognition"'
export ARXIV_CATEGORIES='cs.CV|cs.AI|cs.CL|eess.IV'
python scripts/fetch_arxiv_daily_pro.py
```

---

## 日报输出结构

Markdown 日报分成这些板块：

1. 报告说明
2. 今日执行摘要
3. 今日趋势判断
4. 今日论文概览
5. 今天 OCR / 文档解析论文里的主要创新点
6. 后续 OCR 领域值得推进的改进方向
7. 工程落地启发
8. 优先关注论文
9. 论文逐篇解析

每篇论文会包含：
- 标题 / 链接 / 作者 / 日期 / 分类 / 评分
- 中文摘要
- 核心创新概述
- 创新点拆解
- 当前局限
- 后续可改进方向
- 工程启发
- 为什么值得关注
- 原始摘要

JSON 输出则适合你后续接 RAG、知识库、飞书机器人、数据库或前端页面。

---

## 你后面还能继续加的功能

这套 Pro 版已经是“完整日报代理”的雏形了，后面还可以继续叠：

- 每周综述：自动汇总过去 7 天的日报，生成周报
- 方向分桶：OCR / 表格 / 版面 / 文档 VLM / 手写体 / 多语言
- 飞书 / 企业微信 / Telegram 推送
- 只跟踪你指定作者、机构、关键词
- 自动打标签：benchmark、dataset、training recipe、architecture、efficiency、multilingual
- 把每日 JSON 自动入库，做趋势统计面板

---

## 部署建议

最小部署流程：

```bash
git init
mkdir -p .github/workflows scripts output
# 复制本项目文件

git add .
git commit -m "init ocr research daily pro agent"
git branch -M main
git remote add origin <你的仓库地址>
git push -u origin main
```

然后到 GitHub 仓库配置 `DEEPSEEK_API_KEY`，去 Actions 页面手动运行一次即可。
