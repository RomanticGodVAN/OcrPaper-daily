# OCR / 文档解析研究日报（2026-10-15）

## 报告说明

- 检索源：arXiv API
- 检索查询：`(all:"document parsing" OR all:"document understanding" OR all:"optical character recognition" OR all:OCR OR all:"layout analysis" OR all:"document layout analysis" OR all:"text recognition" OR all:"table recognition" OR all:"form understanding" OR all:"document intelligence" OR all:"page understanding" OR all:"scene text recognition" OR all:"handwritten text recognition" OR all:"information extraction") AND (cat:cs.CV OR cat:cs.AI OR cat:cs.CL OR cat:eess.IV)`
- 生成时间（UTC）：`2026-10-15 05:53:19`
- 大模型综合分析：`开启`

## 一、今日执行摘要

> 今日论文围绕OCR与文档解析的评估细化、长文档结构重建、多模态统一解析和推理效率展开。核心进展包括：提出严重性加权CER和字符级渲染验证器以弥补传统指标对关键错误不敏感的问题；利用逐级多模态记忆和统一数据集提升长文档标题层级与视觉元素描述的结构化输出能力；通过训练无关的视觉token剪枝在保持OCR等细粒度任务性能的同时大幅降低推理成本。工业界关注电商主图生成和GUI定位的端到端方案，但长文档结构一致性与记忆遗忘等开放问题仍未解决。

## 二、今日趋势判断

文档解析正从孤立任务（布局、识别、描述）走向统一建模与结构一致性输出；评估指标开始引入人类感知和字符级验证，而非仅依赖CER或整体相似度；多模态大模型推理加速与视觉token剪枝成为提升OCR细粒度任务可行性的关键路径；工业级应用（电商主图、GUI自动化）推动数据合成、强化学习与多条件生成技术的落地，但长文档级结构重建和记忆管理仍缺乏系统性解决方案。

## 三、今日论文概览

1. **Heading Hierarchy Reconstruction for Complex and Long Documents with Level-Wise Multimodal Memory** | 标签：文档解析、标题层级重建、多模态记忆、视觉语言模型、长文档、基准测试
2. **Read, Parse, Describe: Unified Document Parsing with Visual Element Description Generation** | 标签：文档解析、视觉元素描述、统一数据集、空间感知增强、阅读顺序、视觉语言模型
3. **Efficient Scene-Text Refinement via Pixel-Space Grouped Image Generation** | 标签：场景文本精修、像素空间生成、MeanFlow、生成图像、OCR准确率、基准测试
4. **CommerceGen-Studio: An End-to-End Framework for Commercial-Grade Main-Image Generation** | 标签：电商主图生成、端到端框架、多条件生成、强化学习、文本准确性、工业部署
5. **Equal CER, Unequal Damage: Severity-Weighted Character Error Rate for OCR** | 标签：OCR评估、字符错误率、严重性加权、LLM评判、多语言、基准测试
6. **TextVerifier: Seeing Beyond Recognition to Verify Chinese Text Rendering** | 标签：文本渲染验证、汉字生成、表意文字描述序列、基准测试、强化学习后训练、OCR
7. **Bifocal: Training-Free Mixed Granularity Visual Token Pruning for Multimodal LLMs** | 标签：多模态大模型、视觉token剪枝、OCR、视觉定位、推理加速
8. **GroundGUI: GUI Grounding by High-Quality Data and Distillation-to-Reinforcement Learning** | 标签：GUI定位、多模态大模型、数据集构建、强化学习、蒸馏
9. **Can Agents Forget When Asked? A Benchmark for Memory Unlearning in LLM Agents** | 标签：LLM智能体、记忆遗忘、基准测试、隐私、长期记忆
10. **MMKG-R1: Constructing Multimodal Knowledge Graphs via Reinforcement Learning** | 标签：多模态知识图谱、强化学习、RAG、多模态大模型、知识抽取

## 四、今天 OCR / 文档解析论文里的主要创新点

- 将文档级结构重建（如标题层级）形式化为增量式多模态记忆问题，突破VLM上下文长度限制
- 构建统一的多模态文档解析基准，同时评估布局、阅读顺序、文本识别和视觉元素描述生成
- 采用强化学习或LLM评判为OCR/渲染错误赋予严重性权重，使评估更贴近人类感知
- 设计训练无关的混合粒度视觉token剪枝方法，在细粒度OCR任务上保持高保留率的同时减少计算量
- 利用字符结构先验（如表意文字描述序列）提升生成文本的渲染验证准确率
- 在工业生成框架中引入多阶段强化学习和渐进训练，联合优化主体、商标和字符级文本保真度

## 五、后续 OCR 领域值得推进的改进方向

- 研发面向长文档的全局结构一致性评估指标，将标题层级、阅读顺序和跨页引用关系纳入统一评测
- 探索将严重性加权CER与字符渲染验证器结合，构建端到端的OCR质量优化闭环，并将验证信号反馈给生成模型训练
- 扩展Bifocal等训练无关剪枝方法到多图、视频和动态文档场景，验证其在OCR密集任务上的泛化性和延迟收益
- 设计支持多模态记忆遗忘的文档管理系统架构，在保证长文档结构记忆的同时满足用户删除请求和隐私合规
- 构建涵盖更多领域（法律、医疗、工程图纸）的统一文档解析基准，并测试现有模型在跨领域联合任务上的泛化能力
- 研究将视觉元素描述生成与多模态知识图谱构建联动，使文档解析输出可直接用于RAG和结构化知识抽取

## 六、工程落地启发

- 严重性加权CER可作为OCR和VLM评估的补充指标，在医疗、法律等文本质量敏感场景中优先关注关键字符错误
- 逐级多模态记忆框架可直接集成到长文档解析流水线，通过锚点选择策略控制内存和计算开销，适合RAG前处理
- Bifocal等训练无关视觉token剪枝方法能在资源受限设备上保持超过90%的OCR性能，建议在部署多模态大模型时评估
- 字符级渲染验证器（如TextVerifier）可作为生成式文本图像的质量门控，集成到广告设计、电商主图生成流水线中
- 统一文档解析数据集和空间感知增强器为端到端文档理解模型提供标准化训练和评估基础，建议在内部文档处理系统中参考其任务定义
- 电商主图生成框架的三阶段流水线（信息提取、语义重写、多条件生成）和渐进训练策略对工业级多条件生成任务有直接参考价值

## 七、优先关注论文

- **Heading Hierarchy Reconstruction for Complex and Long Documents with Level-Wise Multimodal Memory**：首次将文档级标题层级重建形式化为增量式多模态记忆问题，并发布大规模专家标注基准，对长文档结构解析和RAG应用有直接推动作用，但锚点策略简单，需关注后续优化。
- **Read, Parse, Describe: Unified Document Parsing with Visual Element Description Generation**：提出统一文档解析任务和大规模多模态基准，并要求模型同时输出布局、阅读顺序和视觉元素描述，可能改变文档理解系统的评估范式，但领域覆盖有限，需观察扩展性。
- **Efficient Scene-Text Refinement via Pixel-Space Grouped Image Generation**：将局部文本精修定义为像素空间分组生成，以极低生成成本实现高字符准确率，对生成图像文本质量提升有直接工程价值，但需验证在大范围编辑和自然场景中的适用性。
- **Equal CER, Unequal Damage: Severity-Weighted Character Error Rate for OCR**：提出基于LLM评判的严重性加权CER，并提供多语言人工评分数据，可能成为OCR评估的新标准，但依赖LLM评判的一致性和跨语言泛化性仍需验证。
- **TextVerifier: Seeing Beyond Recognition to Verify Chinese Text Rendering**：首次形式化文本渲染验证任务，利用IDS和字符级标注基准显著超越OCR置信度和通用VLM，对生成式文本图像的质量控制有直接应用潜力，但仅限中文，需观察多语言扩展。
- **Bifocal: Training-Free Mixed Granularity Visual Token Pruning for Multimodal LLMs**：训练无关的混合粒度剪枝在OCR和视觉定位任务上保持高保留率，为多模态大模型推理加速提供可直接部署方案，但需关注实际延迟和注意力质量敏感性。
- **CommerceGen-Studio: An End-to-End Framework for Commercial-Grade Main-Image Generation**：端到端电商主图生成框架已实现每天数百万张的工业部署，其多阶段流水线和渐进训练策略对商业级生成任务有高参考价值，但依赖专有数据，复现难度大。
- **Can Agents Forget When Asked? A Benchmark for Memory Unlearning in LLM Agents**：首次基准测试LLM智能体记忆遗忘，揭示所有系统端到端通过率不超过1.5%，对文档管理系统中用户删除请求和隐私合规设计有重要警示意义。

## 八、论文逐篇解析

### 1. Heading Hierarchy Reconstruction for Complex and Long Documents with Level-Wise Multimodal Memory

- arXiv: [2610.18238v1](https://arxiv.org/abs/2610.18238v1)
- PDF: [下载链接](https://arxiv.org/pdf/2610.18238v1)
- 作者: Qian Chen, Xianyin Zhang, Lifan Guo, Chi Zhang
- 发布时间: 2026-10-13T12:06:28Z
- 分类: cs.CV, cs.AI
- 相关性评分: 26
- 主题标签: 文档解析、标题层级重建、多模态记忆、视觉语言模型、长文档、基准测试

**中文摘要**

> 针对视觉语言模型在文档解析中逐页预测导致标题层级缺乏文档级一致性的问题，提出基于VLM的框架，通过逐级多模态记忆增量重建标题层级。记忆由锚点选出的紧凑历史页面子集构成，支持灵活锚点选择，本文选取每级最新节点，使VLM能观察各级标题的视觉、文本和布局模式。同时发布CLDoc-HHRBench，包含250个文档、11212页专家验证标注。在CLDoc-HHRBench和三个现有基准上验证了方法有效性。

**核心创新概述**

> 首次将文档级标题层级重建形式化为增量式多模态记忆问题，并设计了基于锚点的逐级记忆机制，突破了VLM输入分辨率和上下文长度限制。

**创新点拆解**

- 提出逐级多模态记忆机制，增量式重建标题层级，避免全文档联合处理
- 设计灵活的锚点选择策略，本文选取每级最新节点以保留各级标题模式
- 构建CLDoc-HHRBench，涵盖250个文档、11212页的专家验证标注，支持长文档标题层级评估

**当前局限**

> 锚点选择策略较为简单（仅取每级最新节点），可能无法充分覆盖复杂层级变化；未与其他记忆压缩方法进行对比；评估主要限于标题层级重建，未验证对下游RAG任务的实际增益。

**工程启发**

> 为长文档解析和结构化输出提供了可落地的VLM框架，直接支持RAG等下游应用对文档级结构的需求，具有较高的工程实用价值。

**为什么值得关注**

> 该工作直接针对OCR/文档解析中的文档级结构重建问题，利用多模态记忆提升长文档标题层级一致性，属于文档解析的前沿方向。

**原始摘要**

Vision-language models (VLMs) have been widely adopted for document parsing and optical character
recognition (OCR), as they can accurately extract page-level elements. However, downstream
applications such as retrieval-augmented generation (RAG) also require coherent document-level
structure. Although these models indicate heading levels using different numbers of preceding ``\#''
symbols, page-by-page prediction often lacks document-level consistency. In practice, input-
resolution and context-length constraints make it infeasible for a VLM to jointly process all page
images in documents containing tens or hundreds of pages. To address this limitation, we propose a
VLM-based framework that incrementally reconstructs heading hierarchies with a \emph{level-wise
multimodal memory}. The memory retains a compact subset of all previously processed pages, selected
by anchors. Our framework supports flexible anchor selection, and in this work we select the most
recent node at each level, allowing the VLM to observe the visual, textual, and layout patterns of
headings at every level. For comprehensive evaluation, we also introduce the Complex and Long
Document Heading Hierarchy Reconstruction Benchmark (CLDoc-HHRBench), comprising 250 documents and
11,212 pages with expert-verified annotations. Experiments on CLDoc-HHRBench and three existing
benchmarks demonstrate the effectiveness of our method.

---

### 2. Read, Parse, Describe: Unified Document Parsing with Visual Element Description Generation

- arXiv: [2610.20335v1](https://arxiv.org/abs/2610.20335v1)
- PDF: [下载链接](https://arxiv.org/pdf/2610.20335v1)
- 作者: Yuheng Chen, Yufan Chen, Zhuojun Cai, Ruiping Liu, Junwei Zheng, Jiale Wei, Di Wen, Weijia Fan, Kunyu Peng, Jiaming Zhang, Rainer Stiefelhagen
- 发布时间: 2026-10-14T15:17:28Z
- 分类: cs.CV, cs.AI
- 相关性评分: 24
- 主题标签: 文档解析、视觉元素描述、统一数据集、空间感知增强、阅读顺序、视觉语言模型

**中文摘要**

> 针对文档理解系统通常分离评估布局分析、文本识别、阅读顺序预测和图像描述，导致科学图表、标题与视觉语义连接薄弱的问题，提出Read-Parse-Describe统一数据集，要求模型对页面图像输出有序布局元素列表，包含边界框、语义标签、阅读顺序索引、识别文本内容以及视觉元素的替代文本描述。基准包含2402个文档、18163页、125218个布局元素和11338个视觉实例。同时提出即插即用的空间感知增强器，重用多层视觉特征并向视觉语言令牌注入网格感知空间引导。实验表明现有系统难以联合恢复阅读顺序和视觉语义，而增强模型实现了强联合性能。

**核心创新概述**

> 首次将文档解析与视觉元素描述生成统一为单一任务，并构建了大规模多模态文档解析基准，同时提出空间感知增强器提升布局感知生成。

**创新点拆解**

- 定义统一文档解析任务，输出有序布局元素列表并生成视觉元素替代文本描述
- 构建Read-Parse-Describe数据集，涵盖2402个文档、18163页、125218个布局元素和11338个视觉实例
- 提出即插即用的空间感知增强器，重用多层视觉特征并注入网格感知空间引导

**当前局限**

> 数据集主要针对科学文档，领域覆盖有限；增强器为通用插件，未深入探索不同架构的适配性；评估指标可能未充分衡量描述生成的质量。

**工程启发**

> 为文档理解系统提供了统一的评估基准和增强模块，有助于推动端到端文档解析模型的研发，在自动化文档处理、无障碍阅读等场景具有应用潜力。

**为什么值得关注**

> 该工作直接涉及OCR和文档解析，通过统一任务定义和数据集推动文档理解从孤立模块向联合模型发展，与OCR研究密切相关。

**原始摘要**

Document understanding systems are typically evaluated as separate components via layout analysis,
optical text recognition, reading-order prediction, and image captioning. This separation leaves
scientific figures, captions, and visual semantics weakly connected, and fails to measure whether a
model can produce a single page-level parse that is both structurally faithful and semantically
accessible. We introduce Read-Parse-Describe, a unified dataset for document parsing with visual
element description generation. Given a page image, models are required to output an ordered list of
layout elements containing bounding boxes, semantic labels, reading-order indices, recognized
textual content, and alternative text descriptions for visual elements. The benchmark is built from
2,402 documents, comprising 18,163 continuous pages, 125,218 layout elements, and 11,338 visual
instances. Besides, we further propose a plug-and-play space-awareness enhancer that reuses multi-
layer visual features and injects grid-aware spatial guidance into vision-language tokens for
layout-aware generation. Experiments across end-to-end VLMs and pipeline parsers show that existing
systems still struggle to jointly recover reading order and visual semantics, while our enhanced
model achieves strong joint performance. These results highlight the need to move beyond isolated
document parsing modules toward unified models that jointly read, parse, and describe complex
documents. The new dataset and code will be made publicly available at
https://github.com/yufanchen96/RPD

---

### 3. Efficient Scene-Text Refinement via Pixel-Space Grouped Image Generation

- arXiv: [2610.18284v1](https://arxiv.org/abs/2610.18284v1)
- PDF: [下载链接](https://arxiv.org/pdf/2610.18284v1)
- 作者: Yaoli Liu, Guo-Hua Wang, Yiyang Chen, Qing-Guo Chen, Zhao Xu, Weihua Luo, Yao-Xiang Ding
- 发布时间: 2026-10-13T12:34:42Z
- 分类: cs.CV
- 相关性评分: 13
- 主题标签: 场景文本精修、像素空间生成、MeanFlow、生成图像、OCR准确率、基准测试

**中文摘要**

> 针对生成图像中小文本和复杂字符局部错误影响可读性的问题，提出PixText，将局部文本精修形式化为像素空间的分组图像生成。基于原始图像条件，仅生成目标区域，保留未编辑内容，并使用MeanFlow进行四步生成。同时提出Text Refinement Bench评估文本纠正和图像保持。在基准上，PixText达到83.06%字形通过率和94.66%精确目标字符OCR准确率，远超最强基线的36.77%和52.31%。四步MeanFlow变体保持81.84%通过率，每张图像摊销生成成本低于1 GPU秒。

**核心创新概述**

> 首次将局部文本精修定义为像素空间的分组图像生成，采用MeanFlow实现高效四步生成，并构建了专门的文本精修基准。

**创新点拆解**

- 提出像素空间分组图像生成范式，仅生成目标区域，避免全图编辑导致的背景偏移
- 利用MeanFlow实现四步生成，平衡质量与效率
- 构建Text Refinement Bench，评估文本纠正和图像保持

**当前局限**

> 方法专注于局部文本精修，可能不适用于大范围文本编辑或复杂版面重构；MeanFlow的步骤数较少可能限制生成多样性；评估基准仅针对生成图像中的文本，未涵盖自然场景文本。

**工程启发**

> 为生成图像中的文本质量提升提供了高效解决方案，在广告设计、电商主图、社交媒体内容生成等场景具有直接应用价值。

**为什么值得关注**

> 该工作涉及OCR准确率评估和文本生成质量，与OCR技术中的文本识别和生成紧密相关，属于OCR在生成内容中的应用延伸。

**原始摘要**

Generated images often have coherent layouts and visual content, yet local errors in small text and
complex characters still limit their readability and practical use. Scene-text refinement requires
accuracy, preservation, and efficiency. Existing methods based on variational autoencoders (VAEs)
can lose fine strokes during reconstruction, while full-image editing can shift background colors.
In this work, we introduce PixText, a model that formulates local text refinement as grouped image
generation in pixel space. Conditioned on the original image, PixText generates only the target
regions, preserves unedited content, and uses MeanFlow for four-step generation. We further
introduce Text Refinement Bench to evaluate text correction and image preservation in generated
images. On this benchmark, PixText achieves 83.06% glyph pass and 94.66% exact target-character OCR
accuracy, versus 36.77% and 52.31% for the strongest baseline. Its four-step MeanFlow variant
retains an 81.84% pass rate with less than one GPU-second of amortized generation cost per image.

---

### 4. CommerceGen-Studio: An End-to-End Framework for Commercial-Grade Main-Image Generation

- arXiv: [2610.20603v1](https://arxiv.org/abs/2610.20603v1)
- PDF: [下载链接](https://arxiv.org/pdf/2610.20603v1)
- 作者: Xiaoli Xu, Zhengtao Wu, Zhengze Xu, Tao Liu, Yongchao Du, Zuan Gao, Xingjian Wang, Hao Yan, Mengting Chen, Wei Li, Bo Zheng
- 发布时间: 2026-10-14T17:59:48Z
- 分类: cs.CV
- 相关性评分: 10
- 主题标签: 电商主图生成、端到端框架、多条件生成、强化学习、文本准确性、工业部署

**中文摘要**

> 提出CommerceGen-Studio，一个端到端生成商业级电商主图的框架，包含信息提取、语义重写和多条件生成三阶段。PERL-Agent通过VLM和LLM迭代闭环将异构SKU元数据提炼为简洁卖点文本列表；LTO通过交替领域特定策略优化对齐重写器与标题和渲染图像质量；SKU-DiT在RDR渐进训练下联合以白底产品图、商标裁剪和结构化布局为条件，保持主体保真度、商标完整性和字符级文本准确性。框架每天处理数百万张主图，延迟几秒。发布CommerceGen-Bench，在编辑任务上总体得分最高，可匹配更大闭源模型。

**核心创新概述**

> 首次提出端到端商业级主图生成框架，整合信息提取、语义重写与多条件生成，并通过强化学习策略优化和渐进训练实现工业级部署。

**创新点拆解**

- 设计三阶段流水线：PERL-Agent信息提取、LTO语义重写、SKU-DiT多条件生成
- 提出Reinforce-Distill-Reinforce渐进训练策略，联合优化主体、商标和文本保真度
- 发布CommerceGen-Bench，涵盖全品类真实流量难例

**当前局限**

> 框架依赖大量专有数据和计算资源，复现难度高；评估主要针对电商主图，通用性有限；未详细讨论生成图像中文本准确性的具体错误类型。

**工程启发**

> 为电商行业提供了可规模化部署的主图生成方案，显著降低人工设计成本，提升商品展示效果，具有极高的商业应用价值。

**为什么值得关注**

> 该工作涉及字符级文本准确性生成，与OCR技术中的文本识别和生成质量评估相关，属于OCR在生成式AI中的工程应用。

**原始摘要**

We present CommerceGen-Studio, an end-to-end framework for generating commercial-grade main images
for e-commerce Stock Keeping Units (SKUs). Our framework is organized along a three-stage pipeline
of information extraction, semantic rewriting, and multi-condition generation: Prompt-Eval-Refine-
Loop Agent (PERL-Agent) distills heterogeneous SKU metadata into concise selling-point text lists
through an iterative closed loop of VLM and LLM roles scored by a reference-free rubric. Layout
Thinker Optimization (LTO) aligns the rewriter with both caption and rendered-image quality via
alternating domain-specific policy optimization. SKU-DiT, trained under Reinforce-Distill-Reinforce
(RDR) progressive training, conditions jointly on the white-background product image, the trademark
crop, and the structured layout to hold subject fidelity, trademark integrity, and character-level
text accuracy together. The framework runs in production at a scale of millions of main images per
day with a latency of a few seconds per image, which we believe makes it among the first systems of
this kind to operate at commercial scale. We also release CommerceGen-Bench, a benchmark of hard
cases collected from live traffic across all product categories. On it, our framework achieves the
highest overall scores among the evaluated open-source baselines on both editing tracks, with and
without prompt enhancement. It also matches much larger closed-source models, and beats several of
them at Instruction Following and Product Integration - the two properties that determine whether an
image can be published.

---

### 5. Equal CER, Unequal Damage: Severity-Weighted Character Error Rate for OCR

- arXiv: [2610.20461v1](https://arxiv.org/abs/2610.20461v1)
- PDF: [下载链接](https://arxiv.org/pdf/2610.20461v1)
- 作者: Nguyen Nguyen, Yongyi Zang
- 发布时间: 2026-10-14T16:44:22Z
- 分类: cs.CL, cs.AI, cs.CV
- 相关性评分: 9
- 主题标签: OCR评估、字符错误率、严重性加权、LLM评判、多语言、基准测试

**中文摘要**

> 针对字符错误率（CER）将拼写错误与错误名称同等计价的问题，提出semCER，保留CER的对齐和分母，由LLM评判为每个字素编辑赋予严重性，无需分词。归一化CER保持整体转录得分，semCER将其分解为具名编辑。在英语、越南语和中文中，评分与读者评分逐编辑跟踪，且将读者认为最严重的编辑排在排序列表顶部。在CER与semCER不一致的样本对上，读者更支持semCER。跨16种语言，评判对错误变音符号或声调的严重性赋值差异大。释放6100万评判编辑、聚合读者评分和蒸馏评分器。

**核心创新概述**

> 首次提出基于LLM评判的严重性加权字符错误率，突破传统CER对错误一视同仁的局限，并构建了多语言人工评分数据集。

**创新点拆解**

- 定义semCER，通过LLM为每个字素编辑赋予严重性权重，保留CER对齐和分母
- 构建多语言（16种）人工评分数据集，涵盖6100万编辑
- 提供可分解的具名编辑评分，支持错误严重性排序

**当前局限**

> 严重性评分依赖LLM评判，可能存在偏见或不一致；未在所有语言上验证与读者评分的一致性；计算复杂度高于传统CER。

**工程启发**

> 为OCR和VLM评估提供了更贴近人类感知的指标，有助于优化模型在关键错误上的表现，在文本质量敏感的应用（如医疗、法律）中具有实用价值。

**为什么值得关注**

> 该工作直接改进OCR核心评估指标，提出严重性加权的字符错误率，对OCR研究和应用具有重要影响。

**原始摘要**

Character Error Rate (CER), the standard metric for OCR and vision-language models (VLMs), charges a
typo as much as a wrong name. We introduce semCER, which keeps CER's alignment and denominator and
charges each grapheme edit a severity from an LLM judge, with no word segmentation. Normalized CER
keeps the score of a whole transcription, where it tracks readers as well as semCER or better, and
semCER breaks that score down into named edits. The charges track readers' ratings edit by edit in
English, Vietnamese, and Chinese and put the edits readers rate most severe near the top of a sorted
list. On pairs drawn where CER and semCER disagreed, readers side with semCER more often than with
normalized CER in English and Chinese, and equally often in Vietnamese. Across 16 languages, the
judge charges a wrong diacritic or tone mark almost nothing in Spanish but nearly a wrong letter's
severity in Telugu. Where we can count real words, a general VLM's wrong letter forms one far above
chance while a classical pipeline's stays near it. We release the 61 million judged edits, the
aggregated reader ratings, and the distilled scorer at https://github.com/nguyenx2t/semcer.

---

### 6. TextVerifier: Seeing Beyond Recognition to Verify Chinese Text Rendering

- arXiv: [2610.19551v1](https://arxiv.org/abs/2610.19551v1)
- PDF: [下载链接](https://arxiv.org/pdf/2610.19551v1)
- 作者: Yiyang Chen, Guo-Hua Wang, Yaoli Liu, Qing-Guo Chen, Zhao Xu, Weihua Luo, Xiujun Ma
- 发布时间: 2026-10-14T04:07:15Z
- 分类: cs.CV
- 相关性评分: 9
- 主题标签: 文本渲染验证、汉字生成、表意文字描述序列、基准测试、强化学习后训练、OCR

**中文摘要**

> 针对文本到图像模型生成的汉字存在局部渲染缺陷（如多笔少笔、部件畸形），而OCR和VLM对此不敏感的问题，将文本渲染验证形式化为目标条件问题：给定目标字符和图像裁剪，判断裁剪是否正确渲染该字符。TEXTVERIFIER向文本塔输入表意文字描述序列（IDS）而非单字符符号，在1270万裁剪-IDS对及无标签“同字不同质”难例上训练。构建TEXTRENDERBENCH-ZH，首个生成汉字逐字符基准，标注7358个字符的位置、身份和正确性。TEXTVERIFIER达到F1 0.844，远超OCR置信度（0.526）、通用VLM（0.329）和TextPecker（0.590）。作为Flow-GRPO后训练的逐字符奖励，进一步减少渲染错误。

**核心创新概述**

> 首次将文本渲染验证形式化为目标条件问题，并利用表意文字描述序列（IDS）增强字符结构感知，构建了首个生成汉字逐字符评估基准。

**创新点拆解**

- 提出目标条件文本渲染验证任务，区分识别与渲染验证
- 使用IDS替代单字符符号，增强对汉字结构的敏感度
- 构建TEXTRENDERBENCH-ZH，标注7358个生成汉字的位置、身份和正确性
- 将验证器作为Flow-GRPO的逐字符奖励，实现检测与纠正一体化

**当前局限**

> 目前仅针对中文汉字，未扩展至其他表意文字；依赖IDS输入，对未知字符或变体字可能受限；训练数据中的难例采样策略可能影响泛化性。

**工程启发**

> 为文本到图像生成中的文本质量验证提供了有效工具，可集成到生成流水线中提升输出可读性，在广告、设计、出版等领域有应用前景。

**为什么值得关注**

> 该工作涉及OCR与VLM在文本渲染验证中的局限性，提出专门验证方法，与OCR技术密切相关，属于OCR在生成内容质量保障中的新应用。

**原始摘要**

Text-to-image models increasingly generate readable Chinese text that still contains local rendering
defects, such as a character with an extra or missing stroke or a malformed component. Such errors
are invisible to OCR and vision-language models, which are trained for recognition and are therefore
invariant to the very structural deviations that define a rendering error. We formalize text
rendering verification as a target-conditioned problem: given a target character and an image crop,
decide whether the crop is a correct rendering of that character. Our verifier TEXTVERIFIER feeds
the text tower a character's Ideographic Description Sequence (IDS) rather than a single-character
symbol, and is trained on 12.7M crop-IDS pairs plus label-free "same-character, different-quality"
hard pairs sampled from the training trajectory of a text-region inpainting model. To evaluate this
ability we build TEXTRENDERBENCH-ZH, the first per-character benchmark for generated Chinese text,
annotating position, identity, and correctness for 7,358 characters. TEXTVERIFIER reaches an F1 of
0.844, far above OCR confidence (0.526), a general VLM (0.329), and TextPecker (0.590). Used as a
per-character reward for Flow-GRPO post-training, it further reduces rendering errors, showing that
its score can both detect and correct errors.

---

### 7. Bifocal: Training-Free Mixed Granularity Visual Token Pruning for Multimodal LLMs

- arXiv: [2610.18399v1](https://arxiv.org/abs/2610.18399v1)
- PDF: [下载链接](https://arxiv.org/pdf/2610.18399v1)
- 作者: Peiran Yin, Hao Wu, Zihao Yang, Fengyu Zhou, Yijuan Liang, Haozhe Hu, Xudong Wang, Wei Zhang, Xiaoyu Shen
- 发布时间: 2026-10-13T13:46:32Z
- 分类: cs.CV
- 相关性评分: 9
- 主题标签: 多模态大模型、视觉token剪枝、OCR、视觉定位、推理加速

**中文摘要**

> 针对多模态大模型视觉 token 剪枝中细粒度任务性能下降的问题，提出无需训练的混合粒度两阶段剪枝方法 Bifocal。方法在 LLM 前将问题词与视觉区域匹配，结合去偏图像显著性与软连接，并选择最大化表征覆盖的图像内在证据；在 LLM 内利用密度调整的文本到图像注意力进一步剪枝。仅保留约四分之一视觉 token 时，在三个模型家族和五类能力组上均保持超过 90% 的未剪枝性能，在九个模型预算设置中平均排名第一。

**核心创新概述**

> 首次系统揭示现有视觉 token 剪枝在 OCR 和视觉定位等细粒度任务上的严重退化，并提出训练无关的混合粒度剪枝框架，分别分配查询聚焦与图像内在证据预算，并加入全局粗粒度表示。

**创新点拆解**

- 提出两阶段训练无关剪枝方法，结合 LLM 前软连接匹配与 LLM 内密度调整注意力剪枝
- 设计混合粒度预算分配机制，为查询聚焦证据和图像内在证据分别设置 token 预算，并补充全局池化粗表示
- 通过去偏图像显著性与最大化表征覆盖选择图像内在证据，缓解稀疏 patch 选择对图像内容和空间完整性的破坏

**当前局限**

> 论文摘要未给出具体计算开销或推理延迟数据；方法依赖文本到图像注意力，可能对注意力质量敏感；未报告在视频或多图场景下的适用性。

**工程启发**

> 为多模态大模型推理加速提供可直接部署的训练无关剪枝方案，显著降低视觉 token 数量同时保持 OCR 等细粒度任务可用性，适合在资源受限场景中落地。

**为什么值得关注**

> 论文直接针对 OCR 相关细粒度任务在视觉 token 剪枝下的性能退化问题，并验证了在保留少量 token 时 OCR 能力不显著下降，对 OCR 系统与多模态模型结合具有直接参考价值。

**原始摘要**

Visual token pruning for multimodal large language models (MLLMs) appears highly effective, with
existing methods retaining over 95% of unpruned performance on common VQA benchmarks using a quarter
of the visual tokens or fewer. However, our extensive evaluation of ten methods across three MLLM
families and five ability groups reveals a critical gap: strong general performance often comes at
the cost of severe degradation on fine-grained tasks such as OCR and visual grounding. We trace
these failures to two limitations of the prevailing paradigm of retaining the highest-ranked native
patches. A single importance ranking overlooks the complementary evidence required by different
tasks, while sparse patch selection disrupts both image content and spatial integrity. To address
these limitations, we propose Bifocal, a training-free, two-stage pruning method built on a mixed-
granularity framework. It allocates separate budgets to query-focused and image-intrinsic evidence,
complemented by a pooled coarse representation of the entire image. Before the LLM, Bifocal matches
question words to visual regions through a soft conjunction balanced against norm-debiased image
saliency, while selecting image-intrinsic evidence to maximize representational coverage. Inside the
LLM, it further prunes tokens using density-adjusted text-to-image attention. With roughly a quarter
of the original visual tokens, Bifocal is the only evaluated method to retain over 90% of unpruned
performance in every ability group across all three models, and ranks first on average in all nine
model-budget settings. The code is available at: https://github.com/EIT-NLP/Bifocal

---

### 8. GroundGUI: GUI Grounding by High-Quality Data and Distillation-to-Reinforcement Learning

- arXiv: [2610.19100v1](https://arxiv.org/abs/2610.19100v1)
- PDF: [下载链接](https://arxiv.org/pdf/2610.19100v1)
- 作者: Qingsong Xie, Jiahao Tian, Jiacheng Tang, Zhifeng Li, Madalina Ciobanu, Navan Preet Singh, Qingqing Mao, Ritankar Das
- 发布时间: 2026-10-13T19:37:49Z
- 分类: cs.AI, cs.CL, cs.CV
- 相关性评分: 8
- 主题标签: GUI定位、多模态大模型、数据集构建、强化学习、蒸馏

**中文摘要**

> 针对 GUI 视觉定位高质量数据稀缺问题，构建 ScreenRef 数据集，包含 58.6 万张截图和超过 63.3 万条指代表达实例，覆盖桌面、网页和移动端，涉及文字识别、视觉匹配、空间理解和拒绝场景。提出 Distillation-to-Reinforcement Learning 方法，结合 SFT 与强化学习，训练 Qwen3-VL-8B-Instruct 得到 GroundGUI-8B，在 ScreenSpot-V2、ScreenSpot-Pro、OSWorld-G、MMBench-GUI L2 和 UI-Vision 上取得有竞争力的结果。

**核心创新概述**

> 构建大规模跨平台 GUI 定位数据集 ScreenRef，并提出 D2RL 训练范式，将蒸馏与强化学习顺序结合，缓解监督微调泛化不足和强化学习稀疏奖励问题。

**创新点拆解**

- 发布 ScreenRef 数据集，涵盖桌面、网页、移动端，包含框和点标注以及拒绝场景，规模达 58.6 万截图和 63.3 万指代实例
- 提出 D2RL 方法，先通过 SFT 蒸馏再使用强化学习，解决强化学习稀疏奖励和 SFT 泛化受限的问题
- 在 8B 规模模型上使用开源数据训练，性能可比或超过闭源数据训练的模型

**当前局限**

> 摘要未说明 D2RL 中强化学习的具体奖励设计和训练稳定性；未讨论数据集中文字识别任务的标注质量与噪声；未报告推理效率或实际 GUI 交互部署延迟。

**工程启发**

> 为 GUI 智能体提供高质量开源定位数据和可复现训练方案，有助于降低对闭源数据的依赖，推动桌面、网页和移动端自动化操作系统的落地。

**为什么值得关注**

> 论文覆盖文字识别、视觉匹配等 OCR 相关任务，且 GUI 定位是 OCR 与多模态交互结合的重要应用场景，数据集与训练方法对 OCR 驱动的界面理解有直接帮助。

**原始摘要**

Constructing robust GUI agents relies on multimodal visual grounding: the ability to precisely map
natural language intents to actionable on-screen components. Despite abundant desktop, web, and
mobile benchmarks, high-fidelity resources tailored for diverse environments are surprisingly
scarce. To bridge this gap, we introduce the Screen Referring Grounding Dataset (ScreenRef), a
comprehensive GUI grounding dataset consisting of GUI screenshots paired with natural language
referring expressions and box or point annotations. Spanning desktop, web, and mobile domains,
ScreenRef comprises 586K screenshots and over 633K referring expression instances, covering tasks
such as text recognition, visual matching, spatial understanding, and refusal scenarios. To boost
the model's grounding performance, we propose the Distillation-to-Reinforcement Learning (D2RL)
method to address the limited generalization of supervised fine-tuning and the sparse reward problem
in reinforcement learning. Utilizing ScreenRef, we train Qwen3-VL-8B-Instruct via sequential SFT and
D2RL training, yielding GroundGUI-8B. GroundGUI-8B achieves 95.2% on ScreenSpot-V2, 63.9% on
ScreenSpot-Pro, 65.4% on OSWorld-G, 86.8% on MMBench-GUI L2, and 38.3% on UI-Vision. Among 8B-scale
models, it produces substantial gains over models trained on open-source datasets, with performance
comparable or even superior to models trained on closed-source data. Code, models, and datasets are
available at https://github.com/PrentisAI/GroundGUI.

---

### 9. Can Agents Forget When Asked? A Benchmark for Memory Unlearning in LLM Agents

- arXiv: [2610.18052v1](https://arxiv.org/abs/2610.18052v1)
- PDF: [下载链接](https://arxiv.org/pdf/2610.18052v1)
- 作者: Bofan Xie, Chaokun Wang, Guanchen Ge, Songyao Wang, Fang Niu, Hang Zhang, Wei Wang
- 发布时间: 2026-10-13T09:41:12Z
- 分类: cs.AI
- 相关性评分: 6
- 主题标签: LLM智能体、记忆遗忘、基准测试、隐私、长期记忆

**中文摘要**

> 针对 LLM 智能体长期记忆中的用户删除请求，提出首个记忆遗忘基准 Bemula。包含 50 个多会话对话实例、135 个六类遗忘请求和 1742 个测试问题，每个对话配有对照版本。通过五个测试套件评估存储、删除、保留无关记忆、相似事实重学习和抗提取攻击。评估六种主流记忆系统和三种骨干 LLM，结果显示所有系统端到端通过遗忘请求的比例不超过 1.5%，多数完全失败。

**核心创新概述**

> 首次形式化并基准测试 LLM 智能体记忆遗忘问题，提出配对对话设计以控制存储前提，并系统评估遗忘的精确性、完整性与安全性。

**创新点拆解**

- 构建首个面向 LLM 智能体记忆遗忘的基准 Bemula，包含多会话对话、六类遗忘请求和配对控制版本
- 设计五套测试套件，分别衡量存储、请求信息删除、无关记忆保留、相似事实重学习和抗提取攻击
- 揭示现有记忆系统在遗忘请求上几乎全部失败，指出记忆遗忘是开放挑战

**当前局限**

> 摘要未说明基准是否覆盖多模态记忆或非文本记忆；未分析失败原因与具体记忆系统架构的关系；样本规模相对有限，仅 50 个对话实例。

**工程启发**

> 为智能体记忆系统提供可量化的遗忘评估标准，有助于推动隐私合规的长期记忆设计，对需要处理用户删除请求的对话系统与 OCR 文档管理系统具有工程指导意义。

**为什么值得关注**

> OCR 和文档解析系统常用于长期记忆与知识管理，用户可能要求删除扫描文档中的敏感文本，该基准提示了记忆遗忘在 OCR 相关智能体中的重要性。

**原始摘要**

Long-term memory has become a core component of large language model (LLM) agents. As agents
accumulate personal information over long-term use, users increasingly ask them to delete sensitive
or outdated facts. A memory system should honor such requests. It should remove exactly what was
requested and keep the rest of its memory intact. However, existing memory benchmarks evaluate only
memory writing, retrieval, and organization, so whether agents can forget at the user's explicit
request remains under-evaluated. To address this gap, we propose Bemula, the first benchmark
dedicated to memory unlearning. It comprises 50 multi-session dialogue instances, 135 forget
requests of six types, and 1,742 test questions. Each dialogue has a control version without the
requests, so that only systems that have stored the target can earn credit for forgetting. Across
the paired versions, five test suites measure storage, removal of the requested information,
preservation of unrelated memories, relearning of similar facts, and resistance to extraction
attacks. On Bemula, we evaluate six mainstream memory systems under three backbone LLMs, together
with the Full Context LLM on two of them. The results are negative. Across all evaluated systems and
backbones, no system passes more than 1.5% of forget requests end to end, and most pass none at all.
These systems either leave the requested information extractable under simple attacks or delete far
more than requested. Memory unlearning therefore remains an open challenge for agent memory design.
We release our data and code at https://github.com/Nboxff/bemula-benchmark.

---

### 10. MMKG-R1: Constructing Multimodal Knowledge Graphs via Reinforcement Learning

- arXiv: [2610.19341v1](https://arxiv.org/abs/2610.19341v1)
- PDF: [下载链接](https://arxiv.org/pdf/2610.19341v1)
- 作者: Zongyu Wu, Yilong Wang, Xiaochen Wang, Minhua Lin, Yuan Zhong, Fenglong Ma, Xiang Zhang, Suhang Wang
- 发布时间: 2026-10-14T00:35:59Z
- 分类: cs.CV
- 相关性评分: 3
- 主题标签: 多模态知识图谱、强化学习、RAG、多模态大模型、知识抽取

**中文摘要**

> 针对多模态知识图谱构建中缺乏显式质量引导的问题，提出 MMKG-R1，一种以 MMKG 质量驱动的强化学习框架，用于训练多模态大模型作为多模态知识构建器。引入多个质量感知奖励，直接评估从单个知识源抽取的信息质量和组装后的 MMKG 质量，并用于指导强化学习训练。实验表明构建的 MMKG 提升下游问答准确率。

**核心创新概述**

> 将强化学习与 MMKG 质量直接对齐，设计多维度质量感知奖励，而非依赖最终答案正确性的间接反馈来训练知识构建器。

**创新点拆解**

- 提出质量驱动的强化学习框架 MMKG-R1，直接优化多模态知识图谱的构建质量
- 设计多个质量感知奖励，分别评估单源信息抽取质量和整体 MMKG 组装质量
- 将 MLLM 训练为多模态知识构建器，并通过下游问答验证构建质量提升

**当前局限**

> 摘要未说明质量感知奖励的具体定义和可扩展性；未报告构建 MMKG 的计算成本与训练稳定性；缺乏与多种基线在大规模数据集上的详细对比。

**工程启发**

> 为多模态知识图谱构建提供质量驱动的训练范式，可提升 RAG 系统的事实准确性和多模态检索能力，对需要结构化多模态知识的应用具有落地潜力。

**为什么值得关注**

> OCR 常作为多模态知识图谱构建中的文本来源，论文关注从多模态源抽取高质量知识并组装图谱，与 OCR 信息抽取和结构化任务相关。

**原始摘要**

Multimodal knowledge graphs (MMKGs) organize information across different modalities to support
multimodal Graph Retrieval-Augmented Generation (RAG), which aims to improve the performance of
multimodal large language models (MLLMs). The effectiveness of these multimodal Graph RAG methods
largely depends on the quality of the constructed MMKGs. However, most existing methods construct
MMKGs without explicit guidance on graph quality, while reinforcement learning (RL)-based methods
that rely on final-answer correctness may provide only indirect feedback on MMKG quality. To address
these limitations, we propose MMKG-R1, a novel MMKG-quality-driven RL framework for training an MLLM
as a multimodal knowledge constructor. To be specific, MMKG-R1 introduces multiple quality-aware
rewards to directly evaluate both the quality of information extracted from individual knowledge
sources and the quality of the assembled MMKG. These rewards are then used to guide the RL training.
Experiments across multiple datasets show that MMKG-R1 constructs MMKGs that improve downstream
question-answering accuracy.

---
