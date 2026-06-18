# OCR / 文档解析研究日报（2026-06-18）

## 报告说明

- 检索源：arXiv API
- 检索查询：`(all:"document parsing" OR all:"document understanding" OR all:"optical character recognition" OR all:OCR OR all:"layout analysis" OR all:"document layout analysis" OR all:"text recognition" OR all:"table recognition" OR all:"form understanding" OR all:"document intelligence" OR all:"page understanding" OR all:"scene text recognition" OR all:"handwritten text recognition" OR all:"information extraction") AND (cat:cs.CV OR cat:cs.AI OR cat:cs.CL OR cat:eess.IV)`
- 生成时间（UTC）：`2026-06-18 06:09:21`
- 大模型综合分析：`开启`

## 一、今日执行摘要

> 今日研究覆盖从预训练数据、低资源语言OCR到半监督标注、法律文本处理等多个方向，产出了多个高质量数据集和实用创新方法。斯坦福EDGAR数据集提供了金融领域长上下文预训练的新资源；阿拉伯语和乌尔都语手写识别工作填补了低资源语言基准空白；BBLP半监督框架显著降低了版面分析重标注成本；产品图像身份保持和文本到图像RL训练等工作则展示了多模态领域的最新进展。整体上，数据驱动与半监督/弱监督策略成为主流，低资源语言和多模态融合是关注焦点。

## 二、今日趋势判断

数据构建向高质量、低污染、长上下文方向发展；低资源语言（如乌尔都语、阿拉伯语、欧洲葡萄牙语）的手写和印刷OCR基准持续涌现；半监督学习与标签传播技术被应用于减少人工标注成本；强化学习与扩散模型的结合在多模态生成任务中表现出潜力；法律、金融等专业领域文档处理需求推动专用数据集和模型开发。

## 三、今日论文概览

1. **The Stanford EDGAR Filings Dataset: Reconstructing U.S. Corporate and Financial Disclosures into Layout-Faithful and Token-Efficient Pretraining Data** | 标签：长上下文预训练、文档重建、金融NLP、数据集构建、基准测试
2. **Urdu Katib Handwritten Dataset: A Historical Document Dataset for Offline Urdu Handwritten Text Recognition with CRNN-Based Baseline Evaluation** | 标签：手写识别、乌尔都语、数据集、CRNN、历史文档
3. **Analyzing and Encoding the Al-Mawrid Arabic-English Dictionary with the ISO Language Markup Framework and TEI Lex-0** | 标签：数字化、词典编码、阿拉伯语处理、ISO标准、TEI、信息提取
4. **Freeing the Law with LOCUS: A Local Ordinance Corpus for the United States** | 标签：法律AI、语料库构建、OCR、法规分析、ModernBERT
5. **Bounding Box Label Propagation for Re-Annotation of Document Layout Analysis Datasets** | 标签：半监督学习、标签传播、文档布局分析、目标检测、重标注
6. **Performance Gap Analysis between Latin and Arabic Scripts HTR** | 标签：手写识别、阿拉伯语、拉丁语、性能差距、CRNN、脚本差异
7. **IUU+DB: Tracking Illegal, Unreported, and Unregulated Fishing, Seafood Fraud, and Labor Abuse through LLM-driven Information Extraction** | 标签：信息抽取、大语言模型、渔业应用
8. **ProductConsistency: Improving Product Identity Preservation in Instruction-Based Image Editing via SFT and RL** | 标签：图像编辑、产品身份保持、强化学习
9. **PorTEXTO: A European Portuguese Benchmark for Visual Text Extraction** | 标签：OCR、低资源语言、基准数据集
10. **Spotlight: Synergizing Seed Exploration and Spot GPUs for DiT RL Post-Training** | 标签：强化学习、扩散模型、高效训练
11. **STAR: SpatioTemporal Adaptive Reward Allocation for Text-to-Image RL Post-Training** | 标签：图像生成、强化学习、文本渲染
12. **SAMA: Semantic Anchor-aligned Augmentation for Unified Low-Resource Multimodal Information Extraction** | 标签：数据增强、多模态信息抽取、大语言模型

## 四、今天 OCR / 文档解析论文里的主要创新点

- 多篇论文通过构建高质量专用数据集（如SEFD、UKHD、PorTEXTO）填补长期空白
- 半监督和标签传播方法（如BBLP）被用于降低人工标注成本
- 利用LLM或多模态模型自动或辅助生成标注数据（如SAMA、PorTEXTO的标注流程）
- 跨脚本/跨语言的性能对比分析（如拉丁vs阿拉伯）揭示数据质量和视觉变异性是关键瓶颈

## 五、后续 OCR 领域值得推进的改进方向

- 探索将SEFD的数据构建方法扩展到其他语种（如中文、欧洲语言）的财务披露文件
- 结合字符频率分布和视觉变异性分析，设计针对阿拉伯语等重尾脚本的数据增强和模型结构改进
- 利用BBLP框架在多目标检测数据集上验证，并融入主动学习策略以最大化标注效率
- 扩展PorTEXTO基准到更多欧洲低资源语言，并研究跨语言迁移的OCR方法
- 将产品身份保持方法应用于视频商品编辑，跟踪目标在时序上的连续一致性
- 研究无注意力图依赖的空间奖励分配方法，提升文本到图像生成中复杂文本渲染的鲁棒性
- 构建多语言、多地区的地方法规语料库，并改进OCR后处理以获得更干净的文本
- 开发融合知识图谱的词典编码方案，超越TEI Lex-0对阿拉伯语语义关系的支持局限
- 结合卫星图像等多模态数据，增强IUU+系统对非文本事件来源的监测能力
- 将STAR中的时空自适应奖励分配方法扩展到视频生成和更复杂的多条件控制

## 六、工程落地启发

- SEFD数据集可立即用于金融NLP的长上下文预训练，减少数据清洗和构建成本
- UKHD和性能差距分析为乌尔都语/阿拉伯语HTR系统提供性能基准和优化方向
- BBLP框架可集成到文档版面分析的数据标注管线中，显著降低重标注成本
- PorTEXTO为欧洲葡萄牙语OCR提供标准评估，有助于在该语言上开展技术验证和改进
- LOCUS法律语料库可用于法律AI模型的微调和评估，支持公共政策分析
- SAMA数据增强方法可直接提升多模态信息抽取在低资源场景下的性能

## 七、优先关注论文

- **The Stanford EDGAR Filings Dataset: Reconstructing U.S. Corporate and Financial Disclosures into Layout-Faithful and Token-Efficient Pretraining Data**：高质量长上下文金融预训练数据集，可能推动金融领域LLM的进步，值得跟踪其扩展版本和下游任务评估结果。
- **Urdu Katib Handwritten Dataset: A Historical Document Dataset for Offline Urdu Handwritten Text Recognition with CRNN-Based Baseline Evaluation**：首个乌尔都语历史手写数据集，为低资源手写识别树立基准，未来整合语言模型后的性能提升值得关注。
- **Bounding Box Label Propagation for Re-Annotation of Document Layout Analysis Datasets**：高效的半监督重标注框架，若在更多数据集上验证并开源，将可能改变版面分析数据维护的工程实践。
- **Performance Gap Analysis between Latin and Arabic Scripts HTR**：系统性地揭示了拉丁与阿拉伯手写识别的性能差距成因，为后续阿拉伯语HTR优化提供路线图。
- **PorTEXTO: A European Portuguese Benchmark for Visual Text Extraction**：首个现代欧洲葡萄牙语OCR基准，可能带动低资源语言OCR评估标准化和模型改进。

## 八、论文逐篇解析

### 1. The Stanford EDGAR Filings Dataset: Reconstructing U.S. Corporate and Financial Disclosures into Layout-Faithful and Token-Efficient Pretraining Data

- arXiv: [2606.18192v2](https://arxiv.org/abs/2606.18192v2)
- PDF: [下载链接](https://arxiv.org/pdf/2606.18192v2)
- 作者: Nick Bettencourt, Xiaowei Ding, Kay Giesecke
- 发布时间: 2026-06-16T17:22:34Z
- 分类: cs.AI
- 相关性评分: 17
- 主题标签: 长上下文预训练、文档重建、金融NLP、数据集构建、基准测试

**中文摘要**

> 针对大语言模型中长上下文训练数据稀缺且昂贵的问题，提出斯坦福EDGAR文件数据集（SEFD），通过对SEC文件进行版面忠实的多标记重建，生成用于金融语言模型的长上下文预训练数据。该数据集与Common Crawl重叠不到0.1%，并提供两个衍生基准测试，用于文件基础数值预测和复杂财务表格转录。

**核心创新概述**

> 首次将SEC财务披露文件系统重建为布局保真、可token高效使用的长上下文预训练语料，且提供高覆盖率、低污染的公开数据集。

**创新点拆解**

- 基于SEC文件的多标记（MultiMarkdown）重建，保留原始布局并提高token效率
- 构建152B token初始快照和预估550B token的大规模档案，与Common Crawl语料重叠极低
- 定义文件接地数值预测和复杂财务表格转录两个新基准测试
- 将审计财务报告等专业文档用作LLM长上下文训练数据

**当前局限**

> 数据集目前仅覆盖美国SEC文件，可能不适用于其他国家的金融文档；版面重建可能丢失部分原始格式细节。

**后续可改进方向**

- 扩展至其他国家或地区的财务披露文件
- 探索更高效的版面保持与token压缩方法
- 进一步验证长上下文预训练在下游金融任务中的效果提升

**工程启发**

> 直接提供高质量、模型就绪的长上下文预训练数据，减少数据清洗和构建成本；支持金融领域LLM训练和评估。

**为什么值得关注**

> 涉及文档重建、长上下文预训练数据处理，与OCR/文档分析领域的数据构建与评估紧密相关。

**原始摘要**

As high-quality public web corpora become increasingly exhausted, clean long-context documents have
become a scarce and expensive source of training data for large language models (LLMs). Existing
long-context corpora are often proprietary and costly to acquire, synthetically generated, or
concentrated in narrow domains such as programming. We introduce the Stanford EDGAR Filings Dataset
(SEFD), an open reconstruction of SEC filings into layout-faithful MultiMarkdown for financial
language modeling and evaluation. SEFD makes audited financial statements, risk disclosures,
ownership reports, accounting notes, and market-moving event filings usable as long-context
pretraining data and as a basis for financial reasoning, forecasting, compliance, and document
understanding. The resulting corpus is token-efficient, model-ready, and has less than 0.1% overlap
with Common Crawl-derived corpora. We release SEFD-v1, a 152B-token initial public snapshot, and
provide corpus-level analyses of a larger 18.5M-filing archive estimated at 550B tokens. We further
introduce two SEFD-derived benchmarks: EDGAR-Forecast, which evaluates filing-grounded numerical
forecasting after model knowledge cutoffs, and EDGAR-OCR, which evaluates transcription of complex
financial tables.

---

### 2. Urdu Katib Handwritten Dataset: A Historical Document Dataset for Offline Urdu Handwritten Text Recognition with CRNN-Based Baseline Evaluation

- arXiv: [2606.19139v1](https://arxiv.org/abs/2606.19139v1)
- PDF: [下载链接](https://arxiv.org/pdf/2606.19139v1)
- 作者: Ramza Basharat, Muhammad Usman Ali
- 发布时间: 2026-06-17T14:46:29Z
- 分类: cs.CV, cs.CL
- 相关性评分: 14
- 主题标签: 手写识别、乌尔都语、数据集、CRNN、历史文档

**中文摘要**

> 针对乌尔都语手写文本识别研究中基准数据集稀缺的问题，提出乌尔都语Katib手写数据集（UKHD），该数据集包含历史上使用平板笔书写的Nastalique字体变体。基于CRNN的混合模型评估显示，CNN-BGRU-CTC模型在字符错误率和词错误率上表现最佳。

**核心创新概述**

> 首次专门从历史文献中收集乌尔都语离线手写文本行数据集，聚焦于Nastalique书法风格中的平板笔书写变体。

**创新点拆解**

- 构建了第一个面向历史乌尔都语手写的离线文本行数据集（UKHD），包含丰富的书写变化
- 对多种CRNN变体进行系统比较，确定CNN-BGRU-CTC架构的最优性能
- 数据集直接从历史Katib书写材料中提取，具有真实性和独特性

**当前局限**

> 数据集规模可能有限，且仅覆盖特定历史时期和书法风格；基线模型尚未达到高精度。

**后续可改进方向**

- 扩大UKHD数据集的规模和多样性，纳入更多历史时期和书写风格
- 探索结合语言模型或注意力机制的端到端识别方法
- 研究迁移学习或数据增强以缓解数据稀疏问题

**工程启发**

> 为乌尔都语手写识别研究提供首个公开基准数据集和基线模型，促进该领域算法开发和性能对比。

**为什么值得关注**

> 直接涉及手写文本识别数据集构建和模型评估，与OCR方向相关。

**原始摘要**

Automatic Handwritten Text Recognition (HTR) is inherently a challenging task, and its complexity is
further increased when dealing with cursive scripts. Although significant efforts have been made on
various cursive scripts, research regarding Urdu Handwritten Text Recognition (UHTR) has been
relatively limited. This lag of research is primarily due to the unique challenges posed by its
script, and the scarcity and unavailability of benchmark datasets. Therefore, to advance research in
UHTR, this study presents a specialized real dataset called the Urdu Katib Handwritten Dataset
(UKHD). To the best of our knowledge, this is the first offline Urdu handwritten text lines dataset
specifically curated from the materials written by Katibs in historical times. It encompasses a
diverse range of flat nib writing variations in the Nastalique calligraphic style. Additionally, the
effectiveness of different CRNN-based hybrid models has been evaluated to identify the optimal
architecture for Urdu Katib Handwriting Recognition (UKHR). Among the analyzed models, the CNN-BGRU-
CTC model showed more robust performance, with low Character Error Rate (CER) and Word Error Rate
(WER). This research work aims to support and encourage the research community in developing a
robust recognition system for preserving Urdu handwritten literature.

---

### 3. Analyzing and Encoding the Al-Mawrid Arabic-English Dictionary with the ISO Language Markup Framework and TEI Lex-0

- arXiv: [2606.18205v1](https://arxiv.org/abs/2606.18205v1)
- PDF: [下载链接](https://arxiv.org/pdf/2606.18205v1)
- 作者: Diaa Fayed, Laurent Romary
- 发布时间: 2026-06-16T17:35:11Z
- 分类: cs.CL
- 相关性评分: 14
- 主题标签: 数字化、词典编码、阿拉伯语处理、ISO标准、TEI、信息提取

**中文摘要**

> 提出一种系统方法论，将Al-Mawrid阿拉伯语-英语词典从印刷资源数字化编码为标准化计算词典，同时符合ISO词汇标记框架（LMF）和TEI Lex-0指南。基于字母Ayn样本的结构解析准确率达91%，同义词提取精度85%、召回率98%。并讨论了TEI Lex-0在建模阿拉伯语特有现象时的局限性。

**核心创新概述**

> 首次将20世纪双语阿拉伯语词典同时映射到ISO LMF和TEI Lex-0两种标准，并解决其结构歧义和标点不一致问题。

**创新点拆解**

- 采用双标准（LMF和TEI Lex-0）框架编码旧版双语词典
- 提出编辑视角解析词典宏观和微观结构，处理历史印刷问题
- 定量评估结构解析和信息提取性能（精度85%、召回率98%）
- 分析TEI Lex-0对阿拉伯语隐性开放集语义关系的建模不足

**当前局限**

> 仅对字母Ayn样本进行了详细验证，未覆盖全部字母；TEI Lex-0对某些阿拉伯语现象支持有限。

**后续可改进方向**

- 扩展编码至整部词典，并验证其他字母的性能
- 改进TEI Lex-0或提出扩展以支持阿拉伯语特有语义关系
- 利用Linked Open Data集成，增强资源的互操作性和可发现性

**工程启发**

> 为阿拉伯语计算词汇学提供高质量标准化词典资源，可用于NLP任务如机器翻译、语义分析。

**为什么值得关注**

> 涉及数字化文档的结构化编码和信息提取，与文档理解相关。

**原始摘要**

This paper presents a robust methodology for the systematic digitization and encoding of the Al-
Mawrid Arabic-English dictionary, transforming it from a legacy print resource into a standardized
computational lexicon. Addressing a significant gap in Arabic lexical infrastructure, the study
adopts a dual-standard framing that aligns the ISO Lexical Markup Framework (LMF) with the Text
Encoding Initiative TEI Lex-0 guidelines. By applying an editorial view to the dictionary's macro-
and microstructure, the research resolves the structural ambiguities and punctuation inconsistencies
typical of 20th-century bilingual dictionaries. The methodology is grounded in an empirical analysis
of the dictionary's lexical knowledge density. Drawing on a representative sample (the letter Ayn,
comprising 4.6% of the total volume), the study provides scientific weight to the encoding process,
demonstrating a structural parsing accuracy of 91%. Quantitative evaluation of the information
extraction rules reveals high performance, with 85% precision and 98% recall for synonyms, and 88%
precision for other morpho-semantic features. Beyond technical description, the paper provides a
critical comparison with existing Arabic lexical resources and discusses the limitations of TEI
Lex-0 when modelling specific Arabic phenomena, such as implicit "open set" semantic relations and
scattered morphological cues. Furthermore, the study explores the potential for Linguistic Linked
Open Data (LLOD) integration by establishing a scalable prefix-based referencing system that
facilitates the resource's inclusion in the semantic web. The result is an interoperable, machine-
tractable resource that provides a reproducible workflow for the retro-digitization of complex
legacy bilingual lexicons within the Arabic NLP and Digital Humanities communities.

---

### 4. Freeing the Law with LOCUS: A Local Ordinance Corpus for the United States

- arXiv: [2606.19334v1](https://arxiv.org/abs/2606.19334v1)
- PDF: [下载链接](https://arxiv.org/pdf/2606.19334v1)
- 作者: Denis Peskoff, Joe Barrow, Christopher Vu, Diag Davenport
- 发布时间: 2026-06-17T17:58:22Z
- 分类: cs.CL, cs.CY, cs.LG
- 相关性评分: 13
- 主题标签: 法律AI、语料库构建、OCR、法规分析、ModernBERT

**中文摘要**

> 为解决美国地方法规碎片化、不易获取的问题，构建LOCUS数据集，涵盖了9,239个市县的地方法典，并提供一个县级协调访问层覆盖大多数人口。使用OCR处理多种文档格式，并训练基于ModernBERT的分类器分析法规特征。

**核心创新概述**

> 首次大规模收集和统一处理美国市县地方法典，构建可用于法律AI研究的机器可读语料库。

**创新点拆解**

- 构建覆盖9,239个市县的地方法典原始语料库（LOCUS）
- 提供县级协调访问层，覆盖2,309个县
- 利用OCR处理异构文档格式，将法律文本转化为机器可读形式
- 训练ModernBERT分类器进行法规维度分析（如透明度、家长作风）

**当前局限**

> OCR可能引入错误，且仅覆盖美国地方法规；县级协调层仅包含前2,309个县，未全面覆盖。

**后续可改进方向**

- 改进OCR质量，减少转录错误
- 扩展覆盖范围，包括更多国家和更低层级立法
- 开发更细粒度的法律特征分析模型

**工程启发**

> 提供大规模法律文本语料库和预训练分类器，支持法律AI研究和公共政策分析。

**为什么值得关注**

> 涉及OCR处理异构文档、法律文本语料构建，直接关联文档分析和OCR应用。

**原始摘要**

Progress in legal AI increasingly depends on access to authoritative legal text at scale. Yet one of
the most consequential layers of American law remains largely absent from existing machine-readable
corpora: local ordinances. Local codes govern zoning, housing, business licensing, public health,
noise, animal control, and many other domains of everyday regulation, but they are fragmented across
vendor platforms designed for human browsing rather than bulk research access. We introduce LOCUS -
the Local Ordinance Corpus for the United States - a comprehensive corpus and county-harmonized
access layer for U.S. municipal and county ordinance codes. The raw corpus, available for release to
researchers, represents nearly all publicly available municipal and county ordinance codes. The
resulting raw corpus contains codes from 9,239 cities and counties. A smaller county-harmonized
LOCUS access layer provides coverage for the largest 2,309 of 3,144 U.S. counties, accounting for a
majority of the population. We use OCR to handle the myriad of document formats that have kept the
law from being a public resource. We release the corpus with coverage metadata to support
reproducibility, downstream legal AI research, and the incremental expansion of machine-readable
access to local law. We train a collection of ModernBERT-based classifiers and scorers to facilitate
analyzing U.S. local law among several dimensions, such as opacity and paternalism, that have not
previously been studied at this scale. LOCUS-v1 and its derivative models are available at:
https://huggingface.co/datasets/LocalLaws/LOCUS-v1

---

### 5. Bounding Box Label Propagation for Re-Annotation of Document Layout Analysis Datasets

- arXiv: [2606.17644v1](https://arxiv.org/abs/2606.17644v1)
- PDF: [下载链接](https://arxiv.org/pdf/2606.17644v1)
- 作者: Nick Jochum, Tobias Alt-Veit, Christian Schön, Alexander Lück, René Schuster, Didier Stricker
- 发布时间: 2026-06-16T08:04:27Z
- 分类: cs.CV, cs.AI
- 相关性评分: 11
- 主题标签: 半监督学习、标签传播、文档布局分析、目标检测、重标注

**中文摘要**

> 提出边界框标签传播（BBLP）框架，用于文档版面分析数据集的半监督重标注。设计目标编码器整合视觉、文本和位置嵌入，在仅10%标注数据的情况下，在D4LA数据集上达到全监督性能的81.6%。

**核心创新概述**

> 首次将标签传播方法应用于目标检测任务中的重分类，专门处理文档版面分析的半监督标注传播问题。

**创新点拆解**

- 提出BBLP伪标签框架，以plug-and-play方式支持目标检测实例的重标注
- 设计融合视觉、文本和位置信息的目标编码器，生成联合嵌入用于标签传播
- 在10%标注数据下达到全监督81.6% mAP，验证有效性

**当前局限**

> 实验仅在单个D4LA数据集上验证，泛化性未知；未与其他半监督目标检测方法对比。

**后续可改进方向**

- 在更多文档版面数据集和实际场景中验证BBLP的泛化能力
- 探索更高效的目标编码器或传播策略以提升性能
- 结合主动学习进一步减少人工标注成本

**工程启发**

> 显著降低文档版面分析任务中重标注的人力成本，适用于持续增长的动态数据集。

**为什么值得关注**

> 直接解决文档布局分析中标注稀疏和类别演化问题，与OCR预处理和版面理解相关。

**原始摘要**

Datasets in practical document processing scenarios typically grow over time, and their class
annotations undergo continuous refinement. This creates significant re-annotation efforts, which are
time-consuming and costly. A promising remedy is to re-annotate only a small subset of available
documents manually and apply semi-supervised learning techniques that leverage both labelled and
unlabelled data. Although there are numerous approaches to tackle this problem for classification,
there exists no adaptation for the problem of re-classifying object detection instances, e.g. for
document layout analysis. To this end, we propose Bounding Box Label Propagation (BBLP), a pseudo-
labelling framework for object detection. An object encoder integrates visual, textual, and
positional embeddings from object detection samples to come up with a joint embedding that can be
used for Label Propagation on partially annotated datasets in a plug-and-play fashion. Evaluation
results indicate that the proposed approach produces high-quality class annotations of bounding
boxes. In the D4LA layout analysis dataset, it achieves a mAP of 54.0%, corresponding to 81.6% of
fully supervised performance, while using only 10% labelled data. Our work demonstrates the
potential of Label Propagation for object detection and lays the groundwork for reducing manual
annotation efforts in real-world document processing applications.

---

### 6. Performance Gap Analysis between Latin and Arabic Scripts HTR

- arXiv: [2606.18884v1](https://arxiv.org/abs/2606.18884v1)
- PDF: [下载链接](https://arxiv.org/pdf/2606.18884v1)
- 作者: Sana Al-azzawi, Elisa Barney, Marcus Liwicki
- 发布时间: 2026-06-17T10:00:22Z
- 分类: cs.CV
- 相关性评分: 10
- 主题标签: 手写识别、阿拉伯语、拉丁语、性能差距、CRNN、脚本差异

**中文摘要**

> 通过统一CRNN模型对多数据集进行控制实验，分析拉丁文和阿拉伯文手写识别（HTR）的性能差距。结果表明，在低资源情况下差距大，全量数据下仍有5-7个CER点的差距；标注质量、视觉变异性和字符频率分布是影响因素。

**核心创新概述**

> 首次在统一框架下对拉丁和阿拉伯手写识别进行系统的控制对比，定量分析性能差距的成因。

**创新点拆解**

- 采用统一CRNN模型在9个数据集上对比拉丁和阿拉伯手写识别性能
- 发现性能差距随数据量增加而缩小但持续存在，定量为5-7 CER
- 揭示标注错误和视觉变异性是差距来源，清洗数据可缩小差距
- 通过字符频率分布分析说明阿拉伯语分布更重尾

**当前局限**

> 仅使用单一CRNN架构，未测试Transformer等新型模型；部分数据集本身标注质量不一。

**后续可改进方向**

- 在更大规模、多样化的数据集上验证差距普遍性
- 探索针对阿拉伯语视觉变异性的数据增强或模型结构改进
- 研究更先进的标注校正方法，提升数据质量
- 比较不同脚本的语言模型或后处理的影响

**工程启发**

> 为阿拉伯语和类似复杂脚本的HTR系统优化提供指导，明确性能瓶颈和解决方向。

**为什么值得关注**

> 直接对比不同脚本的OCR性能，分析差距原因，对多语言OCR系统开发有参考价值。

**原始摘要**

Recent studies have shown that handwritten text recognition (HTR) systems perform worse on Arabic-
script datasets than on Latin-script data. However, the reasons for this gap are still not well
understood due to the lack of controlled comparisons. In this work, we present a comprehensive study
of Arabic and Latin scripts HTR using a unified CRNN model for line-level HTR across nine datasets
(including KHATT (Arabic), Muharaf (Arabic), NUST-UHWR (Urdu), PHTD (Persian), IAM (English),
READ-2016 (German), and others) and di ferent training sizes (K in {100, 500, 1000, 2000, ...,
Kfull}). Our results show the performance gap remains: it is large in low-resource settings,
decreases with more data, but remains even at full scale, with a consistent difference of 5-7 CER
points. We show that annotation quality matters, as many datasets contain labeling errors. Cleaning
reduces error rates and narrows the gap, but does not eliminate it. In addition, we find that a
fixed number of training samples provides less effective coverage in Arabic due to higher visual
variability, requiring more data to learn similar representations. We compare recognition across
datasets in terms of the number of text lines and the number of characters, showing an equivalence
trade-off. We compare character frequency distributions across scripts and show that Arabic is
significantly more heavy-tailed than Latin. Our error analysis reveals that around 30 percent of
substitution errors in Arabic datasets (e.g., KHATT) are caused by confusion between visually
similar characters, compared to about 15 percent in Latin-script datasets such as IAM.

---

### 7. IUU+DB: Tracking Illegal, Unreported, and Unregulated Fishing, Seafood Fraud, and Labor Abuse through LLM-driven Information Extraction

- arXiv: [2606.18181v1](https://arxiv.org/abs/2606.18181v1)
- PDF: [下载链接](https://arxiv.org/pdf/2606.18181v1)
- 作者: Henry Bodwell, Hong Yang, John C. Simeone, Kelvin Gorospe, Bella Sullivan, Lana Huang, Jessica Gephart, Sandy Aylesworth, Molly Masterton, Naren Ramakrishnan
- 发布时间: 2026-06-16T17:16:05Z
- 分类: cs.IR, cs.AI, cs.CY
- 相关性评分: 10
- 主题标签: 信息抽取、大语言模型、渔业应用

**中文摘要**

> 提出IUU+概念，涵盖非法、无报告和无管制捕捞及相关供应链犯罪。基于大语言模型构建IUU+DB系统，从异构文档中提取事件关键要素（如行为者、地点、物种、船只等），支持去重和趋势分析。

**核心创新概述**

> 首次将非法捕捞概念扩展至IUU+，并利用LLM构建全球事件数据库。

**创新点拆解**

- 定义IUU+概念以覆盖更广泛渔业犯罪
- 基于LLM的信息抽取系统，处理异构文档
- 支持去重与趋势分析的数据库构建方法

**当前局限**

> 依赖文档质量，可能漏检非文本来源事件。

**后续可改进方向**

- 探索多模态信息融合（如卫星图像）
- 优化低资源语言场景下的抽取能力
- 增强实时监控与预警功能

**工程启发**

> 为渔业监管、政策制定和供应链风险评估提供自动化数据支撑。

**为什么值得关注**

> 展示LLM在特定领域文档解析与信息抽取中的应用，与OCR/文档解析技术的任务定义和工程实现相关。

**原始摘要**

Illegal, unreported, and unregulated fishing (IUU) traditionally refers to fishing activities that
violate applicable laws or occur in areas that lack applicable laws. We propose the term IUU+ to
capture a broader suite of fisheries sector environmental and associated supply chain trade-related
crimes and behaviors. Although IUU+ activity is widely recognized as a serious threat to marine
ecosystems, markets, and livelihoods, a quantitative understanding of these incidents, e.g., their
frequency, geography, species, actors, and patterns in the type of illicit activity, remains
difficult to obtain. We propose IUU+DB, a large language model driven system for building a global
incident database of IUU+ activity. The system ingests heterogeneous documents, classifies whether
they describe relevant incidents, extracts key data elements such as actors, locations, species,
vessels, violations, and enforcement outcomes, and supports deduplication and trend analysis. Case
studies and validation results show that IUU+DB can help organize fragmented evidence, surface
geographic and behavioral hotspots, support fisheries-domain specific research in academia and non-
government organizations, assist source and species risk assessments for industry, and provide
support for policy implementation and targeted enforcement efforts to government agencies.

---

### 8. ProductConsistency: Improving Product Identity Preservation in Instruction-Based Image Editing via SFT and RL

- arXiv: [2606.19103v1](https://arxiv.org/abs/2606.19103v1)
- PDF: [下载链接](https://arxiv.org/pdf/2606.19103v1)
- 作者: Mukund Khanna, Raj Singh Yadav, Kunal Singh
- 发布时间: 2026-06-17T14:16:47Z
- 分类: cs.CV, cs.AI
- 相关性评分: 9
- 主题标签: 图像编辑、产品身份保持、强化学习

**中文摘要**

> 针对指令式图像编辑中产品身份保持难题，构建ProductConsistency数据集（87k监督样本、869张RL图像），并提出基于循环一致性的RL训练方法，显著提升产品一致性、文本渲染和视觉质量。

**核心创新概述**

> 首次聚焦产品级图像编辑中的身份保持问题，提出专用数据集和RL训练范式。

**创新点拆解**

- 构建产品编辑SFT数据集和RL数据集
- 提出循环一致性奖励用于保留产品身份
- 建立产品编辑基准测试集

**当前局限**

> 数据集规模有限，可能未覆盖所有产品类型。

**后续可改进方向**

- 扩展产品类别和场景多样性
- 探索更细粒度的身份保持评估指标
- 结合多模态输入提升鲁棒性

**工程启发**

> 提升电商场景下图像编辑工具的产品一致性，具有直接商业应用价值。

**为什么值得关注**

> 涉及文本渲染（OCR相关能力）和指令编辑中的身份保持，与文档解析中的文本信息处理相关。

**原始摘要**

Recent advances in instruction-based image editing have enabled models to perform complex visual
edits from natural language instructions. However, in product-centric scenarios where preserving
product features, branding, and textual elements are critical, current open and closed source models
often struggle to maintain this fine-grained object identity. This issue is further compounded by
the lack of datasets for instruction-based product image editing with text fidelity constraints,
leaving it largely treated as an implicit capability of instruction-based image editing models. In
this work, we introduce the ProductConsistency dataset which is designed to improve product-centric
image editing. Our approach includes a supervised fine-tuning (SFT) dataset of 87k samples for
product editing, a reinforcement learning (RL) dataset with 869 unique product images, and a new
benchmark dataset, the ProductConsistency Benchmark, to allow rigorous and standardized evaluation
of editing models. To guide RL training, we propose a Cyclic Consistency reward that enforces
semantic preservation of product identity by using caption similarity between the original product
description and captions generated from the edited image. We fine-tune both Qwen-Image-Edit-2511 and
Flux.1-Kontext-dev using our dataset and demonstrate consistent improvements over baseline models in
OCR and Perceptual metrics, and MLLM-based evaluations as well, indicating stronger product
consistency, text rendering, and overall visual quality; with the Qwen-Image-Edit-2511 model
achieving a 5x reduction in the character error rate. The code and pipeline is available at
https://anonymous.4open.science/r/ProductConsistency-6FCC/README.md

---

### 9. PorTEXTO: A European Portuguese Benchmark for Visual Text Extraction

- arXiv: [2606.19096v1](https://arxiv.org/abs/2606.19096v1)
- PDF: [下载链接](https://arxiv.org/pdf/2606.19096v1)
- 作者: João Cardeira, Diogo Glória-Silva, Manuel Letras da Luz, Rafael Ferreira, Diogo Tavares, David Semedo, João Magalhães
- 发布时间: 2026-06-17T14:06:26Z
- 分类: cs.CV
- 相关性评分: 9
- 主题标签: OCR、低资源语言、基准数据集

**中文摘要**

> 发布首个面向现代欧洲葡萄牙语的视觉文本提取基准PorTEXTO，包含文化和当代相关样本。采用前沿LVLM与母语者审查结合的标注流程，发现专用多语言数据比模型规模更关键。

**核心创新概述**

> 填补欧洲葡萄牙语在现代OCR场景中的基准缺失。

**创新点拆解**

- 构建首个当代pt-PT视觉文本提取基准
- 设计人工与LVLM结合的标注流程
- 揭示多语言专用数据对性能的主导作用

**当前局限**

> 基准规模较小，仅覆盖有限场景。

**后续可改进方向**

- 扩展覆盖更多领域和文本类型
- 研究低资源语言的跨域迁移方法
- 开发更高效的标注策略

**工程启发**

> 为欧洲葡萄牙语OCR系统提供标准化评估和资源，促进该语言方向的技术发展。

**为什么值得关注**

> 直接针对OCR提取任务，提供低资源语言评估基准，与文档解析的文本提取和语言适应性相关。

**原始摘要**

European Portuguese (pt-PT) is largely absent from OCR benchmarks, which skew toward high-resource
languages. The few benchmarks that cover pt-PT focus on historical artifacts and literature. This
work addresses modern OCR applications, introducing PorTEXTO, the first benchmark for contemporary
and culturally relevant pt-PT visual text extraction. To ascertain quality, we employ an annotation
pipeline combining transcriptions from a frontier LVLM with exhaustive review by native speakers. We
observe a sharp performance drop from synthetic to real world samples in most models, and find that,
currently, specialized multilingual data is a better driver for pt-PT performance than model size or
resolution budget, motivating the release of open pt-PT OCR resources.

---

### 10. Spotlight: Synergizing Seed Exploration and Spot GPUs for DiT RL Post-Training

- arXiv: [2606.19004v1](https://arxiv.org/abs/2606.19004v1)
- PDF: [下载链接](https://arxiv.org/pdf/2606.19004v1)
- 作者: Ruiqi Lai, Dakai An, Wei Gao, Ju Huang, Siran Yang, Jiamang Wang, Lin Qu, Dmitrii Ustiugov, Wei Wang
- 发布时间: 2026-06-17T12:31:44Z
- 分类: cs.DC, cs.AI, cs.LG
- 相关性评分: 9
- 主题标签: 强化学习、扩散模型、高效训练

**中文摘要**

> 提出Spotlight系统，利用spot GPU实现扩散变换器强化学习后训练的成本降低。通过种子探索的权重解耦和弹性序列并行技术，支持预抢占环境下的高效训练。

**核心创新概述**

> 首次实现spot GPU在DiT RL后训练中的应用，解决预抢占和拓扑碎片问题。

**创新点拆解**

- 提出可容忍过时权重的探索方法
- 设计弹性序列并行以快速恢复分组
- 开发基于bandit的探索规划器和预抢占感知调度器

**当前局限**

> 仅验证于特定模型，通用性待考察。

**后续可改进方向**

- 扩展到更多模型架构
- 优化探索效率与训练稳定性的平衡
- 探索跨云环境的迁移性

**工程启发**

> 显著降低DiT RL后训练成本，促进扩散模型在资源受限场景的应用。

**为什么值得关注**

> 涉及训练范式的工程优化，虽非直接OCR但可启发文档分析模型的低成本训练。

**原始摘要**

Reinforcement learning (RL) post-training of Diffusion Transformers (DiTs) is prohibitively
expensive, requiring thousands of high-end GPUs. Existing works explore two directions to reduce
cost: seed exploration improves training convergence by selecting high-contrast samples, yet adds
compute to the critical path; spot GPUs offer 69--77\% lower cost, yet sit idle during training
because DiT rollouts finish nearly simultaneously, which prevents LLM-style pipelining of rollout
with training. Spot preemptions further break Sequence Parallelism (SP) groups, fragmenting GPU
topology. We present Spotlight, the first system that harvests spot GPUs for DiT RL post-training.
Spotlight rests on two key insights we devise: (1)~we show that exploration can tolerate stale model
weights because exploration that uses the model weights from the previous iteration preserves the
relative ranking of random seeds, allowing exploration to run on idle spot GPUs during training.
(2)~SP reconfiguration can reuse on-node state, reducing group recovery from minutes to sub-second
launches. Built on these insights, Spotlight introduces three techniques: a bandit-based exploration
planner that maximizes reward variance within the training time budget, elastic sequence parallelism
that reconfigures SP groups on the fly via persistent schedulers and intra-node weight copying, and
a preemption-aware pull-based request scheduler that balances load and commits in-flight state upon
preemption. We implement Spotlight on the open-source RL platform ROLL and evaluate it on Qwen-Image
post-training. Spotlight reaches the same target validation score $4\times$ faster than baselines,
reducing total cost by $1.4$-$6.4\times$ while achieving superior image quality on DeepSeek-OCR and
Geneval datasets with resolution $512\times512$ and $1280\times1280$.

---

### 11. STAR: SpatioTemporal Adaptive Reward Allocation for Text-to-Image RL Post-Training

- arXiv: [2606.17979v1](https://arxiv.org/abs/2606.17979v1)
- PDF: [下载链接](https://arxiv.org/pdf/2606.17979v1)
- 作者: Jinjie Shen, Wei Deng, Xian Hu, Daiguo Zhou, Jian Luan
- 发布时间: 2026-06-16T14:30:12Z
- 分类: cs.AI
- 相关性评分: 9
- 主题标签: 图像生成、强化学习、文本渲染

**中文摘要**

> 提出时空自适应奖励（STAR）分配方法，用于文本到图像生成模型的RL后训练。利用文本-图像注意力构建空间分配图，对与提示核心内容相关的潜层区域施加更强策略更新，提升语义对齐和文本渲染。

**核心创新概述**

> 首次在文本到图像RL后训练中引入时空细粒度的优势分配。

**创新点拆解**

- 提出基于注意力的空间奖励分配图
- 设计区域解析的策略目标函数
- 在GenEval和OCR任务上显著提升性能

**当前局限**

> 依赖注意力图质量，可能受模型内部表示影响。

**后续可改进方向**

- 探索无注意力依赖的分配方法
- 扩展到视频生成等时序场景
- 结合人类偏好进行细粒度优化

**工程启发**

> 提升文本到图像生成的质量和可控性，对广告、设计等应用有直接价值。

**为什么值得关注**

> OCR文本渲染是评估任务之一，其时空分配思想可迁移至文档图像生成的文本质量控制。

**原始摘要**

Existing RL post-training methods for text-to-image generation usually convert the final-image
reward into a single scalar advantage and apply it with the same strength to the entire generative
trajectory. However, text-to-image generation naturally has temporal and spatial structure:
different denoising steps are responsible for different generation stages, and the content that
truly determines text alignment often appears only in part of the image. This granularity mismatch
makes it difficult for policy updates to focus on the generative components that actually affect the
reward. To address this issue, we propose \textbf{SpatioTemporal Adaptive Reward (STAR) Allocation}
for RL post-training of text-to-image diffusion and flow models. STAR uses text-image attention
inside the generative model and starts from the core content that the user truly cares about in the
prompt. It constructs spatial allocation maps that dynamically vary across denoising steps and
rollouts, and allocates the same group-relative advantage to more relevant latent regions with
almost no additional computational overhead. STAR then applies stronger policy updates to these
regions through a spatially resolved policy objective. We use Stable Diffusion 3.5 Medium as the
base model and evaluate on three tasks: GenEval, OCR text rendering, and PickScore. Experimental
results show that STAR improves compositional semantic alignment, text rendering, and preference
optimization without changing the external reward source, achieving $\mathbf{0.9759}$,
$\mathbf{0.9757}$, and $\mathbf{23.60}$ on GenEval, OCR, and PickScore, respectively.

---

### 12. SAMA: Semantic Anchor-aligned Augmentation for Unified Low-Resource Multimodal Information Extraction

- arXiv: [2606.18780v1](https://arxiv.org/abs/2606.18780v1)
- PDF: [下载链接](https://arxiv.org/pdf/2606.18780v1)
- 作者: Quanjiang Guo, Chong Mu, Jiazhou Pan, Ming Jia, Ling Tian, Hui Gao, Zhao Kang
- 发布时间: 2026-06-17T07:43:33Z
- 分类: cs.CV, cs.CL, cs.MM
- 相关性评分: 6
- 主题标签: 数据增强、多模态信息抽取、大语言模型

**中文摘要**

> 提出语义锚定对齐增强（SAMA）框架，用于多模态信息抽取的统一数据增强。构建结构化语义锚引导多专家大模型生成文本，并采用锚保持扩散机制合成图像，通过双约束过滤保证质量。

**核心创新概述**

> 首次提出统一的多模态数据增强框架，共享跨任务语义知识。

**创新点拆解**

- 设计语义锚构造方法指导数据生成
- 提出协作多专家多模态大模型
- 引入锚保持扩散和双约束过滤机制

**当前局限**

> 合成数据与真实数据仍存在分布差异。

**后续可改进方向**

- 研究更逼真的图像合成技术
- 探索跨语言跨模态的扩展
- 增强小样本场景下的适应能力

**工程启发**

> 缓解多模态信息抽取的数据稀缺问题，提升低资源下的抽取性能。

**为什么值得关注**

> 多模态信息抽取依赖文本和图像理解，与文档解析中的联合建模相关。

**原始摘要**

Multimodal Information Extraction (MIE)-covering tasks such as Multimodal Named Entity Recognition
(MNER), Relation Extraction (MRE), and Event Extraction (MEE)-is essential for understanding
multimedia content but remains constrained by severe data scarcity. Although data augmentation is a
promising remedy, existing approaches are impeded by coarse cross-modal alignment and fragmented,
task-specific designs that fail to exploit shared semantic knowledge. To overcome these limitations,
we introduce Semantic Anchor-aligned Multimodal Augmentation (SAMA), a unified framework for
generating high-fidelity, task-aware synthetic data. SAMA constructs structured semantic anchors
from ground-truth labels to guide a Collaborative Multi-Experts Multimodal Large Language Model
(CME-MLLM), which integrates a Universal Adapter for shared semantics with Task-Specific Adapters to
produce diverse yet constraint-compliant textual samples. For image synthesis, SAMA employs an
Anchor-Preserving Diffusion mechanism that uses anchor-weighted prompts and latent conditioning to
maintain critical semantic anchors while diversifying visual contexts. To eliminate the need for
manual verification, SAMA further introduces a Dual-Constraint Filtering module that selects
synthetic samples based on both cross-modal consistency and anchor fidelity. Extensive experiments
across benchmark datasets for MNER, MRE, and MEE demonstrate that SAMA consistently outperforms
state-of-the-art augmentation baselines under both fully supervised and low-resource settings,
underscoring its versatility, robustness, and effectiveness.

---
