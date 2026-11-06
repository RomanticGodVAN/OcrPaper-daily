# OCR / 文档解析研究日报（2026-11-06）

## 报告说明

- 检索源：arXiv API
- 检索查询：`(all:"document parsing" OR all:"document understanding" OR all:"optical character recognition" OR all:OCR OR all:"layout analysis" OR all:"document layout analysis" OR all:"text recognition" OR all:"table recognition" OR all:"form understanding" OR all:"document intelligence" OR all:"page understanding" OR all:"scene text recognition" OR all:"handwritten text recognition" OR all:"information extraction") AND (cat:cs.CV OR cat:cs.AI OR cat:cs.CL OR cat:eess.IV)`
- 生成时间（UTC）：`2026-11-06 07:54:06`
- 大模型综合分析：`开启`

## 一、今日执行摘要

> 本期四篇论文分别覆盖文档解析输出表示与评测（AmbiHTMLBench）、医疗多语种信息抽取（CardioLM）、低资源历史手写识别（ATHAAR）与图检索智能体（ArcRAG）。其中最值得关注的是 AmbiHTMLBench：它把文档解析的输出从 Markdown 转向可执行 HTML，并首次系统构建双协议评测，发现客观自动指标与人类感知保真度排序不一致。其余工作分别提示：领域预训练对严格跨度指标收益有限、历史手写场景现有 VLM 仍明显不足、检索流程与图构建解耦可行但绝对精度受图质量制约。整体看，OCR/文档解析的瓶颈正从"能否识别文字"转向"结构保真度如何度量"与"低资源复杂书写如何迁移"。

## 二、今日趋势判断

文档解析研究正在从纯文本转录转向可编辑、结构敏感的输出表示，并配套可复现的评测协议；同时医疗、历史手稿等垂直领域的低资源结构化抽取持续受到关注，评测开始引入临床医生、LLM 评判等主观锚定与多语言、跨构建等鲁棒性维度。

## 三、今日论文概览

1. **AmbiHTMLBench: A Benchmark for HTML-based Visually Rich Document parsing** | 标签：文档解析、HTML重建、基准评测、视觉丰富文档、多模态大模型
2. **CardioLM: A multilingual suite of small language models for the cardiology domain** | 标签：临床NLP、多语种命名实体识别、领域预训练、心脏病学、医疗文档结构化
3. **ATHAAR: A Medieval Scientific Arabic Manuscript Dataset for Handwritten Text Recognition** | 标签：手写文本识别、历史手稿、低资源OCR、视觉语言模型、阿拉伯语
4. **ArcRAG: Agentic Compositional Retrieval over Knowledge Graphs** | 标签：GraphRAG、知识图谱检索、智能体、跨构建可移植性、多跳问答

## 四、今天 OCR / 文档解析论文里的主要创新点

- 将评测从单一准确率扩展为客观指标与人类感知/临床评分相结合的双轨或多轨体系。
- 通过任务特定微调或继续预训练让中小参数专家模型在垂直场景（文档到HTML、心脏病学NER）达到可用水平。
- 构建带结构化标注的领域专用数据集（HTML页面、多语病例报告、阿拉伯语手稿），并公开标注规范。
- 在评测中显式引入跨领域/跨构建/跨字体的迁移与鲁棒性设定，而非仅在同分布测试集上报告。

## 五、后续 OCR 领域值得推进的改进方向

- 针对 HTML 重建任务设计更贴近人类感知的客观度量，重点校准表格保真度与二维布局一致性指标与人类偏好的排序相关性。
- 将 AmbiHTMLBench 扩展到公式、多栏排版及非英语文档，并增加 HTML 合法性与可渲染性校验作为硬约束指标。
- 研究文档解析中结构重建的边界检测与后处理解码，解决 NER 与 HTR 中普遍存在的实体/字符边界错误。
- 面向连写合字与变音符号设计视觉编码或语言先验约束，并在阿拉伯语手稿上验证跨字体、跨抄本的迁移效果。
- 探索以抄本间对齐与校勘信息作为弱监督信号，降低历史手写数据的人工标注成本。
- 系统比较小参数专家模型与通用多模态大模型在结构重建上的能力边界，给出按文档类型选型的量化依据。
- 把跨构建可移植性评测从多跳问答扩展到文档级结构化抽取与表格检索任务，检验检索智能体的通用性。

## 六、工程落地启发

- 文档解析产品应优先支持 HTML 等可编辑、可检查的结构化输出，并将渲染一致性与表格几何纳入回归测试。
- 在医疗多语种抽取落地时，不要默认领域预训练必然提升严格 F1，应同时准备联合多语训练骨干作为对照。
- 历史手写或复杂书写数字化项目应预留边界纠错与人工校勘环节，当前 VLM 在该场景尚不能直接替代人工。
- 构建 GraphRAG 或知识图谱检索系统时可采用查询时接口归纳降低对图模式的耦合，但需为图构建质量变化保留精度余量。
- 评测体系应同时报告客观指标与主观/人工评分，避免仅凭自动分数做模型选型。

## 七、优先关注论文

- **AmbiHTMLBench: A Benchmark for HTML-based Visually Rich Document parsing**：首次系统提出以 HTML 作为文档解析输出表示并配套双协议评测，直接关系文档解析产品的输出格式与回归测试设计。
- **ATHAAR: A Medieval Scientific Arabic Manuscript Dataset for Handwritten Text Recognition**：揭示现有视觉语言模型在连写合字与变音符号场景下的明显不足，是低资源历史手写 OCR 的关键验证基准。
- **CardioLM: A multilingual suite of small language models for the cardiology domain**：量化了领域预训练收益有限而多语联合训练更优的结论，对医疗文档结构化选型有直接参考价值。
- **ArcRAG: Agentic Compositional Retrieval over Knowledge Graphs**：提出跨图构建可移植性这一新评测维度，若扩展到文档结构化检索可降低系统对图模式的耦合成本。

## 八、论文逐篇解析

### 1. AmbiHTMLBench: A Benchmark for HTML-based Visually Rich Document parsing

- arXiv: [2611.06449v1](https://arxiv.org/abs/2611.06449v1)
- PDF: [下载链接](https://arxiv.org/pdf/2611.06449v1)
- 作者: Boyu Niu, Yingjie Xiong, Shurui Li, Linhan Pang, Yuntong Zhang, Han Wang, Hao Wu, Kai Zuo, Xu Tang, Xuanhe Zhou, Fan Wu
- 发布时间: 2026-11-04T12:51:26Z
- 分类: cs.AI
- 相关性评分: 19
- 主题标签: 文档解析、HTML重建、基准评测、视觉丰富文档、多模态大模型

**中文摘要**

> 该论文指出传统文档解析以Markdown为输出表示，虽适合线性文本但难以完整保留细粒度空间结构、表格几何、视觉层级与渲染语义，因而提出以HTML作为异构、版式敏感文档的可编辑、可检查、可复用输出表示，并构建AmbiHTMLBench基准。该基准包含1,115个多样化页面及结构化标注，采用两种评测协议：客观协议对齐真值与预测渲染块，度量表格保真度、页面级文本错误和二维布局一致性；互补的参考锚定协议通过LLM评判对齐人类偏好来衡量感知保真度。实验显示十个主流多模态系统中最佳客观得分0.8092，而主观获胜者与客观最优不一致，表明自动分解与人类感知保真度具有互补性；进一步微调小参数专家模型在文档到HTML重建任务上取得良好表现。

**核心创新概述**

> 将文档解析的输出表示从Markdown转向可执行HTML，并系统性构建配套基准与双协议评测体系，是该设定下的首个系统研究。

**创新点拆解**

- 提出以可执行HTML作为视觉丰富文档解析的输出表示，保留结构、组织与视觉外观
- 构建AmbiHTMLBench基准，含1,115个多样化页面与结构化标注
- 设计客观协议（表格保真度、页面级文本错误、二维布局一致性）与参考锚定的主观协议（LLM评判对齐人类偏好）双轨评测
- 验证小参数专家模型经任务特定微调可在文档到HTML重建上取得良好表现

**当前局限**

> 客观指标与人类感知保真度排序不一致，说明现有自动度量尚不能完全替代主观评价；基准规模为千级页面，覆盖多样性有限；HTML输出本身的合法性与可渲染性校验细节未充分展开。

**后续可改进方向**

- 研究更贴近人类感知的客观保真度指标，缩小与主观评判的差距
- 扩展基准到更多文档类型、语言与复杂表格/公式场景
- 探索HTML输出中渲染语义与可编辑性的联合约束建模
- 分析小模型专家化与通用大模型在结构重建上的能力边界与互补性

**工程启发**

> 为文档解析系统提供可编辑、可检查的HTML输出范式与配套评测工具，可直接用于版面还原、表格重建类产品的选型与回归测试。

**为什么值得关注**

> 该论文直接研究视觉丰富文档解析的输出表示与评测基准，是OCR与文档解析方向的核心参考。

**原始摘要**

Traditional document parsing systems use Markdown as their output representation, which is effective
for linear text but does not fully preserve fine-grained spatial structure, table geometry, visual
hierarchy, or rendering semantics. We show that HTML is advantageous for heterogeneous and layout-
sensitive documents whose representations must remain editable, inspectable, and reusable, and
introduce AmbiHTMLBench to systematically study this setting. In this benchmark, given a real-world
document, a model must recover executable HTML that preserves its content, organization, and visual
appearance. The benchmark contains 1,115 diverse pages with structured annotations and evaluates
predictions in two different ways: The objective protocol aligns ground-truth and predicted rendered
blocks and measures table fidelity, page-level text error, and a two-dimensional layout consistency;
a complementary reference-anchored protocol measures perceived fidelity by aligning LLM judges with
human preferences. Across ten primary multimodal systems, the best objective score is 0.8092, while
the subjective winner is different, demonstrating that automatic decomposition and human-perceived
fidelity capture complementary properties. We further fine-tune a small-parameter expert model and
find that task-specific adaptation yields good performance on document-to-HTML reconstruction task.
These results position AmbiHTMLBench as a diagnostic testbed for building smarter and more logical
document parsing systems.

---

### 2. CardioLM: A multilingual suite of small language models for the cardiology domain

- arXiv: [2611.07940v1](https://arxiv.org/abs/2611.07940v1)
- PDF: [下载链接](https://arxiv.org/pdf/2611.07940v1)
- 作者: Manuela-Daniela Danu, Miguel Rodríguez-Ortega, Alberto Becerra-Tome, Pablo Arancibia, Fernando Gallego-Donoso, Lorenzo Pratesi, Xi Bai, Andrei-Damian Dinescu, Salvador Lima-López, Andrea Guala, Saskia Haitjema, Jonas Mack, Michele Miranda, Wesam Al Nabki, Jan Rodríguez-Miret, Vasile George Marica, Vladimír Kincl, Kateřina Dostálová, Michael Andrej, Alicia Ujil, Corinne Allaart, Machteld Boonstra, Malin Overmars, Anoop Shah, Giovanna Ceroni, Jonathan Kossoff, Domenico D'Amario, Renzo Laborante, Antonio Iaconelli, Isabella Fumarulo, Jacopo Lenkowicz, Livia Lilli, Emma Weiss, Alex Scafa, Felix Lindberg, Milou Gamage, Eulàlia Farré-Maduell, Sébastien Bratières, Martin Krallinger, Bram van Es
- 发布时间: 2026-11-05T12:41:19Z
- 分类: cs.CL, cs.AI
- 相关性评分: 10
- 主题标签: 临床NLP、多语种命名实体识别、领域预训练、心脏病学、医疗文档结构化

**中文摘要**

> 该文针对心血管领域临床自由文本多为本地语言、NLP资源集中于英语且缺乏心脏病学专用多语种基准的问题，提出CardioCCC语料与CardioLM模型套件。CardioCCC含508篇原以西班牙语发表的心脏病病例报告，经机器翻译、标注投影与临床医生审核扩展至捷克语、荷兰语、英语、意大利语、罗马尼亚语和瑞典语，标注覆盖疾病、症状、操作与药物。CardioLM包括在心脏病学与生物医学语料上继续预训练得到的各语言CardioBERTa编码器，以及在CardioCCC上微调的CardioNER命名实体识别模型。结果显示心脏病学特定预训练使伪困惑度最多降低八倍，但严格跨度级F1变化不超过0.04，收益集中于骨干缺乏生物医学覆盖的语言；联合训练的多语种XLM-RoBERTa-large在几乎所有语言与实体类型上取得最佳严格F1，最高超过最强单语系统0.13；残余错误多与边界检测有关，宽松匹配对疾病、操作、症状可恢复0.10–0.23 F1，对药物仅0.01–0.07；临床医生对CardioNER评分显著高于规则与词典基线。

**核心创新概述**

> 构建首个心脏病学专用、多语种且实体覆盖较广的基准与模型套件，并系统评估领域预训练与多语联合训练的实际收益。

**创新点拆解**

- 构建CardioCCC多语种心脏病学病例报告语料，采用机器翻译、标注投影与临床医生审核相结合的标注流程
- 提出CardioBERTa语言特定编码器，在心脏病学与生物医学语料上继续预训练
- 发布CardioNER命名实体识别模型集，覆盖疾病、症状、操作与药物四类实体
- 系统对比单语与联合多语训练，并引入临床医生主观评分验证

**当前局限**

> 领域预训练对严格跨度F1提升有限，收益依赖骨干原有生物医学覆盖；药物实体的边界错误难以通过宽松匹配缓解；语料规模仅508篇且经机器翻译扩展，翻译质量与标注投影误差可能影响结论。

**后续可改进方向**

- 针对实体边界检测设计专门解码或后处理策略，尤其改善药物实体
- 扩大原语种人工标注规模，减少对机器翻译与标注投影的依赖
- 探索跨语言迁移与领域预训练的联合优化，而非简单继续预训练
- 引入结构化临床信息抽取与文档级解析任务以扩展评测维度

**工程启发**

> 为医疗多语种信息抽取提供可直接复用的语料、编码器与NER模型，并给出领域预训练收益的量化参考，便于临床文档结构化落地。

**为什么值得关注**

> 该文涉及临床文档的文本抽取与多语种NER，与OCR后的文档理解与信息结构化环节相关。

**原始摘要**

Background: Cardiovascular care generates large volumes of clinical free-text documentation in local
languages. However, clinical natural language processing (NLP) resources remain concentrated in
English, and no existing benchmark is cardiology-specific, multilingual, and broad in entity
coverage. Methods: We present two contributions. The first is CardioCCC, a corpus of 508 cardiology
case reports originally published in Spanish and extended to Czech, Dutch, English, Italian,
Romanian, and Swedish through machine translation, annotation projection, and clinician review, with
annotations covering diseases, symptoms, procedures, and medications. The second is CardioLM,
comprising CardioBERTa, a set of language-specific encoders obtained by continued pretraining on
cardiology and biomedical corpora, and CardioNER, a set of named entity recognition (NER) models
fine-tuned on CardioCCC. Results: Cardiology-specific pretraining reduced pseudo-perplexity by up to
a factor of eight, yet changed strict span-level F1 by at most 0.04, with benefits concentrated in
languages whose backbones lacked biomedical coverage. The jointly trained multilingual XLM-RoBERTa-
large models achieved the best strict F1 in nearly every language and entity type, exceeding the
strongest monolingual system by up to 0.13 F1. A large share of residual errors concerned boundary
detection: relaxed matching recovered 0.10-0.23 F1 for disease, procedure, and symptom, but only
0.01-0.07 for medication. Clinicians rated CardioNER well above a rule- and dictionary-based
baseline, with the mean rating across entity types rising from 26% to 73%. Conclusions: Specialty-
specific pretraining is not the decisive factor for downstream entity recognition, whereas
multilingual joint training yields the strongest results in nearly all settings and a simpler
deployment path for multi-country clinical information extraction.

---

### 3. ATHAAR: A Medieval Scientific Arabic Manuscript Dataset for Handwritten Text Recognition

- arXiv: [2611.08091v1](https://arxiv.org/abs/2611.08091v1)
- PDF: [下载链接](https://arxiv.org/pdf/2611.08091v1)
- 作者: Ismail El Jamiy, Khadija Msalek, Guillaume Loizelet, Farah Benamara, Nabil Hathout
- 发布时间: 2026-11-05T14:36:16Z
- 分类: cs.CV, cs.CL
- 相关性评分: 7
- 主题标签: 手写文本识别、历史手稿、低资源OCR、视觉语言模型、阿拉伯语

**中文摘要**

> 该文指出中世纪阿拉伯语科学手稿因连写合字、变音符号多变且缺乏训练数据，仍是当前视觉语言模型手写文本识别（HTR）的开放难题。为此作者提出首个面向科学阿拉伯语手稿转写的标注指南，其思路受文本校勘学启发，随后据此人工标注构建ATHAAR数据集。与既有资源不同，ATHAAR在同一文本的不同抄本、书法风格与内容（含文本与数字）上均有变化。作者基于先进视觉语言模型设计实验，研究模型跨字体、跨章节与跨论著的迁移能力，结果凸显现有系统面对古代科学文本特殊性时的局限。

**核心创新概述**

> 首次为科学阿拉伯语手稿转写制定受文本校勘学启发的标注规范，并构建覆盖多抄本、多书法风格与数字内容的ATHAAR数据集。

**创新点拆解**

- 提出面向科学阿拉伯语手稿转写的标注指南，借鉴文本校勘学方法
- 构建ATHAAR数据集，覆盖同一文本的不同抄本、书法风格与内容类型（文本与数字）
- 基于先进视觉语言模型设计跨字体、跨章节、跨论著的迁移实验

**当前局限**

> 数据集规模与语言范围有限（仅阿拉伯语）；转写标注规范虽经设计但一致性度量未充分报告；实验表明现有VLM在该场景下仍有明显不足，尚未给出有效改进方案。

**后续可改进方向**

- 针对连写合字与变音符号设计专门的视觉编码或语言先验约束
- 扩展多语种历史科学手稿数据与跨手稿联合训练范式
- 引入抄本间对齐与校勘信息作为弱监督信号
- 建立标注一致性评估与可复现的转写评测协议

**工程启发**

> 为历史手写文档数字化提供标注规范与评测数据集，可作为古籍OCR/HTR系统在低资源、复杂书写场景下的验证基准。

**为什么值得关注**

> 该文直接研究手写文本识别与历史文档转写，属OCR核心方向。

**原始摘要**

Despite recent progress in handwritten text recognition, medieval Arabic scientific manuscripts
remain an open challenge for current vision-language models (VLMs) due to cursive ligatures,
variable diacritization, and more importantly the lack of training data. This paper aims to address
this gap, by proposing the first annotation guidelines dedicated to the transcription of scientific
Arabic manuscripts inspired by textual criticism, a well-established approach to historical text
editing. We then propose, ATHAAR, a new dataset manually annotated following this guideline. Unlike
previous resources in the field, ATHAAR varies both witnesses of the same text, calligraphic styles,
and content to deal with texts but also numerals. Relying on state-of-the-art VLMs, we finally
design a set of experiments to study models transfer across scripts, chapters, and treatises. Our
findings highlight the limitations of current systems when faced with the specificities of ancient
scientific texts.

---

### 4. ArcRAG: Agentic Compositional Retrieval over Knowledge Graphs

- arXiv: [2611.06481v1](https://arxiv.org/abs/2611.06481v1)
- PDF: [下载链接](https://arxiv.org/pdf/2611.06481v1)
- 作者: Jyotin Goel, Abhinav Arun, Tejas Prakash Agarwal, Bhaskarjit Sarmah, Stefano Pasquali
- 发布时间: 2026-11-04T13:20:51Z
- 分类: cs.CL, cs.AI, cs.IR
- 相关性评分: 3
- 主题标签: GraphRAG、知识图谱检索、智能体、跨构建可移植性、多跳问答

**中文摘要**

> 该文研究图检索增强生成（GraphRAG）的跨构建可移植性问题，即检索流程在不使用构建特定模式、关系名或重新调参时，能否在知识图构建方式改变后仍然有效。作者提出ArcRAG，在推理时归纳查询局部图接口（问题所指实体可达的节点标签、关系描述与属性键），据此规划多跳遍历，并以Cypher执行与修复。作者将MuSiQue、HotpotQA、TriviaQA各构建为模式引导图（类型化节点、封闭关系集、来源溯源）与开放信息抽取图（无类型节点、自由文本关系）两种形态，检索器配置固定。实验与构建无关的Direct-Cypher智能体对比，在不同重试与轮次预算下消融各阶段，并与既有GraphRAG系统报告结果比较。结果表明检索无需与图构建协同设计：查询时接口归纳使构建无关的检索器在构建变化时保持有效，但构建方式仍影响绝对准确率。

**核心创新概述**

> 提出跨图构建的可移植性研究问题，并给出在推理时归纳查询局部接口的构建无关检索智能体ArcRAG。

**创新点拆解**

- 定义GraphRAG的跨构建可移植性评测设定，同一检索配置应用于两种图构建
- 在推理时归纳查询局部图接口（节点标签、关系描述、属性键），不依赖构建特定模式
- 以Cypher进行多跳遍历规划、执行与自动修复
- 构建模式引导图与开放信息抽取图两类图族并做分阶段消融

**当前局限**

> 构建方式仍显著影响绝对准确率，说明检索器对图质量存在隐性依赖；依赖Cypher与图数据库执行，跨图引擎泛化未验证；评测集中于三个问答语料，领域覆盖有限。

**后续可改进方向**

- 研究图构建质量与检索策略的联合优化，而非仅追求构建无关性
- 扩展接口归纳到更多图查询语言与图存储后端
- 将跨构建可移植性评测扩展至多跳推理之外的结构化抽取任务
- 分析重试与轮次预算对修复成功率与成本的影响并给出调度策略

**工程启发**

> 为知识图谱问答与检索系统提供构建无关的检索智能体设计，可降低图模式变更带来的系统重构成本。

**为什么值得关注**

> 该文涉及文档语料上的检索与结构化知识组织，与OCR后文档知识抽取和检索应用间接相关。

**原始摘要**

Graph-based retrieval-augmented generation (GraphRAG) answers questions by retrieving over a
knowledge graph built from a corpus. Yet retrieval strategies are designed around the structure
their own construction pipeline produces, and whether they survive a change of construction is
rarely tested. We study this cross-construction portability: whether one retrieval procedure, with
no construction-specific schema, relation names, or retuning, stays effective when the graph is
built differently. We introduce ArcRAG, which induces a query-local graph interface at inference
time (the node labels, relation descriptors, and property keys reachable from the entities a
question names), plans multi-hop traversals against it, and executes and repairs them as Cypher. We
build each of the MuSiQue, HotpotQA, and TriviaQA corpora as a schema-guided graph (typed nodes, a
closed relation set, source provenance) and as an open-information-extraction graph (untyped nodes,
free-text relations), with the retriever's configuration fixed across them. We compare against a
construction-agnostic Direct-Cypher agent, ablate each stage across retry and pass budgets on both
graph families, and compare with results reported for prior GraphRAG systems, most of which design
retrieval together with their own graph construction. Across the two constructions, we find that
retrieval need not be co-designed with the graph: query-time interface induction keeps a
construction-agnostic retriever effective when the construction changes, although construction still
shapes absolute accuracy.

---
