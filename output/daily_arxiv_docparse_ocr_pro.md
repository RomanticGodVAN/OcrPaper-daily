# OCR / 文档解析研究日报（2026-04-30）

## 报告说明

- 检索源：arXiv API
- 检索查询：`(all:"document parsing" OR all:"document understanding" OR all:"optical character recognition" OR all:OCR OR all:"layout analysis" OR all:"document layout analysis" OR all:"text recognition" OR all:"table recognition" OR all:"form understanding" OR all:"document intelligence" OR all:"page understanding" OR all:"scene text recognition" OR all:"handwritten text recognition" OR all:"information extraction") AND (cat:cs.CV OR cat:cs.AI OR cat:cs.CL OR cat:eess.IV)`
- 生成时间（UTC）：`2026-04-30 04:44:06`
- 大模型综合分析：`关闭`
- 备注：DeepSeek 处理失败：Expecting ',' delimiter: line 77 column 3 (char 3595)

## 三、今日论文概览

1. **The Structured Output Benchmark: A Multi-Source Benchmark for Evaluating Structured Output Quality in Large Language Models**
2. **A Multistage Extraction Pipeline for Long Scanned Financial Documents: An Empirical Study in Industrial KYC Workflows**
3. **OCR-Memory: Optical Context Retrieval for Long-Horizon Agent Memory**
4. **GPT-Image-2 in the Wild: A Twitter Dataset of Self-Reported AI-Generated Images from the First Week of Deployment**

## 八、论文逐篇解析

### 1. The Structured Output Benchmark: A Multi-Source Benchmark for Evaluating Structured Output Quality in Large Language Models

- arXiv: [2604.25359v1](https://arxiv.org/abs/2604.25359v1)
- PDF: [下载链接](https://arxiv.org/pdf/2604.25359v1)
- 作者: Abhinav Kumar Singh, Harsha Vardhan Khurdula, Yoeven D Khemlani, Vineet Agarwal
- 发布时间: 2026-04-28T08:27:01Z
- 分类: cs.CL, cs.AI
- 相关性评分: 22

**原始摘要**

Large Language Models are increasingly being deployed to extract structured data from unstructured
and semi-structured sources: parsing invoices, medical records, and converting PDF documents to
database entries. Yet existing benchmarks for structured output generation either focus on schema
compliance alone, or evaluate value correctness within a single source domain. We introduce SOB (The
Structured Output Benchmark), a multi-source benchmark spanning three source modalities: native
text, images, and audio conversations. All models receive a text-normalized representation of their
context regardless of source modality; this deliberate design isolates structured-output capability
from raw vision or speech-processing quality, ensuring a fair, source-agnostic comparison. Our
benchmark comprises 5,000 text evaluation records derived from multi-hop QA drawn from a
25,091-record full corpus, 209 image records from OCR-processed PDFs across seven document types
including multi-column layouts, dense tables, scanned historical documents, small-print text, and
mathematical typesetting, and 115 audio records from the AMI corpus. Each record pairs a natural-
language question with a JSON schema that the model must follow and a ground-truth answer verified
against the source context. We evaluate 21 frontier and open-weight models across three source
domains and seven metrics. Our results reveal a consistent pattern: models achieve near-perfect
schema compliance, yet the best Value Accuracy, measured by exact leaf-value match, reaches only
83.0% on text, 67.2% on images, and 23.7% on audio, where longer context makes extraction
substantially harder. We release the dataset, evaluation pipeline, and all related code.

---

### 2. A Multistage Extraction Pipeline for Long Scanned Financial Documents: An Empirical Study in Industrial KYC Workflows

- arXiv: [2604.26462v1](https://arxiv.org/abs/2604.26462v1)
- PDF: [下载链接](https://arxiv.org/pdf/2604.26462v1)
- 作者: Yuxuan Han, Yuanxing Zhang, Yushuo Wang, Yichao Jin, Kenneth Zhu Ke, Jingyuan Zhao
- 发布时间: 2026-04-29T09:19:16Z
- 分类: cs.CV
- 相关性评分: 18

**原始摘要**

Structured information extraction from long, multilingual scanned financial documents is a core
requirement in industrial KYC and compliance workflows. These documents are typically non machine
readable, noisy, and visually heterogeneous. They usually span dozens of pages while containing only
sparse task relevant information. Although recent vision-language models achieve strong benchmark
performance, directly applying them end to end to full financial reports often leads to unreliable
extraction under real world conditions. We present a multistage extraction framework that integrates
image preprocessing, multilingual OCR, hybrid page-level retrieval, and compact VLM-based structured
extraction. The design separates page localization from multimodal reasoning, enabling more accurate
extraction from complex multipage documents. We evaluated the framework on 120 production KYC
documents comprising about 3000 multilingual scanned pages. Across multiple OCR-VLM combinations,
the proposed pipeline consistently outperforms direct PDF-to-VLM baselines, improving field-level
accuracy by up to 31.9 percentage points. The best configuration, PaddleOCR with MiniCPM2.6,
achieves 87.27 percent accuracy. Ablation studies show that page-level retrieval is the dominant
factor in performance improvements, particularly for complex financial statements and non-English
documents.

---

### 3. OCR-Memory: Optical Context Retrieval for Long-Horizon Agent Memory

- arXiv: [2604.26622v1](https://arxiv.org/abs/2604.26622v1)
- PDF: [下载链接](https://arxiv.org/pdf/2604.26622v1)
- 作者: Jinze Li, Yang Zhang, Xin Yang, Jiayi Qu, Jinfeng Xu, Shuo Yang, Junhua Ding, Edith Cheuk-Han Ngai
- 发布时间: 2026-04-29T12:49:30Z
- 分类: cs.CL
- 相关性评分: 9

**原始摘要**

Autonomous LLM agents increasingly operate in long-horizon, interactive settings where success
depends on reusing experience accumulated over extended histories. However, existing agent memory
systems are fundamentally constrained by text-context budgets: storing or revisiting raw
trajectories is prohibitively token-expensive, while summarization and text-only retrieval trade
token savings for information loss and fragmented evidence. To address this limitation, we propose
Optical Context Retrieval Memory (OCR-Memory), a memory framework that leverages the visual modality
as a high-density representation of agent experience, enabling retention of arbitrarily long
histories with minimal prompt overhead at retrieval time. Specifically, OCR-Memory renders
historical trajectories into images annotated with unique visual identifiers. OCR-Memory retrieves
stored experience via a \emph{locate-and-transcribe} paradigm that selects relevant regions through
visual anchors and retrieves the corresponding verbatim text, avoiding free-form generation and
reducing hallucination. Experiments on long-horizon agent benchmarks show consistent gains under
strict context limits, demonstrating that optical encoding increases effective memory capacity while
preserving faithful evidence recovery.

---

### 4. GPT-Image-2 in the Wild: A Twitter Dataset of Self-Reported AI-Generated Images from the First Week of Deployment

- arXiv: [2604.25370v1](https://arxiv.org/abs/2604.25370v1)
- PDF: [下载链接](https://arxiv.org/pdf/2604.25370v1)
- 作者: Kidus Zewde, Simiao Ren, Xingyu Shen, Jenny Wu, Yuchen Zhou, Tommy Duong, Zikang Zhang, Ethan Traister
- 发布时间: 2026-04-28T08:35:51Z
- 分类: cs.CV, cs.AI
- 相关性评分: 9

**原始摘要**

The release of GPT-image-2 by OpenAI marks a watershed moment in AI-generated imagery: the boundary
between photographic reality and synthetic content has never been more difficult to discern. We
introduce the GPT-Image-2 Twitter Dataset, the first published dataset of GPT-image-2 generated
images, sourced from publicly available Twitter/X posts in the immediate aftermath of the model's
April 21, 2026 release. Leveraging the Twitter API v2 and a multi-stage curation pipeline spanning
multilingual text heuristics (English, Japanese, and Chinese), browser-automated Twitter "Made with
AI" badge verification, and model name variant matching, we curate 10,217 confirmed GPT-image-2
images from 27,662 collected records over a six-day window. We characterize the dataset across four
analyses: CLIP-based zero-shot subject taxonomy, OCR text legibility (82.0% of images contain
detectable text), face detection (59.2% of images, 22,583 total faces), and semantic clustering (137
CLIP ViT-L/14 clusters). A key negative result is that C2PA content credentials are systematically
stripped by Twitter's CDN on upload, rendering cryptographic provenance verification infeasible for
social-media-sourced AI images. The dataset and all curation code are released publicly.

---
