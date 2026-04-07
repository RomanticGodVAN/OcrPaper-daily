# OCR / 文档解析研究日报（2026-04-07）

## 报告说明

- 检索源：arXiv API
- 检索查询：`(all:"document parsing" OR all:"document understanding" OR all:"optical character recognition" OR all:OCR OR all:"layout analysis" OR all:"document layout analysis" OR all:"text recognition" OR all:"table recognition" OR all:"form understanding" OR all:"document intelligence" OR all:"page understanding" OR all:"scene text recognition" OR all:"handwritten text recognition" OR all:"information extraction") AND (cat:cs.CV OR cat:cs.AI OR cat:cs.CL OR cat:eess.IV)`
- 生成时间（UTC）：`2026-04-07 04:06:44`
- 大模型综合分析：`开启`

## 一、今日执行摘要

> 今日OCR/文档解析研究日报综合结论显示，研究重点从传统模型架构创新转向数据工程、效率优化和内部机制分析。论文1揭示了视觉文档理解中内部表示与生成响应的差距，提出中间层微调策略以提升一致性。论文2强调数据工程的核心作用，通过系统化数据引擎和训练策略显著提升文档解析性能，挑战了以模型为中心的研究范式。论文3关注效率优化，引入Firebolt-VL模型实现线性时间推理和增强的视觉基础，适用于资源受限场景。论文4针对医疗领域，提出隐私保护的半自动化工作流，使用小型语言模型进行临床文档解析。整体趋势表明，研究正朝着更高效、数据驱动和领域特定的方向发展，为工程应用提供了可复现的解决方案。

## 二、今日趋势判断

当前OCR/文档解析研究呈现三大趋势：一是从模型架构创新转向数据工程优化，强调训练数据质量和系统性处理的重要性；二是关注模型效率和部署可行性，特别是在资源受限环境中；三是深入分析模型内部机制，以提升任务理解和性能一致性。这些趋势反映了领域向更实用、可扩展和可靠的方向演进。

## 三、今日论文概览

1. **Responses Fall Short of Understanding: Revealing the Gap between Internal Representations and Responses in Visual Document Understanding** | 标签：视觉文档理解、大视觉语言模型、线性探测、中间层微调、内部表示分析
2. **MinerU2.5-Pro: Pushing the Limits of Data-Centric Document Parsing at Scale** | 标签：文档解析、数据工程、训练策略、评估协议、数据引擎
3. **Firebolt-VL: Efficient Vision-Language Understanding with Cross-Modality Modulation** | 标签：视觉语言模型、效率优化、液态基础模型、视觉基础、细粒度推理
4. **A Semi-Automated Annotation Workflow for Paediatric Histopathology Reports Using Small Language Models** | 标签：临床文档解析、小型语言模型、半自动化工作流、隐私保护、问答任务

## 四、今天 OCR / 文档解析论文里的主要创新点

- 使用线性探测或数据引擎分析模型内部表示或数据缺陷，以量化性能瓶颈。
- 提出针对中间层或数据层级的微调策略，优化模型在特定任务上的准确性和一致性。
- 引入轻量级模块或工作流，如令牌-网格相关模块或半自动化标注，以提升效率或隐私保护。
- 开发改进的评估协议或实体指南，提供更可靠的性能衡量或任务框架。

## 五、后续 OCR 领域值得推进的改进方向

- 扩展中间层微调方法到更多视觉文档理解基准和模型架构，验证其泛化能力。
- 结合非线性分析或注意力机制研究，深入探索内部表示差距的根本原因。
- 开发自动化数据质量评估和校正技术，减少数据工程中的人工干预和成本。
- 优化令牌-网格相关模块的计算效率，进一步降低视觉语言模型的推理时间。
- 将小型语言模型工作流扩展到更多临床文档类型，如放射学报告或表格数据。
- 研究知识蒸馏或模型压缩技术，在保持性能的同时减小文档解析模型的规模。
- 探索多模态信息集成，如图像与文本结合，以提升文档解析的全面性和准确性。
- 针对资源受限设置，设计轻量级架构与数据工程结合的混合优化策略。

## 六、工程落地启发

- 实施中间层微调策略，以改善视觉文档理解模型的响应一致性和准确性。
- 采用数据引擎方法，如多样性和难度感知采样，优化文档解析系统的训练数据质量。
- 部署Firebolt-VL类高效模型，在边缘设备上实现低延迟的视觉语言理解任务。
- 集成小型语言模型和半自动化工作流，用于隐私敏感的临床文档解析应用。
- 使用改进的评估协议如OmniDocBench v1.6，更可靠地衡量文档解析系统性能。
- 结合实体指南和少样本示例，提升问答任务框架在信息提取中的效果。
- 利用分歧建模框架，优先处理困难样本以提高标注效率和系统鲁棒性。

## 七、优先关注论文

- **Responses Fall Short of Understanding: Revealing the Gap between Internal Representations and Responses in Visual Document Understanding**：揭示了内部表示与生成响应的差距，中间层微调策略可能成为提升视觉文档理解模型可靠性的关键方向。
- **MinerU2.5-Pro: Pushing the Limits of Data-Centric Document Parsing at Scale**：强调数据工程的核心作用，其数据引擎和训练策略优化方法可直接应用于实际系统以突破性能瓶颈。
- **Firebolt-VL: Efficient Vision-Language Understanding with Cross-Modality Modulation**：提供高效的视觉语言模型解决方案，适用于资源受限场景，推动OCR和文档解析在边缘设备的部署。
- **A Semi-Automated Annotation Workflow for Paediatric Histopathology Reports Using Small Language Models**：针对医疗领域提出隐私保护的工作流，为特定行业文档解析提供了资源高效和可复现的实践案例。

## 八、论文逐篇解析

### 1. Responses Fall Short of Understanding: Revealing the Gap between Internal Representations and Responses in Visual Document Understanding

- arXiv: [2604.04411v1](https://arxiv.org/abs/2604.04411v1)
- PDF: [下载链接](https://arxiv.org/pdf/2604.04411v1)
- 作者: Haruka Kawasaki, Ryota Tanaka, Kyosuke Nishida
- 发布时间: 2026-04-06T04:25:52Z
- 分类: cs.CL, cs.AI, cs.CV
- 相关性评分: 16
- 主题标签: 视觉文档理解、大视觉语言模型、线性探测、中间层微调、内部表示分析

**中文摘要**

> 视觉文档理解（VDU）是大视觉语言模型（LVLMs）的一项挑战性任务，需要整合视觉感知、文本识别和对结构化布局的推理。尽管最近LVLMs在VDU基准测试中显示出进展，但其性能通常基于生成的响应进行评估，这可能不一定反映模型是否在内部实际捕获了所需信息。本文通过线性探测研究LVLMs中LLMs不同层如何表示解决VDU任务所需的信息。研究发现：（1）内部表示与生成响应之间存在明显差距；（2）解决任务所需的信息通常从中间层比从最终层更线性地编码。基于这些发现，探索了针对中间层的微调策略。实验表明，微调中间层提高了线性探测准确性和响应准确性，同时缩小了差距。

**核心创新概述**

> 揭示了LVLMs在视觉文档理解任务中内部表示与生成响应之间的差距，并发现中间层比最终层更线性地编码任务相关信息，提出通过微调中间层来改善性能。

**创新点拆解**

- 方法设计：使用线性探测分析LVLMs不同层的信息表示，量化内部表示与响应的差距。
- 训练范式：提出针对中间层的微调策略，以提升模型在VDU任务中的准确性和一致性。
- 数据：通过实验验证中间层编码的有效性，为模型内部机制提供新见解。

**当前局限**

> 研究主要基于线性探测和微调实验，可能未覆盖所有VDU任务类型或模型架构；未深入探讨差距产生的根本原因，如注意力机制或训练数据的影响。

**后续可改进方向**

- 扩展分析到更多VDU基准和模型，验证中间层微调的泛化能力。
- 结合更复杂的探测方法（如非线性分析）来深入理解内部表示机制。
- 探索如何将中间层信息直接集成到响应生成中，以减少差距。

**工程启发**

> 高，为改进LVLMs在文档理解任务中的性能提供了具体策略，有助于提升模型在实际应用中的可靠性和效率。

**为什么值得关注**

> 直接针对视觉文档理解任务，揭示了模型内部表示与输出之间的不一致性，对OCR和文档解析领域有重要启示，可指导模型优化和评估方法。

**原始摘要**

Visual document understanding (VDU) is a challenging task for large vision language models (LVLMs),
requiring the integration of visual perception, text recognition, and reasoning over structured
layouts. Although recent LVLMs have shown progress on VDU benchmarks, their performance is typically
evaluated based on generated responses, which may not necessarily reflect whether the model has
actually captured the required information internally. In this paper, we investigate how information
required to solve VDU tasks is represented across different layers of LLMs within LVLMs using linear
probing. Our study reveals that (1) there is a clear gap between internal representations and
generated responses, and (2) information required to solve the task is often encoded more linearly
from intermediate layers than from the final layer. Motivated by these findings, we explore fine-
tuning strategies that target intermediate layers. Experiments show that fine-tuning intermediate
layers improves both linear probing accuracy and response accuracy while narrowing the gap.

---

### 2. MinerU2.5-Pro: Pushing the Limits of Data-Centric Document Parsing at Scale

- arXiv: [2604.04771v1](https://arxiv.org/abs/2604.04771v1)
- PDF: [下载链接](https://arxiv.org/pdf/2604.04771v1)
- 作者: Bin Wang, Tianyao He, Linke Ouyang, Fan Wu, Zhiyuan Zhao, Tao Chu, Yuan Qu, Zhenjiang Jin, Weijun Zeng, Ziyang Miao, Bangrui Xu, Junbo Niu, Mengzhang Cai, Jiantao Qiu, Qintong Zhang, Dongsheng Ma, Yuefeng Sun, Hejun Dong, Wenzheng Zhang, Jutao Xiao, Jiayong Shi, Pengyu Liao, Xiaomeng Zhao, Huaping Zhong, Liqun Wei, Jing Yu, Jie Yang, Wei Li, Shasha Wang, Qianqian Wu, Xuanhe Zhou, Weijia Li, Zhenxiang Li, Zhongying Tu, Jiang Wu, Lijun Wu, Chao Xu, Kai Chen, Wentao Zhang, Yu Qiao, Bowen Zhou, Dahua Lin, Conghui He
- 发布时间: 2026-04-06T15:44:18Z
- 分类: cs.CV, cs.CL
- 相关性评分: 12
- 主题标签: 文档解析、数据工程、训练策略、评估协议、数据引擎

**中文摘要**

> 当前文档解析方法主要在模型架构创新上竞争，而训练数据的系统工程仍未被充分探索。然而，不同架构和参数规模的SOTA模型在同一组困难样本上表现出高度一致的失败模式，表明性能瓶颈源于训练数据的共享缺陷而非架构本身。基于这一发现，提出MinerU2.5-Pro，仅通过数据工程和训练策略优化推进技术水平，同时保持MinerU的1.2B参数架构完全固定。其核心是一个围绕覆盖性、信息量和标注准确性共同设计的数据引擎：多样性和难度感知采样将训练数据从不足1000万扩展到6550万样本，同时纠正分布偏移；跨模型一致性验证利用异构模型之间的输出一致性来评估样本难度并生成可靠标注；判断与精炼管道通过渲染-验证迭代校正提高困难样本的标注质量。三阶段渐进训练策略——大规模预训练、困难样本微调和GRPO对齐——顺序利用不同质量层级的数据。在评估方面，修复了OmniDocBench v1.5中的元素匹配偏差并引入困难子集，建立了更具区分性的OmniDocBench v1.6协议。在没有任何架构修改的情况下，MinerU2.5-Pro在OmniDocBench v1.6上达到95.69分。

**核心创新概述**

> 强调数据工程而非架构创新，通过系统化数据引擎和训练策略优化显著提升文档解析性能，挑战了当前以模型为中心的研究范式。

**创新点拆解**

- 数据：开发数据引擎，包括多样性和难度感知采样、跨模型一致性验证和判断与精炼管道，以扩展和优化训练数据。
- 训练范式：提出三阶段渐进训练策略，有效利用不同质量的数据层级。
- 任务定义：引入改进的评估协议OmniDocBench v1.6，修复偏差并增加困难子集，提供更可靠的性能衡量。

**当前局限**

> 方法依赖于大规模数据收集和标注，可能成本较高；未探索与其他先进架构的结合，限制了进一步性能提升的潜力。

**后续可改进方向**

- 研究如何将数据工程方法扩展到更小规模或资源受限的设置中。
- 结合轻量级架构优化，以在保持效率的同时进一步提升性能。
- 探索自动化数据质量评估和校正技术，减少人工干预。

**工程启发**

> 非常高，提供了可复现的数据驱动解决方案，可直接应用于实际文档解析系统，提升准确性和鲁棒性。

**为什么值得关注**

> 专注于文档解析的数据瓶颈问题，为OCR领域提供了以数据为中心的新研究方向，有助于解决实际应用中的性能限制。

**原始摘要**

Current document parsing methods compete primarily on model architecture innovation, while
systematic engineering of training data remains underexplored. Yet SOTA models of different
architectures and parameter scales exhibit highly consistent failure patterns on the same set of
hard samples, suggesting that the performance bottleneck stems from shared deficiencies in training
data rather than architecture itself. Building on this finding, we present \minerupro, which
advances the state of the art solely through data engineering and training strategy optimization
while keeping the 1.2B-parameter architecture of \mineru completely fixed. At its core is a Data
Engine co-designed around coverage, informativeness, and annotation accuracy: Diversity-and-
Difficulty-Aware Sampling expands training data from under 10M to 65.5M samples while correcting
distribution shift; Cross-Model Consistency Verification leverages output agreement among
heterogeneous models to assess sample difficulty and generate reliable annotations; the Judge-and-
Refine pipeline improves annotation quality for hard samples through render-then-verify iterative
correction. A three-stage progressive training strategy -- large-scale pre-training, hard sample
fine-tuning, and GRPO alignment -- sequentially exploits these data at different quality tiers. On
the evaluation front, we fix element-matching biases in OmniDocBench~v1.5 and introduce a Hard
subset, establishing the more discriminative OmniDocBench~v1.6 protocol. Without any architectural
modification, \minerupro achieves 95.69 on OmniDocBench~v1.6, improving over the same-architecture
baseline by 2.71 points and surpassing all existing methods including models with over 200$\times$
more parameters.

---

### 3. Firebolt-VL: Efficient Vision-Language Understanding with Cross-Modality Modulation

- arXiv: [2604.04579v1](https://arxiv.org/abs/2604.04579v1)
- PDF: [下载链接](https://arxiv.org/pdf/2604.04579v1)
- 作者: Quoc-Huy Trinh, Mustapha Abdullahi, Bo Zhao, Debesh Jha
- 发布时间: 2026-04-06T10:25:16Z
- 分类: cs.CV
- 相关性评分: 7
- 主题标签: 视觉语言模型、效率优化、液态基础模型、视觉基础、细粒度推理

**中文摘要**

> 多模态大语言模型（MLLMs）的最新进展在视觉语言理解方面取得了显著进步，但其高计算成本限制了在资源受限场景（如个人助手、文档理解和智能摄像头）中的部署。大多数现有方法依赖于基于Transformer的交叉注意力，其二次复杂度阻碍了效率。此外，小型视觉语言模型通常难以精确捕获细粒度、任务相关的视觉区域，导致在细粒度推理任务上性能下降，限制了其在现实世界中的有效性。为解决这些问题，引入Firebolt-VL，一种高效的视觉语言模型，用液态基础模型（LFM）解码器替换基于Transformer的解码器。为进一步增强视觉基础，提出令牌-网格相关模块，计算文本令牌和图像块之间的轻量级相关性，并通过带有FiLM条件的状态空间模型进行调制。这使得模型能够选择性地强调与文本提示相关的视觉区域，同时保持线性时间推理。在多个基准测试上的实验结果表明，Firebolt-VL实现了准确、细粒度的理解，并显著提高了效率。

**核心创新概述**

> 提出高效的视觉语言模型Firebolt-VL，通过LFM解码器和令牌-网格相关模块替代传统Transformer，实现线性时间推理和增强的视觉基础，适用于资源受限场景。

**创新点拆解**

- 架构：用液态基础模型（LFM）解码器替换Transformer解码器，降低计算复杂度。
- 方法设计：引入令牌-网格相关模块，轻量级计算文本-图像相关性，并通过状态空间模型调制以提升视觉基础。
- 任务定义：针对细粒度推理任务优化，提高模型在文档理解等实际应用中的有效性。

**当前局限**

> 模型可能在某些复杂视觉语言任务上性能仍不及大型Transformer模型；未在广泛的实际部署场景中进行验证。

**后续可改进方向**

- 扩展模型到更多视觉语言任务，如文档布局分析或表格识别，以验证泛化能力。
- 优化令牌-网格相关模块的计算效率，进一步减少推理时间。
- 结合知识蒸馏或其他压缩技术，在保持性能的同时进一步减小模型规模。

**工程启发**

> 高，为资源受限环境提供了高效的视觉语言理解解决方案，有助于推动OCR和文档解析在边缘设备上的应用。

**为什么值得关注**

> 直接解决视觉文档理解中的效率和细粒度问题，对OCR领域有重要应用价值，特别是在移动或嵌入式系统中。

**原始摘要**

Recent advances in multimodal large language models (MLLMs) have enabled impressive progress in
vision-language understanding, yet their high computational cost limits deployment in resource-
constrained scenarios such as personal assistants, document understanding, and smart cameras. Most
existing methods rely on Transformer-based cross-attention, whose quadratic complexity hinders
efficiency. Moreover, small vision-language models often struggle to precisely capture fine-grained,
task-relevant visual regions, leading to degraded performance on fine-grained reasoning tasks that
limit their effectiveness in the real world. To address these issues, we introduce Firebolt-VL, an
efficient vision-language model that replaces the Transformer-based decoder with a Liquid Foundation
Model (LFM) decoder. To further enhance visual grounding, we propose a Token-Grid Correlation
Module, which computes lightweight correlations between text tokens and image patches and modulates
via the state-space model with FiLM conditioning. This enables the model to selectively emphasize
visual regions relevant to the textual prompt while maintaining linear-time inference. Experimental
results across multiple benchmarks demonstrate that Firebolt-VL achieves accurate, fine-grained
understanding with significantly improved efficiency. Our model and code are available at:
https://fireboltvl.github.io

---

### 4. A Semi-Automated Annotation Workflow for Paediatric Histopathology Reports Using Small Language Models

- arXiv: [2604.04168v1](https://arxiv.org/abs/2604.04168v1)
- PDF: [下载链接](https://arxiv.org/pdf/2604.04168v1)
- 作者: Avish Vijayaraghavan, Jaskaran Singh Kawatra, Sebin Sabu, Jonny Sheldon, Will Poulett, Alex Eze, Daniel Key, John Booth, Shiren Patel, Jonny Pearson, Dan Schofield, Jonathan Hope, Pavithra Rajendran, Neil Sebire
- 发布时间: 2026-04-05T16:15:39Z
- 分类: cs.CL, cs.IR
- 相关性评分: 6
- 主题标签: 临床文档解析、小型语言模型、半自动化工作流、隐私保护、问答任务

**中文摘要**

> 电子患者记录（EPR）系统包含有价值的临床信息，但其中大部分信息被困在非结构化文本中，限制了其在研究和决策中的使用。大语言模型可以提取此类信息，但需要在本地运行大量计算资源，并且将敏感的临床数据发送到基于云的服务（即使去标识化）也会引发重大的患者隐私问题。在本研究中，开发了一种资源高效的半自动化标注工作流，使用小型语言模型（SLMs）从非结构化EPR数据中提取结构化信息，重点关注儿科组织病理学报告。作为概念验证，将工作流应用于儿科肾活检报告，选择该领域是因为其受限的诊断范围和明确的潜在生物学。通过三次会议与临床监督迭代开发工作流，从Great Ormond Street Hospital的2111份报告中手动标注400份作为黄金标准，同时开发使用SLMs的自动化信息提取方法。将提取框架为基于临床指导实体指南和少样本示例的问答任务，评估五个指令调优的SLMs，并使用分歧建模框架优先考虑临床审查的报告。Gemma 2 2B达到最高准确率84.3%，优于现成模型包括spaCy（74.3%）、BioBERT-SQuAD（62.3%）、RoBERTa-SQuAD（59.7%）和GLiNER（60.2%）。实体指南将性能比零样本基线提高了7-19%，少样本示例进一步提升了效果。

**核心创新概述**

> 针对临床文档解析，提出资源高效的半自动化工作流，使用小型语言模型在隐私敏感环境中提取结构化信息，并通过临床监督和实体指南优化性能。

**创新点拆解**

- 方法设计：将信息提取框架为问答任务，结合临床指导实体指南和少样本示例。
- 数据：使用分歧建模框架优先处理需要临床审查的报告，提高标注效率和质量。
- 训练范式：评估多个指令调优的SLMs，选择最佳模型（Gemma 2 2B）用于实际应用。

**当前局限**

> 工作流主要针对特定领域（儿科肾活检报告），泛化到其他临床文档类型可能需要额外调整；自动化提取的准确率仍有提升空间。

**后续可改进方向**

- 扩展工作流到更多临床文档类型，如放射学报告或出院摘要，以验证通用性。
- 集成多模态信息（如图像或表格）以提升提取的全面性。
- 优化SLMs的微调策略，进一步提高在少样本设置下的性能。

**工程启发**

> 高，为医疗领域的文档解析提供了隐私保护且资源高效的解决方案，可直接应用于临床数据管理，支持研究和决策。

**为什么值得关注**

> 涉及文档解析在特定领域（医疗）的应用，对OCR技术在处理敏感和非结构化文本时的实际部署有参考价值。

**原始摘要**

Electronic Patient Record (EPR) systems contain valuable clinical information, but much of it is
trapped in unstructured text, limiting its use for research and decision-making. Large language
models can extract such information but require substantial computational resources to run locally,
and sending sensitive clinical data to cloud-based services, even when deidentified, raises
significant patient privacy concerns. In this study, we develop a resource-efficient semi-automated
annotation workflow using small language models (SLMs) to extract structured information from
unstructured EPR data, focusing on paediatric histopathology reports. As a proof-of-concept, we
apply the workflow to paediatric renal biopsy reports, a domain chosen for its constrained
diagnostic scope and well-defined underlying biology. We develop the workflow iteratively with
clinical oversight across three meetings, manually annotating 400 reports from a dataset of 2,111 at
Great Ormond Street Hospital as a gold standard, while developing an automated information
extraction approach using SLMs. We frame extraction as a Question-Answering task grounded by
clinician-guided entity guidelines and few-shot examples, evaluating five instruction-tuned SLMs
with a disagreement modelling framework to prioritise reports for clinical review. Gemma 2 2B
achieves the highest accuracy at 84.3%, outperforming off-the-shelf models including spaCy (74.3%),
BioBERT-SQuAD (62.3%), RoBERTa-SQuAD (59.7%), and GLiNER (60.2%). Entity guidelines improved
performance by 7-19% over the zero-shot baseline, and few-shot examples by 6-38%, though their
benefits do not compound when combined. These results demonstrate that SLMs can extract structured
information from specialised clinical domains on CPU-only infrastructure with minimal clinician
involvement. Our code is available at https://github.com/gosh-dre/nlp_renal_biopsy.

---
