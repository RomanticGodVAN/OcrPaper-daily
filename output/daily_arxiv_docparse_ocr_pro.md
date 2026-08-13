# OCR / 文档解析研究日报（2026-08-13）

## 报告说明

- 检索源：arXiv API
- 检索查询：`(all:"document parsing" OR all:"document understanding" OR all:"optical character recognition" OR all:OCR OR all:"layout analysis" OR all:"document layout analysis" OR all:"text recognition" OR all:"table recognition" OR all:"form understanding" OR all:"document intelligence" OR all:"page understanding" OR all:"scene text recognition" OR all:"handwritten text recognition" OR all:"information extraction") AND (cat:cs.CV OR cat:cs.AI OR cat:cs.CL OR cat:eess.IV)`
- 生成时间（UTC）：`2026-08-13 03:32:19`
- 大模型综合分析：`关闭`
- 备注：DeepSeek 处理失败：Expecting ',' delimiter: line 46 column 31 (char 2240)

## 三、今日论文概览

1. **Embedding Rotation Invariance for Provable Multi-Oriented Scene Text Recognition**
2. **RLMOpt: Adaptive Prompt Optimization via Recursive Language Models**
3. **InSight-doc: Agentic Visual Perception for Long-Document Understanding**

## 八、论文逐篇解析

### 1. Embedding Rotation Invariance for Provable Multi-Oriented Scene Text Recognition

- arXiv: [2608.10684v1](https://arxiv.org/abs/2608.10684v1)
- PDF: [下载链接](https://arxiv.org/pdf/2608.10684v1)
- 作者: Zhibin Ma, Pengwen Dai, Yi Liu, Xugong Qin, Chenyun Yu, Xiaochun Cao
- 发布时间: 2026-08-11T09:06:46Z
- 分类: cs.CV
- 相关性评分: 12

**原始摘要**

Multi-oriented text is ubiquitous in real-world scenes and remains a major challenge for scene text
recognition (STR). Existing rotation-aware methods explicitly estimate text orientation. However,
due to the lack of theoretical guarantees, they are prone to error accumulation, increased
computational cost, and strong reliance on data. In this work, we incorporate rotation invariance
into the STR framework to address these limitations. Specifically, we adopt an encoder-decoder
architecture, embedding rotation equivariance in the encoder and rotation invariance in the decoder
to construct a fully rotation-invariant network. On the decoder side, we first identify and prove
the rotation-invariant property of the cross-attention mechanism and use it to formulate a rotation-
invariant text decoder that maps visual features to output text in a rotation-invariant manner. On
the encoder side, we propose a rotation-equivariant local-global extraction network that integrates
deep equivariant convolutions with self-attention, enabling rotation-equivariant feature extraction
while modeling inter-character dependencies and preserving fine-grained visual details. By
integrating the encoder and decoder, we obtain an end-to-end Rotation-Invariant Scene Text
Recognition network (RISTER). RISTER provides rotation invariance with theoretical guarantees,
enhancing robustness on multi-oriented samples without introducing additional inference computation
or relying on data-driven orientation correction. Experiments show that RISTER achieves state-of-
the-art performance on both standard and multi-oriented benchmarks, surpassing the second-best model
by 4.0 percent in accuracy on the general multi-oriented dataset.

---

### 2. RLMOpt: Adaptive Prompt Optimization via Recursive Language Models

- arXiv: [2608.10471v1](https://arxiv.org/abs/2608.10471v1)
- PDF: [下载链接](https://arxiv.org/pdf/2608.10471v1)
- 作者: Subhash Bangalore Satheesha, Nirvik Pande, Deepthi Duddempudi, Bharath Dandala
- 发布时间: 2026-08-11T04:35:05Z
- 分类: cs.AI
- 相关性评分: 6

**原始摘要**

Prompt optimizers automate the search for prompts that improve language-model performance, but
existing methods rely on a predefined optimization procedure: the algorithm determines which
candidates to explore and how the search progresses, while the language model generates or refines
prompt proposals. We introduce RLMOpt, a prompt optimizer that makes the search policy itself
language-model-driven through a recursive language model (RLM). The RLM agent operates over a tool-
based environment, inspecting task information, analyzing failures, generating candidates,
allocating evaluation budget, and deciding when to stop. A deterministic harness complements the
agent by enforcing objective scoring, Pareto-based selection, and regression constraints. We
evaluate RLMOpt across four benchmarks spanning structured clinical information extraction (Chia),
multi-hop question answering (HotpotQA), verifiable instruction following (IFBench-2025), and multi-
turn tool-calling agents (BFCL). In a matched comparison at a single seed, RLMOpt obtains the best
held-out score on all four benchmarks and leads the four-task mean (0.610 against 0.589 for GEPA).
Repeating each benchmark across seeds yields 11 matched benchmark-seed comparisons, in which RLMOpt
outperforms GEPA in 9 cases. Across all 11 runs, it never produced a prompt that underperformed its
seed, whereas GEPA fell below its starting point twice. It is also more efficient, achieving these
results with fewer search rollouts while producing prompts that are 27-79% the size of those
produced by GEPA. Our results further show that optimization gains are determined primarily by the
headroom available in the seed prompt, rather than by the search budget. Efficient optimization
therefore depends on reaching the available headroom reliably and with minimal search

---

### 3. InSight-doc: Agentic Visual Perception for Long-Document Understanding

- arXiv: [2608.10628v1](https://arxiv.org/abs/2608.10628v1)
- PDF: [下载链接](https://arxiv.org/pdf/2608.10628v1)
- 作者: Kaican Li, Weiyan Xie, Lewei Yao, Jiannan Wu, Lanqing Hong, Yongxiang Huang, Nevin L. Zhang
- 发布时间: 2026-08-11T08:15:16Z
- 分类: cs.CV, cs.CL, cs.LG
- 相关性评分: 4

**原始摘要**

Long-document understanding often requires reasoning over many visually rich pages, making inference
costly and prone to context rot. In this work, we propose InSight-doc, an agentic visual perception
framework that treats visual resolution as an adaptive reasoning-time resource. InSight-doc starts
from low resolution and selectively zooms into high-resolution regions for finer evidence, without
relying on any external retriever. To train such an agent, we construct an active-perception corpus
of 17.9K high-quality SFT examples with region-level zoom-in trajectories, accompanied by 19.2K hard
RL examples. Through SFT+RL, InSight-doc-8B improves the baseline by 4.3--16.4 accuracy points over
document VQA benchmarks. On long documents, it reduces hallucination by more than 40% and inference
latency by 41%--68% while maintaining an accuracy lead. Our code, datasets, and model are released
at https://github.com/m-Just/InSight-doc .

---
