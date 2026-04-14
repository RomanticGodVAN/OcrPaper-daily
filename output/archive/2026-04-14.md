# OCR / 文档解析研究日报（2026-04-14）

## 报告说明

- 检索源：arXiv API
- 检索查询：`(all:"document parsing" OR all:"document understanding" OR all:"optical character recognition" OR all:OCR OR all:"layout analysis" OR all:"document layout analysis" OR all:"text recognition" OR all:"table recognition" OR all:"form understanding" OR all:"document intelligence" OR all:"page understanding" OR all:"scene text recognition" OR all:"handwritten text recognition" OR all:"information extraction") AND (cat:cs.CV OR cat:cs.AI OR cat:cs.CL OR cat:eess.IV)`
- 生成时间（UTC）：`2026-04-14 04:20:03`
- 大模型综合分析：`开启`

## 一、今日执行摘要

> 今日论文聚焦于OCR/文档解析领域的多模态评估、基准构建、历史文档处理、信息提取方法及脑解码应用。核心趋势包括：强调受控基准以诊断视觉语言模型（VLM）能力，推动多模态多文档科学推理评估，探索传统与LLM-based OCR在古文字识别的性能比较，提出渐进学习优化通用信息提取（UIE），以及引入显著性先验提升脑解码图像重建。这些研究共同指向更精细化的模型评估、跨模态整合、效率优化和特定领域应用，为工程实践提供诊断工具、标准化平台和高效框架。

## 二、今日趋势判断

研究趋势呈现三大方向：一是基准测试从通用向受控、多模态多文档深化，如TraversalBench和PaperScope强调结构化评估以揭示模型弱点；二是技术融合加速，结合传统OCR、LLM和代理架构处理历史文档，同时渐进学习优化UIE；三是跨领域应用扩展，如脑解码引入显著性先验，与OCR潜在结合。整体上，工作更注重诊断性、真实场景复杂性和计算效率。

## 三、今日论文概览

1. **TraversalBench: Challenging Paths to Follow for Vision Language Models** | 标签：视觉语言模型、基准测试、视觉路径理解、多模态评估
2. **PaperScope: A Multi-Modal Multi-Document Benchmark for Agentic Deep Research Across Massive Scientific Papers** | 标签：多模态基准、科学文献理解、多文档推理、研究代理
3. **The Devil is in the Details -- From OCR for Old Church Slavonic to Purely Visual Stemma Reconstruction** | 标签：历史文档OCR、古文字识别、谱系学、LLM应用、代理架构
4. **ProUIE: A Macro-to-Micro Progressive Learning Method for LLM-based Universal Information Extraction** | 标签：通用信息提取、渐进学习、LLM微调、结构化输出
5. **Brain-Grasp: Graph-based Saliency Priors for Improved fMRI-based Visual Brain Decoding** | 标签：脑解码、显著性先验、扩散模型、图像重建

## 四、今天 OCR / 文档解析论文里的主要创新点

- 设计受控基准以系统评估模型在特定任务（如视觉路径遍历或多文档推理）上的能力，最小化外部依赖。
- 结合多种技术（如传统OCR、LLM、代理架构）处理复杂文档（如古文字），提升识别精度和流程灵活性。
- 采用渐进学习或结构化训练策略（如ProUIE的三阶段框架）优化模型性能，同时降低计算成本。
- 引入先验知识（如图信息显著性先验）或简化输出格式，增强模型的结构保真度和可控性。

## 五、后续 OCR 领域值得推进的改进方向

- 开发结合OCR与视觉路径理解的混合基准，用于评估文档图表或地图中的路径跟踪能力。
- 扩展多模态UIE任务至文档图像，集成OCR输出进行端到端的实体和关系提取。
- 优化LLM微调策略，针对历史文档OCR中的复杂字形和变音符号问题。
- 设计实时交互式研究代理评估任务，模拟真实科学工作流中的多文档检索和推理。
- 探索自适应显著性先验学习机制，用于脑解码中文本刺激的处理，结合OCR技术。

## 六、工程落地启发

- 利用TraversalBench等诊断工具分析VLM在视觉处理中的故障，优化自动驾驶或文档解析模型。
- 采用PaperScope基准评估科学文献分析系统，提升学术搜索引擎和研究助手的多模态推理能力。
- 实施代理OCR架构（如专用后处理代理）处理历史文档，提高古文字识别的准确性和流程效率。
- 应用ProUIE渐进学习框架训练UIE模型，降低生产环境中信息提取的计算开销并提升可控性。
- 集成显著性先验到脑解码流程，增强图像重建的结构一致性，支持医疗诊断应用。

## 七、优先关注论文

- **TraversalBench: Challenging Paths to Follow for Vision Language Models**：提供视觉路径遍历的受控基准，有助于诊断VLM在文档图表解析中的视觉处理能力，工程上可优化路径理解任务。
- **PaperScope: A Multi-Modal Multi-Document Benchmark for Agentic Deep Research Across Massive Scientific Papers**：首个多模态多文档科学推理基准，推动文档解析系统在学术领域的深度应用，如研究助手和知识整合工具。
- **The Devil is in the Details -- From OCR for Old Church Slavonic to Purely Visual Stemma Reconstruction**：系统比较OCR技术并创新纯视觉谱系方法，为历史文档数字化和古籍保护提供实用方案，工程上可扩展至多语言OCR。
- **ProUIE: A Macro-to-Micro Progressive Learning Method for LLM-based Universal Information Extraction**：提出高效渐进学习框架，提升UIE性能并降低计算成本，适用于文档处理流水线中的信息提取优化。

## 八、论文逐篇解析

### 1. TraversalBench: Challenging Paths to Follow for Vision Language Models

- arXiv: [2604.10999v1](https://arxiv.org/abs/2604.10999v1)
- PDF: [下载链接](https://arxiv.org/pdf/2604.10999v1)
- 作者: Clara Petrova, Zhuo Chen, Marin Soljačić
- 发布时间: 2026-04-13T04:58:52Z
- 分类: cs.CV
- 相关性评分: 16
- 主题标签: 视觉语言模型、基准测试、视觉路径理解、多模态评估

**中文摘要**

> 视觉语言模型（VLM）在多模态基准测试中表现优异，但其遵循复杂视觉路径的能力——人类观察者通常认为简单的任务——尚未得到充分测试。本文提出TraversalBench，一个用于精确视觉路径遍历的受控基准。每个实例包含一条连续折线、唯一起始标记和路径顶点标记；任务是从起点到终点遍历路径时恢复遇到的确切有序序列。该基准明确平衡了关键路径结构因素，包括自相交次数、曲折度、顶点数和附近混淆线，同时最小化对OCR、世界知识和开放式规划的依赖。研究发现自相交是主要困难来源。首次交叉分析显示错误高度局部化：在首次交叉前性能相对稳定，当模型必须解析正确延续时急剧下降。相比之下，附近混淆线产生较弱的持续性能下降，并随重复暴露而加剧。这些分析使TraversalBench成为识别模型是否遭受类人失败或持续视觉处理中其他故障的有用诊断工具。辅助阅读顺序基准进一步揭示了对左到右序列化兼容布局的一致偏好，但未解释路径复杂性的主要影响。这些结果共同将TraversalBench定位为受控诊断工具。

**核心创新概述**

> 首次提出专门针对视觉路径遍历能力的受控基准，通过精确控制路径结构因素（如自相交、曲折度）来系统评估VLM的视觉处理能力，而非依赖OCR或世界知识。

**创新点拆解**

- 任务定义创新：设计精确视觉路径遍历任务，要求模型恢复路径上的有序序列
- 基准设计方法：平衡关键路径结构因素（自相交、曲折度、顶点数、混淆线），最小化外部依赖
- 诊断分析框架：通过首次交叉分析和混淆线效应分析，区分类人失败与其他视觉处理故障

**当前局限**

> 基准主要关注合成折线路径，可能未完全覆盖真实世界复杂视觉场景（如自然图像中的遮挡、光照变化）；任务形式相对单一，缺乏多模态交互要素。

**后续可改进方向**

- 扩展基准包含真实图像中的路径跟踪任务
- 引入动态或交互式路径遍历场景
- 结合OCR或文本线索的混合路径理解任务

**工程启发**

> 为VLM视觉处理能力提供标准化诊断工具，有助于模型优化和故障分析，在自动驾驶路径理解、文档图表解析等场景有潜在应用价值。

**为什么值得关注**

> 虽然基准最小化OCR依赖，但其视觉序列理解能力与文档图像中的阅读顺序、流程图解析等OCR相关任务有间接关联。

**原始摘要**

Vision-language models (VLMs) perform strongly on many multimodal benchmarks. However, the ability
to follow complex visual paths -- a task that human observers typically find straightforward --
remains under-tested. We introduce TraversalBench, a controlled benchmark for exact visual path
traversal. Each instance contains a single continuous polyline, a unique start marker, and markers
placed at path vertices; the task is to recover the exact ordered sequence encountered when
traversing the path from start to finish. The benchmark explicitly balances key path-structural
factors including self-intersection count, tortuosity, vertex count, and nearby confounding lines,
while minimizing reliance on OCR, world knowledge, and open-ended planning. We find that self-
intersections are the dominant source of difficulty. A first-crossing analysis shows that errors are
sharply localized: performance is relatively stable immediately before the first crossing, then
drops steeply when the model must resolve the correct continuation. By contrast, nearby confounding
lines produce a weaker persistent degradation that compounds with repeated exposure. These analyses
make TraversalBench a useful diagnostic for identifying whether models suffer from human-like
failures or other breakdowns in sustained visual processing. An auxiliary reading-order benchmark
further reveals a consistent preference for layouts compatible with left-to-right serialization,
while not explaining away the main effects of path complexity. Together, these results position
TraversalBench as a controlled diagnostic of path-faithful visual reasoning and as a useful testbed
for studying multimodal spatial reasoning under ambiguity, clutter, and distractor structure. More
broadly, we position TraversalBench as a contribution to the still-limited area of sustained visual
grounding benchmarks for VLMs.

---

### 2. PaperScope: A Multi-Modal Multi-Document Benchmark for Agentic Deep Research Across Massive Scientific Papers

- arXiv: [2604.11307v1](https://arxiv.org/abs/2604.11307v1)
- PDF: [下载链接](https://arxiv.org/pdf/2604.11307v1)
- 作者: Lei Xiong, Huaying Yuan, Zheng Liu, Zhao Cao, Zhicheng Dou
- 发布时间: 2026-04-13T11:07:08Z
- 分类: cs.AI
- 相关性评分: 10
- 主题标签: 多模态基准、科学文献理解、多文档推理、研究代理

**中文摘要**

> 利用多模态大语言模型（MLLM）加速前沿科学研究前景广阔，但如何严格评估此类系统仍不明确。现有基准主要关注单文档理解，而真实科学工作流需要整合多篇论文的证据，包括文本、表格和图表。因此，多模态、多文档科学推理仍未被充分探索且缺乏系统评估。为填补这一空白，本文提出PaperScope，一个为深度研究代理设计的多模态多文档基准。PaperScope具有三大优势：（1）结构化科学基础：基于包含三年内2000多篇AI论文的知识图谱构建，为研究型查询提供结构化基础。（2）语义密集证据构建：整合语义相关的关键信息节点，采用优化随机游走文章选择器采样主题连贯的论文集，确保足够的语义密度和任务复杂性。（3）科学推理多任务评估：包含超过2000个QA对，涵盖推理、检索、总结和问题解决，支持多步科学推理评估。实验结果显示，即使先进系统如OpenAI Deep Research和Tongyi Deep Research在PaperScope上得分有限，突显了长上下文检索和深度多源推理的难度。PaperScope因此提供了一个严格基准及可扩展流程。

**核心创新概述**

> 首个针对多模态多文档科学推理的基准，强调从大量科学论文（含图表表格）中整合证据的深度研究能力，而非传统单文档理解。

**创新点拆解**

- 基准构建方法：基于知识图谱的结构化科学基础，确保任务真实性和复杂性
- 证据采样策略：优化随机游走文章选择器，生成语义密集且主题连贯的论文集
- 多任务评估框架：涵盖推理、检索、总结、问题解决等多维度科学能力评估

**当前局限**

> 基准目前聚焦AI领域论文，可能未覆盖其他科学领域的特定挑战；多模态内容主要限于图表表格，未包含视频、音频等更丰富模态。

**后续可改进方向**

- 扩展至跨学科科学文献基准
- 纳入更多模态类型（如代码、实验数据）
- 设计实时交互式研究代理评估任务

**工程启发**

> 为科学文献智能分析系统提供标准化评估平台，推动学术搜索引擎、研究助手等工具的发展，提升科研效率。

**为什么值得关注**

> 基准涉及文档图像（图表表格）理解与文本整合，与OCR增强的多文档信息提取任务高度相关。

**原始摘要**

Leveraging Multi-modal Large Language Models (MLLMs) to accelerate frontier scientific research is
promising, yet how to rigorously evaluate such systems remains unclear. Existing benchmarks mainly
focus on single-document understanding, whereas real scientific workflows require integrating
evidence from multiple papers, including their text, tables, and figures. As a result, multi-modal,
multi-document scientific reasoning remains underexplored and lacks systematic evaluation. To
address this gap, we introduce PaperScope, a multi-modal multi-document benchmark designed for
agentic deep research. PaperScope presents three advantages: (1) Structured scientific grounding. It
is built on a knowledge graph of over 2,000 AI papers spanning three years, providing a structured
foundation for research-oriented queries. (2) Semantically dense evidence construction. It
integrates semantically related key information nodes and employs optimized random-walk article
selector to sample thematically coherent paper sets, thereby ensuring adequate semantic density and
task complexity. (3) Multi-task evaluation of scientific reasoning. It contains over 2,000 QA pairs
across reasoning, retrieval, summarization, and problem solving, enabling evaluation of multi-step
scientific reasoning. Experimental results show that even advanced systems such as OpenAI Deep
Research and Tongyi Deep Research achieve limited scores on PaperScope, highlighting the difficulty
of long-context retrieval and deep multi-source reasoning. PaperScope thus provides a rigorous
benchmark alongside a scalable pipeline for constructing large-scale multi-modal, multi-source deep
research datasets.

---

### 3. The Devil is in the Details -- From OCR for Old Church Slavonic to Purely Visual Stemma Reconstruction

- arXiv: [2604.11724v1](https://arxiv.org/abs/2604.11724v1)
- PDF: [下载链接](https://arxiv.org/pdf/2604.11724v1)
- 作者: Armin Hoenen
- 发布时间: 2026-04-13T16:58:57Z
- 分类: cs.CV
- 相关性评分: 8
- 主题标签: 历史文档OCR、古文字识别、谱系学、LLM应用、代理架构

**中文摘要**

> 人工智能时代为许多领域和任务带来新可能性和陷阱。细节决定成败，这在构建新流程和执行小型实践实验时尤为突出。OCR和谱系学也不例外。本研究首先比较了一系列OCR系统（从经典到机器学习再到LLM），针对18世纪晚期手写教会斯拉夫语手稿的大约6000个字符。聚焦基本字母正确性，比较了超过10个CS OCR系统，其中包括2个LLM（GPT5和Gemini3-flash）。然后评估通过LLM的后处理，最后测试不同的代理OCR架构（专用后处理代理、代理流程和RAG）。随着新技术的发展，实验表明教会斯拉夫语基本字母的CER可能低至2-3%，但精细变音符号仍可能存在问题。OCR如何为下游谱系学任务提供支持是文章第二部分的切入点，该部分介绍了一种仅基于图像处理的新谱系方法。这里提出了一个自动化视觉字形提取、聚类和成对统计比较的流程，最终生成距离矩阵和谱系图，并应用于两个小型语料库：一个是14至16世纪的教会斯拉夫语马可福音，另一个是14和15世纪的法语玫瑰传奇。该方法的基本功能得到演示。

**核心创新概述**

> 系统比较传统OCR、机器学习OCR和LLM在古文字（教会斯拉夫语）识别上的性能，并创新提出纯视觉谱系重建方法，不依赖文本转录。

**创新点拆解**

- OCR评估框架：跨多种技术（经典OCR、ML、LLM）系统比较古文字识别性能
- 代理OCR架构：探索专用后处理代理、代理流程和RAG在OCR中的应用
- 纯视觉谱系方法：基于图像处理（字形提取、聚类、统计比较）直接重建谱系，绕过文本转录步骤

**当前局限**

> 实验规模较小（6000字符），可能未充分统计性能；纯视觉谱系方法仅在小语料库验证，泛化性待考；未深入探讨LLM在复杂古文字OCR中的优化策略。

**后续可改进方向**

- 扩展古文字OCR数据集规模和多语言覆盖
- 优化LLM用于历史文档OCR的微调策略
- 融合文本和视觉信息的混合谱系重建方法

**工程启发**

> 为历史文档数字化提供实用OCR方案和谱系分析新工具，在古籍保护、数字人文领域有直接应用价值。

**为什么值得关注**

> 核心聚焦OCR技术（特别是古文字和手写体）及其下游应用（谱系学），是OCR领域的直接研究。

**原始摘要**

The age of artificial intelligence has brought many new possibilities and pitfalls in many fields
and tasks. The devil is in the details, and those come to the fore when building new pipelines and
executing small practical experiments. OCR and stemmatology are no exception. The current
investigation starts comparing a range of OCR-systems, from classical over machine learning to LLMs,
for roughly 6,000 characters of late handwritten church slavonic manuscripts from the 18th century.
Focussing on basic letter correctness, more than 10 CS OCR-systems among which 2 LLMs (GPT5 and
Gemini3-flash) are being compared. Then, post-processing via LLMs is assessed and finally, different
agentic OCR architectures (specialized post-processing agents, an agentic pipeline and RAG) are
tested. With new technology elaborated, experiments suggest, church slavonic CER for basic letters
may reach as low as 2-3% but elaborated diacritics could still present a problem. How well OCR can
prime stemmatology as a downstream task is the entry point to the second part of the article which
introduces a new stemmatic method based solely on image processing. Here, a pipeline of automated
visual glyph extraction, clustering and pairwise statistical comparison leading to a distance matrix
and ultimately a stemma, is being presented and applied to two small corpora, one for the church
slavonic Gospel of Mark from the 14th to 16th centuries, one for the Roman de la Rose in French from
the 14th and 15th centuries. Basic functioning of the method can be demonstrated.

---

### 4. ProUIE: A Macro-to-Micro Progressive Learning Method for LLM-based Universal Information Extraction

- arXiv: [2604.10633v1](https://arxiv.org/abs/2604.10633v1)
- PDF: [下载链接](https://arxiv.org/pdf/2604.10633v1)
- 作者: Wenda Liu, Zhigang Song, Shuai Nie, Guangyao Liu, Lisung Chen, Binyu Yang, Yaran Chen, Peng Zhou, Hongzhen Wang, Yuchen Liu, Wenyue Hu, Jiaming Xu, Runyu Shi, Ying Huang
- 发布时间: 2026-04-12T13:20:58Z
- 分类: cs.CL
- 相关性评分: 6
- 主题标签: 通用信息提取、渐进学习、LLM微调、结构化输出

**中文摘要**

> 基于LLM的通用信息提取（UIE）方法通常依赖原始训练数据之外的额外信息，这增加了训练复杂性却往往收益有限。为解决此问题，本文提出ProUIE，一种从宏观到微观的渐进学习方法，在不引入任何外部信息的情况下改进UIE。ProUIE包含三个阶段：（i）宏观层面完整建模（CM），在完整训练数据上按照NER、RE和EE的内在难度顺序学习，构建统一提取基础；（ii）中观层面精简对齐（SA），在采样数据上操作，简化目标格式，精简和规范化结构化输出，使其更简洁可控；（iii）微观层面深度探索（DE），应用GRPO和逐步细粒度奖励（SFR）在结构单元上引导探索并提升性能。在36个公共数据集上的实验表明，ProUIE持续改进统一提取，在使用较小骨干网络的情况下，在NER和RE上平均优于强指令调优基线，并在大规模生产导向信息提取中进一步显示明显增益。

**核心创新概述**

> 提出无需外部信息的渐进学习框架，通过宏观到微观的三阶段训练优化LLM-based UIE，强调结构化输出的精简和可控性。

**创新点拆解**

- 渐进学习范式：分CM、SA、DE三阶段，从完整建模到精细探索逐步优化
- 训练策略：按任务难度顺序学习，结合简化目标格式和细粒度奖励（SFR）
- 效率设计：使用较小骨干网络实现性能提升，降低计算成本

**当前局限**

> 方法主要针对文本信息提取，未明确涉及多模态（如图像表格）UIE；渐进阶段设计可能增加训练复杂度。

**后续可改进方向**

- 扩展至多模态UIE任务（如文档图像中的实体关系提取）
- 探索更高效的渐进学习调度策略
- 结合OCR输出进行端到端文档信息提取

**工程启发**

> 为通用信息提取提供高效训练框架，提升生产环境中的提取准确率和可控性，适用于文档处理、知识图谱构建等场景。

**为什么值得关注**

> 信息提取是OCR下游核心任务，方法可迁移至文档图像理解，增强结构化信息抽取能力。

**原始摘要**

LLM-based universal information extraction (UIE) methods often rely on additional information beyond
the original training data, which increases training complexity yet often yields limited gains. To
address this, we propose ProUIE, a Macro-to-Micro progressive learning approach that improves UIE
without introducing any external information. ProUIE consists of three stages: (i) macro-level
Complete Modeling (CM), which learns NER, RE, and EE along their intrinsic difficulty order on the
full training data to build a unified extraction foundation, (ii) meso-level Streamlined Alignment
(SA), which operates on sampled data with simplified target formats, streamlining and regularizing
structured outputs to make them more concise and controllable, and (iii) micro-level Deep
Exploration (DE), which applies GRPO with stepwise fine-grained rewards (SFR) over structural units
to guide exploration and improve performance. Experiments on 36 public datasets show that ProUIE
consistently improves unified extraction, outperforming strong instruction-tuned baselines on
average for NER and RE while using a smaller backbone, and it further demonstrates clear gains in
large-scale production-oriented information extraction.

---

### 5. Brain-Grasp: Graph-based Saliency Priors for Improved fMRI-based Visual Brain Decoding

- arXiv: [2604.10617v1](https://arxiv.org/abs/2604.10617v1)
- PDF: [下载链接](https://arxiv.org/pdf/2604.10617v1)
- 作者: Mohammad Moradi, Morteza Moradi, Marco Grassia, Giuseppe Mangioni
- 发布时间: 2026-04-12T12:50:49Z
- 分类: eess.IV, cs.CV, cs.MM
- 相关性评分: 6
- 主题标签: 脑解码、显著性先验、扩散模型、图像重建

**中文摘要**

> 脑引导图像生成的最新进展改善了fMRI基于重建的质量；然而，在保留对象级结构和语义保真度方面仍存在基本挑战。许多现有方法忽视了显著对象的空间排列，导致概念不一致的输出。本文提出一种显著性驱动的解码框架，采用图信息显著性先验将脑信号中的结构线索转换为空间掩码。这些掩码与从嵌入中提取的语义信息一起，条件化扩散模型以引导图像再生，帮助保持对象一致性同时维持自然场景组合。与调用多个扩散阶段的流程相比，我们的方法依赖单个冻结模型，提供更轻量级但有效的设计。实验表明，该策略提高了与原始刺激的概念对齐和结构相似性，同时为高效、可解释和结构基础的脑解码引入了新方向。

**核心创新概述**

> 首次将图信息显著性先验引入fMRI脑解码，通过空间掩码条件化扩散模型，提升重建图像的对象结构和语义一致性。

**创新点拆解**

- 解码框架设计：融合图信息显著性先验和语义嵌入，条件化单扩散模型
- 结构保留机制：通过空间掩码明确编码对象布局，增强重建的结构保真度
- 效率优化：使用冻结单模型，避免多阶段扩散的复杂性和计算开销

**当前局限**

> 方法主要针对视觉刺激重建，未涵盖其他模态（如语言）脑解码；显著性先验的泛化性在不同脑数据集上待验证。

**后续可改进方向**

- 扩展至多模态脑解码任务
- 探索自适应显著性先验学习机制
- 结合OCR技术处理文本刺激的脑解码

**工程启发**

> 为脑机接口和神经科学工具提供更准确、高效的图像重建方法，推动医疗诊断和认知研究应用。

**为什么值得关注**

> 虽然非直接OCR研究，但其图像重建和结构保留技术与文档图像恢复、增强任务有方法论关联。

**原始摘要**

Recent progress in brain-guided image generation has improved the quality of fMRI-based
reconstructions; however, fundamental challenges remain in preserving object-level structure and
semantic fidelity. Many existing approaches overlook the spatial arrangement of salient objects,
leading to conceptually inconsistent outputs. We propose a saliency-driven decoding framework that
employs graph-informed saliency priors to translate structural cues from brain signals into spatial
masks. These masks, together with semantic information extracted from embeddings, condition a
diffusion model to guide image regeneration, helping preserve object conformity while maintaining
natural scene composition. In contrast to pipelines that invoke multiple diffusion stages, our
approach relies on a single frozen model, offering a more lightweight yet effective design.
Experiments show that this strategy improves both conceptual alignment and structural similarity to
the original stimuli, while also introducing a new direction for efficient, interpretable, and
structurally grounded brain decoding.

---
