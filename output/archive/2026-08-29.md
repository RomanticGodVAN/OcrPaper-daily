# OCR / 文档解析研究日报（2026-08-29）

## 报告说明

- 检索源：arXiv API
- 检索查询：`(all:"document parsing" OR all:"document understanding" OR all:"optical character recognition" OR all:OCR OR all:"layout analysis" OR all:"document layout analysis" OR all:"text recognition" OR all:"table recognition" OR all:"form understanding" OR all:"document intelligence" OR all:"page understanding" OR all:"scene text recognition" OR all:"handwritten text recognition" OR all:"information extraction") AND (cat:cs.CV OR cat:cs.AI OR cat:cs.CL OR cat:eess.IV)`
- 生成时间（UTC）：`2026-08-29 07:51:38`
- 大模型综合分析：`开启`

## 一、今日执行摘要

> 今日三篇论文分别聚焦古代中文、历史阿拉伯文手稿识别基准与大型企业文档问答基准，共同揭示现有模型在专业领域、长尾场景及大规模文档处理上的显著不足，并指出多模态、跨脚本、非线性阅读顺序恢复及长文档上下文优化是当前技术突破的关键方向。

## 二、今日趋势判断

研究重点正从通用OCR转向专业领域与历史文档的细粒度识别，基准测试向多维度、规模化发展，同时大模型在长文档与低资源场景下的能力短板成为关注焦点。

## 三、今日论文概览

1. **Ancient-Bench: A Comprehensive Multi-millennial, Multi-medium, and Multi-script Benchmark for Ancient Chinese Artifact Text Recognition** | 标签：基准测试、古代文字识别、多模态、文化遗产
2. **AraMS-28k: The Largest Publicly Released Line-Level Dataset of Historical Arabic Manuscripts with Margin and Insertion-Anchor Annotations** | 标签：数据集、手稿识别、阿拉伯语、HTR
3. **CorporateBench: Large-Scale Q&A Benchmarking with Temporal Knowledge Bases** | 标签：基准测试、问答系统、知识库、大语言模型

## 四、今天 OCR / 文档解析论文里的主要创新点

- 构建大规模、多维度基准，如Ancient-Bench覆盖多年代、多介质、多字体，CorporateBench模拟企业规模文档。
- 引入新型注释标准与流程，如Ancient-Bench的三种标准化注释、AraMS-28k的插入锚点注释，以应对复杂文档结构。
- 利用合成数据或自动流程构建数据集，如CorporateBench基于时间知识库生成，AraMS-28k结合多模态LLM OCR与人工审核。
- 聚焦跨脚本泛化，如AraMS-28k基线实验验证跨脚本能力，Ancient-Bench评估多脚本支持。

## 五、后续 OCR 领域值得推进的改进方向

- 开发针对古代文字变体与幻觉的专用评估指标及优化目标，降低OCR模型对专业符号的误识别率。
- 拓展基准至更多语言与文字系统，并纳入真实企业文档，增强现实适用性。
- 研究插入锚点注释的自动化生成方法，减少对LLM的依赖，提升手稿非线性阅读顺序恢复的准确性。
- 设计长文档处理技术，如分块、摘要或记忆增强机制，以缓解大模型在企业规模文档上的性能退化。
- 探索多模态模型在文化遗产数字化中的端到端应用，集成识别、解析与知识图谱构建。

## 六、工程落地启发

- 构建专业领域基准时，定义分介质注释标准可提升评估有效性，如Ancient-Bench的三级标准。
- 采用多模态LLM与人工审核结合的注释流程可高效构建大规模数据集，如AraMS-28k的RefLAM。
- 基于时间知识库生成逻辑一致的数据，可确保跨文档一致性，适用于企业级问答数据集构建。
- 评估模型时，需涵盖不同规模输入以暴露性能退化，如CorporateBench揭示的长文档短板。
- 跨脚本泛化应成为HTR系统设计目标，可通过多语言语料训练或迁移学习实现。

## 七、优先关注论文

- **Ancient-Bench: A Comprehensive Multi-millennial, Multi-medium, and Multi-script Benchmark for Ancient Chinese Artifact Text Recognition**：该基准揭示通用模型在古代文字识别上的不足，可能催生专项优化技术，且作为文化遗产数字化评估平台有长期应用价值。
- **AraMS-28k: The Largest Publicly Released Line-Level Dataset of Historical Arabic Manuscripts with Margin and Insertion-Anchor Annotations**：该数据集引入插入锚点注释，可推动手稿非线性阅读顺序恢复研究，其RefLAM流程对低资源数据构建有参考意义。
- **CorporateBench: Large-Scale Q&A Benchmarking with Temporal Knowledge Bases**：该基准达到企业规模，揭示LLM长文档处理瓶颈，后续优化技术可能直接影响文档解析与知识管理产品性能。

## 八、论文逐篇解析

### 1. Ancient-Bench: A Comprehensive Multi-millennial, Multi-medium, and Multi-script Benchmark for Ancient Chinese Artifact Text Recognition

- arXiv: [2608.27169v1](https://arxiv.org/abs/2608.27169v1)
- PDF: [下载链接](https://arxiv.org/pdf/2608.27169v1)
- 作者: Hiuyi Cheng, Nuo Xu, Yuyi Zhang, Xuhan Zheng, Wei Pan, Jing Zhang, Dezhi Peng, Minghui Liao, Yihua Teng, Jihao Wu, Haoyu Ren, Lianwen Jin
- 发布时间: 2026-08-27T14:22:12Z
- 分类: cs.CV
- 相关性评分: 19
- 主题标签: 基准测试、古代文字识别、多模态、文化遗产

**中文摘要**

> Ancient-Bench是一个针对中国古代文物文字识别的综合基准，包含2700张图像，覆盖3000年字符演变、9种文物类别、7种历史字体。基准定义了三种注释标准以适应不同介质特性。实验表明，现有通用VLM和OCR专用模型在该任务上表现不佳，面临变体字符、专业符号和幻觉等挑战。

**核心创新概述**

> 首个在多时间跨度、多介质、多字体三个维度上系统评估古代中文文字识别的基准，并提出了针对介质特性的注释标准。

**创新点拆解**

- 构建了包含2700张图像、覆盖3000年字符演变、9种文物类别和7种历史字体的综合基准
- 定义了符号标准化、字符标准化和解析标准化三种注释标准
- 对通用VLM和OCR专用模型进行了系统评估，揭示了当前方法的不足

**当前局限**

> 图像数量有限（2700张），可能无法完全代表古代文物的多样性；评估集中于中文，未覆盖其他语言；基准尚未涵盖所有可能的古代文字形式

**后续可改进方向**

- 扩展基准图像数量和多样性，包括更多年代和介质
- 引入更多语言和文字系统，增强多语言泛化能力
- 开发针对变体字符和幻觉的专用评估指标和优化目标

**工程启发**

> 为古代文物文字识别提供了标准化的评估平台，有助于推动该领域模型的发展，并可用于文化遗产数字化工程的实际应用中。

**为什么值得关注**

> 直接针对OCR领域中的古代文字识别挑战，提供了基准和评估方法，对研究者和工程师均有重要参考价值。

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

### 2. AraMS-28k: The Largest Publicly Released Line-Level Dataset of Historical Arabic Manuscripts with Margin and Insertion-Anchor Annotations

- arXiv: [2608.26921v1](https://arxiv.org/abs/2608.26921v1)
- PDF: [下载链接](https://arxiv.org/pdf/2608.26921v1)
- 作者: Mohamed Guechaoui, Mohamed Diaa Zellagui, Souleyman Chaib, Sahraoui Dhelim
- 发布时间: 2026-08-27T10:16:41Z
- 分类: cs.CV, cs.CL
- 相关性评分: 16
- 主题标签: 数据集、手稿识别、阿拉伯语、HTR

**中文摘要**

> AraMS-28k是最大的公开历史阿拉伯语手稿行级数据集，包含14本书、3043页和28600行注释文本，涵盖三种手写字体和一种石印印刷版本。每行标注为主文本或边注，并对手稿中的插入锚点进行注释以恢复非线性阅读顺序。数据集提供原始带音符转录和去音符版本，并通过RefLAM流程构建，结合多模态LLM OCR和人工审核。基线实验使用Kraken和HATFormer展示跨脚本泛化能力。

**核心创新概述**

> 首个提供行级插入锚点注释的历史阿拉伯语手稿数据集，恢复非线性阅读顺序，且规模最大。

**创新点拆解**

- 构建了包含28600行注释文本的大规模数据集，覆盖多种字体和印刷形式
- 创新性地引入了插入锚点注释，用于恢复手稿的非线性阅读顺序
- 提出了RefLAM注释流程，结合多模态LLM OCR与人工审核，确保数据质量

**当前局限**

> 数据集主要关注阿拉伯语手稿，其他语言手稿可能不适用；注释流程依赖多模态LLM，可能引入误差；仅包含两种基线模型，未与最新HTR方法对比

**后续可改进方向**

- 扩展数据集到其他语言和手稿类型，增加多样性
- 优化注释流程，减少对LLM的依赖，提高自动化程度和准确性
- 引入更多现代HTR模型，进行更全面的基准评估

**工程启发**

> 提供大规模高质量数据，可训练和评估历史阿拉伯语手稿识别系统，对文化遗产数字化工程有实际应用价值。

**为什么值得关注**

> 填补了历史阿拉伯语手稿数据集的空白，提供了创新注释和构建流程，对OCR/HTR领域有重要贡献。

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

### 3. CorporateBench: Large-Scale Q&A Benchmarking with Temporal Knowledge Bases

- arXiv: [2608.27391v1](https://arxiv.org/abs/2608.27391v1)
- PDF: [下载链接](https://arxiv.org/pdf/2608.27391v1)
- 作者: Sil Hamilton, Albert Yu Sun, Oscar J. Romero, Carl-Leander Henneking, David Mimno, Bishan Yang, Igor Labutov
- 发布时间: 2026-08-27T17:23:04Z
- 分类: cs.AI, cs.CL, cs.IR, cs.LG
- 相关性评分: 10
- 主题标签: 基准测试、问答系统、知识库、大语言模型

**中文摘要**

> CorporateBench是一个大规模多任务问答基准，模拟企业环境，包含超过23万文档的评估语料库，通过时间知识库生成逻辑一致的数据。基准评估两个维度：信息抽取和知识库查询。实验显示，随着输入规模增大，LLM性能显著下降，揭示了现有模型在企业规模文档处理上的不足。

**核心创新概述**

> 首个达到企业规模（23万+文档）的问答基准，基于时间知识库确保跨文档逻辑一致性。

**创新点拆解**

- 构建了包含超过23万文档的大规模综合基准，覆盖多种规模的企业场景
- 利用时间知识库生成逻辑一致的数据，确保跨文档一致性
- 评估了五个LLM，揭示了性能随规模下降的关键问题

**当前局限**

> 数据是合成的，可能无法完全真实反映企业文档复杂性；评估限于特定任务（信息抽取和知识库查询），未涵盖其他商业场景；未提供人工评估的细节

**后续可改进方向**

- 纳入真实企业文档数据，增加基准的现实性
- 扩展任务类型，如问答、摘要、推理等
- 开发针对长文档和上下文窗口的优化策略，提升模型处理大规模语料的能力

**工程启发**

> 为评估LLM在企业环境中的表现提供了大规模基准，可用于开发更有效的文档理解系统和知识管理工具。

**为什么值得关注**

> 关注LLM在企业级文档中的应用，与OCR结合可提升文档处理的端到端能力，对智能文档处理有重要参考价值。

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
