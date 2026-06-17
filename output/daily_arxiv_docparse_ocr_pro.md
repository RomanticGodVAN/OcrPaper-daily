# OCR / 文档解析研究日报（2026-06-17）

## 报告说明

- 检索源：arXiv API
- 检索查询：`(all:"document parsing" OR all:"document understanding" OR all:"optical character recognition" OR all:OCR OR all:"layout analysis" OR all:"document layout analysis" OR all:"text recognition" OR all:"table recognition" OR all:"form understanding" OR all:"document intelligence" OR all:"page understanding" OR all:"scene text recognition" OR all:"handwritten text recognition" OR all:"information extraction") AND (cat:cs.CV OR cat:cs.AI OR cat:cs.CL OR cat:eess.IV)`
- 生成时间（UTC）：`2026-06-17 06:26:54`
- 大模型综合分析：`开启`

## 一、今日执行摘要

> 今日论文覆盖文档解析、OCR、表格识别、安全等领域。亮点包括：斯坦福EDGAR金融语料库（布局忠实、152B token）、布局分析半监督标签传播（10%标注达81.6%性能）、表格识别并行解码（推理加速3倍）、以及面向专业LLM的提示注入防御PARSE。整体趋势强调高效标注、领域特化预训练、安全对齐和并行解码。

## 二、今日趋势判断

文档解析领域持续向大规模、高质量预训练语料（如EDGAR、MultiMarkdown）、半监督/弱监督标注方法（如标签传播）和高效解码架构（如非因果注意力）演进；同时，LLM应用安全（如PARSE）成为工程落地关键。

## 三、今日论文概览

1. **The Stanford EDGAR Filings Dataset: Reconstructing U.S. Corporate and Financial Disclosures into Layout-Faithful and Token-Efficient Pretraining Data** | 标签：文档解析、预训练语料、金融分析、布局理解
2. **Analyzing and Encoding the Al-Mawrid Arabic-English Dictionary with the ISO Language Markup Framework and TEI Lex-0** | 标签：文档数字化、文本编码、词法资源、阿拉伯语
3. **Bounding Box Label Propagation for Re-Annotation of Document Layout Analysis Datasets** | 标签：文档布局分析、半监督学习、目标检测、伪标签
4. **IUU+DB: Tracking Illegal, Unreported, and Unregulated Fishing, Seafood Fraud, and Labor Abuse through LLM-driven Information Extraction** | 标签：信息提取、大语言模型、渔业安全、文档分析
5. **STAR: SpatioTemporal Adaptive Reward Allocation for Text-to-Image RL Post-Training** | 标签：文本到图像生成、强化学习、注意力机制、文本渲染
6. **Multiple cyclicity and Wavelet Decomposition with Channel Correlation for Long-term Time Series Forecasting** | 标签：时间序列预测、小波分解、通道相关性、序列建模
7. **PARSE: Provenance-Aware Retrieval Sanitization for Professional Domain LLM Agents** | 标签：LLM安全、提示注入防御、文档净化、专业领域、检索增强生成
8. **Revisiting Structural Dependency in Autoregressive Multi-Task Table Recognition via Order-Independent Cell-Level Representations** | 标签：表格识别、多任务学习、自回归模型、并行解码、文档分析

## 四、今天 OCR / 文档解析论文里的主要创新点

- 利用布局/结构信息提升预训练和下游任务性能（EDGAR数据集、表格识别并行解码）。
- 半监督/弱监督方法减少标注成本（边界框标签传播）。
- 高效解码架构（并行解码）替代传统自回归序列生成。
- LLM安全防御结合溯源和事实保留（PARSE）。

## 五、后续 OCR 领域值得推进的改进方向

- 构建跨领域、多语言的高质量布局忠实预训练语料库。
- 探索更鲁棒的半监督/无监督文档布局分析框架，减少标注依赖。
- 将非因果注意力扩展到更复杂的文档元素（如合并单元格、不规则表格）。
- 结合主动学习与标签传播，进一步降低工业级标注成本。
- 研究针对专业领域文档的LLM安全净化方法，平衡安全与效用。
- 开发可解释的文档元素关系建模方法，提升端到端识别性能。

## 六、工程落地启发

- EDGAR数据集为金融文档理解提供高质量开源预训练数据，可直接用于微调。
- 边界框标签传播方法可快速更新已有标注数据集，适合工业持续迭代。
- 表格识别并行解码方案可显著提升工程部署吞吐量。
- PARSE方法为企业级LLM应用提供即用的文档净化方案，降低安全风险。
- MultiMarkdown格式可作为高效文档表示，减少token消耗。

## 七、优先关注论文

- **The Stanford EDGAR Filings Dataset: Reconstructing U.S. Corporate and Financial Disclosures into Layout-Faithful and Token-Efficient Pretraining Data**：首个布局忠实的金融预训练语料，152B token，与通用语料重叠极低，极具行业应用潜力。
- **Bounding Box Label Propagation for Re-Annotation of Document Layout Analysis Datasets**：仅用10%标注数据即达全监督81.6%性能，显著降低标注成本，工程价值高。
- **Revisiting Structural Dependency in Autoregressive Multi-Task Table Recognition via Order-Independent Cell-Level Representations**：推理速度提升3倍且性能提升，直接契合高吞吐文档处理需求。
- **PARSE: Provenance-Aware Retrieval Sanitization for Professional Domain LLM Agents**：针对专业领域LLM安全的首个真实文档基准和有效防御，工程可落地性强。
- **STAR: SpatioTemporal Adaptive Reward Allocation for Text-to-Image RL Post-Training**：提升文本渲染能力，对文档生成和OCR辅助生成任务有直接帮助。

## 八、论文逐篇解析

### 1. The Stanford EDGAR Filings Dataset: Reconstructing U.S. Corporate and Financial Disclosures into Layout-Faithful and Token-Efficient Pretraining Data

- arXiv: [2606.18192v1](https://arxiv.org/abs/2606.18192v1)
- PDF: [下载链接](https://arxiv.org/pdf/2606.18192v1)
- 作者: Nick Bettencourt, Xiaowei Ding, Kay Giesecke
- 发布时间: 2026-06-16T17:22:34Z
- 分类: cs.AI
- 相关性评分: 17
- 主题标签: 文档解析、预训练语料、金融分析、布局理解

**中文摘要**

> 本文提出斯坦福EDGAR文件数据集，将SEC文件重建为布局忠实、token高效的MultiMarkdown格式，用于金融语言模型预训练和评估。数据集含152B token，与Common Crawl重叠低于0.1%，并引入两个基准：EDGAR-Forecast和EDGAR-OCR。

**核心创新概述**

> 首个将SEC官方文件系统化为布局忠实、token高效的预训练语料库，并引入金融数值预测和表格OCR评估基准。

**创新点拆解**

- 将SEC文件转换为布局忠实的MultiMarkdown格式，保留原始布局信息且token高效
- 构建152B token的公开长文本语料库，与Common Crawl重叠极低
- 提出两个基准：EDGAR-Forecast（数值预测）和EDGAR-OCR（复杂金融表格转录）

**当前局限**

> 语料库仅涵盖SEC文件，领域局限；OCR基准仅针对表格，未覆盖其他文档元素。

**后续可改进方向**

- 扩展至其他监管文件或财务报告格式
- 探索布局信息在更多下游任务中的利用
- 改进表格OCR的细粒度评估指标

**工程启发**

> 为金融领域长文本语言模型提供高质量开源预训练数据，降低数据获取成本。

**为什么值得关注**

> 直接涉及文档场景下的OCR和布局理解，且提供金融文档OCR基准。

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

### 2. Analyzing and Encoding the Al-Mawrid Arabic-English Dictionary with the ISO Language Markup Framework and TEI Lex-0

- arXiv: [2606.18205v1](https://arxiv.org/abs/2606.18205v1)
- PDF: [下载链接](https://arxiv.org/pdf/2606.18205v1)
- 作者: Diaa Fayed, Laurent Romary
- 发布时间: 2026-06-16T17:35:11Z
- 分类: cs.CL
- 相关性评分: 14
- 主题标签: 文档数字化、文本编码、词法资源、阿拉伯语

**中文摘要**

> 本文提出系统性方法对Al-Mawrid阿拉伯语-英语词典进行数字化编码，采用ISO词法标记框架和TEI Lex-0双标准，实现了91%的结构解析准确率，并讨论了TEI Lex-0在建模阿拉伯语特定现象时的局限性。

**核心创新概述**

> 首次将ISO LMF和TEI Lex-0双标准应用于阿拉伯语词典数字化，解决20世纪双语词典的结构歧义问题。

**创新点拆解**

- 采用ISO LMF和TEI Lex-0双标准编码框架，适应阿拉伯语词法特点
- 提出基于前缀的引用系统支持Linguistic Linked Open Data集成
- 实证分析词典词法知识密度，并以Ayn字母样本验证结构解析准确率91%

**当前局限**

> TEI Lex-0对阿拉伯语隐性开放集语义关系和分散形态线索建模不足；样本仅覆盖一个字母。

**后续可改进方向**

- 扩展TEI Lex-0以更好支持阿拉伯语特有现象
- 增加更多字母的样本分析以验证通用性
- 探索LLOD集成在词典检索中的应用

**工程启发**

> 为低资源阿拉伯语词法资源数字化提供可复用的方法论，支持后续NLP应用。

**为什么值得关注**

> 涉及文档数字化和文本编码标准，与文档解析基础设施相关。

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

### 3. Bounding Box Label Propagation for Re-Annotation of Document Layout Analysis Datasets

- arXiv: [2606.17644v1](https://arxiv.org/abs/2606.17644v1)
- PDF: [下载链接](https://arxiv.org/pdf/2606.17644v1)
- 作者: Nick Jochum, Tobias Alt-Veit, Christian Schön, Alexander Lück, René Schuster, Didier Stricker
- 发布时间: 2026-06-16T08:04:27Z
- 分类: cs.CV, cs.AI
- 相关性评分: 11
- 主题标签: 文档布局分析、半监督学习、目标检测、伪标签

**中文摘要**

> 本文提出边界框标签传播方法，用于文档布局分析数据集的半监督重新标注，通过集成视觉、文本和位置嵌入实现目标检测实例的伪标签传播，在D4LA数据集上用10%标注数据达到全监督性能的81.6%。

**核心创新概述**

> 首次将标签传播方法应用于目标检测实例的重新分类，解决文档布局分析中类别标注的持续更新问题。

**创新点拆解**

- 提出边界框标签传播框架用于目标检测伪标签生成
- 设计对象编码器融合视觉、文本和位置嵌入
- 在文档布局分析任务上仅用10%标注数据即达81.6%全监督性能

**当前局限**

> 依赖初始标注质量；仅验证于文档布局分析数据集，泛化性待考。

**后续可改进方向**

- 探索更鲁棒的嵌入融合策略以适应复杂文档
- 扩展到更多文档类型和布局元素
- 结合主动学习进一步减少标注成本

**工程启发**

> 显著降低文档标注更新成本，利于工业场景中数据集持续演化。

**为什么值得关注**

> 直接面向文档布局分析的标注效率提升，与OCR预处理的自动化相关。

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

### 4. IUU+DB: Tracking Illegal, Unreported, and Unregulated Fishing, Seafood Fraud, and Labor Abuse through LLM-driven Information Extraction

- arXiv: [2606.18181v1](https://arxiv.org/abs/2606.18181v1)
- PDF: [下载链接](https://arxiv.org/pdf/2606.18181v1)
- 作者: Henry Bodwell, Hong Yang, John C. Simeone, Kelvin Gorospe, Bella Sullivan, Lana Huang, Jessica Gephart, Sandy Aylesworth, Molly Masterton, Naren Ramakrishnan
- 发布时间: 2026-06-16T17:16:05Z
- 分类: cs.IR, cs.AI, cs.CY
- 相关性评分: 10
- 主题标签: 信息提取、大语言模型、渔业安全、文档分析

**中文摘要**

> 本文提出IUU+DB系统，利用大语言模型从异构文档中提取非法捕鱼、海鲜欺诈和劳工滥用事件，构建全球事件数据库，支持去重和趋势分析，案例验证表明可有效组织分散证据并定位行为热点。

**核心创新概述**

> 首次大语言模型驱动的IUU+渔业犯罪事件数据库构建，覆盖环境与供应链犯罪。

**创新点拆解**

- 定义IUU+概念涵盖更广泛的渔业犯罪
- 设计LLM驱动的异构文档信息提取流水线，包括分类、提取、去重
- 支持地理位置和行为热点分析

**当前局限**

> 依赖文档质量；LLM提取准确率可能受限；未公开数据库规模。

**后续可改进方向**

- 提升LLM提取的准确率和召回率
- 集成多语言文档处理
- 结合知识图谱增强事件关联分析

**工程启发**

> 为渔业监管、风险评估和政策实施提供自动化情报支持。

**为什么值得关注**

> 涉及从非结构化文档中提取结构化信息，与文档解析和OCR后处理相关。

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

### 5. STAR: SpatioTemporal Adaptive Reward Allocation for Text-to-Image RL Post-Training

- arXiv: [2606.17979v1](https://arxiv.org/abs/2606.17979v1)
- PDF: [下载链接](https://arxiv.org/pdf/2606.17979v1)
- 作者: Jinjie Shen, Wei Deng, Xian Hu, Daiguo Zhou, Jian Luan
- 发布时间: 2026-06-16T14:30:12Z
- 分类: cs.AI
- 相关性评分: 9
- 主题标签: 文本到图像生成、强化学习、注意力机制、文本渲染

**中文摘要**

> 本文提出时空自适应奖励分配方法，用于文本到图像生成的强化学习后训练，通过文本-图像注意力动态分配空间奖励，在GenEval、OCR文本渲染和PickScore任务上显著提升对齐性能，几乎无额外计算开销。

**核心创新概述**

> 首次在文本到图像RL后训练中引入时空自适应奖励分配，解决奖励粒度与生成过程不匹配问题。

**创新点拆解**

- 提出时空自适应奖励分配，基于文本-图像注意力动态构造空间分配图
- 在保持计算效率下将优势奖励分配给更相关的潜在区域
- 在三个任务上验证提升，包括OCR文本渲染

**当前局限**

> 仅基于Stable Diffusion 3.5 Medium验证；依赖注意力图质量。

**后续可改进方向**

- 探索更精细的时间步分配策略
- 扩展到其他基础模型和任务
- 结合更多外部奖励源改进文本对齐

**工程启发**

> 提升文本到图像生成的中文渲染和语义对齐能力，助力文档生成场景。

**为什么值得关注**

> 涉及图像中的文本渲染质量，与OCR的逆问题相关。

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

### 6. Multiple cyclicity and Wavelet Decomposition with Channel Correlation for Long-term Time Series Forecasting

- arXiv: [2606.17996v1](https://arxiv.org/abs/2606.17996v1)
- PDF: [下载链接](https://arxiv.org/pdf/2606.17996v1)
- 作者: Bin Wang, Heming Yang, Jinfang Sheng
- 发布时间: 2026-06-16T14:44:23Z
- 分类: cs.LG, cs.AI
- 相关性评分: 6
- 主题标签: 时间序列预测、小波分解、通道相关性、序列建模

**中文摘要**

> 本文提出McWC长期时间序列预测模型，分别建模周期性、趋势和通道间相关性，采用多层周期性构建、多层感知机提取通道相关、多级小波分解高低频信息，在六个真实数据集上达到最优性能且计算高效。

**核心创新概述**

> 首次将多层小波分解与通道间相关性建模结合，并解耦通道内自相关性。

**创新点拆解**

- 多层周期性构建模块显式分离周期分量
- 多层感知机提取通道间相关性
- 多级小波分解融合高低频信息
- 频域损失函数解耦通道内自相关

**当前局限**

> 仅验证于通用时间序列预测，未涉及文档或OCR相关序列。

**后续可改进方向**

- 应用到文档流或OCR置信度序列预测
- 探索更复杂的周期模式建模
- 优化小波分解的层数自适应选择

**工程启发**

> 提供高效准确的长序列预测模型，可迁移至文档处理中的时间序列任务。

**为什么值得关注**

> 虽不直接面向文档，但长期预测方法可应用于文档系统日志、OCR输出序列等。

**原始摘要**

Cyclicity and trend are important components of time series data and many studies based on cyclicity
and trend have achieved good results in long-term time series forecasting. However, we believe that
current work neglects the influence of real-world inter-channel correlations in time series data
which leads to suboptimal predictions. Furthermore, these models rely on complex designs to capture
diverse information so that resulting in low computational efficiency. To address this challenge, we
propose McWC, a long-term time series forecasting model that separately models the cyclicity, trend,
and inter-channel correlations. Specifically, McWC first decouples cyclical information from data
using a multi-layer cyclicity construction module. Then, it extracts inter-channel correlations
using multi-layer perceptron. Next, it models and fuses the multi-layer high-frequency and low-
frequency information from data using a multi-level wavelet decomposition module. Finally, it
aggregates the results of different components to obtain the output. Simultaneously, we decouple
intra-channel autocorrelations by calculating a loss function in the frequency domain. Experiments
on six real-world datasets demonstrate that McWC achieves state-of-the-art performance, exhibiting
excellent computational efficiency and historical information extraction capabilities.

---

### 7. PARSE: Provenance-Aware Retrieval Sanitization for Professional Domain LLM Agents

- arXiv: [2606.17467v1](https://arxiv.org/abs/2606.17467v1)
- PDF: [下载链接](https://arxiv.org/pdf/2606.17467v1)
- 作者: Aaditya Pai
- 发布时间: 2026-06-16T03:29:23Z
- 分类: cs.CR, cs.CL
- 相关性评分: 4
- 主题标签: LLM安全、提示注入防御、文档净化、专业领域、检索增强生成

**中文摘要**

> 针对专业领域LLM代理的提示注入防御，现有方法在合成基准上有效，但在真实文档中表现不佳。真实文档更长、更密集，且混杂合法权威语言和事实内容。研究表明，最强防御“改写”在真实文档上无显著效果（p=0.500），且降低效用。本文提出PARSE（溯源感知检索净化）方法，通过句子级别注入可能性分类、结构化事实提取和一致性检查，实现领域感知的事实保留净化。PARSE在保持接近基线效用的同时，攻击成功率降至15.6%，较基线25.4%降低38%。

**核心创新概述**

> 揭示真实文档与合成基准的关键差异，提出首个结合溯源感知和事实保留的净化管道，适用于专业领域。

**创新点拆解**

- 提出面向专业文档的溯源感知检索净化方法PARSE
- 设计直接性门控机制，将59%文档路由至轻量路径
- 构建包含金融、法律、医疗等五个专业的真实文档基准（122任务）
- 通过句子级注入分类和结构化事实提取实现领域自适应

**当前局限**

> 实验限于英文文档，未涉及多语言场景；攻击成功率仍达15.6%，高安全场景需更严格的防御。

**后续可改进方向**

- 扩展到多语言和跨领域文档类型
- 探索更精细的实体级而非句子级净化策略
- 结合对抗训练提升对未知注入模式的鲁棒性
- 设计可解释性更强的攻击模式分类机制

**工程启发**

> 为实际企业级LLM应用中的安全部署提供可落地的净化方案，平衡安全与效用。

**为什么值得关注**

> 该研究直接针对LLM在文档处理中的安全漏洞，与OCR后文本的安全利用和检索增强生成密切相关。

**原始摘要**

Prompt injection defenses evaluated on synthetic benchmarks do not generalize to real enterprise
documents, which are longer, denser, and interleave legitimate authority language with factual
content. We demonstrate this gap with a real-document benchmark of 122 tasks across five
professional domains (financial, legal, medical, scientific, DevOps) using actual SEC filings,
Federal Register rules, PubMed abstracts, arXiv papers, and GitHub postmortems. Paraphrasing, the
strongest defense on synthetic benchmarks, shows no statistically significant attack success rate
reduction on real documents (p=0.500) while degrading utility from 91.8% to 82.8%. We introduce
PARSE (Provenance-Aware Retrieval Sanitization), a domain-aware, fact-preserving sanitization
pipeline that classifies each sentence by injection likelihood, extracts structured facts before
rewriting, and verifies fact preservation via a consistency-checking loop. A directiveness gate
routes 59% of real enterprise documents to a lightweight path, concentrating computational cost on
high-risk documents. PARSE achieves 15.6% attack success rate -- a 38% reduction versus the 25.4%
baseline -- at 86.9% utility, the only condition that is both statistically significant (p=0.014,
adequately powered) and maintains near-baseline utility. Practitioners should evaluate defenses on
domain-matched real documents, not synthetic proxies.

---

### 8. Revisiting Structural Dependency in Autoregressive Multi-Task Table Recognition via Order-Independent Cell-Level Representations

- arXiv: [2606.17874v1](https://arxiv.org/abs/2606.17874v1)
- PDF: [下载链接](https://arxiv.org/pdf/2606.17874v1)
- 作者: Takaya Kawakatsu
- 发布时间: 2026-06-16T12:45:57Z
- 分类: cs.CV, cs.LG
- 相关性评分: 3
- 主题标签: 表格识别、多任务学习、自回归模型、并行解码、文档分析

**中文摘要**

> 多任务表格识别中，现有自回归解码器生成表格结构时，细胞表示依赖于序列顺序，影响全局一致性。本文提出结构精炼模块，通过非因果注意力生成顺序无关的细胞特征，实现细胞内容的并行推理，同时每个细胞以精炼特征中的全局上下文为条件。在两个大型数据集上，该方法在细胞定位和端到端识别上持续改进，推理时间减少约三倍。

**核心创新概述**

> 首次在自回归多任务表格识别中引入非因果注意力以消除顺序依赖，实现并行解码和全局上下文建模。

**创新点拆解**

- 提出结构精炼模块，通过非因果注意力生成顺序无关细胞特征
- 实现细胞内容的并行推理，同时保持全局上下文条件
- 在细胞定位和端到端识别任务中均取得一致提升
- 推理时间降低约三倍

**当前局限**

> 依赖现有自回归骨干网络，可能受限于整体架构设计；实验仅在两个数据集上验证，泛化性需进一步测试。

**后续可改进方向**

- 探索完全非自回归的表格识别架构
- 结合自监督预训练提升细胞特征的表征能力
- 扩展到更复杂的表格结构（如合并单元格、不规则布局）
- 与文档版面分析模型协同优化端到端性能

**工程启发**

> 显著提升表格识别效率（推理时间减少约三倍），适合高吞吐量文档处理场景，且不牺牲性能。

**为什么值得关注**

> 表格是OCR文档中的重要信息载体，该研究直接改进表格识别中的细胞表示和解码效率。

**原始摘要**

Multi-task table recognition jointly addresses table structure prediction, cell localization, and
cell content recognition within a unified framework. Existing approaches often rely on
autoregressive decoders to generate table structures and reuse their hidden states for cell
localization and content recognition. This autoregressive generation process can make cell
representations order-dependent, degrading global consistency across cells. This paper proposes a
structural refinement module that produces order-independent cell features through non-causal
attention. This design enables parallel inference of cell contents while conditioning each cell on
global context encoded in the refined features. Experiments on two large datasets demonstrate
consistent gains in cell localization and end-to-end recognition, while reducing overall inference
time by around threefold.

---
