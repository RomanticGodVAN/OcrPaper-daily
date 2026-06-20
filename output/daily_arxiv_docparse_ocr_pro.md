# OCR / 文档解析研究日报（2026-06-20）

## 报告说明

- 检索源：arXiv API
- 检索查询：`(all:"document parsing" OR all:"document understanding" OR all:"optical character recognition" OR all:OCR OR all:"layout analysis" OR all:"document layout analysis" OR all:"text recognition" OR all:"table recognition" OR all:"form understanding" OR all:"document intelligence" OR all:"page understanding" OR all:"scene text recognition" OR all:"handwritten text recognition" OR all:"information extraction") AND (cat:cs.CV OR cat:cs.AI OR cat:cs.CL OR cat:eess.IV)`
- 生成时间（UTC）：`2026-06-20 05:43:03`
- 大模型综合分析：`开启`

## 一、今日执行摘要

> 今日论文聚焦手写数学表达式生成与医学病理信息抽取两个方向。DiffMath 首次将潜在扩散模型与层次化结构感知表示结合，显著提升手写数学表达式生成的结构一致性，并通过数据增强提高下游 OCR 准确率；另一工作则利用零样本 LLM 智能体工作流从临床文本中抽取病理信息，展示了无需标注的低成本解决方案潜力。两者共同体现了从结构化到非结构化、从监督到零样本的扩展趋势。

## 二、今日趋势判断

当前研究趋势包括：1) 利用扩散模型或 LLM 生成合成数据增强 OCR/信息抽取系统；2) 结构感知表示设计以处理复杂布局（如数学公式）；3) 零样本/少样本范式降低对标注数据的依赖；4) 智能体工作流（Agentic Workflow）用于复杂信息抽取任务。

## 三、今日论文概览

1. **DiffMath: Symbol- and Graph-Aware Latent Diffusion Transformer for Handwritten Mathematical Expression Generation** | 标签：手写数学表达式生成、潜在扩散模型、结构感知表示、数据增强、OCR
2. **Prompt, Plan, Extract: Zero-Shot Agentic LLMs Workflows for Lung Pathology Extraction from Clinical Narratives** | 标签：临床信息抽取、大语言模型、零样本学习、病理报告、自然语言处理

## 四、今天 OCR / 文档解析论文里的主要创新点

- 采用潜在扩散模型学习结构保持的潜在表示，避免显式空间监督。
- 利用关系抽象语法树（RelAST）紧凑编码层次化结构信息。
- 构建零样本智能体工作流，通过提示、规划、提取步骤从无结构文本中抽取结构化信息。
- 将生成任务作为数据增强手段，直接提升下游 OCR 或信息抽取模型性能。
- 全局符号计数先验注入条件去噪过程，提高生成结果的结构一致性。

## 五、后续 OCR 领域值得推进的改进方向

- 研究更鲁棒的空间关系编码方法以处理手写数学表达式中的不规则布局。
- 探索无结构或弱结构先验下的生成方法，扩展至自由手写文本或图表场景。
- 结合在线手写轨迹信息提升生成表达式的真实感和动态特性。
- 在零样本信息抽取中引入检索增强生成（RAG）或领域微调以弥补 LLM 知识缺口。
- 设计更高效的提示策略减少 LLM 的幻觉和遗漏，提升抽取准确性。
- 将智能体工作流扩展至多模态文档（如图表、表格混合文本）理解与信息抽取。

## 六、工程落地启发

- DiffMath 的 RelAST 表示可降低数学表达式生成与识别中对标注框的依赖。
- MathVAE 与 MathDiT 结合可生成高质量合成数据，提升现有 OCR 模型准确率。
- 零样本智能体工作流以低部署成本从临床文本抽取结构化字段，适合资源受限场景。
- 开源 LLM（如 GPT-OSS-20B）在零样本抽取任务中可达到接近监督方法的性能（召回率 0.949）。

## 七、优先关注论文

- **DiffMath: Symbol- and Graph-Aware Latent Diffusion Transformer for Handwritten Mathematical Expression Generation**：首次将潜在扩散模型与数学表达式层次结构结合，其结构感知表示和生成质量提升有望直接应用于手写数学 OCR 的数据增强与识别改进。
- **Prompt, Plan, Extract: Zero-Shot Agentic LLMs Workflows for Lung Pathology Extraction from Clinical Narratives**：零样本智能体工作流在医疗信息抽取中表现接近监督方法，低成本部署方案具高工程价值，未来可扩展至文档智能中的复杂信息抽取任务。

## 八、论文逐篇解析

### 1. DiffMath: Symbol- and Graph-Aware Latent Diffusion Transformer for Handwritten Mathematical Expression Generation

- arXiv: [2606.19939v1](https://arxiv.org/abs/2606.19939v1)
- PDF: [下载链接](https://arxiv.org/pdf/2606.19939v1)
- 作者: Wei Pan, Xuhan Zheng, Yilin Shi, Huiguo He, Hiuyi Cheng, Dezhi Peng, Minghui Liao, Lianwen Jin
- 发布时间: 2026-06-18T08:37:02Z
- 分类: cs.CV
- 相关性评分: 15
- 主题标签: 手写数学表达式生成、潜在扩散模型、结构感知表示、数据增强、OCR

**中文摘要**

> 提出 DiffMath，一种用于手写数学表达式生成的符号与图感知的潜在扩散框架。通过设计关系抽象语法树（RelAST）将数学表达式结构化为紧凑三元组，消除对符号级标注框的依赖。引入 MathVAE 学习结构保持的潜在表示，并使用 MathDiT 进行条件去噪，结合全局符号计数先验提高结构一致性。实验表明，生成的结构一致的手写表达式性能优于现有方法，且通过数据增强提升了下游 OCR 模型的准确率。

**核心创新概述**

> 首次将潜在扩散模型与数学表达式层次结构结合，无需显式空间监督；提出了基于关系抽象语法树的紧凑表示方法。

**创新点拆解**

- 设计 RelAST 表示，将 MathML 树蒸馏为 [S, R, D] 三元组，编码符号身份、空间关系和嵌套深度。
- 提出 MathVAE，通过符号感知和关系感知的正则化学习结构保持的潜在表示。
- 引入 MathDiT，在结构化潜在空间中进行条件去噪，并使用 AdaLN 注入全局符号计数先验。

**当前局限**

> 可能对高度潦草的书写风格或极端复杂的表达式泛化能力有限；依赖 LaTeX 结构先验，可能不适用于无结构场景。

**后续可改进方向**

- 探索更鲁棒的空间关系编码方法，以处理不规则布局。
- 研究无结构或弱结构先验下的生成方法，以扩展应用范围。
- 结合在线手写轨迹信息，提升生成的真实感。

**工程启发**

> 可显著降低手写数学表达式生成的数据标注成本，并提升下游 OCR 系统的性能。

**为什么值得关注**

> 针对手写数学表达式生成中的结构性挑战，提出了一种无需空间标注的生成框架，对文档解析和 OCR 数据增强有直接价值。

**原始摘要**

Handwritten Mathematical Expression Generation (HMEG) is challenging due to the complex two-
dimensional layouts and long-range structural dependencies of mathematical expressions. Existing
methods typically rely on explicit spatial supervision, such as symbol-level bounding boxes, which
incurs high annotation costs and limits scalability. In this work, we propose DiffMath, a symbol-
and graph-aware latent diffusion framework that leverages the hierarchical structure inherent in
LaTeX as a structural prior, eliminating the need for positional supervision. First, we design a
Relational Abstract Syntax Tree (RelAST), a generation-oriented representation that distills MathML
trees into compact triplet sequences [S, R, D], where each token directly encodes a symbol identity,
spatial relation, or nesting depth. Second, we introduce MathVAE, which learns structure-preserving
latent representations through symbol-aware and relation-aware perceptual regularization, ensuring
that the latent space captures both character semantics and spatial topology. Third, MathDiT
performs conditional denoising in this structured latent space, further guided by a global symbol-
count prior via Adaptive Layer Normalization (AdaLN) to improve structural coherence. Experiments
show that DiffMath produces structurally consistent handwritten expressions, achieves superior
performance over existing methods, and improves the accuracy of downstream OCR models through
synthetic data augmentation.

---

### 2. Prompt, Plan, Extract: Zero-Shot Agentic LLMs Workflows for Lung Pathology Extraction from Clinical Narratives

- arXiv: [2606.19852v1](https://arxiv.org/abs/2606.19852v1)
- PDF: [下载链接](https://arxiv.org/pdf/2606.19852v1)
- 作者: Aman Pathak, Cheng Peng, Mengxian Lyu, Ziyi Chen, Reema Solan, Sankalp Talankar, Yasir Khan, Hiren Mehta, Aokun Chen, Yi Guo, Yonghui Wu
- 发布时间: 2026-06-18T07:00:43Z
- 分类: cs.CL, cs.LG
- 相关性评分: 6
- 主题标签: 临床信息抽取、大语言模型、零样本学习、病理报告、自然语言处理

**中文摘要**

> 开发了一种零样本、基于智能体的工作流，使用开源的生成式大语言模型从肺癌病理报告中提取 13 个 CAP 概要字段。与监督基线 GatorTron 对比，最佳零样本模型（GPT-OSS-20B）的 Micro-F1 为 0.893（召回率 0.949），虽低于基线（0.960），但无需任务特定训练，展示了低成本解决方案的潜力。

**核心创新概述**

> 首次将零样本智能体工作流应用于病理报告信息提取，并评估了多个开源 LLM，无需标注数据。

**创新点拆解**

- 构建零样本智能体工作流，通过提示、规划、提取步骤从临床叙述中抽取结构化信息。
- 提出与癌症登记对齐的评估框架，用于比较零样本和监督方法。
- 展示了开源 LLM 在无需任务特定训练下抽取复杂关系（如病理分期）的能力。

**当前局限**

> 性能仍低于监督基线；依赖 LLM 的推理能力，可能受限于模型在医疗领域的知识缺口。

**后续可改进方向**

- 探索领域微调或检索增强生成以提升零样本性能。
- 设计更高效的提示策略，减少 LLM 的幻觉和遗漏。
- 扩展到更多类型的病理报告和下游任务。

**工程启发**

> 提供了一种低成本、可快速部署的病理信息提取方案，减少人工标注负担。

**为什么值得关注**

> 关注从临床叙述中提取结构化信息，与文档解析中的信息抽取任务紧密相关，且零样本方法具有实用价值。

**原始摘要**

Information extraction from pathology reports is essential for cancer staging, tumor registry
population. Yet key data remains embedded in narrative reports, making manual extraction labor-
intensive and error-prone. Traditional supervised Natural Language Processing pipelines address this
through fully supervised Named Entity Recognition and Relation Extraction, but require expensive
manual annotation and suffer cascading failures when upstream entities are missed. In this study, we
developed a zero-shot, agentic workflow, and evaluated five open-source generative Large Language
Models (LLMs) to populate 13 College of American Pathologists synoptic fields from lung resection
pathology reports. We compared them against a state-of-the-art supervised GatorTron NER-RE baseline
using a novel, registry-aligned evaluation framework. The baseline achieved Micro-F1of 0.960, while
the best zero-shot model (GPT-OSS-20B) achieved Micro-F1 of 0.893 (recall: 0.949), accurately
extracting complex relations like Pathologic Stage without task-specific training. These results
suggest that open-source, zero-shot agentic LLMs are a low-cost solution for extracting lung
pathology information.

---
