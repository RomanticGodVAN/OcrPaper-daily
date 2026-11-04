# OCR / 文档解析研究日报（2026-11-04）

## 报告说明

- 检索源：arXiv API
- 检索查询：`(all:"document parsing" OR all:"document understanding" OR all:"optical character recognition" OR all:OCR OR all:"layout analysis" OR all:"document layout analysis" OR all:"text recognition" OR all:"table recognition" OR all:"form understanding" OR all:"document intelligence" OR all:"page understanding" OR all:"scene text recognition" OR all:"handwritten text recognition" OR all:"information extraction") AND (cat:cs.CV OR cat:cs.AI OR cat:cs.CL OR cat:eess.IV)`
- 生成时间（UTC）：`2026-11-04 07:29:03`
- 大模型综合分析：`关闭`
- 备注：DeepSeek 处理失败：Expecting ':' delimiter: line 1 column 1004 (char 1003)

## 三、今日论文概览

1. **OCR in the Foundation Model Era: From Specialist Models to Unified Models** | 标签：OCR综述、基础模型、文档解析、视觉语言模型、幻觉评测、统一模型
2. **DR Pixel: Page-Native Deep Research with Vision-Language Models** | 标签：页面原生检索、深度研究智能体、多模态RAG、视觉语言模型、智能体训练、文档理解
3. **ArabGeoText: Tool-Augmented Vision-Language Models for Arabic Geospatial Text Spotting** | 标签：地理空间文本定位、阿拉伯语OCR、视觉语言模型、LoRA微调、基准数据集、工具增强
4. **FlowTranslator: Training-Free In-Image Machine Translation with Flow-Based Editing** | 标签：图像内机器翻译、扩散模型、免训练方法、流编辑、OCR回读、文本渲染
5. **Unlocking Criminal Court Decisions: Flexible Information Extraction for Empirical Legal Research** | 标签：信息抽取、法律文书、大语言模型、标注指令、一致性分析、文档结构化
6. **RxnMiner: A Multimodal Agent for Structured Reaction Data Extraction from Chemistry Figures** | 标签：化学插图解析、多模态智能体、信息抽取、科学文档、基准数据集、领域工具箱
7. **EP-LVMQA: Evidence-Preserving Coarse-to-Fine Localization for Low-Quality Long Video Moment Question Answering** | 标签：长视频时刻问答、多模态证据定位、由粗到细定位、低质量多模态输入、OCR稀疏场景、不确定性建模、视频问答

## 八、论文逐篇解析

### 1. OCR in the Foundation Model Era: From Specialist Models to Unified Models

- arXiv: [2611.04874v1](https://arxiv.org/abs/2611.04874v1)
- PDF: [下载链接](https://arxiv.org/pdf/2611.04874v1)
- 作者: Zhiheng Li, Zongyang Ma, Jiaxian Chen, Cheng Cui, Yi Liu, Ziqi Zhang, Chunfeng Yuan, Bing Li, Xiang Bai, Weiming Hu
- 发布时间: 2026-11-03T13:27:22Z
- 分类: cs.CV
- 相关性评分: 34
- 主题标签: OCR综述、基础模型、文档解析、视觉语言模型、幻觉评测、统一模型

**中文摘要**

> 该综述系统梳理了基础模型时代的OCR发展脉络，将OCR定义为忠实转录任务：在指定视觉范围内完整重建图像中可观察的文本、符号和文档结构，且输出中每个元素都须可由图像视觉证据验证。文章追踪了从专用OCR模型到统一模型的发展，涵盖文本检测与识别联合建模、结构化序列生成以及预训练视觉-语言模型的应用，并将当代OCR系统划分为五类共存的体系：模块化工具包与任务专用模型、专用文档VLM、混合工作流、通用VLM、商业产品与托管服务。文中比较了这些体系在架构、数据和训练方面的差异，讨论了生成式OCR中的幻觉与遗漏、空间定位不足和推理成本问题，并评述了从字符/场景文本识别到结构元素解析和整页转录的评测现状，指出输出定义不一致、性能归因于单个组件困难、真实采集条件与可见内容结构覆盖不足等评测缺口。

**核心创新概述**

> 以忠实转录为核心重新定义OCR任务边界，提出统一模型与专用模型并存的五类系统分类框架，并系统性地将幻觉/遗漏、空间定位和推理成本纳入生成式OCR的质量与评测讨论。

**创新点拆解**

- 将OCR任务形式化为可视觉验证的忠实转录，明确输出须由图像证据支撑
- 提出模块化工具包、专用文档VLM、混合工作流、通用VLM、商业服务五类系统分类
- 系统比较不同体系在架构、训练数据和推理成本上的取舍
- 梳理从字符级到整页转录的评测谱系并指出归因与覆盖缺口

**当前局限**

> ['综述性质，未提出新的可训练方法或模型', '对五类系统的划分主要基于定性观察，缺乏统一的定量对比', '对生成式OCR幻觉的讨论停留在问题描述层面，未给出系统化度量方案', '真实采集条件与可见结构覆盖的评测缺口仅被指出，未提供具体基准设计']

**后续可改进方向**

- 构建可验证忠实转录的评测协议，将输出元素与图像证据显式对齐并量化幻觉率
- 设计组件级消融与归因基准，分离检测、识别、结构化生成各环节的贡献
- 扩展真实拍摄条件（模糊、遮挡、透视、低分辨率）下的整页转录评测集
- 探索统一模型中检测、识别与结构解析的联合训练范式及其成本-精度权衡

**工程启发**

> 为OCR系统选型提供清晰的技术版图：模块化管线适合可控成本与可解释场景，专用文档VLM适合结构化文档解析，通用VLM适合开放场景但需警惕幻觉与推理成本。对构建生产级OCR/文档解析流水线具有直接参考价值。

**为什么值得关注**

> 该文直接聚焦OCR在基础模型时代的范式转变与评测体系，是理解当前OCR技术格局与后续研究方向的纲领性文献。

**原始摘要**

Optical Character Recognition (OCR) is among the oldest and most widely deployed applications of
artificial intelligence. This survey reviews its development, focusing on the Foundation Model Era.
We define OCR through faithful transcription: within a specified visual scope, OCR should completely
reconstruct the text, notation, and document structure observable in the source image, and every
textual, notational, or structural element in the output must be verifiable from visual evidence in
that image. We trace the development from specialist OCR models toward unified models, examining
joint text detection and recognition, structured sequence generation, and the use of pretrained
vision-language models (VLMs). We organize contemporary OCR systems into five coexisting families:
modular toolkits and task-specific models, specialized document VLMs, hybrid workflows, general-
purpose VLMs, and commercial products and managed services. We compare their architectures, data,
and training, examining hallucination and omission, insufficient spatial grounding, and inference
cost in generative OCR. We review evaluation from character and scene text recognition to parsing
individual structural elements and full-page transcription, highlighting gaps in consistent output
definitions, attribution of performance to individual components, and coverage of real capture
conditions and visible content and structure. Finally, we summarize the challenges facing OCR and
discuss directions for future research. We continuously track related work at
https://github.com/zhihengli-casia/Awesome-OCR-in-the-Foundation-Model-Era.

---

### 2. DR Pixel: Page-Native Deep Research with Vision-Language Models

- arXiv: [2611.03097v1](https://arxiv.org/abs/2611.03097v1)
- PDF: [下载链接](https://arxiv.org/pdf/2611.03097v1)
- 作者: Tiansheng Hu, Yichuan Wang, James V. Talwar, Nicholas Tomlin, Chen Zhao, Sewon Min
- 发布时间: 2026-11-02T13:13:42Z
- 分类: cs.CV, cs.CL, cs.IR
- 相关性评分: 16
- 主题标签: 页面原生检索、深度研究智能体、多模态RAG、视觉语言模型、智能体训练、文档理解

**中文摘要**

> 针对现有深度研究智能体通常将论文压缩为OCR抽取文本的问题，作者提出页面原生深度研究：直接检索并推理渲染后的文档页面图像。构建了DR Pixel，首个以渲染页面图像为唯一检索与推理单元的端到端多模态深度研究智能体，语料规模达106万页。同时构建DRPixelBench基准，要求对科学论文中的文本、图、表和公式进行联合推理。实验发现，无需训练的页面原生方法在GPT-5.4、Gemini-3.5-Flash、Qwen3.6-27B等模型上已优于基于OCR文本的基线，且工具调用更少。针对智能体监督微调中教师轨迹噪声大的问题，提出反事实信用重加权方法，按各推理与动作步骤对最终答案的反事实贡献进行细粒度赋权。训练后检索召回提升约15个百分点，最终准确率提升超10个百分点，并在四个现有基准上超过未训练基线；在分布外ViDoRe-V3上距oracle仅1.8个点。

**核心创新概述**

> 提出以渲染页面图像为唯一检索与推理单元的页面原生深度研究范式，并给出首个开源端到端多模态DR智能体与配套基准，同时提出面向智能体轨迹的反事实信用重加权训练方法。

**创新点拆解**

- 任务定义上以页面图像替代OCR文本作为检索与推理的基本单元
- 构建DRPixelBench，覆盖文本、图、表、公式的跨模态推理评测
- 提出反事实信用重加权，对推理与动作步骤进行细粒度信用分配以抑制教师轨迹噪声
- 端到端多模态智能体架构，训练后检索召回与最终准确率同步提升

**当前局限**

> ['页面图像作为检索单元带来更高的视觉编码与推理开销，长文档场景下的可扩展性未充分讨论', '信用重加权重依赖教师轨迹质量与反事实模拟的合理性', '基准以科学论文为主，对扫描件、手写、低质量文档的泛化性未知', '分布外评测仅在一个基准上报告，结论稳健性有待扩展']

**后续可改进方向**

- 研究页面图像表示的高效压缩与多粒度检索索引，降低页面级推理成本
- 将反事实信用分配扩展到多轮工具调用与失败恢复轨迹的自动筛选
- 把页面原生范式与OCR文本混合检索结合，探索互补而非替代关系
- 扩展到扫描文档、多语言和历史档案等真实采集条件进行评测

**工程启发**

> 为文档问答与科研情报检索系统提供了绕过OCR误差传播的工程路径：直接对页面图像做检索与推理，可减少表格、公式、图注等结构化信息的丢失；其信用重加权方法也可用于训练其他工具调用型智能体。

**为什么值得关注**

> 该文直接挑战OCR文本作为文档理解中间表示的主流做法，与OCR/文档解析研究中的信息损失和级联误差问题高度相关。

**原始摘要**

Complex documents such as scientific papers contain rich information in tables, figures, and
equations; however, existing deep research (DR) agents typically reduce papers to OCR-extracted
text. We instead ask whether vision-language models (VLMs) can enable page-native deep research:
directly retrieving and reasoning over rendered document page images. We introduce DR Pixel, the
first open-source end-to-end multimodal DR agent that uses rendered page images as its sole
retrieval and reasoning unit, operating over a corpus of 1.06M pages. To evaluate this setting, we
construct DRPixelBench, a benchmark on scientific papers requiring reasoning over text, figures,
tables, and equations. Surprisingly, page-native DR already works well without training,
outperforming OCR-based baselines across state-of-the-art models like GPT-5.4, Gemini-3.5-Flash, and
Qwen3.6-27B, while requiring fewer tool calls. We next turn to DR training. A key challenge is that
teacher trajectories for agentic supervised finetuning are noisy, mixing critical reasoning and
action steps with redundant or failed attempts. To address this, we introduce counterfactual credit
reweighting, a fine-grained credit assignment method that weights individual reasoning and action
steps by their counterfactual contribution to the final answer. Our training improves retrieval
recall by about 15 points and final accuracy by over 10 points on DRPixelBench, and likewise
outperforms the untrained baseline on four existing benchmarks. On out-of-distribution ViDoRe-V3, DR
Pixel comes within 1.8 points of an oracle that is given the gold pages directly. Our results
suggest that the conventional OCR-then-retrieve pipeline is not only unnecessary but suboptimal:
directly retrieving and reasoning over visual document pages makes complex DR both more effective
and more efficient.

---

### 3. ArabGeoText: Tool-Augmented Vision-Language Models for Arabic Geospatial Text Spotting

- arXiv: [2611.03339v1](https://arxiv.org/abs/2611.03339v1)
- PDF: [下载链接](https://arxiv.org/pdf/2611.03339v1)
- 作者: Yakoub Bazi, Sarah Alsaleh, Mohamad M. Al Rahhal, Mohamed A. Mekhtiche, Mansour Zuair
- 发布时间: 2026-11-02T15:58:02Z
- 分类: cs.CV
- 相关性评分: 12
- 主题标签: 地理空间文本定位、阿拉伯语OCR、视觉语言模型、LoRA微调、基准数据集、工具增强

**中文摘要**

> 地理空间文本定位旨在栅格地图中定位并转录道路名、行政区名和地标等地理标注，这类文本通常尺寸小、排列密集且方向任意。阿拉伯语文本识别在文档和自然场景中已有较多研究，但阿拉伯语地理空间文本定位仍属空白。作者提出ARABGEOTEXT基准，覆盖利雅得和吉达970个地理位置，每种视图类型含17,875个人工标注文本实例；每个位置配对一个OpenStreetMap渲染图与叠加在遥感影像上的合成图，成对视图保持标注内容与像素几何一致，便于跨背景评测，并按地理分区支持同城与跨城评测检测、识别和端到端定位。实验显示直接使用Qwen3.5-4B做定位难以恢复瓦片内全部标注，因此提出工具增强的视觉语言框架，结合YOLO26定位与裁剪矫正、经LoRA适配的Qwen3.5-4B识别。该框架在两种视图和测试城市上均优于直接LoRA适配的Qwen3.5-4B，且在定位固定时，读取器适配进一步优于零样本读取器。

**核心创新概述**

> 构建首个阿拉伯语地理空间文本定位基准，提供OSM渲染图与遥感影像叠加图的成对视图及地理分区评测协议，并提出定位与识别解耦的工具增强VLM框架。

**创新点拆解**

- 任务定义上聚焦阿拉伯语地理空间文本定位这一未被覆盖的场景
- 数据构建上采用成对视图设计，保持标注内容与像素几何一致以隔离背景变化
- 评测协议按地理分区支持同城与跨城泛化评估
- 方法上将YOLO26定位裁剪与LoRA适配VLM识别组合为工具增强框架

**当前局限**

> ['仅覆盖利雅得和吉达两座城市，地理与语言多样性有限', '采用YOLO与VLM两阶段级联，误差会在定位与识别之间传递', '遥感叠加图为合成生成，与真实遥感底图上的地图标注分布可能存在域差异', '未报告密集小文本在低分辨率瓦片下的召回上限分析']

**后续可改进方向**

- 扩展至更多阿拉伯语城市及多语言地图标注，检验跨语言跨区域迁移
- 研究定位与识别的端到端联合优化，减少级联误差传播
- 引入真实遥感底图与更多地图样式，缩小合成视图与真实分布的差距
- 针对密集小文本设计超分辨率或瓦片级自适应裁剪策略

**工程启发**

> 为地图类文档与地理信息产品的文本提取提供了可复用方案：将目标检测定位与LoRA微调的VLM识别解耦，可在保持定位精度的同时低成本适配特定语言与字体，适合地图POI抽取和地图数字化工程。

**为什么值得关注**

> 该文属于OCR中场景/地图文本定位与识别方向，涉及小文本、密集排列、任意方向和低资源语言等典型难点，与OCR研究直接相关。

**原始摘要**

Geospatial text spotting involves locating and transcribing geographic labels, such as road names,
district names, and landmarks, in raster maps. These labels are often small, densely arranged, and
arbitrarily oriented. Although Arabic text recognition has been studied extensively in documents and
natural scenes, Arabic geospatial text spotting remains underexplored. We introduce ARABGEOTEXT, an
Arabic-centric benchmark covering 970 geographic locations in Riyadh and Jeddah, with 17,875
manually annotated text instances per view type. For each location, we pair an OpenStreetMap (OSM)
rendering with a composite created by overlaying that rendering on the corresponding remote sensing
(RS) imagery. The paired views preserve label content and pixel geometry, allowing evaluation across
different backgrounds. Geographic partitions support in-city and city-disjoint evaluation of
detection, recognition, and end-to-end spotting. Experiments with direct Qwen3.5-4B spotting show
difficulties in recovering all labels within a tile. We therefore propose a tool-augmented vision-
language framework that combines YOLO26 localization and crop rectification with Qwen3.5-4B
recognition adapted through low-rank adaptation (LoRA). The framework outperforms direct LoRA-
adapted Qwen3.5-4B spotting across both image views and test cities. With localization held fixed,
reader adaptation further improves recognition over the pretrained zero-shot reader. The dataset and
code will be made publicly available at https://github.com/yakoubbazi/ArabGeoText.

---

### 4. FlowTranslator: Training-Free In-Image Machine Translation with Flow-Based Editing

- arXiv: [2611.04303v1](https://arxiv.org/abs/2611.04303v1)
- PDF: [下载链接](https://arxiv.org/pdf/2611.04303v1)
- 作者: Zhixian Li, Xingsong Ye, Yongkun Du, Yunyan Xiao, Yanglin Huang, Pinxuan Chen, Jiyu Zhuang, Cong Xu, Zhineng Chen
- 发布时间: 2026-11-03T04:33:47Z
- 分类: cs.CV, cs.AI
- 相关性评分: 9
- 主题标签: 图像内机器翻译、扩散模型、免训练方法、流编辑、OCR回读、文本渲染

**中文摘要**

> 图像内机器翻译需在保留周围视觉上下文的前提下替换图像中的文字。现有任务专用模型效果可观但依赖大量翻译前后配对图像。随着文本到图像模型在多语言文本生成上达到可用水平，作者认为该能力可迁移至图像内机器翻译，提出免训练的FlowTranslator框架：先用OCR模型与LLM生成翻译提示，注入基于T2I的扩散模型；为优化译文的准确与自然生成，引入两种轨迹控制——区域耦合释放（RCR）在轨迹早期部分解耦文本区域内的目标分支噪声，耦合扩展（CE）在轨迹中期放大正在形成的编辑位移。在EasyOCR回读协议下，FlowTranslator取得平均PRIM BLEU 20.6和COMET 57.2，显著超过强训练基线UniTranslator；在更具挑战性的真实整图ScenePair照片翻译为中文任务上，达到40.1%的精确匹配准确率，超过现有编辑系统。

**核心创新概述**

> 将预训练T2I模型的多语言文本生成能力迁移到图像内机器翻译，提出完全免训练的基于流编辑框架，并通过两种轨迹控制操作实现文本区域替换与视觉上下文保持。

**创新点拆解**

- 任务范式上以扩散模型流编辑替代配对数据监督，实现免训练图像内翻译
- 提出区域耦合释放与耦合扩展两种扩散轨迹控制策略，分别作用于早期与中期去噪阶段
- 以OCR模型加LLM自动生成翻译提示，形成闭环的免标注流水线
- 在整图真实照片翻译任务上验证方法有效性

**当前局限**

> ['依赖T2I模型的多语言文本渲染能力，对非拉丁文字或长文本的生成保真度可能不稳定', '评测采用EasyOCR回读协议，可能引入识别误差并偏向易被OCR识别的渲染结果', '免训练方法在字体、字号、颜色与背景纹理匹配上仍可能偏离原图风格', 'ScenePair整图翻译精确匹配准确率40.1%，距实用仍有差距']

**后续可改进方向**

- 研究译文渲染与原始字体、颜色、透视的显式风格对齐约束
- 将OCR回读反馈纳入去噪轨迹的在线校正，形成生成-验证闭环
- 扩展到低资源语言与竖排、艺术字等非标准排版场景
- 设计更贴近人类判断的评测协议，减少对OCR回读的依赖

**工程启发**

> 展示了免训练、免配对数据的图像翻译工程路径，可显著降低跨境电商、多语言海报和截图本地化的数据标注成本；其轨迹控制思路也可迁移到其他基于扩散模型的图像文本编辑任务。

**为什么值得关注**

> 该方法以OCR作为翻译提示生成与效果验证的关键组件，属于OCR下游应用与OCR反馈驱动生成的交叉方向。

**原始摘要**

In-image machine translation (IIMT) replaces text in an image with its translation while preserving
the surrounding visual context. Existing task-specific models achieve convincing performance but
require massive paired training images before and after translation. As advanced text-to-image (T2I)
models have reached a practically usable level of multilingual text generation, we argue that this
capability can be transferred to IIMT and present FlowTranslator. It is a training-free IIMT
framework that first employs an OCR model and an LLM to generate the translation prompt, which is
injected into the T2I-based diffusion model. To optimize the accurate and natural generation of
translated text, we introduce two trajectory controls: Region Coupling Release (RCR) partially
decorrelates target-branch noise inside the text region early in the trajectory, while Coupling
Expansion (CE) amplifies the emerging edit displacement mid-trajectory. Under the EasyOCR read-back
protocol, FlowTranslator achieves average PRIM BLEU and COMET scores of 20.6 and 57.2, respectively,
substantially outperforming the strong training-based baseline UniTranslator. On the more
challenging and realistic whole-image ScenePair photographs translated into Chinese, it reaches
40.1\% exact-match accuracy and surpasses existing editing systems, some of which only address the
text-rendering stage rather than the complete IIMT task. These results establish flow-based editing
as a strong, fully training-free baseline for IIMT.

---

### 5. Unlocking Criminal Court Decisions: Flexible Information Extraction for Empirical Legal Research

- arXiv: [2611.03051v1](https://arxiv.org/abs/2611.03051v1)
- PDF: [下载链接](https://arxiv.org/pdf/2611.03051v1)
- 作者: Tomáš Knap, Ivana Kvapilíková, Jan Černý, Klára Bendová, Jaromír Šavelka, Vojtěch Pour, Jakub Drápal
- 发布时间: 2026-11-02T12:46:53Z
- 分类: cs.CL, cs.AI
- 相关性评分: 6
- 主题标签: 信息抽取、法律文书、大语言模型、标注指令、一致性分析、文档结构化

**中文摘要**

> 刑事判决书包含犯罪行为描述，可支撑定量法律研究，但结构化这些文本所需的属性和抽取规则往往无法预先完整指定。作者提出基于LLM的流水线，通过属性探索、文本片段抽取和取值归一化构建结构化数据集，并由法律专家持续修订标注指令。在醉驾（DUI）和禁驾期驾驶（DDB）两类交通犯罪上评测：DUI中修订指令后抽取准确率从52%升至70%，标注者间一致性也提高；同一模型重复运行的结果彼此一致性高于其与金标注的一致性，说明输出一致不等于正确；标注者之间与模型之间的分歧有助于暴露指令不清晰之处。DDB中指令定义了固定类别和输出格式，多数属性的—致性较高。

**核心创新概述**

> 提出由法律专家迭代精炼标注指令驱动的LLM信息抽取流水线，并将标注者间与模型间分歧作为指令质量的诊断信号，而非单纯追求输出一致性。

**创新点拆解**

- 将属性探索、片段抽取与取值归一化组织为可迭代的LLM流水线
- 以专家可修订的标注指令作为抽取规则的主要载体，应对规则无法预先完全指定的问题
- 实证揭示模型重复运行的自洽性高于与金标注的一致性，区分一致性与正确性
- 将分歧分析用作指令不清的探测手段

**当前局限**

> ['仅在两类交通犯罪上验证，罪名与文书类型覆盖有限', '抽取准确率70%仍不足以支撑高置信度的定量法律研究', '未与其他信息抽取范式（如微调模型、规则系统）进行系统对比', '指令迭代依赖法律专家投入，规模化成本未评估']

**后续可改进方向**

- 扩展至更多罪名、多语言与多司法辖区判决书，检验流水线泛化性
- 引入不确定性估计与人工复核路由，将低置信抽取交由专家裁定
- 研究指令自动诊断与改写方法，降低对专家反复迭代的依赖
- 构建判决书信息抽取的标准评测集与统一属性模式

**工程启发**

> 为法律文书等长文本结构化场景提供了可落地的LLM抽取工程范式：以专家指令迭代替代固定规则，并利用一致性/分歧分析做质量控制，适合法律科技中的案件数据化与实证研究支撑。

**为什么值得关注**

> 该文属于文档信息抽取方向，与OCR后的文档结构化理解环节衔接紧密，其指令驱动抽取与质量诊断思路可迁移到OCR下游任务。

**原始摘要**

Criminal verdicts contain descriptions of criminal behavior that can support quantitative legal
research, but structuring them requires attributes and extraction rules that cannot always be fully
specified in advance. We present an LLM-based pipeline that builds a structured dataset through
attribute exploration, text span extraction, and value normalization, guided by annotation
instructions that legal experts can refine. We evaluate it on two traffic offenses: driving under
the influence (DUI) and driving despite a ban (DDB). For DUI, revising the instructions was
associated with higher extraction accuracy (from 52% to 70% of correctly extracted values) and
higher agreement between human annotators. Repeated runs of the same model agreed with each other
more than with the gold annotations, showing that consistent output is not necessarily correct,
while disagreement between annotators and between models helped reveal unclear instructions. For
DDB, where the instructions defined fixed categories and output formats, agreement was high for most
attributes.

---

### 6. RxnMiner: A Multimodal Agent for Structured Reaction Data Extraction from Chemistry Figures

- arXiv: [2611.02826v1](https://arxiv.org/abs/2611.02826v1)
- PDF: [下载链接](https://arxiv.org/pdf/2611.02826v1)
- 作者: Jinbo Hu, Songren Zhang, Chuanxun Fu, Jinrui Huang, Zhen Hao Wong, Dongxu Cui, Haoran Fan, Muhao Ge, Zhen Jian, Jian Zhou, Chengxiang Luo, Han Lyu, Haoyi Tao, Chaozheng Huang, Hanzheng Li, ZiChen Wang, Hengtian Ma, Jinyang Dai, Nan Wang, Yanhui Hong, Xi Fang, Guolin Ke
- 发布时间: 2026-11-02T09:24:55Z
- 分类: cs.AI
- 相关性评分: 6
- 主题标签: 化学插图解析、多模态智能体、信息抽取、科学文档、基准数据集、领域工具箱

**中文摘要**

> 反应数据支撑反应预测、条件推荐和逆合成规划的机器学习，但从文献插图中抽取这些数据仍需大量人工。许多插图通过共享模板、取代基表和产物网格编码多个实验，恢复具体反应记录需要分子识别、证据与单个实验条目的关联以及间接指定参与物的重建。作者提出RxnMiner多模态智能体系统，将专家启发的抽取流程与化学工具箱结合，协调上述操作：读取分子结构、解析共享与条目特异的证据、从模板实例化参与物，从而组装可溯源的反应记录。同时构建ChemRxn-Bench基准，含603个反应插图、8,547条人工标注并复核的反应记录，在统一协议下按精确分子身份与反应物-产物配对评测。以Qwen3.8-Flash-Next为骨干，RxnMiner将立体化学感知的反应宏F1从直接预测的21.0%提升至71.0%，最强现有抽取系统为25.0%；在五个骨干上，较无抽取流程与化学工具箱的同一基础智能体提升9.4至25.5个点。无人工干预应用于10,107个文献插图，产出88,202条可溯源反应记录的银语料。

**核心创新概述**

> 面向化学插图这一结构化多条目文档，提出结合专家抽取流程与化学工具箱的多模态智能体，实现从共享模板和表格中重建间接指定的反应记录，并提供大规模人工复核基准与银语料。

**创新点拆解**

- 任务定义上聚焦多实验插图到具体反应记录的实例化与溯源
- 方法上将专家启发流程与化学工具箱结合，协调分子识别、证据关联和模板实例化
- 构建ChemRxn-Bench，按精确分子身份和反应物-产物配对进行统一评测
- 无人工干预产出8.8万条可溯源银语料，展示规模化数据生产潜力

**当前局限**

> ['基准覆盖603个插图，化学空间与插图排版多样性可能有限', '依赖外部化学工具箱，工具箱错误会传导至最终记录', '银语料未经全量人工校验，下游使用存在噪声风险', '智能体流程步骤较多，推理成本与延迟未系统报告']

**后续可改进方向**

- 扩展至更多反应类型、复杂多步路线图与非常规排版插图
- 研究工具箱调用结果的自校验与回溯机制，降低级联错误
- 对银语料引入主动学习式抽样复核，量化噪声并持续修正
- 优化智能体流程压缩冗余步骤，降低大规模文献处理的推理成本

**工程启发**

> 为化学文献的自动化数据生产提供了可复用架构：专家流程加领域工具箱的多模态智能体可显著提升复杂科学插图的抽取精度，银语料范式也可迁移到材料、生物等其他科学图表抽取场景。

**为什么值得关注**

> 该文处理的是科学插图中的结构化信息抽取，属于OCR/文档解析在领域文档上的延伸，涉及分子结构识别、多条目关联与模板重建等文档理解难点。

**原始摘要**

Reaction data underpin machine learning for reaction prediction, condition recommendation, and
retrosynthetic planning, yet extracting these data from literature figures still requires
substantial manual effort. Many figures encode multiple experiments through shared templates,
substituent tables, and product grids. Recovering concrete reaction records therefore requires
molecular recognition, association of evidence with individual experimental entries, and
reconstruction of indirectly specified participants. We present RxnMiner, a multimodal agent system
that combines an expert-informed extraction procedure with a chemistry toolbox to coordinate these
operations. The agent reads molecular structures, resolves shared and entry-specific evidence, and
instantiates participants from templates to assemble source-linked reaction records. We also
introduce ChemRxn-Bench, a benchmark of 603 reaction figures with 8,547 manually annotated and
reviewed reaction records, evaluated under a common protocol for exact molecular identity and
reactant-product pairing. On this benchmark, with Qwen3.8-Flash-Next as the backbone, RxnMiner
raises stereochemistry-aware reaction macro-F1 from 21.0% under direct prediction to 71.0%, compared
with 25.0% for the strongest existing extraction system. Across five backbones, it also outperforms
the same base agent without the extraction procedure and chemistry toolbox by 9.4 to 25.5 points.
Applied without human intervention to 10,107 literature figures, RxnMiner produces a silver corpus
of 88,202 source-linked reaction records.

---

### 7. EP-LVMQA: Evidence-Preserving Coarse-to-Fine Localization for Low-Quality Long Video Moment Question Answering

- arXiv: [2611.04913v1](https://arxiv.org/abs/2611.04913v1)
- PDF: [下载链接](https://arxiv.org/pdf/2611.04913v1)
- 作者: Guoning Chen, Zhexun Hu, Yifan Wei, Yixuan Weng, Bin Li, Yufei Zhao
- 发布时间: 2026-11-03T13:53:08Z
- 分类: cs.CV
- 相关性评分: 2
- 主题标签: 长视频时刻问答、多模态证据定位、由粗到细定位、低质量多模态输入、OCR稀疏场景、不确定性建模、视频问答

**中文摘要**

> 该论文研究长视频时刻问答（LVMQA），要求系统返回带时间戳、可支撑答案的证据片段，而非仅输出标签或自由文本。针对教学、工业培训等长视频中字幕缺失、ASR噪声、OCR稀疏、关键动作短暂无解说等低质量证据问题，提出EP-LVMQA证据保留的由粗到细框架，包含不确定性感知多模态证据时间线、粗粒度证据规划器和证据条件细粒度定位器，并通过证据卡在两个模块间传递规划分数、匹配线索、源置信度代理、模态证据、邻域上下文和时间先验。在MedVidQA上取得26.1 R1@0.5和31.8 mIoU，较最强非本方法结果分别提升6.3和5.1点；Suff.@2与Ver.@2提升至25.4和22.6；在匹配低质量扰动下平均相对退化从14.6%降至11.1%；在Ego4D-NLQ和QVHighlights上与已有任务专用定位方法大体相当。

**核心创新概述**

> 将长视频时刻问答定义为返回时间戳证据的任务，并设计证据保留的由粗到细定位框架，显式建模多模态证据的不确定性及源置信度，以证据卡实现规划与细定位之间的结构化信息传递。

**创新点拆解**

- 任务定义上强调输出可检查的时间戳证据支撑，而非答案标签或自由文本
- 提出不确定性感知多模态证据时间线，对字幕、ASR、OCR等低质量模态证据进行置信度建模
- 设计证据卡机制，在粗规划器与细定位器之间传递规划分数、匹配线索、源置信度代理、邻域上下文和时间先验
- 采用由粗到细的两阶段定位架构，先规划候选证据区间再条件化细粒度定位
- 引入Suff.@2和Ver.@2等证据充分性与可验证性指标评估证据质量

**当前局限**

> 方法主要在MedVidQA上验证，在Ego4D-NLQ和QVHighlights上仅与任务专用定位方法大体相当，未体现明显优势；证据卡中的源置信度代理为启发式设计，缺乏对OCR、ASR等模态可靠性的系统校准；低质量扰动实验为人工匹配设置，与真实退化分布可能存在差异。

**后续可改进方向**

- 在更多长视频问答数据集上验证框架的跨域泛化性，尤其是非医学教学与工业流程场景
- 对ASR、OCR、字幕等模态的源置信度进行可学习校准，替代启发式代理
- 研究证据卡中各字段的消融贡献与信息压缩方式，降低模块间传递的冗余
- 将证据时间线扩展到细粒度时空证据，支持画面区域与时间段联合定位
- 设计更贴近真实退化的低质量基准，评估模态缺失与噪声组合下的鲁棒性

**工程启发**

> 框架输出带时间戳的可检查证据，适合医学教育、工业培训等需要可追溯依据的长视频问答场景；由粗到细的规划-定位结构和证据卡接口便于模块化工程实现与替换。

**为什么值得关注**

> 论文直接涉及OCR稀疏、ASR噪声等低质量文档/视频证据条件下的多模态证据定位与问答，其不确定性感知与证据保留思路对OCR下游的多模态问答与证据检索系统有参考价值。

**原始摘要**

Long instructional videos are increasingly used in medical education, industrial training, and
procedural knowledge transfer, yet their evidence is often incomplete or unreliable: subtitles may
be missing, ASR noisy, OCR sparse, and decisive actions briefly shown without narration. Existing
VideoQA systems typically return labels or free-form text, making answer support difficult to
inspect. We study Long Video Moment Question Answering (LVMQA), where a system returns timestamped
answer-supporting evidence. We propose EP-LVMQA, an evidence-preserving coarse-to-fine framework
comprising an Uncertainty-Aware Multimodal Evidence Timeline, a Coarse Evidence Planner, and an
Evidence-Conditioned Fine Localizer. An evidence card transfers planner scores, matched cues,
source-confidence proxies, modality-specific evidence, neighboring context, and a temporal prior
between the latter two modules. On MedVidQA, EP-LVMQA achieves 26.1 R1@0.5 and 31.8 mIoU, improving
the strongest non-ours results by 6.3 and 5.1 points. It raises Suff.@2 and Ver.@2 to 25.4 and 22.6,
gains of 9.5 and 8.8 points. Under matched low-quality perturbations, average relative degradation
is reduced from the strongest non-ours value of 14.6% to 11.1%. On Ego4D-NLQ and QVHighlights, EP-
LVMQA remains broadly comparable to established task-specific localization methods.

---
