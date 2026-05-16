# OCR / 文档解析研究日报（2026-05-16）

## 报告说明

- 检索源：arXiv API
- 检索查询：`(all:"document parsing" OR all:"document understanding" OR all:"optical character recognition" OR all:OCR OR all:"layout analysis" OR all:"document layout analysis" OR all:"text recognition" OR all:"table recognition" OR all:"form understanding" OR all:"document intelligence" OR all:"page understanding" OR all:"scene text recognition" OR all:"handwritten text recognition" OR all:"information extraction") AND (cat:cs.CV OR cat:cs.AI OR cat:cs.CL OR cat:eess.IV)`
- 生成时间（UTC）：`2026-05-16 04:37:16`
- 大模型综合分析：`开启`

## 一、今日执行摘要

> 今日 OCR 与文档解析研究聚焦于自监督场景文本识别和长期记忆多模态基准。Masked Next-Scale Prediction (MNSP) 通过跨尺度预测与掩码重建提升了场景文本识别的性能，而 MemLens 基准为评估多模态多轮对话中的记忆能力提供了标准。两者共同指向了更鲁棒和更具记忆能力的模型架构。

## 二、今日趋势判断

自监督学习的应用从单尺度向多尺度分层表示演进，多模态大模型的研究焦点开始从单轮感知扩展至长期记忆与多轮交互能力。

## 三、今日论文概览

1. **Masked Next-Scale Prediction for Self-supervised Scene Text Recognition** | 标签：场景文本识别、自监督学习、掩码图像建模、多尺度表示、预训练
2. **MemLens: Benchmarking Multimodal Long-Term Memory in Large Vision-Language Models** | 标签：多模态大模型、长期记忆、基准测试、多轮对话、视觉语言模型

## 四、今天 OCR / 文档解析论文里的主要创新点

- 跨尺度预测与掩码重建的结合用于场景文本识别。
- 多尺度语言对齐模块保持不同分辨率间的语义一致性。
- 跨模态 token 计数方案统一不同长度上下文，用于记忆基准测试。
- 图像消融实验验证了视觉证据的必要性。
- 长期记忆与长上下文注意力的混合架构被提出作为方向。

## 五、后续 OCR 领域值得推进的改进方向

- 探索轻量级跨尺度融合结构以降低 MNSP 的计算成本。
- 将 MNSP 扩展到手写文本与多语言场景文本识别。
- 研究未标注数据多样性对自监督预训练效果的影响。
- 开发包含视频与音频的多模态长期记忆基准。
- 优化长上下文注意力与结构化多模态检索的混合架构。
- 研究记忆压缩策略在保持视觉保真度时的优化。

## 六、工程落地启发

- MNSP 可减少对标注数据的依赖，提升工业场景文本识别模型的泛化能力。
- MemLens 为多模态对话系统的记忆模块设计提供了量化评估标准，可指导实际部署中的架构选择。

## 七、优先关注论文

- **Masked Next-Scale Prediction for Self-supervised Scene Text Recognition**：提出新颖的多尺度自监督框架，计算开销可能是工程部署的瓶颈，值得跟踪轻量化改进方向。
- **MemLens: Benchmarking Multimodal Long-Term Memory in Large Vision-Language Models**：首个多模态记忆基准，其提出的混合架构和记忆压缩策略有望成为多模态文档对话系统的设计指南。

## 八、论文逐篇解析

### 1. Masked Next-Scale Prediction for Self-supervised Scene Text Recognition

- arXiv: [2605.14885v1](https://arxiv.org/abs/2605.14885v1)
- PDF: [下载链接](https://arxiv.org/pdf/2605.14885v1)
- 作者: Zhuohao Chen, Zeng Li, Yifei Zhang, Chang Liu, Yu Zhou
- 发布时间: 2026-05-14T14:28:55Z
- 分类: cs.CV
- 相关性评分: 16
- 主题标签: 场景文本识别、自监督学习、掩码图像建模、多尺度表示、预训练

**中文摘要**

> 提出了 Masked Next-Scale Prediction (MNSP) 自监督框架，通过跨尺度预测和掩码重建建模场景文本的分层视觉结构，在 Union14M 和标准数据集上达到 SOTA 性能。

**核心创新概述**

> 首次将跨尺度预测与掩码图像重建结合，解决单尺度 MIM 无法捕获分层结构的问题。

**创新点拆解**

- Next-Scale Prediction 机制学习从低分辨率到高分辨率的层次表示
- 联合优化跨尺度预测和掩码重建，兼顾全局布局与局部细节
- 多尺度语言对齐模块保持不同分辨率间的语义一致性

**当前局限**

> 在极端低质量或严重遮挡场景下准确率仍有下降；跨尺度预测的计算开销较大。

**后续可改进方向**

- 探索更轻量的跨尺度融合结构以降低计算成本
- 将 MNSP 扩展到手写文本或多语言场景文本识别
- 研究未标注数据的多样性对预训练效果的影响

**工程启发**

> 可减少对标注数据的依赖，提升工业场景下文本识别模型的泛化能力和鲁棒性。

**为什么值得关注**

> 直接面向场景文本识别，提出新的自监督预训练范式，对降低数据需求、提升模型性能有重要参考价值。

**原始摘要**

Scene Text Recognition requires modeling visual structures that evolve from coarse layouts to fine-
grained character strokes. Training such models relies on large amounts of annotated data. Recent
self-supervised approaches, such as Masked Image Modeling (MIM), alleviate this dependency by
leveraging large-scale unlabeled data. Yet most existing MIM methods operate at a single spatial
scale and fail to capture the hierarchical nature of scene text. In this work, we introduce Masked
Next-Scale Prediction (MNSP), a unified self-supervised framework designed to explicitly model
cross-scale structural evolution. The framework incorporates Next-Scale Prediction (NSP), which
learns hierarchical representations by predicting higher-resolution features from lower-resolution
contexts. Naive scale prediction, however, tends to produce spatially diffuse attention, directing
the model toward background regions rather than textual structures. MNSP resolves this limitation by
jointly learning cross-scale prediction and masked image reconstruction. NSP captures global layout
priors across resolutions, while masked reconstruction imposes strong local constraints that guide
attention toward informative text regions. A Multi-scale Linguistic Alignment module further
maintains semantic consistency across different resolutions. Extensive experiments demonstrate that
MNSP achieves state-of-the-art performance, reaching 86.2\% average accuracy on the challenging
Union14M benchmark and 96.7\% across six standard datasets. Additional analyses show that our method
improves robustness under extreme scale and layout variations. Code is available at
https://github.com/CzhczhcHczh/MNSP

---

### 2. MemLens: Benchmarking Multimodal Long-Term Memory in Large Vision-Language Models

- arXiv: [2605.14906v1](https://arxiv.org/abs/2605.14906v1)
- PDF: [下载链接](https://arxiv.org/pdf/2605.14906v1)
- 作者: Xiyu Ren, Zhaowei Wang, Yiming Du, Zhongwei Xie, Chi Liu, Xinlin Yang, Haoyue Feng, Wenjun Pan, Tianshi Zheng, Baixuan Xu, Zhengnan Li, Yangqiu Song, Ginny Wong, Simon See
- 发布时间: 2026-05-14T14:41:17Z
- 分类: cs.CV
- 相关性评分: 9
- 主题标签: 多模态大模型、长期记忆、基准测试、多轮对话、视觉语言模型

**中文摘要**

> 提出 MemLens 基准，系统评估长上下文 LVLM 和记忆增强代理在多模态多轮对话中的记忆能力，发现两者互补，混合架构是方向。

**核心创新概述**

> 首个针对多模态多轮对话中长时记忆能力的综合基准，包含跨模态 token 计数和图像消融验证。

**创新点拆解**

- 设计跨模态 token 计数方案统一不同长度上下文
- 图像消融实验证明任务必须依赖视觉证据
- 覆盖 5 种记忆能力和 4 种上下文长度

**当前局限**

> 基准规模相对有限（789 题），未涵盖视频或音频等更多模态。

**后续可改进方向**

- 扩展到多模态长期记忆的其他场景（如视频理解）
- 探索长上下文注意力与结构化多模态检索的混合架构
- 研究记忆压缩策略在保持视觉保真度方面的优化

**工程启发**

> 为多模态对话系统的记忆模块设计提供量化评估标准，指导实际部署中的架构选择。

**为什么值得关注**

> 聚焦长期记忆能力评估，对 OCR / 文档解析中需要跨多轮对话保持视觉信息一致性的场景有参考意义。

**原始摘要**

Memory is essential for large vision-language models (LVLMs) to handle long, multimodal
interactions, with two method directions providing this capability: long-context LVLMs and memory-
augmented agents. However, no existing benchmark conducts a systematic comparison of the two on
questions that genuinely require multimodal evidence. To close this gap, we introduce MEMLENS, a
comprehensive benchmark for memory in multimodal multi-session conversations, comprising 789
questions across five memory abilities (information extraction, multi-session reasoning, temporal
reasoning, knowledge update, and answer refusal) at four standard context lengths (32K-256K tokens)
under a cross-modal token-counting scheme. An image-ablation study confirms that solving MEMLENS
requires visual evidence: removing evidence images drops two frontier LVLMs below 2% accuracy on the
80.4% of questions whose evidence includes images. Evaluating 27 LVLMs and 7 memory-augmented
agents, we find that long-context LVLMs achieve high short-context accuracy through direct visual
grounding but degrade as conversations grow, whereas memory agents are length-stable but lose visual
fidelity under storage-time compression. Multi-session reasoning caps most systems below 30%, and
neither approach alone solves the task. These results motivate hybrid architectures that combine
long-context attention with structured multimodal retrieval. Our code is available at
https://github.com/xrenaf/MEMLENS.

---
