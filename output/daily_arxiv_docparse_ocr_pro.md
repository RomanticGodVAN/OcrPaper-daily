# OCR / 文档解析研究日报（2026-11-27）

## 报告说明

- 检索源：arXiv API
- 检索查询：`(all:"document parsing" OR all:"document understanding" OR all:"optical character recognition" OR all:OCR OR all:"layout analysis" OR all:"document layout analysis" OR all:"text recognition" OR all:"table recognition" OR all:"form understanding" OR all:"document intelligence" OR all:"page understanding" OR all:"scene text recognition" OR all:"handwritten text recognition" OR all:"information extraction") AND (cat:cs.CV OR cat:cs.AI OR cat:cs.CL OR cat:eess.IV)`
- 生成时间（UTC）：`2026-11-27 09:39:02`
- 大模型综合分析：`开启`

## 一、今日执行摘要

> 本期日报聚焦多页文档理解中的跨页上下文建模问题。DocSEAM 提出在视觉编码器与语言模型之间插入轻量跨页编码模块，通过局部三元组和方向性门控融合相邻页信息，在不增加视觉 token 数量的前提下提升多页 VQA 性能与分页边界鲁棒性，为文档解析系统处理跨页表格、跨页段落等场景提供了可集成的工程方案。

## 二、今日趋势判断

当前 OCR/文档解析研究正从单页独立处理转向多页上下文感知，重点解决分页边界导致的信息断裂问题；技术路线倾向于在现有视觉编码器-LLM 管线中插入轻量模块，以低侵入方式注入跨页信息，并补充分页鲁棒性等评测维度。

## 三、今日论文概览

1. **DocSEAM: Bidirectional Cross-Page Encoding for Multi-Page Document Understanding** | 标签：多页文档理解、跨页上下文建模、文档视觉语言模型、视觉编码器融合、文档VQA、分页边界鲁棒性

## 四、今天 OCR / 文档解析论文里的主要创新点

- 在视觉编码器与语言模型之间插入轻量跨页融合模块，保持视觉 token 数量与下游接口不变。
- 采用中心页加前后邻页的局部三元组建模跨页上下文，并通过中心锚定掩码自注意力仅更新中心页表示。
- 引入方向性显著性门控区分前后邻页信息重要性，实现方向感知的跨页融合。
- 设计跨页监督预热后冻结模块的多页微调策略，降低对基座模型训练的侵入性。
- 通过受控重排页实验量化分页边界敏感性，补充常规精度之外的鲁棒性评测。

## 五、后续 OCR 领域值得推进的改进方向

- 将局部三元组扩展为可学习的稀疏跨页注意力或层次化跨页记忆，以覆盖跨多页的长程依赖而不显著增加 token 成本。
- 研究方向性显著性门控在不同分页策略与文档类型（扫描件、双栏排版）下的自适应校准方法。
- 探索 DocSEAM 与跨页阅读顺序建模、跨页表格/段落合并任务的联合训练，验证表示迁移能力。
- 分析冻结模块微调与端到端联合优化之间的性能-成本权衡，并给出更细粒度的跨页定位评测协议。
- 构建针对跨页表格结构还原、跨页段落连贯性、跨页引用关系解析的专项基准与评测指标。
- 研究跨页上下文建模与文档检索增强生成的结合，利用跨页表示提升长文档问答的片段定位精度。

## 六、工程落地启发

- DocSEAM 模块化且不改变视觉 token 数量，可低成本集成到现有视觉编码器-LLM 文档解析管线中。
- 对分页边界鲁棒性的提升有助于减少实际 PDF 解析中跨页表格与跨页段落的后处理拼接错误。
- 跨页监督预热后冻结模块的微调策略可在不重训基座模型的情况下适配多页文档任务。
- 受控重排页实验可作为工程上评估文档解析系统分页鲁棒性的可复用测试方法。
- 当前方案仅覆盖相邻页，面向跨多页长程依赖的文档解析场景需评估其局限并规划扩展方案。

## 七、优先关注论文

- **DocSEAM: Bidirectional Cross-Page Encoding for Multi-Page Document Understanding**：首个在视觉编码器与 LLM 之间以轻量模块实现双向跨页编码的工作，不改变 token 数量且提升分页边界鲁棒性，对多页文档解析系统集成有直接参考价值，需关注其后续对长程跨页依赖的扩展与更多文档类型的泛化验证。

## 八、论文逐篇解析

### 1. DocSEAM: Bidirectional Cross-Page Encoding for Multi-Page Document Understanding

- arXiv: [2611.34420v1](https://arxiv.org/abs/2611.34420v1)
- PDF: [下载链接](https://arxiv.org/pdf/2611.34420v1)
- 作者: Hoang-Nhat Nguyen, Chen Change Loy
- 发布时间: 2026-11-25T14:11:06Z
- 分类: cs.CV, cs.CL
- 相关性评分: 7
- 主题标签: 多页文档理解、跨页上下文建模、文档视觉语言模型、视觉编码器融合、文档VQA、分页边界鲁棒性

**中文摘要**

> 该论文提出 DocSEAM，一个插入在预训练视觉编码器与语言模型之间的轻量模块，通过为每页构造包含前后相邻页的局部三元组，并施加中心锚定的掩码自注意力与方向性显著性门控，将跨页上下文注入中心页视觉表示，且不改变视觉 token 数量。经过跨页监督预热与冻结 DocSEAM 的多页微调后，9B 参数模型在五个多页文档 VQA 基准上取得开放权重≤10B 模型中的最优结果，并在受控重排页实验下降低对分页边界的敏感性、改善跨页片段定位。

**核心创新概述**

> 针对多页文档 VLM 逐页独立编码导致页边界特征不连续的问题，提出在视觉编码器与语言模型之间进行轻量跨页特征融合的模块化方案，并以保持视觉 token 数不变的方式实现双向跨页编码。

**创新点拆解**

- 任务/问题定义：显式将多页文档理解中的页边界特征不连续作为独立问题，提出跨页视觉表示注入的建模范式。
- 架构设计：在视觉编码器与 LLM 之间插入 DocSEAM 模块，以中心页加左右邻页构成局部三元组，采用中心锚定掩码自注意力仅更新中心页 token，保持 token 数量与下游接口不变。
- 机制设计：引入方向性显著性门控，区分前后邻页信息的重要性，实现可学习的方向感知跨页融合。
- 训练范式：采用跨页监督预热后冻结 DocSEAM 的多页微调策略，降低对基座模型训练的侵入性。
- 评测设计：通过受控重排页实验量化分页边界敏感性，并评估跨页片段定位能力，补充了常规 VQA 精度之外的鲁棒性维度。

**当前局限**

> 局部三元组仅覆盖相邻页，对跨多页的长程依赖与全局文档结构建模有限；方向性门控与预热策略依赖多页标注数据；实验集中于≤10B 开放权重模型与多页 VQA 基准，未充分验证对长文档检索、表格跨页合并等任务的泛化；模块收益与基座编码器容量及分页质量的关系尚不明确。

**后续可改进方向**

- 将局部三元组扩展为可学习的稀疏跨页注意力或层次化跨页记忆，以覆盖跨多页的长程依赖而不显著增加 token 成本。
- 研究方向性显著性门控在不同分页策略与文档类型（如扫描件、双栏排版）下的自适应校准方法。
- 探索 DocSEAM 与跨页阅读顺序建模、跨页表格/段落合并任务的联合训练，验证表示迁移能力。
- 分析冻结模块微调与端到端联合优化之间的性能—成本权衡，并给出更细粒度的跨页定位评测协议。

**工程启发**

> 模块化设计且不改变视觉 token 数量，便于在现有视觉编码器—LLM 管线中低成本集成；对分页边界鲁棒性的提升有利于实际文档解析系统在 PDF 分页不规则、跨页表格与跨页段落场景下减少后处理拼接错误。

**为什么值得关注**

> 该工作直接面向多页文档的视觉表示与跨页上下文建模，属于文档理解与 OCR 下游解析的关键环节，其边界敏感性与跨页定位分析对 OCR 版面分析和跨页内容重组具有参考价值。

**原始摘要**

Multi-page document vision-language models encode each page independently, creating a feature-level
discontinuity at page boundaries: visual tokens are formed without access to content on adjacent
pages, and the language model must reason over these page representations formed in isolation. We
introduce DocSEAM (Document Selective Enrichment via Anchored Masking), a lightweight module
inserted between a pretrained vision encoder and the language model that injects the inductive bias
of local cross-page context into visual representations. For each page, DocSEAM forms a local
triplet with its two neighbors, applies center-anchored masked self-attention with directional
salience gates to fuse information from neighbor pages, and returns only the enriched center-page
tokens, leaving the visual token count unchanged. After a supervised cross-page warm-up and multi-
page fine-tuning with DocSEAM frozen, our 9B-parameter model achieves state-of-the-art results among
the evaluated open-weight models of up to 10B parameters on five multi-page document VQA benchmarks.
We further show that under controlled re-pagination, DocSEAM reduces sensitivity to boundary
placement and improves cross-page span localization

---
