# OCR / 文档解析研究日报（2026-06-10）

## 报告说明

- 检索源：arXiv API
- 检索查询：`(all:"document parsing" OR all:"document understanding" OR all:"optical character recognition" OR all:OCR OR all:"layout analysis" OR all:"document layout analysis" OR all:"text recognition" OR all:"table recognition" OR all:"form understanding" OR all:"document intelligence" OR all:"page understanding" OR all:"scene text recognition" OR all:"handwritten text recognition" OR all:"information extraction") AND (cat:cs.CV OR cat:cs.AI OR cat:cs.CL OR cat:eess.IV)`
- 生成时间（UTC）：`2026-06-10 05:48:00`
- 大模型综合分析：`开启`

## 一、今日执行摘要

> 今日OCR/文档解析研究进展聚焦于多语言、历史文档和表格的结构化理解，以及隐私保护与图表数据校正。亮点包括轻量级表格提取模型POTATR凭借极高性价比超越MLLM，MUDIDI框架利用LLM实现多语言词典数字化，以及VisShield通过VLM进行敏感文本定位与去标识化。同时，形态学方法实现了历史手稿的自动计量，ChartLens则通过双分支框架增强了图表数据校正与摘要生成的事实性。技术趋势显示，基于Transformer和原型学习的细粒度文档分析、LLM在结构化抽取中的优势、以及融合OCR与视觉语言模型的隐私保护成为研究热点。

## 二、今日趋势判断

1. 从行级标注到字符原型的弱监督学习成为历史手稿分析主流。2. LLM与轻量CNN/Transformers在文档结构化任务中表现互补，LLM擅长复杂结构理解，轻量模型在效率上优势明显。3. 视觉语言模型（VLM）正从通用理解向特定任务（隐私保护、图表校正）微调发展。4. 性能评估日益强调人类对齐与事实性，如DRG指标和OCR辅助证据归因。

## 三、今日论文概览

1. **Leveraging Morphology for Historical Script Metrological Analysis** | 标签：手写文本识别、古文字学、字符原型学习、Transformer
2. **MUDIDI: A Two-Stage Framework for Multilingual Dictionary Digitization with Language Models** | 标签：词典数字化、LLM、多语言OCR、文档结构化
3. **POTATR: A Lightweight Image-to-Graph Model for Page-Level Table Extraction** | 标签：表格提取、轻量模型、页面级理解、文档处理
4. **Vision Language Model Helps Private Information De-Identification in Vision Data** | 标签：隐私保护、VLM、OCR、医疗影像
5. **KCSAT-ML: Probing Reasoning Models with Nationwide-Cohort Human Difficulty** | 标签：数学推理、基准测试、人类对齐、测试时扩展
6. **ChartLens: A Dual-Branch Framework for Chart Data Correction and Factual Summary Refinement** | 标签：图表理解、数据校正、摘要生成、OCR

## 四、今天 OCR / 文档解析论文里的主要创新点

- 弱监督从行级转录学习字符原型，降低对字符级标注的依赖。
- 利用LLM实现跨语言字典的结构化分割与映射，释放多语言数据集。
- 轻量图模型（如POTATR）以29M参数在表格提取上超越庞大MLLM，成本降低300倍。
- VLM通过指令微调实现敏感文本的精确定位与去标识化，端到端处理。
- 双分支框架分别处理图表数据校正与摘要生成，结合OCR增强事实性。

## 五、后续 OCR 领域值得推进的改进方向

- 探索无监督/半监督的原型学习，减少对行级标注的依赖，应用于更多历史风格手稿。
- 将MUDIDI框架扩展到多列混合布局及手写词典，结合视觉-语言模型协同。
- 为POTATR集成端到端OCR，实现扫描文档表格的完全自动化提取，并研究跨页合并策略。
- 将VisShield扩展到多语言敏感文本检测，并测试对抗攻击下的鲁棒性。
- 利用DRG指标指导模型自适应分配测试时计算资源，优化推理效率。
- 为ChartLens引入端到端联合训练及图表类型检测，处理3D、嵌套等复杂图表。
- 研究跨语言词典实体对齐，降低LLM推理成本，推动低资源语言数字化。
- 结合形态学与深度学习，建模个体书写差异，提升历史文档字符级分析精度。

## 六、工程落地启发

- POTATR可直接集成到企业级文档流水线，提供高性价比的表格提取。
- MUDIDI与LLM的组合适用于低资源语言词典的批量数字化。
- VisShield可嵌入医疗影像系统，自动化PHI去标识化。
- ChartLens适用于数据报告自动生成与验证，提升摘要事实性。
- 形态学方法可辅助古文字学家的量化分析，降低人工成本。

## 七、优先关注论文

- **Leveraging Morphology for Historical Script Metrological Analysis**：弱监督字符原型学习对历史文档分析具有泛化潜力，未来可能推动更多手写风格的自动化计量。
- **MUDIDI: A Two-Stage Framework for Multilingual Dictionary Digitization with Language Models**：多语言词典数字化框架结合LLM，有望成为低资源语言数字化的标准方案，释放大量历史词典数据。
- **POTATR: A Lightweight Image-to-Graph Model for Page-Level Table Extraction**：轻量级高精度表格提取模型，具有极高工程价值，其扩展至扫描文档和跨页合并的能力值得跟踪。
- **Vision Language Model Helps Private Information De-Identification in Vision Data**：VLM在隐私保护中的新应用，医学影像领域需求强烈，其多语言扩展和鲁棒性研究将有重要影响。
- **ChartLens: A Dual-Branch Framework for Chart Data Correction and Factual Summary Refinement**：图表理解中的数据校正与事实性增强是该领域痛点，其OCR辅助证据归因方法有参考价值。

## 八、论文逐篇解析

### 1. Leveraging Morphology for Historical Script Metrological Analysis

- arXiv: [2606.09446v1](https://arxiv.org/abs/2606.09446v1)
- PDF: [下载链接](https://arxiv.org/pdf/2606.09446v1)
- 作者: Malamatenia Vlachou Efstathiou, Raphaël Baena, Dominique Stutzmann, Mathieu Aubry
- 发布时间: 2026-06-08T12:55:02Z
- 分类: cs.CV
- 相关性评分: 17
- 主题标签: 手写文本识别、古文字学、字符原型学习、Transformer

**中文摘要**

> 本文提出一种基于形态学的历史手写文本计量分析方法，利用基于Transformer的检测架构和原型重建模块，仅需行级转录标注即可学习字符原型，并实现字符边界框预测，为古文字学提供可扩展、有意义的度量。方法在14世纪手稿上验证，能区分不同抄写员的图形特征并发现细微变化。

**核心创新概述**

> 将形态学分析与深度学习结合，提出从行级标注学习字符原型的方法，实现无需字符级标注的自动古文字测量。

**创新点拆解**

- 提出基于Transformer的检测架构+原型行重建模块，从行级转录监督学习字符原型及其位置与变形。
- 引入字符、双字母、间距等自动计量指标，并验证其古文字学意义。
- 扩展了14世纪手稿的标注至160页，用于验证方法有效性。

**当前局限**

> 当前方法依赖行级标注，可能对高度粘连或变形严重的字符建模困难；原型数量需预设，可能不适用于未知字符集。

**后续可改进方向**

- 探索无监督或半监督的原型学习方法，减少对标注的依赖。
- 将方法推广到更多历史时期和手写风格的文档。
- 融合字形风格特征，提升对个体书写差异的建模能力。

**工程启发**

> 为历史手稿的数字化分析提供了一种自动化、定量化的工具，可辅助古文字学家进行大规模风格辨识和演变研究。

**为什么值得关注**

> 涉及行级文本检测与字符建模，与OCR领域的端到端文档理解密切相关。

**原始摘要**

Advances in handwritten text recognition have enabled large-scale transcription of historical
documents, but still provide limited access to interpretable visual measurements for paleography,
the study of historical scripts. In this paper, our main insight is that morphological script
analysis, in particular the capacity to learn character prototypes from line-level transcriptions,
enables the definition of scalable, meaningful, and stable paleographic measurements. More
precisely, we leverage a transformer-based detection architecture together with a prototype-based
line reconstruction module to learn prototypical characters and their occurrence, deformation, and
positioning. Our contributions are twofold. First, we introduce a deep architecture and learning
methodology that enables efficient character modeling with only line-level transcription
supervision, significantly improving over the Learnable Typewriter baseline and enabling accurate
character bounding box prediction, unlocking its potential for paleographic measurements. Second, we
introduce and demonstrate the paleographical relevance of automatic measurements enabled by our
architecture for characters, bi-grams, and spaces between graphical units. For this demonstration,
we extend the annotations of the codex Paris, BnF, fr. 2813, commissioned in the late fourteenth
century by Charles V and copied by four hands, to 160 pages. We visualize our measurements over
these pages, showing how they enable us not only to differentiate graphical profiles, but also to
discover and analyze subtle variations. This case study outlines the scalability of our approach and
its frugality in terms of required training data, since a single column of text is sufficient to
compute our measurements on each of the 160 pages. Data and code are publicly available at:
https://malamatenia.github.io/morphology4metrology-analysis.

---

### 2. MUDIDI: A Two-Stage Framework for Multilingual Dictionary Digitization with Language Models

- arXiv: [2606.09435v1](https://arxiv.org/abs/2606.09435v1)
- PDF: [下载链接](https://arxiv.org/pdf/2606.09435v1)
- 作者: David Setiawan, Temuulen Khishigsuren, Milind Agarwal, Pagnarith Pit, Aso Mahmudi, Ekaterina Vylomova
- 发布时间: 2026-06-08T12:44:47Z
- 分类: cs.CL
- 相关性评分: 17
- 主题标签: 词典数字化、LLM、多语言OCR、文档结构化

**中文摘要**

> MUDIDI是一个两阶段多语言词典数字化框架：第一阶段评估字符识别与标记保留质量，第二阶段进行词典条目分割并映射到机器可读格式。释放了包含30种公开领域词典的人工标注数据集，基准测试显示LLM在多数语言中表现优于OCR和VLM。

**核心创新概述**

> 针对多语言词典数字化，提出了两阶段评估与转换框架，并构建了涵盖多语种、多格式的标注数据集。

**创新点拆解**

- 提出两阶段框架，分别关注字符识别质量与词典结构理解。
- 构建了含30种不同语言和格式的词典数据集。
- 验证了LLM在词典结构化任务中的优势，并提出添加词典前言可改善结果。

**当前局限**

> 主要针对公共领域单页词典扫描，对复杂布局或手写词典的适用性未充分测试；LLM推理成本可能较高。

**后续可改进方向**

- 扩展到更复杂的页面布局（如多列混合），研究视觉-语言模型的协同。
- 探索更高效的小模型或知识蒸馏方法，降低推理成本。
- 研究跨语言词典的实体对齐与脱机技术。

**工程启发**

> 为低资源语言和濒危语言的词典数字化提供了实用工具，可直接集成到现有文献保存工作流中。

**为什么值得关注**

> 涉及OCR后处理与结构理解，是文档解析的重要应用场景。

**原始摘要**

Multilingual dictionaries are among the most valuable documentary resources for low-resource and
endangered languages, yet many remain available only as scans. For many decades, their digitization
and conversion into a machine-readable format was nearly impossible due to language-specific
scripts, complex multi-column layouts full of entries with abbreviations and cross-references.
Recent vision-language models offer a promising solution, but it is unclear how well they preserve
characters, markup, and process lexicographic structure. We introduce MUDIDI, a two-stage framework
for multi-lingual dictionary digitization. Stage One evaluates the quality of character recognition
and markup preservation; Stage Two focuses on dictionary entry segmentation with subsequent mapping
into a machine-readable lexicographic schema, SIL's Multi-Dictionary Formatter. We also release a
dataset that consists of human-annotated lexicographic entries collected from 30 public-domain
dictionaries featuring diverse writing systems, language families, and formats. We benchmark OCR
systems, general-purpose Large Language Models (LLMs), and Vision Language Models (VLMs) on the
dataset, demonstrating superior performance of LLMs across most writing systems and languages in
both stages, and provide practical guidelines on improving the results for more challenging
scenarios. Finally, we show that supplementing additional information, such as dictionary
introduction, to the LLMs can improve the quality of the digitized dictionary. Github:
https://github.com/DavidSamuell/MUDIDI-Pipeline-for-Digitization-of-Multilingual-Dictionary/

---

### 3. POTATR: A Lightweight Image-to-Graph Model for Page-Level Table Extraction

- arXiv: [2606.09788v1](https://arxiv.org/abs/2606.09788v1)
- PDF: [下载链接](https://arxiv.org/pdf/2606.09788v1)
- 作者: Brandon Smock, Libin Liang, Max Sokolov, Amrit Ramesh, Valerie Faucon-Morin, Tayyibah Khanam, Maury Courtland
- 发布时间: 2026-06-08T17:43:44Z
- 分类: cs.CV
- 相关性评分: 16
- 主题标签: 表格提取、轻量模型、页面级理解、文档处理

**中文摘要**

> POTATR是一个轻量级（29M参数）图像到图模型，用于页面级表格提取。在PubTables-v2单页基准上达到0.964 GriTS_Con，比前沿MLLM快130倍、成本低300倍。输出带边界框的空间定位，支持视觉验证和几何文本分配，可扩展至扫描文档和跨页合并。

**核心创新概述**

> 提出轻量级页面级表格提取模型，在保持高精度的同时大幅提升推理效率和降低成本。

**创新点拆解**

- 扩展Table Transformer架构，实现页面级上下文表格提取。
- 29M参数即可超越庞大MLLM，同时速度和成本优势显著。
- 输出空间定位信息，支持视觉验证和与其他模型组合。

**当前局限**

> 依赖于外部OCR处理扫描文档，对非规范表格（如手写表格）的鲁棒性未知。

**后续可改进方向**

- 集成端到端OCR模块，实现完全自动化的扫描文档表格提取。
- 研究跨页表格的合并策略，提升文档级表格重建完整性。
- 探索更复杂的表格结构（如合并单元格、不完整表格）的建模。

**工程启发**

> 高性能低成本，适合大规模文档处理，可直接用于企业级文档数字化流水线。

**为什么值得关注**

> 直接针对文档中的表格提取，是OCR后结构理解的核心任务。

**原始摘要**

Large-scale document processing requires contextually aware table extraction (TE) that is both
accurate and efficient. Yet current approaches require billions of parameters, hundreds of
autoregressive steps, or costly API inference. Motivated by this, we introduce the Page-Object Table
Transformer (POTATR), a lightweight 29M parameter image-to-graph model that extends the Table
Transformer (TATR) for contextualized page-level TE. POTATR outperforms all models tested on the
PubTables-v2 Single Pages benchmark -- including frontier MLLMs -- achieving
$\textrm{GriTS}_\textrm{Con}$ of 0.964 while running over 130$\times$ faster at roughly 300$\times$
lower cost. Further, POTATR's output is spatially grounded: every recognized element has a bounding
box, enabling visual verification and geometric text assignment. As a result, POTATR performs
unified page-level TE while composing with other models, enabling extension to scanned documents via
external OCR and to full-document TE via techniques like cross-page merging. Code and models will be
released.

---

### 4. Vision Language Model Helps Private Information De-Identification in Vision Data

- arXiv: [2606.09132v1](https://arxiv.org/abs/2606.09132v1)
- PDF: [下载链接](https://arxiv.org/pdf/2606.09132v1)
- 作者: Tiejin Chen, Pingzhi Li, Kaixiong Zhou, Tianlong Chen, Hua Wei
- 发布时间: 2026-06-08T07:30:20Z
- 分类: cs.AI
- 相关性评分: 16
- 主题标签: 隐私保护、VLM、OCR、医疗影像

**中文摘要**

> VisShield是一个端到端框架，旨在增强视觉语言模型的隐私保护能力。通过专用指令微调数据集OPTIC和定制训练策略，使VLM能够精确定位并处理图像中的敏感文本（如医疗影像中的受保护健康信息），输出边界框以便后续遮盖。实验表明其在隐私保护任务上显著优于现有方法。

**核心创新概述**

> 将VLM用于视觉隐私保护，提出隐私导向的OCR任务微调方法，同时实现敏感文本定位与处理。

**创新点拆解**

- 构建了隐私文本指令微调数据集OPTIC，涵盖多种敏感文本类型。
- 提出训练策略使VLM能够输出敏感文本的精准边界框。
- 端到端框架无需额外模块，直接利用VLM进行隐私保护。

**当前局限**

> 依赖预训练VLM的OCR能力，对罕见字体或模糊图像可能定位不准；未考虑多语言场景。

**后续可改进方向**

- 扩展到多语言敏感文本检测，适应全球医疗场景。
- 研究对抗性攻击下的鲁棒性，确保隐私保护不被绕过。
- 探索更精细的文本内容理解，区分需保留和需遮盖的信息。

**工程启发**

> 为医疗影像等隐私敏感场景提供自动化去标识化方案，具有直接应用价值。

**为什么值得关注**

> 涉及OCR在视觉隐私保护中的角色，是文档安全处理的重要方向。

**原始摘要**

Visual Language Models (VLMs) have gained significant popularity due to their remarkable ability.
While various methods exist to enhance privacy in text-based applications, privacy risks associated
with visual inputs remain largely overlooked such as Protected Health Information (PHI) in medical
images. To tackle this problem, two key tasks: accurately localizing sensitive text and processing
it to ensure privacy protection should be performed. To address this issue, we introduce VisShield
(Vision Privacy Shield), an end-to-end framework designed to enhance the privacy awareness of VLMs.
Our framework consists of two key components: a specialized instruction-tuning dataset OPTIC
(Optical Privacy Text Instruction Collection) and a tailored training methodology. The dataset
provides diverse privacy-oriented prompts that guide VLMs to perform targeted Optical Character
Recognition (OCR) for precise localization of sensitive text, while the training strategy ensures
effective adaptation of VLMs to privacy-preserving tasks. Specifically, our approach ensures that
VLMs recognize privacy-sensitive text and output precise bounding boxes for detected entities,
allowing for effective masking of sensitive information. Extensive experiments demonstrate that our
framework significantly outperforms existing approaches in handling private information, paving the
way for privacy-preserving applications in vision-language models. Our dataset and code can be found
here.

---

### 5. KCSAT-ML: Probing Reasoning Models with Nationwide-Cohort Human Difficulty

- arXiv: [2606.10403v1](https://arxiv.org/abs/2606.10403v1)
- PDF: [下载链接](https://arxiv.org/pdf/2606.10403v1)
- 作者: Sanghee Park, Geewook Kim, Kee-Eung Kim
- 发布时间: 2026-06-09T04:25:44Z
- 分类: cs.CL
- 相关性评分: 9
- 主题标签: 数学推理、基准测试、人类对齐、测试时扩展

**中文摘要**

> KCSAT-ML是基于韩国高考数学试题的推理基准，包含664道题，其中339道题具有官方每题错误率。提出难度对齐推理增益（DRG）指标用于评估模型错误与人类难易的对齐程度。实验发现：低预算模型在高错误率题目上崩溃；测试时计算扩展在难题上表现为反缩放，易题上过度思考；相同准确率的模型DRG可能截然相反。

**核心创新概述**

> 构建了带有全国规模人类错误率标注的数学推理基准，并提出了揭示模型与人类难度对齐的新指标DRG。

**创新点拆解**

- 利用十年韩国高考数学题，首次提供基于数十万考生的大规模每题错误率。
- 提出DRG指标，从难度对齐角度评估模型，揭示准确率无法反映的差异。
- 发现测试时计算扩展在难题和易题上的非单调性及反缩放现象。

**当前局限**

> 仅覆盖数学推理，且为韩国高考风格，结论对其他学科或文化背景的泛化性需验证。

**后续可改进方向**

- 将基准扩展到更多学科和语言，验证人类难度对齐的普遍性。
- 研究模型内部表征与人类认知难度的关系，指导训练策略改进。
- 探索利用DRG指导模型自适应分配计算资源。

**工程启发**

> 提供了评估模型人类对齐度的方法，可用于改进教育场景中的辅助工具。

**为什么值得关注**

> 涉及OCR在数学文档理解中的应用，以及模型评估与文档内容难度分析。

**原始摘要**

Math reasoning benchmarks have proliferated, yet most lack a per-item difficulty signal grounded in
actual human performance. We introduce KCSAT-ML, a decade (2014-2025) of Korean College Scholastic
Ability Test (KCSAT; Suneung) mathematics: 664 problems with a 339-item core set carrying official
per-item error rates from nationwide cohorts of hundreds of thousands of examinees. We pair the
benchmark with Difficulty-aligned Reasoning Gain (DRG): a score-orthogonal metric that asks whether
a model's mistakes concentrate on the items humans found hard, or on items humans found easy.
Together they expose, across a wide range of VLMs (and LLMs via OCR), three patterns: (i) low-budget
accuracy collapses on the high-human-error tail at every model size; (ii) test-time scaling (TTS)
raises token use roughly linearly with cohort error rate, while accuracy gains follow a non-
monotonic curve; (iii) within a single family, TTS flips between anti-scaling on the hardest items
and overthinking on easier ones -- two faces of the same alignment failure. On DRG, models with
near-identical accuracy can sit at near-opposite values: one model gets wrong what humans also find
hard, while another solves the hardest items yet fails on items humans find easy -- a contrast that
aggregate accuracy hides. Our code and dataset builder will be open-sourced at
https://github.com/naver-ai/KCSAT-ML.

---

### 6. ChartLens: A Dual-Branch Framework for Chart Data Correction and Factual Summary Refinement

- arXiv: [2606.10640v1](https://arxiv.org/abs/2606.10640v1)
- PDF: [下载链接](https://arxiv.org/pdf/2606.10640v1)
- 作者: Hao Liu, Ruping Cao, Kun Wang, Zhiran Li, Fan Liu, Yupeng Hu, Liqiang Nie
- 发布时间: 2026-06-09T09:45:01Z
- 分类: cs.CV
- 相关性评分: 8
- 主题标签: 图表理解、数据校正、摘要生成、OCR

**中文摘要**

> ChartLens是一个双分支框架，用于图表数据校正和事实性摘要精炼。包含结构感知CSV验证校正模块（SAVC）和文本保留引导摘要精炼模块（TRSR）。通过模型适配、校正生成和OCR辅助证据归因，在DataMFM挑战赛Track 2中获得第一名，总体得分69.10。

**核心创新概述**

> 提出双分支框架分别处理图表数据提取校正和摘要生成，结合OCR辅助的事实性增强。

**创新点拆解**

- 结构感知CSV验证与校正模块，提升结构化数据提取可靠性。
- 文本保留引导摘要精炼模块，强化关键数值和文本证据的保留。
- 将OCR结果作为证据归因，提升摘要事实性。

**当前局限**

> 依赖OCR对图表中文字识别的准确性；对复杂图表（如3D、嵌套）的适用性未充分验证。

**后续可改进方向**

- 端到端联合训练数据提取与摘要生成，减少模块依赖。
- 引入图表类型检测与自适应策略，处理更多样化的图表风格。
- 探索图表中数值与文本的空间关系建模，提升结构化恢复精度。

**工程启发**

> 为图表理解提供可靠的方法，可直接应用于数据报告自动生成与验证系统。

**为什么值得关注**

> 涉及图表OCR与结构理解，是文档智能中信息提取与总结的典型任务。

**原始摘要**

In this report, we present our champion solution for the DataMFM Challenge Track 2: Chart
Understanding. This track requires models to recover structured chart data and generate faithful
natural-language summaries from chart images. To address the complementary requirements of accurate
data extraction and factual narration, we propose ChartLens, a dual-branch framework for chart data
correction and summary refinement. ChartLens consists of two key modules: Structure-Aware CSV
Verification and Correction (SAVC) and Text-Retention-Guided Summary Refinement (TRSR). SAVC
improves the reliability of structured data extraction through verification and correction, while
TRSR enhances summary generation by preserving critical textual and numerical evidence from charts.
By combining model adaptation, correction-based generation, and OCR-assisted evidence grounding,
ChartLens improves both structured data recovery and summary factuality. On the test set, our final
system achieves an overall score of 69.10 and ranks first in Track 2, demonstrating its
effectiveness for accurate chart understanding. Our code will be released at:
https://github.com/iLearn-Lab/CVPRW26-ChartLens.

---
