# OCR / 文档解析研究日报（2026-05-01）

## 报告说明

- 检索源：arXiv API
- 检索查询：`(all:"document parsing" OR all:"document understanding" OR all:"optical character recognition" OR all:OCR OR all:"layout analysis" OR all:"document layout analysis" OR all:"text recognition" OR all:"table recognition" OR all:"form understanding" OR all:"document intelligence" OR all:"page understanding" OR all:"scene text recognition" OR all:"handwritten text recognition" OR all:"information extraction") AND (cat:cs.CV OR cat:cs.AI OR cat:cs.CL OR cat:eess.IV)`
- 生成时间（UTC）：`2026-05-01 04:57:29`
- 大模型综合分析：`关闭`
- 备注：DeepSeek 处理失败：Expecting ',' delimiter: line 78 column 3 (char 3794)

## 三、今日论文概览

1. **A Multistage Extraction Pipeline for Long Scanned Financial Documents: An Empirical Study in Industrial KYC Workflows**
2. **Linguistically Informed Multimodal Fusion for Vietnamese Scene-Text Image Captioning: Dataset, Graph Framework, and Phonological Attention**
3. **OCR-Memory: Optical Context Retrieval for Long-Horizon Agent Memory**
4. **SpecVQA: A Benchmark for Spectral Understanding and Visual Question Answering in Scientific Images**

## 八、论文逐篇解析

### 1. A Multistage Extraction Pipeline for Long Scanned Financial Documents: An Empirical Study in Industrial KYC Workflows

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

### 2. Linguistically Informed Multimodal Fusion for Vietnamese Scene-Text Image Captioning: Dataset, Graph Framework, and Phonological Attention

- arXiv: [2604.27712v1](https://arxiv.org/abs/2604.27712v1)
- PDF: [下载链接](https://arxiv.org/pdf/2604.27712v1)
- 作者: Nhi Ngoc-Yen Nguyen, Anh-Duc Nguyen, Nghia Hieu Nguyen, Kiet Van Nguyen, Ngan Luu-Thuy Nguyen
- 发布时间: 2026-04-30T10:57:38Z
- 分类: cs.CV, cs.CL
- 相关性评分: 9

**原始摘要**

Scene-text image captioning requires fusing three information streams -- visual features, OCR-
detected text, and linguistic knowledge -- to generate descriptions that faithfully integrate text
visible in images. Existing fusion approaches treat text as language-agnostic, which fails for
Vietnamese: a tonal language where diacritics alter word meaning, OCR errors are pervasive, and word
boundaries are ambiguous. We argue that Vietnamese scene-text captioning demands
\textit{linguistically informed multimodal fusion}, where language-specific structural knowledge is
explicitly incorporated into the fusion mechanism. Motivated from these insights, we propose
\textbf{HSTFG} (Heterogeneous Scene-Text Fusion Graph), a general-purpose graph fusion framework
with learned spatial attention bias, and show through topology analysis that cross-modal graph edges
are harmful for scene-text fusion. Building on this finding, we design \textbf{PhonoSTFG}
(Phonological Scene-Text Fusion Graph) which specializes graph-level fusion for Vietnamese
linguistic reasoning. To support evaluation, we introduce \textbf{ViTextCaps}, the first large-scale
Vietnamese scene-text captioning dataset (\textbf{15{,}729} images with \textbf{74{,}970} captions),
with comprehensive linguistic analysis showing that 52.8\% of the vocabulary is at risk of diacritic
collision.

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

### 4. SpecVQA: A Benchmark for Spectral Understanding and Visual Question Answering in Scientific Images

- arXiv: [2604.28039v1](https://arxiv.org/abs/2604.28039v1)
- PDF: [下载链接](https://arxiv.org/pdf/2604.28039v1)
- 作者: Jialu Shen, Han Lyu, Suyang Zhong, Hanzheng Li, Haoyi Tao, Nan Wang, Changhong Chen, Xi Fang
- 发布时间: 2026-04-30T15:51:10Z
- 分类: cs.AI
- 相关性评分: 6

**原始摘要**

Spectra are a prevalent yet highly information-dense form of scientific imagery, presenting
substantial challenges to multimodal large language models (MLLMs) due to their unstructured and
domain-specific characteristics. Here we introduce SpecVQA, a professional scientific-image
benchmark for evaluating multimodal models on scientific spectral understanding, covering 7
representative spectrum types with expert-annotated question-answer pairs. The aim comprises two
aspects: spectra scientific QA evaluation and corresponding underlying task evaluation. SpecVQA
contains 620 figures and 3100 QA pairs curated from peer-reviewed literature, targeting both direct
information extraction and domain-specific reasoning. To effectively reduce token length while
preserving essential curve characteristics, we propose a spectral data sampling and interpolation
reconstruction approach. Ablation studies further confirm that the approach achieves substantial
performance improvements on the proposed benchmark. We test the capability of prominent MLLMs in
scientific spectral understanding on our benchmark and present a leaderboard. This work represents
an essential step toward enhancing spectral understanding in multimodal large models and suggests
promising directions for extending visual-language models to broader scientific research and data
analysis.

---
