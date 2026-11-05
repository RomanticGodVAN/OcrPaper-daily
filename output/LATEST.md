# OCR / 文档解析研究日报（2026-11-05）

## 报告说明

- 检索源：arXiv API
- 检索查询：`(all:"document parsing" OR all:"document understanding" OR all:"optical character recognition" OR all:OCR OR all:"layout analysis" OR all:"document layout analysis" OR all:"text recognition" OR all:"table recognition" OR all:"form understanding" OR all:"document intelligence" OR all:"page understanding" OR all:"scene text recognition" OR all:"handwritten text recognition" OR all:"information extraction") AND (cat:cs.CV OR cat:cs.AI OR cat:cs.CL OR cat:eess.IV)`
- 生成时间（UTC）：`2026-11-05 07:53:45`
- 大模型综合分析：`关闭`
- 备注：DeepSeek 处理失败：Expecting property name enclosed in double quotes: line 1 column 4105 (char 4104)

## 三、今日论文概览

1. **OCR in the Foundation Model Era: From Specialist Models to Unified Models**
2. **AmbiHTMLBench: A Benchmark for HTML-based Visually Rich Document parsing**
3. **Rewrite, Then Veto: Rewriter-Agnostic Edit Gating for LLM-Based Post-OCR Correction**
4. **ArcRAG: Agentic Compositional Retrieval over Knowledge Graphs**
5. **EP-LVMQA: Evidence-Preserving Coarse-to-Fine Localization for Low-Quality Long Video Moment Question Answering**

## 八、论文逐篇解析

### 1. OCR in the Foundation Model Era: From Specialist Models to Unified Models

- arXiv: [2611.04874v1](https://arxiv.org/abs/2611.04874v1)
- PDF: [下载链接](https://arxiv.org/pdf/2611.04874v1)
- 作者: Zhiheng Li, Zongyang Ma, Jiaxian Chen, Cheng Cui, Yi Liu, Ziqi Zhang, Chunfeng Yuan, Bing Li, Xiang Bai, Weiming Hu
- 发布时间: 2026-11-03T13:27:22Z
- 分类: cs.CV
- 相关性评分: 34

**原始摘要**

Optical Character Recognition (OCR) is among the oldest and most widely deployed applications of
artificial intelligence. This survey reviews its development, focusing on the Foundation Model Era.
We define OCR through faithful transcription: within a specified visual scope, OCR should completely
reconstruct the text, notation, and document structure observable in the source image, and every
textual, notational, or structural element in the output must be verifiable from visual evidence in
that image. We trace the development from specialist OCR models toward unified models, examining
joint text detection and recognition, structured sequence generation, and the use of pretrained
vision-language models (VLMs). We organize contemporary OCR systems into five coexisting families:
modular toolkits and task-specific models, specialized document VLMs, hybrid workflows, general-
purpose VLMs, and commercial products and managed services. We compare their architectures, data,
and training, examining hallucination and omission, insufficient spatial grounding, and inference
cost in generative OCR. We review evaluation from character and scene text recognition to parsing
individual structural elements and full-page transcription, highlighting gaps in consistent output
definitions, attribution of performance to individual components, and coverage of real capture
conditions and visible content and structure. Finally, we summarize the challenges facing OCR and
discuss directions for future research. We continuously track related work at
https://github.com/zhihengli-casia/Awesome-OCR-in-the-Foundation-Model-Era.

---

### 2. AmbiHTMLBench: A Benchmark for HTML-based Visually Rich Document parsing

- arXiv: [2611.06449v1](https://arxiv.org/abs/2611.06449v1)
- PDF: [下载链接](https://arxiv.org/pdf/2611.06449v1)
- 作者: Boyu Niu, Yingjie Xiong, Shurui Li, Linhan Pang, Yuntong Zhang, Han Wang, Hao Wu, Kai Zuo, Xu Tang, Xuanhe Zhou, Fan Wu
- 发布时间: 2026-11-04T12:51:26Z
- 分类: cs.AI
- 相关性评分: 19

**原始摘要**

Traditional document parsing systems use Markdown as their output representation, which is effective
for linear text but does not fully preserve fine-grained spatial structure, table geometry, visual
hierarchy, or rendering semantics. We show that HTML is advantageous for heterogeneous and layout-
sensitive documents whose representations must remain editable, inspectable, and reusable, and
introduce AmbiHTMLBench to systematically study this setting. In this benchmark, given a real-world
document, a model must recover executable HTML that preserves its content, organization, and visual
appearance. The benchmark contains 1,115 diverse pages with structured annotations and evaluates
predictions in two different ways: The objective protocol aligns ground-truth and predicted rendered
blocks and measures table fidelity, page-level text error, and a two-dimensional layout consistency;
a complementary reference-anchored protocol measures perceived fidelity by aligning LLM judges with
human preferences. Across ten primary multimodal systems, the best objective score is 0.8092, while
the subjective winner is different, demonstrating that automatic decomposition and human-perceived
fidelity capture complementary properties. We further fine-tune a small-parameter expert model and
find that task-specific adaptation yields good performance on document-to-HTML reconstruction task.
These results position AmbiHTMLBench as a diagnostic testbed for building smarter and more logical
document parsing systems.

---

### 3. Rewrite, Then Veto: Rewriter-Agnostic Edit Gating for LLM-Based Post-OCR Correction

- arXiv: [2611.05539v1](https://arxiv.org/abs/2611.05539v1)
- PDF: [下载链接](https://arxiv.org/pdf/2611.05539v1)
- 作者: Jorge Ramón Fonseca Cacho
- 发布时间: 2026-11-03T19:31:36Z
- 分类: cs.CL, cs.CV
- 相关性评分: 10

**原始摘要**

LLMs can repair noisy OCR transcripts of historical documents, but they also change text that was
already correct. We propose EditVeto, a veto gate placed after a full-context LLM rewrite. The
rewrite is character-aligned to the OCR input, its differences are split into blocks, and a
0.6B-parameter gate keeps or reverts each block. An oracle analysis motivates the design: given the
true error locations, per-span generation is worse than no correction, whereas vetoing a full
rewrite's edits helps. Trained on rewrites by two Qwen3 models and evaluated, frozen, on the eight
HIPE-OCRepair-2026 test sets, the gate improves all five rewriters tested, two of them unseen in
training: weighted cMER falls by 0.0026-0.0044 and the preference score rises by 0.15-0.25 (paired
bootstrap, p ~ 0.0002 each). On published competition outputs it lowers cMER for three of four teams
but raises it for the winning run (0.0050 to 0.0065). In a second, disclosed test look, a retrained
gate still improves LoRA-tuned rewriters (cMER -0.0011 to -0.0021), and an ensemble of their gated
edits reaches a cMER of 0.0069 and a preference score of 0.928, mostly through fine-tuning and
pooling rather than gating. Built only on public models and data, it is behind the winner (0.0050)
and tied with the second-ranked run (0.0071), both from the only team using domain pre-training, and
ahead of all other published runs. A third, secondary look shows the unchanged gate improving zero-
shot Qwen3.8-27B (cMER 0.0114 to 0.0108) but only the preference score of its LoRA-tuned version.

---

### 4. ArcRAG: Agentic Compositional Retrieval over Knowledge Graphs

- arXiv: [2611.06481v1](https://arxiv.org/abs/2611.06481v1)
- PDF: [下载链接](https://arxiv.org/pdf/2611.06481v1)
- 作者: Jyotin Goel, Abhinav Arun, Tejas Prakash Agarwal, Bhaskarjit Sarmah, Stefano Pasquali
- 发布时间: 2026-11-04T13:20:51Z
- 分类: cs.CL, cs.AI, cs.IR
- 相关性评分: 3

**原始摘要**

Graph-based retrieval-augmented generation (GraphRAG) answers questions by retrieving over a
knowledge graph built from a corpus. Yet retrieval strategies are designed around the structure
their own construction pipeline produces, and whether they survive a change of construction is
rarely tested. We study this cross-construction portability: whether one retrieval procedure, with
no construction-specific schema, relation names, or retuning, stays effective when the graph is
built differently. We introduce ArcRAG, which induces a query-local graph interface at inference
time (the node labels, relation descriptors, and property keys reachable from the entities a
question names), plans multi-hop traversals against it, and executes and repairs them as Cypher. We
build each of the MuSiQue, HotpotQA, and TriviaQA corpora as a schema-guided graph (typed nodes, a
closed relation set, source provenance) and as an open-information-extraction graph (untyped nodes,
free-text relations), with the retriever's configuration fixed across them. We compare against a
construction-agnostic Direct-Cypher agent, ablate each stage across retry and pass budgets on both
graph families, and compare with results reported for prior GraphRAG systems, most of which design
retrieval together with their own graph construction. Across the two constructions, we find that
retrieval need not be co-designed with the graph: query-time interface induction keeps a
construction-agnostic retriever effective when the construction changes, although construction still
shapes absolute accuracy.

---

### 5. EP-LVMQA: Evidence-Preserving Coarse-to-Fine Localization for Low-Quality Long Video Moment Question Answering

- arXiv: [2611.04913v1](https://arxiv.org/abs/2611.04913v1)
- PDF: [下载链接](https://arxiv.org/pdf/2611.04913v1)
- 作者: Guoning Chen, Zhexun Hu, Yifan Wei, Yixuan Weng, Bin Li, Yufei Zhao
- 发布时间: 2026-11-03T13:53:08Z
- 分类: cs.CV
- 相关性评分: 2

**原始摘要**

Long instructional videos are increasingly used in medical education, industrial training, and
procedural knowledge transfer, yet their evidence is often incomplete or unreliable: subtitles may
be missing, ASR noisy, OCR sparse, and decisive actions briefly shown without narration. Existing
VideoQA systems typically return labels or free-form text, making answer support difficult to
inspect. We study Long Video Moment Question Answering (LVMQA), where a system returns timestamped
answer-supporting evidence. We propose EP-LVMQA, an evidence-preserving coarse-to-fine framework
comprising an Uncertainty-Aware Multimodal Evidence Timeline, a Coarse Evidence Planner, and an
Evidence-Conditioned Fine Localizer. An evidence card transfers planner scores, matched cues,
source-confidence proxies, modality-specific evidence, neighboring context, and a temporal prior
between the latter two modules. On MedVidQA, EP-LVMQA achieves 26.1 R1@0.5 and 31.8 mIoU, improving
the strongest non-ours results by 6.3 and 5.1 points. It raises Suff.@2 and Ver.@2 to 25.4 and 22.6,
gains of 9.5 and 8.8 points. Under matched low-quality perturbations, average relative degradation
is reduced from the strongest non-ours value of 14.6% to 11.1%. On Ego4D-NLQ and QVHighlights, EP-
LVMQA remains broadly comparable to established task-specific localization methods.

---
