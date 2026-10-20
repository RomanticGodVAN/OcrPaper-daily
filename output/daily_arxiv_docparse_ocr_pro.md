# OCR / 文档解析研究日报（2026-10-20）

## 报告说明

- 检索源：arXiv API
- 检索查询：`(all:"document parsing" OR all:"document understanding" OR all:"optical character recognition" OR all:OCR OR all:"layout analysis" OR all:"document layout analysis" OR all:"text recognition" OR all:"table recognition" OR all:"form understanding" OR all:"document intelligence" OR all:"page understanding" OR all:"scene text recognition" OR all:"handwritten text recognition" OR all:"information extraction") AND (cat:cs.CV OR cat:cs.AI OR cat:cs.CL OR cat:eess.IV)`
- 生成时间（UTC）：`2026-10-20 05:59:31`
- 大模型综合分析：`关闭`
- 备注：DeepSeek 处理失败：Expecting ',' delimiter: line 1 column 6252 (char 6251)

## 三、今日论文概览

1. **GAIDA: Generative AI for Human-in-the-Loop Document Annotation**
2. **Evaluating Cloud and Self-Hosted OCR Systems for Arabic, English, and French Documents: Bounding Box Detection, Text Recognition, and Mathematical Expression Recognition**
3. **Design Considerations in Low-Resource Archival OCR: A Case Study in Lakota**
4. **One Fact, Many Places: Redundant Evidence in Long Visual Documents Breaks Single-Gold Evaluation of Retrieval, Citation and Attribution**
5. **DeOverlay: A Benchmark and Source-Anchored Flow for Video Overlay Removal**
6. **CIS-Transolver: A Cross-Layer Incremental-State Neural Operator for Fine-Scale Automotive Aerodynamic Flow Prediction**
7. **Long-form Video-to-Text Summarization using Recursive Language Models**

## 八、论文逐篇解析

### 1. GAIDA: Generative AI for Human-in-the-Loop Document Annotation

- arXiv: [2610.26362v1](https://arxiv.org/abs/2610.26362v1)
- PDF: [下载链接](https://arxiv.org/pdf/2610.26362v1)
- 作者: Islam Mesabah, Ali Elhosary, Priyabanta Sandulu, Darko Obradovic, Sebastian J. Vollmer
- 发布时间: 2026-10-19T13:22:13Z
- 分类: cs.AI
- 相关性评分: 28

**原始摘要**

Document annotation is a fundamental yet labor-intensive step in building document information
extraction systems. While Optical Character Recognition (OCR) and Large Language Models (LLMs) can
automate parts of this process, we argue that annotation systems should be judged not by how
completely they remove human effort, but by how effectively they redirect it toward review and
correction. We propose a modular human-in-the-loop architecture that integrates OCR-based
extraction, LLM-based semantic pre-annotation, and human validation in a single editable workflow,
and present \textbf{GAIDA}, a research prototype serving as its reference implementation. GAIDA
supports interchangeable OCR engines, LLM backends, and prompt configurations, and enables stage-
specific measurement of annotation effort. In an initial single-annotator, stage-specific study on
the FUNSD scanned-form and WildReceipt retail-receipt benchmarks, OCR assistance reduced region-
creation and transcription time by up to \textbf{80.9\%}, and reviewing LLM pre-annotations reduced
semantic-labeling time by up to \textbf{73.7\%}, despite imperfect pre-annotations of 78.86\% and
86.98\% Micro F1 on FUNSD and WildReceipt, respectively. Finally, we reuse the same implementation,
adapting only OCR and prompt configuration, to build and openly release \textbf{AraReceipt}, a
manually annotated dataset of 100 Arabic receipt images labeled with 25 key-information classes. The
results indicate that imperfect automated outputs provide practical value when presented as editable
suggestions under human control.

---

### 2. Evaluating Cloud and Self-Hosted OCR Systems for Arabic, English, and French Documents: Bounding Box Detection, Text Recognition, and Mathematical Expression Recognition

- arXiv: [2610.25235v1](https://arxiv.org/abs/2610.25235v1)
- PDF: [下载链接](https://arxiv.org/pdf/2610.25235v1)
- 作者: Jumana Alsubhi, Ahmed Alhusayni, Abdulrahman Gharawi, Israa Hamdine, Khadija Alansari, Alshaymaa Allahim, Lamees Alhumaid, Ahmad Shabana
- 发布时间: 2026-10-18T12:54:44Z
- 分类: cs.CV
- 相关性评分: 23

**原始摘要**

Choosing an OCR system for a multilingual archive requires balancing accuracy against deployment
constraints. This study compares cloud and self-hosted systems on three tasks: bounding box
detection on 48 Arabic, English, and French pages, text recognition on 315 pages across nine
document types, and mathematical expression recognition on 83 English and Arabic samples. Detection
was assessed by page-level visual grades, text by character error rate (CER) against a Gemini-
generated reference transcription, and mathematics by scores against known answers. Main estimates
are accompanied by 95% intervals and paired comparisons. Google Document AI and Surya produced Good
line boxes on 47 of 48 (98%) and 46 of 48 (96%) pages. Datalab, Azure Document Intelligence, and
Document AI had mean CERs of 0.145-0.152, with no difference detected in unadjusted paired
comparisons. Surya had the lowest mean CER among self-hosted systems (0.199). No mathematical test
had a statistically clear leader. Strict checks showed that near-perfect page scores could conceal a
replaced Arabic variable or Eastern Arabic digits rewritten in Western form. Reliable evaluation
therefore requires uncertainty estimates, structural checks, and notation-specific tests in addition
to aggregate recognition scores.

---

### 3. Design Considerations in Low-Resource Archival OCR: A Case Study in Lakota

- arXiv: [2610.25440v1](https://arxiv.org/abs/2610.25440v1)
- PDF: [下载链接](https://arxiv.org/pdf/2610.25440v1)
- 作者: Téa Wright, Laura X. Ma, Claudia Iron Hawk, Hannah J. Haynie, Alexis Palmer, Alane Suhr, Abteen Ebrahimi, Katharina von der Wense
- 发布时间: 2026-10-18T18:02:32Z
- 分类: cs.CL
- 相关性评分: 20

**原始摘要**

Building and expanding access to digital archives supports language reclamation and creates lasting
resources for community revitalization. Designing effective tools to support these efforts requires
taking into account the community-, language-, and document-specific context. We investigate how
small ($\leq$3B) vision-language models (VLMs) can be adapted as optical character recognition (OCR)
tools for Lakota, a North American Indigenous language. In addition to benchmarking modeling
approaches, we inspect four practical facets of low-resource archival OCR that arise in previous
work and conversations with community members: constrained training budgets, segmentation noise,
scan degradation, and orthographic variance. We demonstrate that fine-tuning VLMs for OCR post-
correction on 35 pages of transcribed data decreases character error rate (CER) from 17.1 to 3.9\%
on a bilingual corpus, and find that training only with nine pages increases CER by only 1.1\% over
this. However, evaluating under realistic automatic segmentation nearly doubles the CER of the best-
performing models, stressing the importance of taking realistic use cases into account. We hope this
work encourages future research on developing language technologies grounded in the workflows and
constraints of ongoing revitalization efforts.

---

### 4. One Fact, Many Places: Redundant Evidence in Long Visual Documents Breaks Single-Gold Evaluation of Retrieval, Citation and Attribution

- arXiv: [2610.26401v1](https://arxiv.org/abs/2610.26401v1)
- PDF: [下载链接](https://arxiv.org/pdf/2610.26401v1)
- 作者: Xiaokang Yuan, Binhui Yao, Luwei Yang, Ruimin Chen, Zeng Wang
- 发布时间: 2026-10-19T13:43:29Z
- 分类: cs.CV
- 相关性评分: 13

**原始摘要**

Document understanding is increasingly judged on where an answer comes from, scored against
annotated gold locations as if each fact lived in one place. In long visual documents, a fact often
lives in several places: a chart value is restated in the text, a key figure reappears in the
summary. We ask how often such copies occur in standard benchmarks and what they do to evaluation.
We annotate 420 questions from MMLongBench-Doc and MMDocRAG with the locations that independently
establish each required fact, checked by two independent reviewers. Copies are common and often
cross-modal: 19.5% of MMLongBench-Doc test questions have a strict copy outside the gold, and in 28%
of MMDocRAG questions a non-gold candidate alone supplies a required fact. Single-gold scoring then
fails in three predictable ways. A retriever that finds a copy is scored as a miss: page recall@1 of
text and visual retrievers is underestimated by 13-24 points on questions with a cross-page copy. A
model that cites a copy is scored as citing wrongly: crediting equivalent evidence reverses 11% of
pairwise orderings among 65 competitive MMDocRAG systems. Masking the gold region leaves the fact
available elsewhere: with a copy in the input, 41-56% of correct answers across four models survive
it yet fail once every annotated instance is masked. Set-level masking with automatically found
copies closes 78% of the gap to masking every annotated instance at matched granularity (three
models); an unverified key-string rule lowers survival at least as far but masks three times the
area. We release the annotations and redundancy-aware metrics.

---

### 5. DeOverlay: A Benchmark and Source-Anchored Flow for Video Overlay Removal

- arXiv: [2610.26081v1](https://arxiv.org/abs/2610.26081v1)
- PDF: [下载链接](https://arxiv.org/pdf/2610.26081v1)
- 作者: Deshui Miao, Yuhang Ma, Shaoyong Jia, Wenzhao Gao, Yue Zhang, Shaohui Jiao, Xin Li
- 发布时间: 2026-10-19T09:39:06Z
- 分类: cs.CV
- 相关性评分: 9

**原始摘要**

Video overlay removal aims to recover scenes obscured by subtitles, titles, and logos while
preserving surrounding content. Existing methods use temporal propagation or source-conditioned
generation, but can leave residual overlays and distort scene structure when useful source
information is obscured. We propose DeOverlay, a source-anchored flow model that reconstructs the
clean video from the source latent with fixed source guidance. Specifically, we train a shared
velocity network along paired source-to-clean paths using region-weighted flow matching, enabling
successive cor- rections from intermediate states. To select local source cues, we develop
visibility-normalized temporal aggregation that excludes masked positions and averages the remaining
observations. Global source context and edit-region embeddings complement these cues through
additive condi- tioning, retaining a single video-token sequence. To evaluate scene recovery across
diverse overlay conditions, we introduce DVTE-Bench, comprising 1,631 paired videos across eight
text-overlay categories, with OCR-screened clean targets, frame-aligned pixel masks, and a common
evaluation protocol. Experiments on the complete release show that DeOverlay outperforms four
baselines on all five reconstruction and perceptual metrics, reducing Mask LPIPS and Mask VFID by
58.3% and 70.3%, respectively, relative to the strongest evaluated baseline. Additional qualitative
examples demonstrate the removal of graphic logos and stickers. We will make the complete benchmark,
evaluation code, and test outputs availabl. Project page:https://yahooo-m.github.io/DVTE-Bench/

---

### 6. CIS-Transolver: A Cross-Layer Incremental-State Neural Operator for Fine-Scale Automotive Aerodynamic Flow Prediction

- arXiv: [2610.26337v1](https://arxiv.org/abs/2610.26337v1)
- PDF: [下载链接](https://arxiv.org/pdf/2610.26337v1)
- 作者: Jianglong Liu, Zhicheng Zhu, Jia Hao, Liangyue Jia
- 发布时间: 2026-10-19T13:08:19Z
- 分类: cs.LG, cs.AI
- 相关性评分: 6

**原始摘要**

Neural operators offer an efficient data-driven approach to rapid prediction of complex automotive
aerodynamic flows. However, spectral bias and other factors limit accurate reconstruction of fine-
scale flow variations near complex geometries. Existing studies improve the representation and
fitting of fine-scale information mainly through information extraction and training objectives.
Further study is needed to determine how extracted local details can be used continually in
subsequent operator computations and contribute effectively to the overall flow-field
representation. We propose CIS-Transolver, a cross-layer incremental-state neural operator that
extends fine-scale modeling from local information extraction to its use across layers. The method
extracts fine-scale information through local multiscale analysis and encodes it as geometric moment
states that are propagated and updated across layers. By combining information from previous layers
with feedback to the value representations in Physics-Attention, the method allows local details to
contribute continually to subsequent modeling of global physical correlations. We systematically
evaluate CIS-Transolver on three public automotive aerodynamics benchmarks, ShapeNet-Car, AhmedML,
and DrivAerNet++, covering surface pressure fields and volumetric pressure and velocity fields. CIS-
Transolver achieves the lowest mean relative L2 error among the evaluated methods for all five
prediction metrics across the three benchmarks. The relative error reductions average 8.72% across
the five metrics compared with the best baseline for each metric, reaching 16.38% for ShapeNet-Car
pressure prediction and 15.60% for AhmedML velocity prediction. These results provide a new approach
to fine-scale flow prediction for complex geometries.

---

### 7. Long-form Video-to-Text Summarization using Recursive Language Models

- arXiv: [2610.26431v1](https://arxiv.org/abs/2610.26431v1)
- PDF: [下载链接](https://arxiv.org/pdf/2610.26431v1)
- 作者: Alessia Intini, Lorenzo Vaiani, Enrico Chen, Luca Cagliero
- 发布时间: 2026-10-19T13:56:33Z
- 分类: cs.CV
- 相关性评分: 3

**原始摘要**

While VideoLLMs have made significant progress in understanding short video benchmarks, they often
struggle to summarize long-form ones. This is mainly due to performance degradation caused by long-
context prompts, the inherent difficulty of preserving temporal continuity and a lack of
semantically rich concepts in event descriptions. To tackle these issues, this paper introduces the
first recursive Video Language Summarization Model (RVLSM) designed for video processing and
tailored to long-form video-to-text summarization. RVLSM recursively decomposes videos into
semantically coherent segments and delegates chunk-level reasoning to VideoLLM sub-models and
external tools. It employs (1) Semantic Temporal Decomposition (STD), which preserves temporal
coherence and continuity through a scene-aware chunking strategy that dynamically partitions videos
according to semantic boundaries, and (2) Adaptive Multimodal Tool Calling (AMTC), which ensures
semantic richness of the summary via a routing mechanism that selectively invokes auxiliary modules
such as action recognition, optical character recognition, automatic speech recognition, and object
detection. Experiments on the VideoXum and MixTyVSum benchmarks show that RVLSM consistently
improves over zero-shot VideoLLM baselines across multiple model settings and performance metrics,
and is competitive with a state-of-the-art fine-tuned model for video-to-text summarization.
Importantly, the named entities in the RVLSM's summaries align more closely with those detected in
the ground-truth summaries than those detected by baseline and state-of-the-art methods, confirming
the saliency of the event descriptions it generates.

---
