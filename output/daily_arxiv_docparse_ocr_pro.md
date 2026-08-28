# OCR / 文档解析研究日报（2026-08-28）

## 报告说明

- 检索源：arXiv API
- 检索查询：`(all:"document parsing" OR all:"document understanding" OR all:"optical character recognition" OR all:OCR OR all:"layout analysis" OR all:"document layout analysis" OR all:"text recognition" OR all:"table recognition" OR all:"form understanding" OR all:"document intelligence" OR all:"page understanding" OR all:"scene text recognition" OR all:"handwritten text recognition" OR all:"information extraction") AND (cat:cs.CV OR cat:cs.AI OR cat:cs.CL OR cat:eess.IV)`
- 生成时间（UTC）：`2026-08-28 12:45:35`
- 大模型综合分析：`开启`

## 一、今日执行摘要

> 今日研究显示OCR领域正向多模态、低资源语言和复杂文档处理演进，但现有模型在基准测试中仍面临挑战，提示工程化需结合具体场景优化。

## 二、今日趋势判断

OCR研究趋势从通用模型转向特定领域（如古文、手稿），并注重数据集构建和基准测试；多模态RAG和视觉优先方法成为主流，强调视觉理解与文本解析的融合。

## 三、今日论文概览

1. **Systematic Literature Review of Machine Learning Models and Applications for Text Recognition** | 标签：OCR、文献综述、机器学习、文本识别、挑战与方向
2. **Ancient-Bench: A Comprehensive Multi-millennial, Multi-medium, and Multi-script Benchmark for Ancient Chinese Artifact Text Recognition** | 标签：古代文本、基准测试、OCR、视觉语言模型、文化遗产
3. **AraMS-28k: The Largest Publicly Released Line-Level Dataset of Historical Arabic Manuscripts with Margin and Insertion-Anchor Annotations** | 标签：手写识别、历史文档、数据集、阿拉伯语、注释
4. **CorporateBench: Large-Scale Q&A Benchmarking with Temporal Knowledge Bases** | 标签：问答系统、大语言模型、基准测试、知识库、企业应用
5. **PlanSightRAG: A Visual-First Multimodal RAG for Automating Question Answering and Compliance Checking for Civil Standard Plans** | 标签：多模态RAG、土木工程、合规检查、视觉理解、文档分析
6. **PailitaoGR: Latent Think-with-Images for Generative Image Retrieval** | 标签：生成式检索、图像检索、多模态、目标感知、电商
7. **When Is Noise Response Universal? Tokenization as the Hidden Variable in Language Models** | 标签：噪声鲁棒性、tokenization、语言模型、OCR噪声、对比训练
8. **Multi-Granularity Context-Enhanced RAG over Multimodal Knowledge Graphs** | 标签：多模态知识图谱、GraphRAG、上下文增强、视觉语言模型、信息检索

## 四、今天 OCR / 文档解析论文里的主要创新点

- 多模态RAG和视觉优先框架，减少对OCR的依赖，直接处理图像信息。
- 大规模、多介质、多语言数据集的构建，推动模型泛化能力。
- 利用LLM和视觉语言模型进行标注和解析，提高效率。
- 关注噪声鲁棒性，从tokenization层面解释和提升模型抗噪能力。

## 五、后续 OCR 领域值得推进的改进方向

- 开发低资源语言和手写体的自适应识别模型，利用自监督学习增强泛化。
- 构建多模态知识图谱融合文本、图像和上下文，提升复杂文档解析精度。
- 设计视觉-语言联合模型，实现端到端文档理解，避免中间OCR误差。
- 探索无监督或弱监督学习，减少对大规模标注数据的依赖。
- 研究动态上下文增强机制，结合用户意图和任务需求，提升RAG检索质量。

## 六、工程落地启发

- 采用视觉优先的RAG框架，可减少OCR信息丢失，提高合规检查等场景的准确率。
- 构建专用基准（如Ancient-Bench）时，需定义多级注释标准，确保可评估性。
- 噪声增强训练和鲁棒tokenization能显著提升OCR系统在真实场景下的稳定性。
- 利用多模态LLM进行数据标注（如RefLAM管道）可提高效率，但需人工审核保证质量。
- 评估模型时，应模拟真实输入规模（如企业文档），以避免性能高估。

## 七、优先关注论文

- **Ancient-Bench: A Comprehensive Multi-millennial, Multi-medium, and Multi-script Benchmark for Ancient Chinese Artifact Text Recognition**：首个古文多介质基准，可能成为文化遗产数字化的标准评估工具，值得跟踪其扩展和应用。
- **PlanSightRAG: A Visual-First Multimodal RAG for Automating Question Answering and Compliance Checking for Civil Standard Plans**：视觉优先RAG在专业文档（土木图纸）中表现优异，有望推广至其他工程领域。
- **AraMS-28k: The Largest Publicly Released Line-Level Dataset of Historical Arabic Manuscripts with Margin and Insertion-Anchor Annotations**：创新性的锚点注释支持非线性阅读顺序恢复，可能影响历史手稿数字化标准。
- **When Is Noise Response Universal? Tokenization as the Hidden Variable in Language Models**：揭示了tokenization对噪声鲁棒性的关键作用，为OCR后处理提供理论指导，可转化为工程实践。

## 八、论文逐篇解析

### 1. Systematic Literature Review of Machine Learning Models and Applications for Text Recognition

- arXiv: [2608.26500v1](https://arxiv.org/abs/2608.26500v1)
- PDF: [下载链接](https://arxiv.org/pdf/2608.26500v1)
- 作者: Nuzhat Khan, Ab Al-Hadi Ab Rahman, Shahriyar Masud Rizvi, Ibrahim Yousef Alshareef, Muhammad Nadzir Marsono, Muhammad Paend Bakht, Mohd Shahrizal Rusli, Shahidatul Sadiah
- 发布时间: 2026-08-27T00:48:11Z
- 分类: cs.CV, cs.LG
- 相关性评分: 31
- 主题标签: OCR、文献综述、机器学习、文本识别、挑战与方向

**中文摘要**

> 本综述基于PRISMA指南，对2015年1月至2025年1月间发表的97项OCR研究进行了系统评估，追踪了AI模型在文本识别领域的演变，涵盖了模型架构、应用领域、数据类型、语言覆盖范围及挑战。研究发现，OCR技术在处理结构化与非结构化文本、场景文本识别和多语言处理方面取得了显著进展，但仍面临资源稀缺语言支持不足、手写文本高变异性、字符视觉相似性以及实时OCR应用限制等挑战。为此，提出了自监督学习、多模态AI、自动化机器学习（AutoML）、AI辅助后处理等潜在解决方案。

**核心创新概述**

> 采用PRISMA标准进行系统文献综述，提供近十年OCR模型发展的全面评估，涵盖多维度分析。

**创新点拆解**

- 应用PRISMA指南进行系统性文献综述
- 综合分析97项研究，覆盖模型、应用、数据、语言等多个维度
- 识别关键OCR模型并分析其性能、优势和局限

**当前局限**

> 仅基于选定研究的定性分析，缺乏定量对比实验；可能遗漏某些最新进展；依赖文献发表质量。

**后续可改进方向**

- 开展更多针对低资源语言的OCR研究，探索自监督学习等方法
- 发展多模态AI融合文本结构与语义信息
- 利用AutoML自动化模型选择与调优
- 开发AI辅助后处理机制提升识别准确性

**工程启发**

> 为OCR领域研究者提供清晰的进展图谱和未来方向建议，有助于制定研究路线。

**为什么值得关注**

> 系统总结OCR技术演进，为后续研究提供基础参考和挑战梳理。

**原始摘要**

Optical Character Recognition (OCR) for text recognition using machine vision has significantly
improved, particularly when handling heterogeneous textual data. Traditional OCR models struggle
with script variations, writing styles, and degraded documents. Advancements in technology are
leading to new AI models with improved architecture for handling multiple languages and complex data
formats. Despite this progress, a comprehensive evaluation of OCR advancements remains limited.
Based on the established preferred reporting items for systematic reviews and meta-analysis (PRISMA)
guidelines, this literature review presents an extensive assessment of OCR research to trace the
evolution of AI models over the past decade. It explores the transition in AI models, application
domains, data types, linguistic coverage, and challenges. Through a detailed analysis of 97 selected
studies published during January 2015 - January 2025, key OCR models are identified, and their
performance, strengths, and limitations are analyzed. The findings highlight how OCR technologies
have evolved to address structured and unstructured text, scene text recognition, and multilingual
processing. Unresolved challenges include limited resources for underrepresented languages, high
variability in handwritten text, visual similarity among characters, and constraints in real-time
OCR applications. To address these issues, several promising approaches are proposed. Key
suggestions include self-supervised learning, multimodal AI, automated machine learning (AutoML),
AI-assisted postprocessing, tiny machine learning (TinyML), and the creation of joint corpora for
script matching. The future recommendations aim to enhance OCR accuracy and tackle the challenges
identified for real-time industrial applications. This study will guide future research and
establish a foundation for OCR field.

---

### 2. Ancient-Bench: A Comprehensive Multi-millennial, Multi-medium, and Multi-script Benchmark for Ancient Chinese Artifact Text Recognition

- arXiv: [2608.27169v1](https://arxiv.org/abs/2608.27169v1)
- PDF: [下载链接](https://arxiv.org/pdf/2608.27169v1)
- 作者: Hiuyi Cheng, Nuo Xu, Yuyi Zhang, Xuhan Zheng, Wei Pan, Jing Zhang, Dezhi Peng, Minghui Liao, Yihua Teng, Jihao Wu, Haoyu Ren, Lianwen Jin
- 发布时间: 2026-08-27T14:22:12Z
- 分类: cs.CV
- 相关性评分: 19
- 主题标签: 古代文本、基准测试、OCR、视觉语言模型、文化遗产

**中文摘要**

> 针对古代中文文物文本识别，现有基准存在时间覆盖有限、介质多样性不足、字体类型不完整等问题。为此，提出Ancient-Bench基准，包含2700张图像，覆盖三千年字符演变、九类文物介质、七种历史字体形式。并定义了三种注释标准（符号、字符、解析标准化）以应对异构介质。实验表明，通用视觉语言模型和OCR专用模型在此基准上表现不佳，古代文本识别仍面临变体字、特殊符号、幻觉等挑战。数据集已公开。

**核心创新概述**

> 首个多千年、多介质、多字体的古代中文文物文本识别基准，并定义了标准化注释方案。

**创新点拆解**

- 构建大规模多介质古代文本基准Ancient-Bench
- 定义三类注释标准以适配不同材质
- 跨学科整合考古与OCR技术

**当前局限**

> 基准规模相对有限（2700张），可能未覆盖所有古代文本变体；实验表明现有模型性能有限。

**后续可改进方向**

- 扩展基准覆盖更多历史时期和介质
- 开发针对古代变体字和符号的专用识别模型
- 利用多模态信息辅助识别以减少幻觉

**工程启发**

> 为古代文物数字化提供标准化评估工具，推动文化遗产保护技术发展。

**为什么值得关注**

> 填补古代中文文本识别基准的空白，对OCR研究人员和数字人文领域具有重要参考价值。

**原始摘要**

Ancient Chinese artifact text recognition is fundamental to heritage digitization, and benchmarks
for ancient texts are essential for evaluating current model capabilities. However, existing
benchmarks suffer from ''fragmentation'', manifested in limited temporal coverage, limited medium
diversity, and incomplete script types. Therefore, we present Ancient-Bench, a comprehensive
benchmark of 2,700 images for ancient Chinese artifact text recognition, featuring three dimensions:
Multi-millennial (spanning 3,000 years of character evolution), Multi-medium (covering nine artifact
categories), and Multi-script (encompassing seven historical script forms). To enable consistent and
fair evaluation across heterogeneous media, we further define three annotation standards tailored to
the medium-specific characteristics of ancient texts: symbol standardization, character
standardization, and parsing standardization. Extensive experiments on Ancient-Bench covering
general Vision-Language Models (VLMs) and OCR-specialist models reveal that ancient Chinese artifact
text recognition remains fundamentally unsolved, with persistent challenges in variant characters,
specialized symbols, and hallucination. The dataset is available at https://github.com/SCUT-
DLVCLab/Ancient_Bench.

---

### 3. AraMS-28k: The Largest Publicly Released Line-Level Dataset of Historical Arabic Manuscripts with Margin and Insertion-Anchor Annotations

- arXiv: [2608.26921v1](https://arxiv.org/abs/2608.26921v1)
- PDF: [下载链接](https://arxiv.org/pdf/2608.26921v1)
- 作者: Mohamed Guechaoui, Mohamed Diaa Zellagui, Souleyman Chaib, Sahraoui Dhelim
- 发布时间: 2026-08-27T10:16:41Z
- 分类: cs.CV, cs.CL
- 相关性评分: 16
- 主题标签: 手写识别、历史文档、数据集、阿拉伯语、注释

**中文摘要**

> 介绍AraMS-28k，至今最大的公开行级历史阿拉伯语手稿数据集，包含14本书、3043页、28600个标注文本行（主文本27971行，边缘629行）。覆盖三种手写传统（Naskh、Ruq'ah、Maghrebi）及一种石印印刷版。每个行标注主文本或边缘类别，边缘行如与主文本有明确连接点则标注插入锚点，以恢复手稿的真实非线性阅读顺序，这是首次为历史阿拉伯语手稿语料库发布此类标注。数据集提供原始带音符转录和去除音符的版本，构建采用RefLAM管道，结合多模态LLM OCR与人工审核。提供了使用Kraken和HATFormer的基线HTR结果，包括跨脚本泛化实验。

**核心创新概述**

> 首个带有插入锚点注释的历史阿拉伯语手稿数据集，提供行级非线性阅读顺序信息。

**创新点拆解**

- 发布大规模行级手稿数据集AraMS-28k
- 创新注释方案包括边缘行插入锚点标注
- 利用RefLAM管道结合多模态LLM与人工审核提高标注质量

**当前局限**

> 数据仅覆盖阿拉伯语手稿，跨语言泛化性未知；基线HTR模型性能有限。

**后续可改进方向**

- 扩展数据集至其他语言和书写风格
- 探索更强大的HTR模型以处理复杂手写体
- 利用锚点信息辅助文档解析和阅读顺序恢复

**工程启发**

> 为阿拉伯语手稿数字化和文档解析研究提供宝贵资源，促进历史文档分析技术发展。

**为什么值得关注**

> 提供新颖的数据集和注释范式，对OCR和手写识别领域有直接贡献。

**原始摘要**

We introduce AraMS-28k, the largest publicly released line-level dataset of genuine historical
Arabic manuscripts, comprising 14 books, 3,043 pages, and 28,600 annotated text lines (27,971 main-
text, 629 margin). Thirteen books are hand-copied manuscripts spanning three script traditions --
Naskh, Ruq'ah, and Maghrebi -- and one is a lithographed printed edition included to broaden format
diversity. Each line is labelled as main-text or margin, and margin lines that have an unambiguous
attachment point in the main text are further annotated with an insertion anchor, recovering the
manuscript's true non-linear reading order at line-level granularity -- to our knowledge the first
such annotation released for a historical Arabic manuscript corpus. Because reference transcriptions
are fully vocalised while manuscript hands are typically undiacritised, we release both the raw
diacritised transcription and a diacritic-normalised counterpart for every line. The dataset was
constructed with RefLAM, a reference-grounded annotation pipeline that aligns multimodal-LLM OCR
against independently sourced clean transcriptions and routes every line through human review,
combining automatic verification with expert oversight. We describe the construction and quality-
control process, present the annotation schema, report dataset statistics at both the corpus and
per-book level, and provide baseline HTR results using Kraken and HATFormer, including a cross-
script generalisation gradient from in-distribution pages to fully unseen books. AraMS-28k is
released with page images, line-level annotations, and fixed train/val/test splits under CC BY-NC-SA
4.0 to support reproducible research on Arabic manuscript recognition, layout analysis, and reading-
order recovery.

---

### 4. CorporateBench: Large-Scale Q&A Benchmarking with Temporal Knowledge Bases

- arXiv: [2608.27391v1](https://arxiv.org/abs/2608.27391v1)
- PDF: [下载链接](https://arxiv.org/pdf/2608.27391v1)
- 作者: Sil Hamilton, Albert Yu Sun, Oscar J. Romero, Carl-Leander Henneking, David Mimno, Bishan Yang, Igor Labutov
- 发布时间: 2026-08-27T17:23:04Z
- 分类: cs.AI, cs.CL, cs.IR, cs.LG
- 相关性评分: 10
- 主题标签: 问答系统、大语言模型、基准测试、知识库、企业应用

**中文摘要**

> 针对企业级文档集问答评估困难的问题，提出CorporateBench基准，包含超过23万文档，模拟4家合成企业（员工数12-10000），基于时间演化的知识库生成，保证跨文档逻辑一致性。该基准评估LLM在信息抽取和知识库查询两个维度上的能力。实验显示，随着输入规模接近实际水平，LLM性能显著下降，揭示了其在企业通信推理上的不足。该基准填补了评估生态中的空白。

**核心创新概述**

> 首个接近企业真实规模的多任务Q&A基准，能保证跨文档逻辑一致性。

**创新点拆解**

- 构建大规模合成企业文档语料库
- 基于时间演化知识库生成数据，保证一致性
- 提出跨两个维度的评估任务

**当前局限**

> 合成数据可能不完全代表真实企业文本的复杂性；评估侧重于LLM，可能忽略专门模型。

**后续可改进方向**

- 引入更多真实企业数据以提高生态效度
- 扩展到多模态文档场景
- 探索模型压缩以处理大规模输入

**工程启发**

> 为企业级LLM应用提供可靠评估工具，帮助开发者了解模型在真实场景下的表现。

**为什么值得关注**

> 强调了大规模真实场景评估的重要性，与OCR后文本理解相关。

**原始摘要**

LLMs are increasingly able to answer complex questions about enterprise-scale document collections.
But evaluation is hard: companies don't want to share internal communications, and synthetic
datasets have been overly simple. We present CorporateBench (CB), a human-validated multi-task Q&A
benchmark whose scale approaches the conditions LLMs encounter in corporate communication networks,
with evaluation corpora surpassing 230,000 documents. CB evaluates LLMs across two dimensions
(information extraction and knowledge base querying) through four synthetically generated firms
ranging from 12 to 10,000 employees. Each corpus is sampled from a temporally evolving knowledge
base describing a consistent world, guaranteeing cross-document logical consistency even across
hundreds of thousands of documents. We evaluate five LLMs on CB, revealing increasingly poor
performance as input size approaches realistic scales. CB provides LLM developers a metric for
corporate communication reasoning, filling a crucial gap in the benchmarking ecosystem.

---

### 5. PlanSightRAG: A Visual-First Multimodal RAG for Automating Question Answering and Compliance Checking for Civil Standard Plans

- arXiv: [2608.26091v1](https://arxiv.org/abs/2608.26091v1)
- PDF: [下载链接](https://arxiv.org/pdf/2608.26091v1)
- 作者: Nabaraj Subedi, Shuvo Dip Datta, Ahmed Abdelaty, Shivanand Venkanna Sheshappanavar
- 发布时间: 2026-08-26T17:54:24Z
- 分类: cs.IR, cs.CL, cs.CV
- 相关性评分: 10
- 主题标签: 多模态RAG、土木工程、合规检查、视觉理解、文档分析

**中文摘要**

> 针对土木工程合规检查依赖人工读取图纸的问题，提出PlanSightRAG框架，采用视觉优先的多模态RAG方法，直接对图纸图像进行索引和推理。集成ColNomic-3B多向量检索、代理式Planner-Retriever-Auditor-Synthesizer流程，并利用MaxSim热图作为证据踪迹。构建了包含5个州交通部标准图纸共4056对问题的基准。零样本检索Recall@5达91.47%，在密歇根州交通部数据集上为91.40%。对于合成合规图纸，Qwen2.5-VL-72B流水线在预置规则阈值时达到100%判定准确率，但非视觉OCR基线已达76.4%。此外，实现了自主视觉规则定位，从规范中提取数值限制。

**核心创新概述**

> 提出视觉优先的多模态RAG，直接基于图纸图像进行推理，避免了OCR丢失几何信息的问题。

**创新点拆解**

- 基于多模态RAG的视觉优先框架
- 多向量检索与代理式流程结合
- 生成MaxSim热图作为证据追踪

**当前局限**

> 依赖预置规则阈值时表现最优；测试数据为合成生成，可能无法完全反映真实图纸复杂度。

**后续可改进方向**

- 扩展到更多真实图纸场景
- 进一步自动化规则提取以减少人工干预
- 增强模型对复杂几何布局的理解

**工程启发**

> 为土木工程文档自动化检查提供新思路，减少人工阅读成本，提高合规检查效率。

**为什么值得关注**

> 展示了OCR在多模态文档理解中的局限，及视觉优先方法作为替代方案的价值。

**原始摘要**

Civil infrastructure compliance checking has long relied on engineers manually reading legacy 2D
plans; however, OCR-based automation strips away the geometry and layout essential for interpreting
these plans. We present a Visual-First Multimodal Retrieval-Augmented Generation (RAG) framework
called PlanSightRAG. It indexes and reasons directly over plan imagery, integrates a ColNomic-3B
multi-vector retrieval, an agentic Planner-Retriever-Auditor-Synthesizer, and MaxSim heatmaps as an
evidence trail. We introduce a 4,056-pair benchmark from five state Departments of Transportation
(DOT) standard plans (1,898 pages). PlanSightRAG achieves 91.47% Recall@5 on zero-shot retrieval,
while on a held-out Michigan DOT corpus, it achieves 91.40%. On synthetic, parametrically-generated
compliance drawings, our Qwen2.5-VL-72B pipeline reaches 100% verdict accuracy only when supplied a
pre-resolved rule threshold, a controlled ceiling that a non-VLM OCR baseline already reaches at
76.4%. Finally, we demonstrate autonomous visual rule-grounding by extracting numeric limits
directly from a specification corpus without any human-supplied rules.

---

### 6. PailitaoGR: Latent Think-with-Images for Generative Image Retrieval

- arXiv: [2608.26658v1](https://arxiv.org/abs/2608.26658v1)
- PDF: [下载链接](https://arxiv.org/pdf/2608.26658v1)
- 作者: Xiaomeng Fan, Yueran Liu, Shengyu Zhou, Chenghan Fu, Wanxian Guan, Feng Li, Chuan Yu, Jian Xu, Bo Zheng
- 发布时间: 2026-08-27T06:12:32Z
- 分类: cs.CV, cs.AI, cs.IR
- 相关性评分: 9
- 主题标签: 生成式检索、图像检索、多模态、目标感知、电商

**中文摘要**

> 提出了PailitaoGR方法，用于生成式图像检索，通过“潜在图像思维”机制，使生成式检索模型能够内部化目标聚焦感知和选择性辅助证据利用，实现“无裁剪缩放”和“无OCR阅读”。具体包含目标感知机制（目标增强器和基于策略蒸馏与注意力引导损失的学习策略）和选择性辅助证据利用机制（辅助增强器和容量内增量对比蒸馏策略）。构建了来自真实在线图像搜索日志的训练和验证集。实验表明，该方法在平均性能上超过现有基线13.8%。

**核心创新概述**

> 首次将“潜在思维”概念引入生成式图像检索，使模型能够隐式处理目标聚焦和辅助证据选择。

**创新点拆解**

- 目标聚焦感知机制，增强目标区域视觉token
- 选择性辅助证据利用机制，动态利用辅助信息
- 结合策略蒸馏和对比蒸馏的学习方法

**当前局限**

> 依赖真实用户搜索日志构建数据，可能引入噪声；仅关注图像检索，未涉及文本信息。

**后续可改进方向**

- 融合OCR信息以提升对图像中文本的理解
- 扩展到视频检索领域
- 增强对辅助证据的细粒度利用

**工程启发**

> 为电商图像检索提供高效方案，提升搜索体验，降低对精确裁剪和OCR的依赖。

**为什么值得关注**

> 展示了无需OCR即可实现图像中的文本理解，对OCR与检索交叉领域有启示。

**原始摘要**

Generative retrieval has demonstrated strong performance by directly generating product semantic
identifiers (SIDs). Extending this paradigm to image search, however, is nontrivial because real-
world query images contain diverse information, including the search target, useful auxiliary
evidence, and irrelevant visual content. This requires the model to identify and focus on the search
target while selectively utilizing auxiliary evidence. In this paper, we propose
\textbf{PailitaoGR}, a \emph{Latent Think-with-Images} method for generative image retrieval, which
internalizes target-focused perception and selective auxiliary-evidence utilization into a the
generative retrieval model, enabling \textit{Zooming without Cropping} and \textit{Reading without
OCR}. Specifically, we design a target-focused perception mechanism that identifies and enhances
visual tokens of the search target, consisting of a target Enhancer and a learning strategy based on
on-policy distillation and attention guidance loss, enabling the model to focus on search-target
regions. We also design a selective auxiliary-evidence utilization mechanism that identifies and
enhances visual tokens of auxiliary evidence, including an auxiliary enhancer and an in-capacity
incremental contrastive distillation strategy, enabling the model to exploit auxiliary evidence. We
construct training and validation sets sampled from real-world online image-search logs. Experiments
show that our method outperforms existing baselines by an average of 13.8\%, validating its
effectiveness.

---

### 7. When Is Noise Response Universal? Tokenization as the Hidden Variable in Language Models

- arXiv: [2608.26319v1](https://arxiv.org/abs/2608.26319v1)
- PDF: [下载链接](https://arxiv.org/pdf/2608.26319v1)
- 作者: Yefan Tao, Gerald Friedland, Luyang Kong
- 发布时间: 2026-08-26T18:51:51Z
- 分类: cs.CL, cs.LG
- 相关性评分: 9
- 主题标签: 噪声鲁棒性、tokenization、语言模型、OCR噪声、对比训练

**中文摘要**

> 该研究探讨了文本神经模型在输入噪声（如拼写错误、OCR错误或单词遗漏）下的性能退化规律。研究发现，在词级噪声下，不同架构的模型表现出大致相同的退化曲线；而在字符级噪声下，模型表现分化。作者将这一差异归因于训练目标而非架构，并通过对比训练实验验证了tokenization的作用：单个字符编辑会导致分词器重新切分词，从而对token序列造成更大干扰。该发现可用于无需噪声评估即可预测模型鲁棒性，并通过噪声增强训练来提升特定噪声尺度下的鲁棒性。

**核心创新概述**

> 揭示了模型对噪声鲁棒性的通用性与噪声尺度的关系，并确定tokenization为关键因素，而非通常认为的模型架构或训练目标。

**创新点拆解**

- 通过大规模实验比较了多种神经模型在词级和字符级噪声下的鲁棒性，发现词级噪声下退化曲线具有跨架构一致性。
- 识别出训练目标（预训练范式）而非架构是决定噪声鲁棒性的主要因素，通过对比训练可统一性能表现。
- 提出tokenization机制作为解释词级和字符级噪声差异的根本原因，并验证了单字符编辑对token序列的更大干扰。
- 提供一种无需噪声评估即可预测模型鲁棒性的方法，以及通过噪声增强训练来在特定噪声尺度上安装鲁棒性的手段。

**当前局限**

> 研究主要基于文本模型，对多模态或视觉模型未涉及；噪声类型限于拼写、OCR等，未涵盖更复杂的结构化噪声；预测鲁棒性的方法可能受限于训练数据分布。

**后续可改进方向**

- 探索更鲁棒的分词方法或字符级编码策略，以减轻字符级噪声对token序列的扰动。
- 研究噪声增强训练在不同噪声尺度下的最优比例，以及如何动态调整训练噪声。
- 将发现扩展到多模态语音或视觉模型，验证其普适性。
- 开发基于该机制的鲁棒性评估基准，实现无需噪声数据的模型鲁棒性预测。

**工程启发**

> 为OCR系统提供理论指导：在字符级干扰下，可通过鲁棒分词或噪声增强训练提升系统健壮性；同时，提供了一种快速评估模型对噪声敏感性的方法，节省测试成本。

**为什么值得关注**

> OCR中常见字符级噪声（如识别错误），该研究直接分析了字符级噪声对模型的影响机制，并提出了提升鲁棒性的方法，对OCR后处理及模型优化具有直接指导意义。

**原始摘要**

The performance of textual neural models often degrades when their inputs are corrupted by noise
such as typos, OCR errors, or dropped words. We study the degradation rate across neural models,
both sentence embeddings and decoder-only LLMs, and find that how consistent it is depends on the
scale of the noise: under word-level noise, models with very different architectures decline along
nearly the same curve, while under character-level noise they separate. We further identify the
determining factor to be the training objective, not the architecture: eight encoders spanning six
pretraining paradigms are scattered initially, and collapse onto a common curve after a short
contrastive training recipe. We trace the word/character split to tokenization: a single character
edit forces the tokenizer to re-segment the surrounding word, disturbing the token sequence far more
than dropping a whole word does. This finding and its underlying mechanism provide a practical means
to predict a model's robustness to noise without any noisy evaluation, and to install robustness at
a chosen noise scale through noise-augmented training.

---

### 8. Multi-Granularity Context-Enhanced RAG over Multimodal Knowledge Graphs

- arXiv: [2608.25986v1](https://arxiv.org/abs/2608.25986v1)
- PDF: [下载链接](https://arxiv.org/pdf/2608.25986v1)
- 作者: Zongyu Wu, Yilong Wang, Xiaochen Wang, Minhua Lin, Zhichao Xu, Fenglong Ma, Xiang Zhang, Suhang Wang
- 发布时间: 2026-08-26T16:38:02Z
- 分类: cs.AI
- 相关性评分: 6
- 主题标签: 多模态知识图谱、GraphRAG、上下文增强、视觉语言模型、信息检索

**中文摘要**

> 该研究提出了一种上下文增强的多模态知识图谱（CEMMKG）框架，以改进多模态GraphRAG的性能。现有方法在视觉信息提取和多模态融合时对文本上下文利用不足，导致图像与文本之间存在语义差距。CEMMKG通过为每张图像补充局部和全局文本上下文，并在局部上下文中采用多粒度设计，来丰富图像信息。实验证明该方法在视觉中心数据集上有效。

**核心创新概述**

> 提出在构建多模态知识图谱时，不仅利用相邻文本，还引入语义相关句子和全局摘要作为图像上下文，并采用多粒度设计，以缩小图像-文本语义鸿沟。

**创新点拆解**

- 提出CEMMKG框架，为图像补充局部和全局文本上下文，超越传统的周围文本。
- 局部上下文引入语义相关句子（通过语义相似度检索），全局上下文提供段落摘要。
- 设计多粒度局部上下文，捕获不同细节层次的相关信息。
- 将CEMMKG应用于多模态GraphRAG，提升视觉问答等任务的性能。

**当前局限**

> 实验仅在特定视觉中心数据集上评估，未在更多任务或更大规模数据上验证；上下文增强可能引入冗余信息，增加计算开销；未详细分析不同粒度选择的影响。

**后续可改进方向**

- 探索自适应上下文粒度选择，如基于图像复杂度或任务类型动态调整局部上下文粒度。
- 研究更有效的文本上下文过滤机制，减少噪声和冗余，提高检索效率。
- 将CEMMKG与其他多模态融合技术结合，如跨模态注意力，进一步提升语义对齐。
- 在更多任务（如视觉推理、图文生成）和多种数据集上验证泛化性。

**工程启发**

> 为多模态知识图谱构建和GraphRAG系统提供了可实施的增强方案，能提升视觉问答等应用的准确性，对工业界部署多模态RAG系统有参考价值。

**为什么值得关注**

> OCR是构建多模态知识图谱的重要环节，本文关于多模态知识图谱的上下文增强方法有助于OCR与其他模态信息的融合，为OCR在知识图谱中的应用提供思路。

**原始摘要**

Retrieval-augmented generation (RAG) is widely used to mitigate hallucination issues in large
language models (LLMs) and multimodal large language models (MLLMs). In particular, knowledge graph
(KG)-based RAG leverages structured knowledge to provide (M)LLMs with high-quality external
information. Building on these works, recent studies have explored multimodal knowledge graphs
(MMKGs) as knowledge bases for GraphRAG. This enables Graph RAG to integrate knowledge across
multiple modalities, thereby further enhancing its performance. However, existing MMKG-based RAG
methods generally follow a common pipeline in which different modalities are largely processed
independently before being fusion. As a result, textual context is only used to a limited extent
during visual information extraction and subsequent multimodal knowledge fusion. This brings a
semantic gap between images and text which limits the multimodal GraphRAG performance. To address
this issue, we propose a novel framework for constructing a Context-Enhanced MMKG (CEMMKG) to better
support multimodal GraphRAG. The proposed CEMMKG enriches each image with complementary textual
context at both local and global scopes. Local context goes beyond the surrounding text by
incorporating sentences that are semantically related to the image, while global context provides a
summary of the entire passage. We further introduce a multi-granularity design for the local
context, allowing it to capture semantically relevant information at different levels of detail.
Extensive experiments on the selected vision-centric dataset validate that CEMMKG is effective in
leveraging contextual information to improve MMKG-based RAG performance. Moreover, its effectiveness
across different MMKG-based RAG methods demonstrates its broad applicability.

---
