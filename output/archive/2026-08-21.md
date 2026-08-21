# OCR / 文档解析研究日报（2026-08-21）

## 报告说明

- 检索源：arXiv API
- 检索查询：`(all:"document parsing" OR all:"document understanding" OR all:"optical character recognition" OR all:OCR OR all:"layout analysis" OR all:"document layout analysis" OR all:"text recognition" OR all:"table recognition" OR all:"form understanding" OR all:"document intelligence" OR all:"page understanding" OR all:"scene text recognition" OR all:"handwritten text recognition" OR all:"information extraction") AND (cat:cs.CV OR cat:cs.AI OR cat:cs.CL OR cat:eess.IV)`
- 生成时间（UTC）：`2026-08-21 02:36:44`
- 大模型综合分析：`开启`

## 一、今日执行摘要

> 今日OCR与文档解析研究聚焦于构建大规模、可复用的处理流水线，提升对历史文档、手写文本和对抗性场景的鲁棒性，并探索统一智能体框架。关键进展包括：波士顿公共图书馆和哈佛图书馆分别推出了处理历史报纸和书籍的模块化流水线及大规模数据集；DocClaw提出了统一智能体文档处理范式；OmniHandwritingOCR提供了手写场景的评估基准；ArmorOCR关注对抗性感知；ThermoDPO则从偏好优化角度改善了生成模型的OCR性能。整体趋势是向系统化、标准化和鲁棒化方向发展。

## 二、今日趋势判断

今日论文呈现三大趋势：一是构建端到端、可扩展的文档处理流水线，强调结构化输出和元数据保留；二是使用统一智能体框架整合多种文档任务，减少系统复杂性；三是关注特殊场景（手写、历史文稿、对抗性攻击）下的性能评估与提升，推动系统鲁棒性。同时，大语言模型和偏好优化技术被引入OCR领域，用于提升生成质量和对齐性。

## 三、今日论文概览

1. **Institutional Newspapers Pipeline: Deriving billions of high quality tokens from historical newspapers** | 标签：historical documents、OCR pipeline、dataset、layout analysis、digital humanities
2. **DocClaw: A Unified Agentic System for Intelligent Document Processing** | 标签：agentic system、document processing、OCR、docQA、KIE
3. **OmniHandwritingOCR: A Diagnostic Benchmark for Evaluating Multimodal LLMs in Handwritten OCR Scenarios** | 标签：handwritten OCR、benchmark、multimodal LLM、mathematical expressions、evaluation
4. **Impact of Iterative Fine-Tuning on Transcription Accuracy in Complex Historical Sanskrit Manuscripts** | 标签：historical manuscripts、Sanskrit、OCR、iterative fine-tuning、layout analysis
5. **Institutional Books - Enriched Text: A customizable multilingual open-source pipeline for denoising, deduplicating, and annotating OCR text at scale** | 标签：large-scale OCR、text enrichment、multilingual、metadata、digital libraries
6. **ArmorOCR: Grounded Adversarial Visual Perception via Observation-Transferred Self-Distillation** | 标签：adversarial OCR、grounded perception、reinforcement learning、self-distillation、robustness
7. **Institutional Books - Visual Elements: An open-source pipeline for extracting, classifying, deduplicating, and captioning visual elements from digital book collections** | 标签：视觉元素提取、历史书籍、数字人文、开源流水线、数据集
8. **Manifold Drift in Flow Preference Optimization: A Root Cause of Reward Hacking** | 标签：偏好优化、流匹配、奖励黑客、流形漂移、ThermoDPO

## 四、今天 OCR / 文档解析论文里的主要创新点

- 采用模块化流水线设计，各步骤独立可定制，便于针对特定任务优化。
- 发布大规模公开数据集和开源工具，促进研究和复现。
- 利用小模型和轻量级方法在有限硬件上处理历史文档。
- 强调元数据保留和注释，而非简单过滤，以支持下游分析。
- 引入智能体和强化学习等新技术，提升文档处理的交互性和鲁棒性。

## 五、后续 OCR 领域值得推进的改进方向

- 开发自适应OCR流水线，能针对不同语料库（如不同语言、时代、扫描质量）自动调整预处理和识别参数。
- 探索无监督或半监督方法，利用大规模未标注文档数据提升模型泛化能力，减少人工标注。
- 建立更全面的基准，涵盖手写、对抗性、多种布局和噪声类型，以系统评估系统鲁棒性。
- 结合视觉语言模型，实现从文本提取到视觉元素理解的一体化文档解析。
- 优化智能体框架的推理效率，实现低延迟的文档问答和关键信息提取。
- 研究如何利用流形学习和对抗训练，使OCR系统在对抗性攻击下保持可靠。
- 推动跨机构合作，整合多来源数字馆藏，构建多样化的大规模数据集。
- 开发统一文档表示和交互标准，使不同工具和模型可互相操作。
- 探索从生成模型中利用偏好优化和流形约束，提高合成数据的质量，用于训练更鲁棒的OCR模型。
- 开发低资源语言的历史文档识别技术，结合语言模型和领域知识提高准确率。

## 六、工程落地启发

- 设计流水线时应考虑计算效率和硬件限制，如使用小模型和模块化处理。
- 利用注释而非过滤来保留元数据，为用户提供定制化灵活性。
- 历史文档处理需要迭代微调策略，以适应目标分布，降低标注成本。
- 统一框架可简化多任务系统的部署和维护，但需平衡性能与推理开销。
- 对抗性攻击是安全的隐患，建议在开发流程中嵌入鲁棒性评估。
- 流匹配偏好优化可改善生成模型的OCR性能，可作为训练工具。

## 七、优先关注论文

- **Institutional Newspapers Pipeline: Deriving billions of high quality tokens from historical newspapers**：提供了大型历史报纸数据集，可测试其他系统的泛化性；流水线设计具有可复用性。
- **DocClaw: A Unified Agentic System for Intelligent Document Processing**：统一的智能体框架可能成为文档处理的新范式，其性能与效率的权衡值得持续关注。
- **OmniHandwritingOCR: A Diagnostic Benchmark for Evaluating Multimodal LLMs in Handwritten OCR Scenarios**：为手写OCR提供诊断基准，其挑战性场景可驱动模型改进，未来可能扩展至更多语言。
- **Impact of Iterative Fine-Tuning on Transcription Accuracy in Complex Historical Sanskrit Manuscripts**：迭代微调方法在特定领域取得效果，后续可能推广至其他历史文档，相关数据集有价值。
- **Institutional Books - Enriched Text: A customizable multilingual open-source pipeline for denoising, deduplicating, and annotating OCR text at scale**：大规模多语言处理流水线，其注释方法可能成为数字图书馆标准。
- **ArmorOCR: Grounded Adversarial Visual Perception via Observation-Transferred Self-Distillation**：首次提出对抗性OCR基准和训练方法，可能推动鲁棒性研究，尤其对安全敏感应用重要。
- **Institutional Books - Visual Elements: An open-source pipeline for extracting, classifying, deduplicating, and captioning visual elements from digital book collections**：大型视觉元素数据集，可支持多模态模型训练，流水线贡献社区。
- **Manifold Drift in Flow Preference Optimization: A Root Cause of Reward Hacking**：从优化理论角度提升OCR性能，其方法可能应用于生成模型的数据增强，值得跟踪。

## 八、论文逐篇解析

### 1. Institutional Newspapers Pipeline: Deriving billions of high quality tokens from historical newspapers

- arXiv: [2608.18972v1](https://arxiv.org/abs/2608.18972v1)
- PDF: [下载链接](https://arxiv.org/pdf/2608.18972v1)
- 作者: Matteo Cargnelutti, Catherine Brobston, Eben English, Jake Sadow, Kacie Bailey, Greg Leppert, Amanda Watson, Jessica Chapel, Jonathan Zittrain
- 发布时间: 2026-08-19T14:41:12Z
- 分类: cs.CL, cs.DL
- 相关性评分: 26
- 主题标签: historical documents、OCR pipeline、dataset、layout analysis、digital humanities

**中文摘要**

> 本文介绍了一个名为机构报纸流水线的模块化系统，由波士顿公共图书馆联合设计，用于从历史报纸扫描件中提取高质量、结构化的数据集。系统架构强调每一步的可解释性和可定制性，并优化了计算效率以适应工作站级硬件。流水线执行多步骤处理：首先将扫描件分割成独立的类型无关块，然后对每个块进行OCR，再进行文本分析、类型分类、阅读顺序检测、命名实体识别、主题分类、语言检测和预计算嵌入生成。作者对波士顿公共图书馆的馆藏部分运行了该流水线，并发布了开放数据集，包含147万份1795年至1930年的公共领域报纸扫描件，OCR输出为163亿个o200k_base词元，来自8310万个独立块。报告详细描述了各步骤的方法、训练的小模型、评估结果和数据集规模测量，并将此工作定位为解锁高质量历史报纸数据的重要一步。

**核心创新概述**

> 提出了一个端到端的模块化流水线，专门针对历史报纸的复杂布局和噪声进行优化，且设计强调在小型硬件上运行，同时产出了大规模公开数据集。

**创新点拆解**

- 模块化流水线设计，每个步骤独立可解释和可定制
- 类型无关的扫描件分割方法，适应历史报纸的密集和不规则布局
- 训练了多个小模型用于文本分析、类型分类、语言检测等任务
- 发布了大规模开放数据集，包含163亿词元和8310万个块
- 数据集覆盖1795年至1930年的历史报纸，时间跨度大

**当前局限**

> ['评估可能未覆盖所有类型的布局和噪声情况', '数据集仅来自波士顿公共图书馆，可能代表性和通用性有限', '流水线在特定历史报纸上的性能可能与其他类型文档存在差异']

**后续可改进方向**

- 扩展到更多图书馆和历史档案，增强数据集的多样性
- 研究更高效的OCR模型，提高处理速度和准确性
- 探索自适应方法来处理更广泛的布局变化和噪声类型

**工程启发**

> 提供了一个完整、可复用的流水线，能够在常规硬件上处理大规模历史文档，并公开了数据和模型，可直接用于相关研究和应用。

**为什么值得关注**

> 该研究为历史文档数字化提供了实用的解决方案，并开源了数据和工具，对OCR领域和数字人文研究有直接价值。

**原始摘要**

Historical newspapers are an abundant record of public life, but their dense, irregular and
sometimes noisy layouts make computational access to these materials both challenging and limited.
We present the Institutional Newspapers Pipeline, a modular system we jointly designed with Boston
Public Library to extract high-quality, structured datasets from historical newspaper scans. It was
architected so that each step remains interpretable and customizable, and so that the pipeline as a
whole remains computationally frugal enough to run on workstation-level hardware. The pipeline runs
each scan through a multi-step process: it segments scans into individual type-agnostic crops and
performs OCR on each resulting segment before then performing text analysis, type classification,
reading order detection, named entities recognition, subject classification, language detection, and
pre-computed embeddings generation on every crop. We ran this pipeline against a portion of Boston
Public Library's holdings and released the results as an open dataset. The optical character
recognition (OCR) output represents 16.3 billion o200k_base tokens across 83.1 million individual
crops, extracted from 1,473,635 public domain newspaper scans published between 1795 and 1930. This
report describes our methods for each processing step, the small models we trained, as well as the
evaluation results and dataset-scale measurements we collected in the process. It accompanies the
release of the pipeline, models, and dataset. We position this work as a substantial step towards
unlocking high-quality data from tens of millions of newspaper scans.

---

### 2. DocClaw: A Unified Agentic System for Intelligent Document Processing

- arXiv: [2608.18685v1](https://arxiv.org/abs/2608.18685v1)
- PDF: [下载链接](https://arxiv.org/pdf/2608.18685v1)
- 作者: Siqi Xiang, Zhipeng Xu, Yufei Liu, Junhao Ji, Qing Liu, Zulong Chen, Zhibo Yang, Chunyan Miao, Shijian Lu
- 发布时间: 2026-08-19T08:34:48Z
- 分类: cs.CV
- 相关性评分: 23
- 主题标签: agentic system、document processing、OCR、docQA、KIE

**中文摘要**

> 本文提出了DocClaw，这是一个统一的智能体系统，将多种智能文档处理任务（如OCR、文档问答DocQA和关键信息提取KIE）统一为智能体与文档之间的交互过程。给定文档和任务特定查询，DocClaw遵循适当的文档技能，迭代地识别所需信息、调用相关工具，并将观察结果整合到预期输出中。系统通过结构化文档状态组织可复用的文档知识和任务特定的交互上下文，使智能体能够积累、回顾和逐步细化信息。该公式下，任务特定要求由智能体对查询目标和相应文档技能的解释捕获，而底层交互循环、工具空间和文档状态在任务间共享。在多个智能文档处理基准上的实验表明，DocClaw能够在单一智能体框架内有效处理多种任务，并达到有竞争力的性能。

**核心创新概述**

> 将多样的IDP任务统一到一个智能体交互框架中，共享底层机制，而非为每个任务设计独立模型。

**创新点拆解**

- 统一任务公式：将OCR、DocQA和KIE视为智能体与文档的交互过程
- 结构化文档状态管理知识和上下文，支持信息积累和细化
- 共享交互循环和工具空间，适应不同任务
- 在多个基准上验证了多任务处理的有效性

**当前局限**

> ['性能可能未超越专门化系统，尤其是在OCR等基础任务上', '智能体框架的推理开销可能较大，影响效率', '对多种任务的处理依赖文档技能，可能在不同文档类型上表现不稳定']

**后续可改进方向**

- 优化智能体的工具调用和交互策略，降低计算开销
- 增强文档技能库的覆盖，支持更多场景
- 探索在多任务学习中平衡性能与效率的方法

**工程启发**

> 提供了一个统一的文档处理框架，可简化系统部署和维护，并提升多任务处理的一致性。

**为什么值得关注**

> 提出了一种新颖的智能体范式，对构建通用的文档处理系统有启发，且实验证实了其可行性。

**原始摘要**

Intelligent document processing (IDP) encompasses a broad range of tasks, including optical
character recognition (OCR), document question answering (DocQA), and key information extraction
(KIE). Despite their distinct objectives, these tasks share a common need to perceive document
content, acquire task-relevant information, and progressively refine intermediate results. However,
they are typically formulated as separate prediction problems and addressed by task-specific models
or processing pipelines. We introduce DocClaw, a unified agentic system that formulates diverse
intelligent document processing tasks as a shared process of interaction between an agent and a
document. Given a document and a task-specific query, DocClaw follows an appropriate document skill
to iteratively identify the information required, invoke relevant tools, and integrate the resulting
observations into the desired output. Throughout this process, a structured document state organizes
reusable document knowledge and task-specific interaction context, allowing the agent to accumulate,
revisit, and progressively refine information as the interaction proceeds. Under this formulation,
task-specific requirements are captured by the agent's interpretation of the query objective and the
corresponding document skill, while the underlying interaction loop, tool space, and document state
are shared across tasks. Extensive experiments across multiple intelligent document processing
benchmarks demonstrate that DocClaw effectively handles diverse tasks within a single agentic
framework and achieves competitive performance compared with both general-purpose VLMs and task-
specific methods.

---

### 3. OmniHandwritingOCR: A Diagnostic Benchmark for Evaluating Multimodal LLMs in Handwritten OCR Scenarios

- arXiv: [2608.18586v1](https://arxiv.org/abs/2608.18586v1)
- PDF: [下载链接](https://arxiv.org/pdf/2608.18586v1)
- 作者: Zinuo Guo, Min Zhang, Bo Jiang
- 发布时间: 2026-08-19T06:27:05Z
- 分类: cs.CV, cs.AI
- 相关性评分: 20
- 主题标签: handwritten OCR、benchmark、multimodal LLM、mathematical expressions、evaluation

**中文摘要**

> 本文介绍了OmniHandwritingOCR，这是一个用于评估多模态大语言模型（MLLMs）在手写OCR场景中能力的诊断性基准。现有基准多聚焦于印刷文本或简单单行输入，而现实手写场景如多语言手写、作者错误和结构复杂的数学表达式覆盖不足。该基准涵盖手写文本识别和手写数学表达式识别，包含六个子任务和十二个子集，共77,570张带标签图像，来自公开数据集和新收集的学生手写内容。关键组件是难度分层多行公式语料，用于测试在结构复杂性增加下的鲁棒性。作者在统一协议下使用五个互补指标评估了十三个开源和闭源系统。结果显示，当前系统在忠实转录方面仍有较大差距：复杂多行公式上性能急剧下降，不同语言和公式设置下模型排名变化，一些生成模型产生看似合理但视觉上无依据的纠正。该基准为诊断多模态模型在手写OCR场景中的语言、内容、结构和视觉基础失败模式提供了具有挑战性的测试平台。

**核心创新概述**

> 提出了一个专门针对手写OCR的全面诊断基准，包含多语言、多行公式等复杂场景，并采用多指标评估。

**创新点拆解**

- 设计了包含六子任务和十二子集的基准，覆盖广泛的手写场景
- 引入难度分层多行公式语料，测试结构复杂性
- 使用五个互补指标全面评估性能
- 包含新收集的学生手写数据，增加现实性

**当前局限**

> ['基准主要针对手写，对印刷文本场景覆盖有限', '评估的系统数量有限，可能不代表所有最新模型', '多行公式的标注和评估可能受主观因素影响']

**后续可改进方向**

- 扩展基准以涵盖更多语言的书写风格
- 引入更精细的失败模式分析，如词级错误类型
- 将基准与模型训练结合，推动针对性改进

**工程启发**

> 提供了一个标准化的评估工具，可用于衡量和比较不同手写OCR系统的性能，促进技术进步。

**为什么值得关注**

> 填补了现有OCR基准在手写场景上的空白，为多模态模型的研究和部署提供了诊断工具。

**原始摘要**

Multimodal large language models (MLLMs) are increasingly used as OCR systems in document and
knowledge-processing pipelines, but their ability to faithfully read real handwriting remains
underexplored. Existing OCR benchmarks focus largely on printed text or clean single-line inputs,
leaving limited coverage of realistic handwritten OCR scenarios such as multilingual handwriting,
writer errors, and structurally complex mathematical expressions. We introduce OmniHandwritingOCR, a
diagnostic benchmark for evaluating MLLMs and OCR systems on handwritten OCR. It covers handwritten
text recognition and handwritten mathematical expression recognition across six subtasks and twelve
subsets, totaling 77.57K labeled images from public datasets and newly collected student writings. A
key component is a difficulty-stratified multi-line formula corpus designed to test robustness under
increasing structural complexity. We evaluate thirteen open- and closed-source systems with five
complementary metrics under a unified protocol. Results show that current systems remain far from
faithful transcription: performance drops sharply on complex multi-line formulas, model rankings
vary across language and formula settings, and several generative models hallucinate plausible but
visually unsupported corrections. OmniHandwritingOCR provides a challenging testbed for diagnosing
language, content, structural, and visual-grounding failure modes of multimodal models in
handwritten OCR scenarios.

---

### 4. Impact of Iterative Fine-Tuning on Transcription Accuracy in Complex Historical Sanskrit Manuscripts

- arXiv: [2608.18696v1](https://arxiv.org/abs/2608.18696v1)
- PDF: [下载链接](https://arxiv.org/pdf/2608.18696v1)
- 作者: Kartik Chincholikar, Kaushik Gopalan, Mihir Hasabnis
- 发布时间: 2026-08-19T08:50:45Z
- 分类: cs.CV, cs.AI
- 相关性评分: 15
- 主题标签: historical manuscripts、Sanskrit、OCR、iterative fine-tuning、layout analysis

**中文摘要**

> 本文针对历史手写梵文手稿的数字化挑战，提出了一种局部传统OCR流水线，可在布局层面和外观层面进行迭代微调。该方法通过适应目标手稿的分布，在后续页面预测中表现更好，从而减少了人工标注的迭代成本。作者使用该流水线数字化了三份复杂的历史梵文手稿，并发布了带精细布局标注和Unicode标注的数据集（PAGE-XML格式）。实验展示了迭代微调的定量收益，并与领先的多模态大语言模型进行了基准比较。

**核心创新概述**

> 提出了一种针对特定手稿分布的迭代微调OCR流水线，同时处理布局和外观变化，并创建了带精细标注的梵文手稿数据集。

**创新点拆解**

- 迭代微调策略，逐步适应目标手稿的风格和噪声
- 结合布局级和外观级的适应，提高OCR准确性
- 发布了带有精细布局和Unicode标注的数据集
- 提供了开源代码和数据集，便于复现和扩展

**当前局限**

> ['主要针对手稿类文档，适用性可能有限', '人工标注成本仍然较高，尽管通过迭代微调有所减少', '传统OCR方法可能不如深度学习方法灵活']

**后续可改进方向**

- 探索无监督或半监督学习方法，减少标注依赖
- 扩展到更多历史和语言文档，提升泛化能力
- 结合深度学习模型增强特征提取

**工程启发**

> 提供了一个实用的流水线，可减少历史手稿数字化中的人工努力，并开源了数据，对文化遗产保护有应用价值。

**为什么值得关注**

> 针对历史手稿OCR的挑战，提出了有效的迭代微调方法，并开源了资源和数据，对相关研究有直接帮助。

**原始摘要**

Digitizing the text from handwritten historical manuscripts is required to make them easily
accessible, preservable, and to enable historical scholars to study them in new ways. Historical
manuscripts, however, often exhibit complex heterogeneous layouts and non-standard appearance due to
period-specific writing styles, page textures, camera noise, and other nuisance factors, making them
difficult to perform OCR on. To tackle this challenge, we introduce a local traditional OCR
pipeline, which can be iteratively fine-tuned on the target manuscript at the layout-level and the
appearance-level. By adapting to the target manuscript distribution, the proposed Traditional OCR
pipeline makes better predictions on subsequent pages, causing iterative reduction in human
annotation effort, which is expensive and time-consuming as it requires historical domain expertise.
Using this pipeline, we digitize text from three complex historical Sanskrit manuscripts and
introduce a dataset with granular layout-level annotations, along with Unicode annotations in the
standard PAGE-XML format. We demonstrate quantitative gains due to iterative fine-tuning of the
proposed traditional OCR pipeline, and also benchmark the performance of leading Multi-Modal Large
Language Models on the introduced Dataset. Code and dataset are available at:
https://github.com/flame-cai/gnn-synthetic-layout-historical/.

---

### 5. Institutional Books - Enriched Text: A customizable multilingual open-source pipeline for denoising, deduplicating, and annotating OCR text at scale

- arXiv: [2608.19026v1](https://arxiv.org/abs/2608.19026v1)
- PDF: [下载链接](https://arxiv.org/pdf/2608.19026v1)
- 作者: David Lowry-Duda, Matteo Cargnelutti, Catherine Brobston, Salwa Ismail, Greg Leppert, Amanda Watson, Jonathan Zittrain
- 发布时间: 2026-08-19T15:20:54Z
- 分类: cs.CL, cs.DL
- 相关性评分: 14
- 主题标签: large-scale OCR、text enrichment、multilingual、metadata、digital libraries

**中文摘要**

> 本文介绍了机构书籍：哈佛图书馆（IB-HL）的丰富文本版本（IB-HL-ET），这是一个包含983,004卷、242B o200k_base词元的大型语料库。作者提出了一种名为“丰富文本”的方法，不产生单一“完整”的token流，而是通过注释保留元数据，对文本进行标准化。他们分离了补编、检测每段落语言、识别重复段落簇，并计算每段落的每字节位数得分。这些信息通过HTML样式的注释叠加在文本上，用户可以根据需要解析。该流水线适用于该馆藏中的约250种语言。版本中IB-HL-ET包含983,003卷、217B o200k_base词元，组织为13.9亿个带注释的子主题段落。此报告描述了项目的目标、实现和设计原理，并发布了IB-HL-ET和生成该版本的流水线。

**核心创新概述**

> 提出了一种“丰富文本”方法，通过注释保留元数据，而非过滤和丢弃，以满足信息管理需求，适用于大规模多语言OCR文本。

**创新点拆解**

- 采用注释而非过滤的方法，保留灵活性和完整性
- 提供多语言检测、重复段落识别和复杂度评分
- 设计了HTML样式注释，便于用户定制输出
- 适用于约250种语言的大规模处理

**当前局限**

> ['注释可能增加数据大小和处理复杂度', '依赖OCR质量，可能受限于原始扫描件', '面向IB-HL特定语料，对其他语料可能需调整']

**后续可改进方向**

- 优化注释表示，减少冗余和存储开销
- 探索自动化的段落聚类和去重方法，提高效率
- 扩展到其他图书馆和书籍来源，验证通用性

**工程启发**

> 提供了一个可扩展的多语言文本处理流水线，能保留重要元数据，适用于大规模数字图书馆建设。

**为什么值得关注**

> 研究了大规模OCR语料处理中的信息管理问题，提出的方法有助于平衡数据清理和完整性，对数字人文有用。

**原始摘要**

Released in 2025, Institutional Books: Harvard Library (IB-HL) is a collection of 983,004 volumes
(242B o200k_base tokens), originally digitized through Harvard Library's participation in the Google
Books Library project. As researchers and developers have begun to use IB-HL, a tension has emerged
between standard large-scale preprocessing practices and the goals of careful information
stewardship. Many existing pipelines optimize for web text: as a result, they tend to aggressively
filter, deduplicate, restrict by language, and sometimes discard meaningful metadata. Meanwhile,
researchers seeking to use IB-HL duplicate effort while performing similar processing and analysis.
We describe an approach that we call Enriched Text. Instead of producing a single 'complete' stream
of tokens, we normalize the text while preserving metadata through annotations. We separate
endmatter, detect per-paragraph language, identify clusters of duplicate paragraphs, and compute
per-paragraph bits-per-byte scores. We provide this information through HTML-like annotations
layered on top of the text. By parsing these annotations, users can tailor the output to their own
needs instead of accepting a global editorial decision on content. The pipeline applies to all
$\approx$250 languages in the collection. This report describes this project's goals,
implementation, and design rationale. The release includes IB-HL-ET (an enriched-text version of IB-
HL containing 217B o200k_base tokens across 983,003 volumes, organized into 1.39B annotated subtopic
paragraphs) and the pipeline that produced it. These serve to make the collection easier for
machines to parse and for humans to study.

---

### 6. ArmorOCR: Grounded Adversarial Visual Perception via Observation-Transferred Self-Distillation

- arXiv: [2608.20122v1](https://arxiv.org/abs/2608.20122v1)
- PDF: [下载链接](https://arxiv.org/pdf/2608.20122v1)
- 作者: Linhan Cao, Siyuan Li, Jun Lan, Liangbo He, Guannan Li, Xiaolei Huang, Jun Jia, Shuheng Zhou, Huijia Zhu, Weiqiang Wang, Wei Sun
- 发布时间: 2026-08-20T14:52:06Z
- 分类: cs.CV
- 相关性评分: 13
- 主题标签: adversarial OCR、grounded perception、reinforcement learning、self-distillation、robustness

**中文摘要**

> 本文针对大型多模态模型（LMMs）在对抗性视觉文本上的脆弱性，将对抗性OCR形式化为一个接地OCR感知任务，并引入了AdvSpot，这是一个用于接地对抗性OCR评估的首个基准。AdvSpot包含390张图像，带有区域级标注，涵盖5个主要类别和13种细粒度对抗性OCR类型。为解决这些挑战，作者提出了ArmorOCR，一个两阶段训练框架：首先通过策略内自蒸馏（OPSD）从特权变换观察中获取缺失的对抗性OCR感知，然后使用带任务条件奖励的组相对策略优化（GRPO）细化接地OCR感知，包括定位、识别、完整spotting和视觉问答。在AdvSpot和其他对抗性及一般OCR基准上的实验表明，ArmorOCR在保持竞争性的一般OCR能力的同时，持续提高了对抗性OCR的感知能力。

**核心创新概述**

> 首次提出了对抗性OCR的接地感知任务，并构建了专门的基准AdvSpot，以及提出了结合自蒸馏和强化学习的训练框架ArmorOCR。

**创新点拆解**

- 定义了接地对抗性OCR感知任务，包括定位、识别和VQA
- 构建了首个对抗性OCR基准AdvSpot，包含区域级标注和多类别
- 提出了两阶段训练框架，结合OPSD和GRPO
- 在多个基准上验证了改进效果和泛化性

**当前局限**

> ['对抗性OCR的类型可能未完全覆盖所有现实攻击模式', '训练框架计算开销可能较大', '性能提升可能牺牲部分一般OCR能力，尽管实验显示保持']

**后续可改进方向**

- 扩大对抗性OCR任务的种类和规模，增强基准的全面性
- 优化自蒸馏和强化学习过程，提高训练效率
- 探索对抗性训练与其他鲁棒性方法的结合

**工程启发**

> 提供了对抗性OCR的基准和训练方法，有助于开发更鲁棒的文档处理系统，抵御恶意操纵。

**为什么值得关注**

> 关注OCR模型的安全性和鲁棒性，提出了新的评估基准和解决方案，对实际应用有重要价值。

**原始摘要**

Large multimodal models (LMMs) have demonstrated strong OCR recognition capabilities, yet remain
vulnerable to adversarial visual text that is readable to humans but challenging for models to
localize and recognize. Existing OCR benchmarks mainly focus on natural or document-style text,
while adversarial OCR evaluations remain limited in scale, task coverage, or region-aware
evaluation. In this paper, we formulate adversarial OCR as a \textbf{grounded OCR perception} task
and introduce \textbf{AdvSpot}, the first benchmark for grounded adversarial OCR evaluation. AdvSpot
comprises 390 images with region-level annotations, spanning 5 primary categories and 13 fine-
grained adversarial OCR types. To address this challenge, we propose \textbf{ArmorOCR}, a two-stage
training framework for robust adversarial OCR perception. ArmorOCR first acquires missing
adversarial OCR perception from privileged transformed observations through On-Policy Self-
Distillation (OPSD), and then refines grounded OCR perception through Group Relative Policy
Optimization (GRPO) with task-conditioned rewards for localization, recognition, full spotting, and
visual question answering (VQA). Experiments on our AdvSpot, other adversarial OCR benchmarks, and
general OCR benchmarks demonstrate that ArmorOCR consistently improves adversarial OCR perception
while preserving competitive general OCR capability.

---

### 7. Institutional Books - Visual Elements: An open-source pipeline for extracting, classifying, deduplicating, and captioning visual elements from digital book collections

- arXiv: [2608.18957v1](https://arxiv.org/abs/2608.18957v1)
- PDF: [下载链接](https://arxiv.org/pdf/2608.18957v1)
- 作者: Jimmy Mendez, Matteo Cargnelutti, David Lowry-Duda, Catherine Brobston, Salwa Ismail, Greg Leppert, Amanda Watson, Jonathan Zittrain
- 发布时间: 2026-08-19T14:21:56Z
- 分类: cs.CV, cs.DL
- 相关性评分: 13
- 主题标签: 视觉元素提取、历史书籍、数字人文、开源流水线、数据集

**中文摘要**

> 历史书籍收藏中蕴含丰富的视觉元素（如图示、照片、版画、装饰艺术），但在大规模数字化项目中常被忽视。尽管OCR已标准化了文本内容提取，这些视觉组件所承载的细微语境仍未得到充分利用。本文介绍了一个开源端到端流水线，用于从历史书籍收藏中检测、分类、去重和描述视觉元素，并发布了从983,004卷扫描书籍（即Institutional Books: Harvard Library数据集）中提取的2260万视觉元素的初始数据集。这项工作贡献于社区范围内通过计算访问（从AI模型训练到数字人文学研究）为数字化图书馆收藏提供新用例的持续努力。

**核心创新概述**

> 提出了一个完整的、开源的、端到端的视觉元素提取流水线，涵盖检测、分类、去重和描述，并应用于大规模历史书籍数字化数据集，填补了OCR仅处理文本的空白。

**创新点拆解**

- 构建了一个针对历史书籍视觉元素的专用检测、分类、去重和描述流水线
- 发布了包含2260万视觉元素的大规模数据集，来源于983,004卷扫描书籍
- 实现了视觉元素提取的全流程自动化，支持数字人文学研究和AI模型训练
- 提供了开源工具，便于社区扩展和复现

**当前局限**

> ['数据集可能仅覆盖哈佛图书馆收藏，存在库内偏差', '视觉元素的分类和描述质量依赖自动化模型的性能，可能不及人工标注精准', '未提及对低质量扫描或特殊版式的鲁棒性', '工程验证可能缺乏与现有方法的定量对比']

**后续可改进方向**

- 融合视觉语言模型提升描述质量和更细粒度的分类
- 扩展数据集至其他图书馆，增强多样性
- 优化检测模型以处理变形、老化扫描件
- 开发针对版式和装饰性元素的专用特征提取方法

**工程启发**

> 提供了一个可直接部署的视觉元素提取工具链，有助于图书馆数字化项目自动化处理视觉内容，并可作为下游任务（如多模态模型训练）的数据源。

**为什么值得关注**

> OCR领域主要关注文本，但书籍中的视觉元素常被忽略。该流水线补充了文档解析的视觉维度，对全面理解历史文献具有重要价值。

**原始摘要**

Historical book collections contain rich visual elements - such as illustrations, photographs,
engravings, and decorative art - that are frequently under-explored in large-scale digitization
projects. While Optical Character Recognition (OCR) has standardized the extraction of textual
content, these visual components offer a layer of nuance and context that remains largely untapped
by automated text extraction workflows. This technical report introduces Institutional Books -
Visual Elements, an open-source end-to-end pipeline for detecting, classifying, deduplicating, and
captioning visual elements from historical book collections. Alongside this pipeline, we release an
initial dataset of 22.6 million visual elements extracted from the 983,004 scanned volumes that
comprise the Institutional Books: Harvard Library dataset. This work contributes to ongoing,
community-wide efforts to enable new use cases for digitized library collections through
computational access, from artificial intelligence model training to digital humanities research.

---

### 8. Manifold Drift in Flow Preference Optimization: A Root Cause of Reward Hacking

- arXiv: [2608.20011v1](https://arxiv.org/abs/2608.20011v1)
- PDF: [下载链接](https://arxiv.org/pdf/2608.20011v1)
- 作者: Yansen Han, Shengyi Liao, Yuanxing Zhang, Pengfei Wan, Tao Lin
- 发布时间: 2026-08-20T13:25:24Z
- 分类: cs.AI, cs.CV
- 相关性评分: 9
- 主题标签: 偏好优化、流匹配、奖励黑客、流形漂移、ThermoDPO

**中文摘要**

> 偏好优化是生成模型的标准对齐方法，但扩展到连续时间动力学仍有挑战。在流匹配中，奖励驱动的更新修改传输轨迹，没有对预训练数据流形的固有约束，可能使终端样本偏离预训练支持集。我们将这种失败模式形式化为流形漂移。理论上，我们证明了最优流匹配能恢复终端数据分布，而偏好更新只要其诱导的终端位移具有非零法向分量就会离开预训练流形。为此，我们提出了ThermoDPO，一个温度控制的损失函数，将成对偏好优化锚定在偏好样本上。在不同温度制度下，该目标连接了拒绝采样微调和FlowDPO，并控制了点态重建代理以度量流形距离。为了抵消低温下信号减弱，我们进一步引入了加权变体ThermoDPO-weighted。在主要玩具基准上，ThermoDPO-weighted的StrictScore为0.899，对比FlowDPO的0.629和FlowDPO+RFT的0.857。在SD3.5-M上，CFG=4.5时，OCR改进47.5%，四项指标平均改进16.0%。

**核心创新概述**

> 首次将偏好优化中的奖励黑客问题归因于流形漂移，并提出了温度控制的ThermoDPO目标，从理论上证明其能保持预训练流形，为流匹配对齐提供了新见解。

**创新点拆解**

- 形式化了流形漂移概念，揭示偏好优化导致生成样本偏离预训练数据分布的内在机制
- 提出了ThermoDPO，通过温度控制将偏好优化锚定在偏好样本上，避免流形漂移
- 理论证明了最优流匹配恢复终端分布，而偏好更新在非零法向位移时导致漂移
- 引入了加权变体ThermoDPO-weighted，缓解低温下信号减弱问题
- 在流匹配模型上实现了显著的OCR性能提升（47.5%）和平均四项指标改进16.0%

**当前局限**

> ['主要在玩具基准上评估，可能缺乏复杂真实场景的验证', '温度参数的调节需要启发式方法，可能影响稳定性', '理论分析可能假设简单流形结构，现实数据流形更复杂', '计算开销可能因加权机制增加']

**后续可改进方向**

- 在更复杂的真实数据集上验证流形漂移现象及ThermoDPO效果
- 探索自适应温度调节策略以简化超参数选择
- 将ThermoDPO推广到其他生成模型（如扩散模型）
- 结合其他正则化方法进一步约束流形偏移

**工程启发**

> 提供了一个有效的偏好优化方法，可改善生成模型的对齐质量，尤其在OCR等需要高一致性任务的合成数据生成中，减少奖励黑客导致的输出退化。

**为什么值得关注**

> 生成模型广泛用于合成训练数据，奖励黑客会降低合成数据质量，进而影响OCR等下游任务。ThermoDPO通过控制流形漂移提升了合成数据的生成可靠性，对OCR数据增强有直接价值。

**原始摘要**

Preference optimization is a standard alignment method for generative models, yet extending it to
continuous-time dynamics remains non-trivial. In flow matching, reward-driven updates modify
transport trajectories without an inherent constraint to the pretrained data manifold and can move
terminal samples off the pretrained support. We formalize this failure mode as manifold drift.
Theoretically, we show that optimal flow matching recovers the terminal data distribution, whereas a
preference update leaves the pretrained manifold whenever its induced terminal displacement has a
nonzero normal component. As a remedy, we propose ThermoDPO, a temperature-controlled objective that
anchors pairwise preference optimization on preferred samples. Across temperature regimes, this
objective connects rejection sampling fine-tuning and FlowDPO and controls a pointwise
reconstruction-based surrogate for manifold distance. To counteract diminished signals at low
temperatures, we further introduce a weighted variant, ThermoDPO-weighted. On the main toy
benchmark, ThermoDPO-weighted attains a StrictScore of 0.899, compared with 0.629 for FlowDPO and
0.857 for FlowDPO+RFT. On SD3.5-M at CFG = 4.5, it improves OCR by 47.5% and the average of four
metrics by 16.0%.

---
