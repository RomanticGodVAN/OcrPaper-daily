# OCR / 文档解析研究日报（2026-07-17）

## 报告说明

- 检索源：arXiv API
- 检索查询：`(all:"document parsing" OR all:"document understanding" OR all:"optical character recognition" OR all:OCR OR all:"layout analysis" OR all:"document layout analysis" OR all:"text recognition" OR all:"table recognition" OR all:"form understanding" OR all:"document intelligence" OR all:"page understanding" OR all:"scene text recognition" OR all:"handwritten text recognition" OR all:"information extraction") AND (cat:cs.CV OR cat:cs.AI OR cat:cs.CL OR cat:eess.IV)`
- 生成时间（UTC）：`2026-07-17 04:23:15`
- 大模型综合分析：`关闭`
- 备注：DeepSeek 处理失败：Expecting ',' delimiter: line 99 column 3 (char 3747)

## 三、今日论文概览

1. **OvisOCR2 Technical Report**
2. **2D Rotary Position Embedding for Scene Text Recognition with Transformers**
3. **Tactile: Giving Computer-Using Agents Hands and Feet**
4. **Multi-Expert Routing for Multi-Domain Low-Resource OCR: A Manchu Case Study**
5. **CIPHER: A Decoupled Exploration-Selection Framework for Test-Time Scaling of Data Science Agents**

## 八、论文逐篇解析

### 1. OvisOCR2 Technical Report

- arXiv: [2607.13639v1](https://arxiv.org/abs/2607.13639v1)
- PDF: [下载链接](https://arxiv.org/pdf/2607.13639v1)
- 作者: Shiyin Lu, Yinglun Li, Yu Xia, Yuhui Chen, An-Yang Ji, Jun-Peng Jiang, Qing-Guo Chen, Jianshan Zhao, En Lin, Haijun Li, Cheng Qin, Zhao Xu, Weihua Luo
- 发布时间: 2026-07-15T09:32:33Z
- 分类: cs.CV, cs.AI
- 相关性评分: 24

**原始摘要**

We introduce OvisOCR2, a 0.8B document parsing model. OvisOCR2 is designed as an end-to-end parser:
given a document page image, it generates a Markdown representation in natural reading order,
covering text, formulas, tables, and visual regions. We build a data engine that combines filtered
real-document annotations with synthetic pages whose rendered images and Markdown targets are
derived from the same HTML source. The training recipe includes supervised fine-tuning,
reinforcement learning on a 4B branch with a multi-component reward design, on-policy distillation
into the 0.8B model, and model fusion. On OmniDocBench v1.6, OvisOCR2 achieves a state-of-the-art
overall score of 96.58, placing an end-to-end model at the top of this leaderboard previously
dominated by pipeline methods and highlighting the potential of end-to-end document parsing. On
PureDocBench, OvisOCR2 also achieves the highest Avg3 score of 75.06. Beyond these two public
benchmarks, we evaluate OvisOCR2 on an in-house benchmark designed to cover a broader set of long-
tail and challenging scenarios. OvisOCR2 obtains the best overall performance among the compared
methods, providing further evidence of its generalization and robustness. OvisOCR2 is available at
https://huggingface.co/ATH-MaaS/OvisOCR2.

---

### 2. 2D Rotary Position Embedding for Scene Text Recognition with Transformers

- arXiv: [2607.13458v1](https://arxiv.org/abs/2607.13458v1)
- PDF: [下载链接](https://arxiv.org/pdf/2607.13458v1)
- 作者: Zobeir Raisi
- 发布时间: 2026-07-15T05:38:24Z
- 分类: cs.CV
- 相关性评分: 19

**原始摘要**

Scene Text Recognition (STR) remains challenging due to the diversity of text appearances, including
curvature, rotation, and perspective distortion. Recent Transformer-based approaches perform well
but usually rely on one-dimensional positional encodings that ignore the 2D spatial structure of
text images. Axial 2D extensions of Rotary Position Embedding (RoPE) exist for vision Transformers,
but they assume roughly square, isotropic image content and apply the rotation only within encoder
self-attention. Scene text violates both assumptions: crops are markedly anisotropic, and STR models
are encoder-decoder, so the decoder must relate its queries to the encoder's 2D layout through
cross-attention. We introduce 2D-RoPE-STR, which adapts axial 2D-RoPE to this setting through (1) an
anisotropic row/column dimension allocation matched to the aspect ratio of text, and (2) an
extension of the rotary coupling into encoder-decoder cross-attention, letting autoregressive
decoding steps attend to encoder tokens by their 2D layout, a setting not addressed by prior
encoder-only formulations. Both changes are essentially parameter-free and require no architectural
redesign beyond the positional-encoding module. We further introduce a diagnostic protocol (a
controlled ablation pair isolating only the positional encoding, an image-level net-win disagreement
analysis, and encoder attention visualization) that identifies where and why relative 2D position
helps: curved, rotated, and perspective-distorted layouts where reading order departs from a
straight horizontal line. On six standard benchmarks (IIIT5K, SVT, ICDAR 2013, ICDAR 2015, CUTE80,
SVTP), gains concentrate on exactly these irregular layouts, with ablations isolating each design
choice against 1D RoPE and 2D sinusoidal and learnable alternatives.

---

### 3. Tactile: Giving Computer-Using Agents Hands and Feet

- arXiv: [2607.14443v1](https://arxiv.org/abs/2607.14443v1)
- PDF: [下载链接](https://arxiv.org/pdf/2607.14443v1)
- 作者: Yong Liu, Zhenyi Zhong, Zhanpeng Shi
- 发布时间: 2026-07-16T00:35:25Z
- 分类: cs.AI
- 相关性评分: 9

**原始摘要**

Computer-use agents are becoming capable software operators, but their interface to desktop
applications is still often a brittle motor layer: they look at screenshots, predict coordinates,
click, and hope that the visible state changed as intended. This collapses target grounding, action
execution, and outcome verification into a single ambiguous operation. We present Tactile, an open-
source tool layer that gives agents a more reliable "hands and feet" for desktop use. Tactile
converts heterogeneous UI evidence--operating-system accessibility semantics, OCR-grounded text, and
visual fallback regions--into action-grounded interface states: compact target candidates with
source labels, roles or text, state, geometry, executable affordances, and verification cues. Agents
operate through an observe-ground-act-verify loop that prefers native semantic actions when
available, falls back to OCR-grounded coordinates when visible text is the best evidence, and keeps
full provenance for replay and failure attribution. On macOSWorld-style tasks, adding Tactile
improves Codex Success@100 from 41.1% to 50.0% overall and from 45.2% to 55.3% on accessibility-
adapted tasks; a 96-task cross-agent subset shows consistent gains across Codex, Claude Code,
OpenCode, and Goose. These results suggest that reliable computer use requires not only stronger
models, but also a reusable execution substrate that exposes software actions as semantic,
verifiable, and auditable objects rather than anonymous screen coordinates.

---

### 4. Multi-Expert Routing for Multi-Domain Low-Resource OCR: A Manchu Case Study

- arXiv: [2607.14041v1](https://arxiv.org/abs/2607.14041v1)
- PDF: [下载链接](https://arxiv.org/pdf/2607.14041v1)
- 作者: Zhan Chen, Jiqiao Ma, Chih-wen Kuo
- 发布时间: 2026-07-15T17:12:37Z
- 分类: cs.CV, cs.AI, cs.LG
- 相关性评分: 9

**原始摘要**

Historical Manchu OCR must accommodate various visually distinct writing styles, including regular
script, running script, and the semi-cursive chancery hand used in palace memorials, despite limited
labeled data. We study a multi-expert system that reuses checkpoints from an iterative fine-tuning
process as domain specialists and uses a lightweight page-level image classifier to dispatch pages
by visual style. When the checkpoint pool lacks a suitable specialist, we train an additional expert
for that domain. On three frozen test sets, the routed system matches the selected specialist for
each style at two-decimal precision: 0.30 percent CER on regular script, 1.57 percent on memorials,
and 4.83 percent on running script. The router achieves 99.3 percent page-level domain accuracy and
matches the domain-label oracle at the same precision. Two of the three selected specialists were
not trained specifically for their final domain; only the running-script expert was trained with
that domain as its target. We report the evaluation protocol, router design, and per-page
predictions to make the comparison reproducible.

---

### 5. CIPHER: A Decoupled Exploration-Selection Framework for Test-Time Scaling of Data Science Agents

- arXiv: [2607.14386v1](https://arxiv.org/abs/2607.14386v1)
- PDF: [下载链接](https://arxiv.org/pdf/2607.14386v1)
- 作者: Maxime Heuillet, Sharadind Peddiraju
- 发布时间: 2026-07-15T22:01:21Z
- 分类: cs.AI
- 相关性评分: 6

**原始摘要**

Data science tasks span from closed-ended information extraction to open-ended analysis, presenting
significant challenges for automation. Recent AI agents powered by language models show promise for
handling such complex tasks. However, existing agents typically rely on a single initial state that
conditions the entire agent's execution, making them vulnerable to cascading errors initiated by a
suboptimal initial state. To mitigate this, we present CIPHER, an automated data science agent that
leverages test-time scaling through the generation and selection of multiple initial states for
concurrent execution. Unlike existing works on test-time scaling of AI agents, CIPHER explicitly
decouples the generation of candidate initial states from their strategic selection for parallel
execution. Through extensive evaluation on two benchmarks (closed-form and open-form tasks), we
demonstrate that CIPHER exceeds state-of-the-art performance in matched-model comparisons, and
remains competitive against larger-model baselines despite relying on a substantially smaller base
LM. Our empirical study characterizes the design space of the Decoupled Exploration-Selection (DES)
framework: we quantify how generation strategy, selection strategy, and aggregator model capacity
contribute to overall performance, and derive actionable design recommendations for practitioners.

---
