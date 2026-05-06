# OCR / 文档解析研究日报（2026-05-06）

## 报告说明

- 检索源：arXiv API
- 检索查询：`(all:"document parsing" OR all:"document understanding" OR all:"optical character recognition" OR all:OCR OR all:"layout analysis" OR all:"document layout analysis" OR all:"text recognition" OR all:"table recognition" OR all:"form understanding" OR all:"document intelligence" OR all:"page understanding" OR all:"scene text recognition" OR all:"handwritten text recognition" OR all:"information extraction") AND (cat:cs.CV OR cat:cs.AI OR cat:cs.CL OR cat:eess.IV)`
- 生成时间（UTC）：`2026-05-06 04:43:27`
- 大模型综合分析：`开启`

## 一、今日执行摘要

> 今日论文覆盖OCR基准评估、医疗文档信息抽取、历史文档结构化及NER工具比较四大热点，共同指向对真实场景鲁棒性和领域特定需求的关注。CC-OCR V2揭示了现有大模型在真实文档处理中的性能短板；MedStruct-S证明了半结构化提取在OCR噪声下的可行性；ATLAS展示了历史文档结构化管道的潜力；NER工具比较则强调了工具选择对下游任务的影响。

## 二、今日趋势判断

研究重点正从通用OCR性能转向真实场景下的鲁棒性评估和领域特定优化，包括高难度样本、OCR噪声、半结构化提取和知识结构恢复。多模态大模型成为主流工具，但评估显示其在实际部署中仍有明显差距。NER和结构化提取的工具对比与鲁棒性研究受到更多关注。

## 三、今日论文概览

1. **CC-OCR V2: Benchmarking Large Multimodal Models for Literacy in Real-world Document Processing** | 标签：OCR基准、多模态大模型、文档处理、真实场景评估
2. **MedStruct-S: A Benchmark for Key Discovery, Key-Conditioned QA and Semi-Structured Extraction from OCR Clinical Reports** | 标签：OCR临床报告、半结构化提取、信息抽取、模型鲁棒性
3. **ATLAS: Article Tracking, Linking, and Analysis of Swedish Encyclopedias** | 标签：OCR后处理、历史文档、知识结构恢复、书籍结构化
4. **Geolocating News about Extreme Climate Events: A Comparative Analysis of Off-the-Shelf Tools for Toponym Identification in German** | 标签：NER工具比较、地理定位、气候事件、德语文本

## 四、今天 OCR / 文档解析论文里的主要创新点

- 所有研究均强调在真实噪声和边缘情况下的评估与优化，而非仅关注理想场景。
- 多个工作提出了针对特定领域（如医疗、历史文献）的专用基准或结构化管道，推动OCR从通用走向垂直。
- 多模态大模型与编码器-解码器架构的对比成为评估核心，揭示了不同架构在特定任务上的优劣。

## 五、后续 OCR 领域值得推进的改进方向

- 构建包含更多高难度样本和真实噪声的大规模OCR基准，覆盖表格、公式、手写等多类型文档。
- 研究显式建模OCR噪声的方法，例如将噪声类型作为输入特征或设计噪声增强训练策略。
- 探索结合编码器和解码器优势的混合架构，用于半结构化文档的端到端抽取。
- 开发领域自适应OCR后处理管道，利用知识图谱和上下文信息提升结构化恢复的召回率。
- 针对极端气候等特定事件，训练专用NER模型并融合地理知识以提升定位准确率。

## 六、工程落地启发

- 企业选型时应参考如CC-OCR V2的贴近实际场景的基准，而非仅依赖公开榜指标。
- 在医疗等高风险领域，优先考虑微调解码器-only模型或编码器-only模型进行键条件抽取。
- 历史文档数字化可采用ATLAS类管道实现高精确率的结构恢复，但需注意实体链接召回率瓶颈。
- NER工具选择需评估其对下游任务的影响，建议在应用领域进行标准化对比测试。

## 七、优先关注论文

- **CC-OCR V2: Benchmarking Large Multimodal Models for Literacy in Real-world Document Processing**：首个聚焦真实高难度文档处理的OCR基准，可能成为行业评估标准，对模型选型和改进方向有指导意义。
- **MedStruct-S: A Benchmark for Key Discovery, Key-Conditioned QA and Semi-Structured Extraction from OCR Clinical Reports**：针对OCR临床报告的半结构化提取基准，其评估结果和模型对比对医疗文档自动化有直接参考价值，可能推动该领域标准化。

## 八、论文逐篇解析

### 1. CC-OCR V2: Benchmarking Large Multimodal Models for Literacy in Real-world Document Processing

- arXiv: [2605.03903v1](https://arxiv.org/abs/2605.03903v1)
- PDF: [下载链接](https://arxiv.org/pdf/2605.03903v1)
- 作者: Zhipeng Xu, Junhao Ji, Zulong Chen, Zhenghao Liu, Qing Liu, Chunyi Peng, Zubao Qin, Ze Xu, Jianqiang Wan, Jun Tang, Zhibo Yang, Shuai Bai, Dayiheng Liu
- 发布时间: 2026-05-05T15:56:12Z
- 分类: cs.CL
- 相关性评分: 33
- 主题标签: OCR基准、多模态大模型、文档处理、真实场景评估

**中文摘要**

> 提出CC-OCR V2基准，聚焦真实文档处理中的高难度OCR任务，涵盖文本识别、文档解析等5个主要赛道，共7093个样本。对14个先进多模态大模型评估显示，现有模型在真实场景中性能显著下降，与基准测试存在差距。

**核心创新概述**

> 首个针对企业级真实文档处理的高难度OCR基准，包含之前被忽视的关键和边缘情况任务。

**创新点拆解**

- 设计涵盖5个OCR核心任务的综合基准
- 聚焦高难度样本和真实场景边缘情况
- 揭示当前LMM在真实应用中的性能差距

**当前局限**

> 基准样本数量相对有限（7093个），且仅评估了14个模型，未覆盖所有可能的方法。

**后续可改进方向**

- 扩展基准规模，覆盖更多任务类型和场景
- 研究模型在真实噪声和多样性条件下的鲁棒性提升方法

**工程启发**

> 为企业文档处理系统的OCR选型和性能评估提供可靠基准，促进模型在实际应用中的落地。

**为什么值得关注**

> 直接面向OCR在真实场景中的性能评估，为文档OCR研究提供方向和测试平台。

**原始摘要**

Large Multimodal Models (LMMs) have recently shown strong performance on Optical Character
Recognition (OCR) tasks, demonstrating their promising capability in document literacy. However,
their effectiveness in real-world applications remains underexplored, as existing benchmarks adopt
task scopes misaligned with practical applications and assume homogeneous acquisition conditions. To
address this gap, we introduce CC-OCR V2, a comprehensive and challenging OCR benchmark tailored to
real-world document processing. CC-OCR V2 focuses on practical enterprise document processing tasks
and incorporates hard and corner cases that are critical yet underrepresented in prior benchmarks,
covering 5 major OCR-centric tracks: text recognition, document parsing, document grounding, key
information extraction, and document question answering, comprising 7,093 high-difficulty samples.
Extensive experiments on 14 advanced LMMs reveal that current models fall short of real-world
application requirements. Even state-of-the-art LMMs exhibit substantial performance degradation
across diverse tasks and scenarios. These findings reveal a significant gap between performance on
current benchmarks and effectiveness in real-world applications. We release the full dataset and
evaluation toolkit at https://github.com/eioss/CC-OCR-V2.

---

### 2. MedStruct-S: A Benchmark for Key Discovery, Key-Conditioned QA and Semi-Structured Extraction from OCR Clinical Reports

- arXiv: [2605.03103v1](https://arxiv.org/abs/2605.03103v1)
- PDF: [下载链接](https://arxiv.org/pdf/2605.03103v1)
- 作者: Yingyun Li, Yu Wang, Haiyang Qian
- 发布时间: 2026-05-04T19:37:21Z
- 分类: cs.CL, cs.AI, cs.LG
- 相关性评分: 12
- 主题标签: OCR临床报告、半结构化提取、信息抽取、模型鲁棒性

**中文摘要**

> 提出MedStruct-S基准，用于评估OCR临床报告中未知键与OCR噪声下的半结构化信息提取任务。包含3582页标注报告，对比编码器-解码器与解码器-only模型。结果表明，编码器-only模型在空值条件下的键条件问答任务中性能最佳，而微调的解码器-only模型整体最优。

**核心创新概述**

> 首次在OCR临床报告场景中综合考虑未知键表示和OCR噪声，设计三项子任务。

**创新点拆解**

- 定义键发现、键条件问答和端到端键值对提取三项任务
- 考虑未知键和OCR噪声下的鲁棒性评估
- 系统对比编码器-only和解码器-only模型范式

**当前局限**

> 仅基于临床报告领域，通用性有待验证；模型规模范围0.11B-103B，但未覆盖所有最新模型。

**后续可改进方向**

- 扩展至更多领域（如法律、金融）的半结构化文档
- 探索结合编码器和解码器优势的混合架构
- 研究OCR噪声的显式建模方法

**工程启发**

> 为医疗文档自动化处理中的模型选择提供实用指南，降低真实应用中的部署风险。

**为什么值得关注**

> 针对OCR文档中的半结构化信息提取，对医疗、金融等领域具有直接实用价值。

**原始摘要**

Semi-structured information extraction (IE) from OCR-derived clinical reports is crucial for
efficiently reconstructing patients' longitudinal medical histories. In practice, this scenario
commonly involves three tasks: (i) field-header (key) discovery, (ii) key-conditioned question
answering (QA), and (iii) end-to-end key-value pair extraction. However, existing evaluations often
under-model two factors: heterogeneous and incompletely known key representations, and OCR-induced
noise. This makes it difficult to assess model robustness in real-world settings. We present
MedStruct-S, a benchmark specifically designed to evaluate these tasks under unknown keys and OCR
noise. MedStruct-S contains 3,582 annotated real-world clinical report pages. Using MedStruct-S, we
benchmark two representative paradigms: encoder-only sequence labeling with post-processing and
decoder-only structured generation, covering four encoder-only and five decoder-only models spanning
0.11B to 103B parameters. Our results show that encoder-only models achieve the best performance for
non-null-value key-conditioned QA despite being substantially smaller than decoder-only models. When
comparing models of similar order of magnitude, encoder-only models still perform better overall.
Without controlling for model scale, fine-tuned decoder-only models deliver the strongest overall
results. These findings show that the benchmark provides a reliable and practical basis for
selecting and comparing models across different semi-structured IE settings.

---

### 3. ATLAS: Article Tracking, Linking, and Analysis of Swedish Encyclopedias

- arXiv: [2605.02466v1](https://arxiv.org/abs/2605.02466v1)
- PDF: [下载链接](https://arxiv.org/pdf/2605.02466v1)
- 作者: Albin Andersson, Salam Jonasson, Fredrik Wastring, Pierre Nugues
- 发布时间: 2026-05-04T11:08:59Z
- 分类: cs.CL
- 相关性评分: 7
- 主题标签: OCR后处理、历史文档、知识结构恢复、书籍结构化

**中文摘要**

> 构建管道对瑞典百科全书《Nordisk familjebok》的四版进行OCR后结构化处理，包括词条提取（F1 97.8%）、分类（F1 93.4%）、跨版本匹配（精确率93%）和Wikidata链接（精确率85%）。展示了自动化处理历史文本结构的可行性。

**核心创新概述**

> 针对多版百科全书的完整结构化管道，将OCR文本恢复为可追溯的知识结构。

**创新点拆解**

- 设计从OCR文本到结构化条目的完整流程
- 实现跨版本条目匹配和知识图谱链接
- 在瑞典语历史文档上达到高精确率

**当前局限**

> Wikidata链接召回率较低（16.5%），跨版本匹配仅小规模评估；依赖的语言和领域有限。

**后续可改进方向**

- 改进实体链接的召回率，例如利用上下文信息或知识图谱嵌入
- 扩展至更多语言和历史文档类型
- 研究OCR错误对结构化影响的鲁棒方法

**工程启发**

> 为历史文献数字化提供自动化结构恢复方案，促进知识传播和历史研究。

**为什么值得关注**

> 展示OCR后处理中结构恢复的重要性，为文档解析提供实用方法。

**原始摘要**

The digitization of old encyclopedias represents an important step to improve access to historically
structured knowledge. Often, however, this process does not go beyond an optical character
recognition, leaving all the underlying structure unexploited. In addition, many encyclopedias had
multiple editions reflecting the evolution of knowledge. The lack of structure in the raw text makes
it difficult to track changes across these editions. In this work, we built a pipeline to restore
the text structure, where we extract the headwords and identify entries; categorize the entities;
match entries across editions; and link entries to a Wikidata item. We applied this pipeline to the
four major editions of \textit{Nordisk familjebok}, an authoritative Swedish encyclopedia published
between 1876 and 1951. We could extract the headwords with an F1 score of 97.8\% and we obtained an
F1 score of 93.4\% on the headword classification. On a small-scale evaluation, we reached a 93\%
precision on the cross-edition matching, 85\% precision and 16.5\% recall on the Wikidata linking.
This shows that an automated approach to digitized historical knowledge is possible. This should
facilitate the preservation of general knowledge and the understanding of knowledge transmission.
The datasets and programs are available online.

---

### 4. Geolocating News about Extreme Climate Events: A Comparative Analysis of Off-the-Shelf Tools for Toponym Identification in German

- arXiv: [2605.03414v1](https://arxiv.org/abs/2605.03414v1)
- PDF: [下载链接](https://arxiv.org/pdf/2605.03414v1)
- 作者: Brielen Madureira, Mariana Madruga de Brito, Andreas Niekler
- 发布时间: 2026-05-05T06:40:26Z
- 分类: cs.CL
- 相关性评分: 4
- 主题标签: NER工具比较、地理定位、气候事件、德语文本

**中文摘要**

> 比较Flair、Spacy和Stanza三种NER工具在德国新闻文本中识别极端气候事件地点的表现，通过下游任务评估地理定位结果差异。发现工具间的差异会传播到下游任务，影响关于文档地理焦点的决策，进而影响国家在德国媒体中的显著性结论。

**核心创新概述**

> 系统评估NER工具在极端气候事件地理定位中的差异传播影响。

**创新点拆解**

- 对比三种主流NER工具在气候变化领域的表现
- 分析NER输出差异对下游地理定位任务的影响
- 揭示工具选择对结论可靠性的潜在影响

**当前局限**

> 仅聚焦德语新闻，且任务为区域级定位；未考虑OCR噪声对NER的影响。

**后续可改进方向**

- 开发针对极端气候事件的专用NER模型
- 结合地理知识和上下文消歧提高定位准确率
- 研究OCR噪声场景下NER的鲁棒性

**工程启发**

> 为气候研究中的文本地理定位提供工具选择指导，减少分析偏差。

**为什么值得关注**

> OCR常用于新闻数字化，NER工具选择直接影响下游任务，与OCR文档分析相关。

**原始摘要**

Determining the geolocation of extreme climate events and disasters in texts is a common problem in
climate impact and adaptation research. Named-entity recognition (NER) tools are typically used to
identify a pool of toponyms that serve as candidate event locations. In this study, we conduct a
comparative analysis of three off-the-shelf NER tools, namely Flair, Spacy and Stanza. We describe
and quantify differences between their outputs for German news articles and evaluate them
extrinsically based on three methods to determine the country where events took place. We show how
their contrasts are propagated into downstream tasks and can yield distinct decisions about a
document's geographical focus, which, in turn, can impact conclusions about countries' prominence in
German media.

---
