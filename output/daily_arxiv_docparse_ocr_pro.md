# OCR / 文档解析研究日报（2026-05-23）

## 报告说明

- 检索源：arXiv API
- 检索查询：`(all:"document parsing" OR all:"document understanding" OR all:"optical character recognition" OR all:OCR OR all:"layout analysis" OR all:"document layout analysis" OR all:"text recognition" OR all:"table recognition" OR all:"form understanding" OR all:"document intelligence" OR all:"page understanding" OR all:"scene text recognition" OR all:"handwritten text recognition" OR all:"information extraction") AND (cat:cs.CV OR cat:cs.AI OR cat:cs.CL OR cat:eess.IV)`
- 生成时间（UTC）：`2026-05-23 04:52:28`
- 大模型综合分析：`开启`

## 一、今日执行摘要

> 今日 OCR/文档解析研究重点关注多页文档解析标准化基准的建立以及票据文档理解中层次化推理能力的提升。MPDocBench-Parse 首次系统评估了多页文档的语义连续性和层级结构恢复，揭示了现有模型的显著短板；ReceiptBench 通过细粒度子任务划分和度量感知 GRPO 训练方法，在复杂票据推理上超越闭源模型。此外，分布式图像压缩中引入多模态侧信息的技术为文档压缩与传输提供了新思路。

## 二、今日趋势判断

文档解析正从单页、简单版面向多页、复杂语义和层级结构恢复演进，评估标准趋于细粒度、面向实际应用。文档理解方面，层次化推理和严格格式规范化成为关键挑战，强化学习与度量感知训练成为提升结构一致性的有效手段。多模态侧信息在图像压缩中的应用展示了跨模态信息融合在文档处理领域的潜力。

## 三、今日论文概览

1. **MPDocBench-Parse: Benchmarking Practical Multi-page Document Parsing** | 标签：文档解析、多页文档、基准评估、语义连续性、版面分析
2. **From Recognition to Reasoning: Benchmarking and Enhancing MLLMs on Real-World Receipt Document Understanding** | 标签：文档理解、信息提取、票据OCR、层次化任务、强化学习
3. **Distributed Image Compression with Multimodal Side Information at Extremely Low Bitrates** | 标签：分布式图像压缩、多模态、扩散模型、侧信息、极低比特率

## 四、今天 OCR / 文档解析论文里的主要创新点

- 构建大规模、多类型、多层次评估基准，覆盖多种文档类型和复杂版面。
- 设计细粒度、层次化的子任务划分（如基础感知、格式规范化、语义推理），推动模型能力的分级评估。
- 提出基于强化学习的训练方法（如度量感知GRPO），将评估指标直接转化为优化信号。
- 利用多模态侧信息（文本、视觉）增强极低比特率下的图像重建质量。

## 五、后续 OCR 领域值得推进的改进方向

- 扩展MPDocBench-Parse基准至更多语种和文档类型（如古籍、表格密集文档），并加入用户感知质量评估。
- 设计能联合建模多页语义连贯性与层级结构的端到端文档解析模型，可考虑基于Transformer的序列到图架构。
- 将ReceiptBench的层次化任务范式推广到通用文档理解，并探索自动化度量定义以减少人工标注依赖。
- 利用扩散模型或LLM增强文档压缩中的语义重建，尤其在极低比特率下保持表格、公式等结构的保真度。
- 研究文档压缩与解析的联合优化框架，从压缩端提取语义侧信息辅助解析，或在解析中利用压缩先验。

## 六、工程落地启发

- 评估多页文档解析时，必须包含语义连续性、截断内容合并和层级结构恢复的指标，避免仅用单页准确率误导。
- ReceiptBench的度量感知GRPO框架可直接用于票据自动化处理系统，提升格式规范性和推理准确率。
- 极低比特率压缩场景下，可利用预训练的文生图模型（如扩散模型）结合文本侧信息进行高质量重建。

## 七、优先关注论文

- **MPDocBench-Parse: Benchmarking Practical Multi-page Document Parsing**：为多页文档解析提供了首个系统级评估工具，其细粒度指标和实验结论直接揭示了当前模型的瓶颈，后续研究优化方向可参考其发现的不足（如语义连续性）。
- **From Recognition to Reasoning: Benchmarking and Enhancing MLLMs on Real-World Receipt Document Understanding**：度量感知GRPO方法显著提升了结构化推理任务性能，其层次化任务划分范式（感知→格式→语义→结构）有望推广至其他文档类型，值得跟踪其在通用领域的扩展工作。
- **Distributed Image Compression with Multimodal Side Information at Extremely Low Bitrates**：多模态侧信息融合策略在压缩场景的成功应用可能启发文档压缩与解析的联合优化，例如利用OCR文本作为侧信息改善文档图像的压缩与重建。

## 八、论文逐篇解析

### 1. MPDocBench-Parse: Benchmarking Practical Multi-page Document Parsing

- arXiv: [2605.22100v1](https://arxiv.org/abs/2605.22100v1)
- PDF: [下载链接](https://arxiv.org/pdf/2605.22100v1)
- 作者: Bangbang Zhou, Hangdi Xing, Yifan Chen, Jianjun Xu, Qi Zheng, Feiyu Gao, Zhibo Yang, Shuai Bai, Ming Yan, Jieping Ye, Hongtao Xie
- 发布时间: 2026-05-21T07:36:41Z
- 分类: cs.AI
- 相关性评分: 22
- 主题标签: 文档解析、多页文档、基准评估、语义连续性、版面分析

**中文摘要**

> 现有文档解析基准多聚焦单页或特定任务，缺乏对多页、复杂版面、语义连贯性和层级结构恢复的细粒度评估。因此提出MPDocBench-Parse，一个多页文档解析基准，包含433份文档（3246页），覆盖15种类型，支持文档级端到端评估，并设计了涵盖内容保真度和逻辑结构的评估协议。实验显示现有模型在语义连续性集成、视觉内容解析和层级结构恢复上存在显著局限。

**核心创新概述**

> 首次系统性地构建了面向多页文档解析的综合基准，并设计了细粒度评估协议，覆盖语义连续性、层级结构恢复等现有基准忽略的维度。

**创新点拆解**

- 构建了包含433份文档、3246页的多页文档解析基准，覆盖15种中英文文档类型
- 设计了文档级端到端评估协议，包含文本/表格/公式识别、截断内容合并、阅读顺序和标题层级恢复等
- 揭示了现有模型在语义连续性集成、视觉内容解析和层级结构恢复方面的明显不足

**当前局限**

> 基准仅覆盖中英文文档，未包含更多语言和文档类型; 评估指标仍以标准格式为主，未纳入用户主观质量评估。

**后续可改进方向**

- 扩展基准语言和文档类型覆盖
- 设计能更好处理语义连贯性和层级结构的文档解析模型
- 引入用户导向的评估方法，如感知质量评估

**工程启发**

> 为多页文档解析提供了标准化评估工具，可帮助工业界评估和优化文档处理系统的性能。

**为什么值得关注**

> 直接关联文档解析核心任务，提出的基准和评估协议对OCR研究者和工程师评估模型在实际多页文档场景中的表现有重要参考价值。

**原始摘要**

Document parsing converts visually rich documents into machine-readable structured representations,
forming a crucial foundation for information systems. Although many benchmarks have been proposed
for document parsing, they remain inadequate for realistic scenarios. Existing benchmarks either
focus on specific tasks or assess only single-page, text-centric settings, making them insufficient
for practical multi-page parsing. Moreover, they lack fine-grained evaluation of semantic
continuity, hierarchical structure recovery, and visual content preservation. To address these gaps,
we propose MPDocBench-Parse, a benchmark for multi-page document parsing in real-world applications.
It contains 433 manually annotated documents with 3,246 pages, covering 15 document types in English
and Chinese, with diverse layout styles, and supports document-level end-to-end evaluation. We
further design a comprehensive protocol for content fidelity and logical structure, covering text,
table, and formula recognition, truncated text and table merging, figure extraction, reading order,
and heading hierarchy recovery. Experiments show that, while existing models perform well on basic
text extraction, they still suffer clear limitations in semantic continuity integration, visual
content parsing, and hierarchical structure recovery. MPDocBench-Parse provides a unified foundation
for advancing document parsing toward more realistic scenarios.

---

### 2. From Recognition to Reasoning: Benchmarking and Enhancing MLLMs on Real-World Receipt Document Understanding

- arXiv: [2605.22413v1](https://arxiv.org/abs/2605.22413v1)
- PDF: [下载链接](https://arxiv.org/pdf/2605.22413v1)
- 作者: Yandi Wang, Libin Zhan, Ziwei Huang, Tiancheng Luo, Yuxuan Jiang, Wang Dong, Leilei Gan, Jun Chen
- 发布时间: 2026-05-21T12:37:03Z
- 分类: cs.CV
- 相关性评分: 17
- 主题标签: 文档理解、信息提取、票据OCR、层次化任务、强化学习

**中文摘要**

> 现有文档理解基准规模小、缺乏语义粒度，提出ReceiptBench基准（10k张真实票据），并划分四个层次子任务：基础感知、格式规范化、语义推理和结构解析。提出两阶段训练框架，包含度量感知GRPO，将评估约束转化为强化学习信号，提升结构一致性，在复杂推理任务上超越GPT-4V等闭源模型。

**核心创新概述**

> 首次构建大规模、细粒度层次化的票据文档理解基准，并提出度量感知GRPO训练方法，将严格的评估约束转化为强化学习信号。

**创新点拆解**

- 构建了10k张真实票据的基准，包含四个层次化子任务
- 提出度量感知GRPO训练框架
- 在复杂推理任务上达到最优，超越闭源模型

**当前局限**

> 仅针对收据，未验证泛化到其他文档类型; GRPO依赖精确度量定义。

**后续可改进方向**

- 扩展到更多文档类型
- 探索自动化度量设计
- 结合语言模型增强推理能力

**工程启发**

> 为票据自动化处理提供实用解决方案，适用于需要严格格式和结构一致性的商业场景。

**为什么值得关注**

> 针对文档理解核心任务，提出基准和有效方法，对OCR实际应用有直接价值。

**原始摘要**

Extracting structured information from visual documents (Visual Information Extraction, VIE) is a
cornerstone of business automation. While recent Multimodal Large Language Models (MLLMs) have shown
promising capabilities, existing benchmarks suffer from critical limitations in scale and realism,
lack semantic granularity, and fail to cover diverse document types. To bridge this gap, we
introduce ReceiptBench, a large-scale, human-annotated benchmark consisting of 10k diverse receipts,
organizing information extraction into four hierarchical sub-tasks: (1) Basic Perception for raw
text spotting, (2) Format Normalization for strictly following standardization instructions, (3)
Semantic Reasoning for inferring implicit attributes from context, and (4) Structure Parsing for
handling nested line items. Furthermore, we propose a two-stage training framework incorporating
Metric-Aware Group Relative Policy Optimization (GRPO), which translates rigorous evaluation
constraints into reinforcement learning signals to enhance structural consistency. Extensive
experiments demonstrate that our method yields state-of-the-art performance, surpassing leading
proprietary models on complex reasoning tasks. We release our datasets and code at
https://github.com/wwwT0ri/ReceiptBench.

---

### 3. Distributed Image Compression with Multimodal Side Information at Extremely Low Bitrates

- arXiv: [2605.22061v1](https://arxiv.org/abs/2605.22061v1)
- PDF: [下载链接](https://arxiv.org/pdf/2605.22061v1)
- 作者: Guojun Xu, Mingyang Zhang, Jianwen Xiang, Cheng Tan, Yanchao Yang, Junwei Zhou
- 发布时间: 2026-05-21T06:53:03Z
- 分类: cs.CV
- 相关性评分: 3
- 主题标签: 分布式图像压缩、多模态、扩散模型、侧信息、极低比特率

**中文摘要**

> 针对极低比特率下的分布式图像压缩，提出多模态分布式图像压缩（MDIC）框架，首次在多模态方式下利用侧信息。通过文本到图像扩散解码器结合文本侧信息捕获全局语义，设计特征掩码生成器，利用多模态细粒度对齐任务强化视觉侧信息利用，在KITTI Stereo和Cityscapes数据集上取得显著性能提升。

**核心创新概述**

> 首次将多模态侧信息融入分布式图像压缩框架，通过文本到图像扩散解码器捕获全局语义，并设计特征掩码生成器强化视觉侧信息。

**创新点拆解**

- 提出文本到图像扩散解码器，利用文本侧信息捕获全局语义
- 设计特征掩码生成器，通过多模态细粒度对齐任务强化视觉侧信息利用
- 特征掩码同时用于从无损传输的侧信息提取细节和从量化VQ-VAE嵌入中补偿类别信息

**当前局限**

> 仅验证了KITTI Stereo和Cityscapes两个自动驾驶数据集，需在更多场景验证; 依赖文本侧信息的提取质量。

**后续可改进方向**

- 探索更鲁棒的文本侧信息提取方法
- 扩展到更多任务和数据集
- 研究多模态融合的更深层次方式，如自适应权重分配

**工程启发**

> 为极低带宽场景下的图像压缩提供新思路，尤其适用于多摄像头系统（如自动驾驶）的高效传输与重建。

**为什么值得关注**

> 虽然主题为图像压缩，但其多模态侧信息利用的思想可启发文档解析中利用文本和视觉信息的融合策略。

**原始摘要**

Distributed Image Compression (DIC) is crucial for multi-view transmission, especially when
operating at extremely low bitrates (< 0.1 bpp). Its core challenge is effectively utilizing side
information to achieve high-quality reconstruction under strict bitrate budgets. However, existing
DIC approaches struggle to exploit global context and object-level details from side information,
leading to local blurring and the loss of fine details in the reconstruction. To address these
limitations, we propose a Multimodal DIC framework (MDIC), which, for the first time, leverages side
information in a multimodal manner into the DIC paradigm, effectively preserving fine-grained local
details and enhancing global perceptual quality in reconstructed images. Specifically, we introduce
a text-to-image diffusion-based decoder conditioned on textual side information extracted from
correlated images to capture shared global semantics. Moreover, we design a feature-mask generator,
supervised by a multimodal fine-grained alignment task, to strengthen the exploitation of visual
side information. The generated mask serves two purposes: first, it guides the extraction of fine-
grained details from losslessly transmitted side information to preserve the semantic consistency of
reconstructed details; second, it regulates the extraction of clustered feature representations from
the quantized VQ-VAE embeddings, compensating for category information lost under the extreme
compression of the primary image. Extensive experiments on the widely used KITTI Stereo and
Cityscapes datasets demonstrate that MDIC achieves state-of-the-art perceptual quality at extremely
low bitrates.

---
