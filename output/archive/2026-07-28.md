# OCR / 文档解析研究日报（2026-07-28）

## 报告说明

- 检索源：arXiv API
- 检索查询：`(all:"document parsing" OR all:"document understanding" OR all:"optical character recognition" OR all:OCR OR all:"layout analysis" OR all:"document layout analysis" OR all:"text recognition" OR all:"table recognition" OR all:"form understanding" OR all:"document intelligence" OR all:"page understanding" OR all:"scene text recognition" OR all:"handwritten text recognition" OR all:"information extraction") AND (cat:cs.CV OR cat:cs.AI OR cat:cs.CL OR cat:eess.IV)`
- 生成时间（UTC）：`2026-07-28 04:26:29`
- 大模型综合分析：`开启`

## 一、今日执行摘要

> 今日论文聚焦视觉语言模型（VLM）在文档理解中的幻视问题与一致性挑战，揭示了低CER不足以衡量语义保真度，并提出多种新框架：通过认知解耦改善VLM在复杂布局上的注意力，利用无区域标签的引用-检索提升证据归因，以及统一关系抽取中的逻辑一致性。同时，流模型训练方法、低资源语言OCR融合和无监督古代语言学习也提供了工程实用进展。

## 二、今日趋势判断

VLM用于文档OCR和理解时，隐藏的系统性失效模式（如幻视、归因错误、注意力沉没）成为研究重点，推动超越传统字符级指标的评估框架发展。同时，GRPO等强化学习方法被用于优化信息抽取和归因，无需密集标注。文档级关系抽取走向逻辑一致性约束，低资源语言和多模态融合也持续受关注。

## 三、今日论文概览

1. **When Low CER is Not Enough: An Analysis of Hallucinations in Vision-Language OCR Systems on Historical Uruguayan Documents** | 标签：VLM、历史档案OCR、幻视、评估指标、命名实体
2. **CONSISTRE: A Unified Consistency-Aware Framework for Document-Level Relation Extraction with Large Language Models** | 标签：DocRE、LLM、一致性约束、知识蒸馏、GRPO
3. **Evidence Attribution in Visual Document Understanding without Coordinates or Region Labels** | 标签：视觉文档理解、证据归因、VLM、GRPO、布局分析
4. **DeCoRAG: Cognitive Decoupling and Semantic-Aware Cropping for Complex Document Understanding** | 标签：多模态RAG、文档理解、注意力机制、图RAG、语义锚点
5. **FlowCTS: On-policy Continuous Trajectory Supervision of Flow Models** | 标签：流模型、轨迹监督、蒸馏、文本生成、图像生成
6. **Token-Region Guided Cross-Attention Fusion for Multimodal Affect Interpretation** | 标签：多模态融合、低资源语言、政治意图检测、OCR、注意力机制
7. **From transcription to semantic corpus analysis: unsupervised learning of sentence representations for ancient languages** | 标签：无监督学习、句子表示、古代语言、文本复用识别、ATR/HTR噪声

## 四、今天 OCR / 文档解析论文里的主要创新点

- 多篇论文利用GRPO进行训练：CONSISTRE用于关系抽取，Evidence Attribution用于证据归因。
- 多篇论文关注幻视问题：历史档案OCR中命名实体幻视，文档理解中归因幻视。
- 多篇论文提出认知解耦或双轨框架：DeCoRAG和CONSISTRE分别通过宏观语义锚点和双轨一致性应对复杂文档。
- 多篇论文强调超越字符级指标：历史档案论文和证据归因论文共同指出标准准确率不足以衡量语义保真度。
- 多篇论文针对低资源或古代语言：孟加拉语OCR和无监督古代语言句子表示。

## 五、后续 OCR 领域值得推进的改进方向

- 开发融合语义可靠性（如命名实体准确率、逻辑一致性）的OCR评估框架，替代传统CER/WER。
- 设计针对VLM幻视的系统抑制方法，例如通过对比学习或受限解码减少拼写规范化和虚假内容生成。
- 将认知解耦的图RAG管线（DeCoRAG）扩展至表格、多栏等更复杂布局，并优化语义锚点生成策略。
- 在更多跨领域文档（如法律、医疗）上验证关系抽取的一致性约束，并研究动态约束权重。
- 探索证据归因中更精细的检索策略和无需区域标签的训练方法，以覆盖更多文档类型。
- 将流模型连续轨迹监督（FlowCTS）应用于OCR文本生成任务，如手写识别或版面恢复。
- 扩展低资源语言融合框架至更多语言，并研究无监督域适应以提升泛化能力。
- 结合部分标注数据或主动学习，提升古代语言无监督句子表示的语义质量，并应用于主题建模等任务。

## 六、工程落地启发

- 采用语言接口（引用原文+检索）替代坐标接口进行证据归因，可显著提升召回率并降低幻视，且无需区域标注。
- 在历史档案数字化选型时，必须设置额外的语义保真度测试（如命名实体检查），不能仅依赖CER/WER。
- 部署VLM做复杂文档理解时，可用语义锚点+区域感知裁剪缓解注意力沉没，提升准确性与效率。
- 黑盒LLM在文档级关系抽取中可通过约束提示+自反思保证一致性，应用成本低。
- GRPO方法可用于小模型蒸馏，同时优化抽取性能和逻辑一致性，适合资源受限环境。

## 七、优先关注论文

- **When Low CER is Not Enough: An Analysis of Hallucinations in Vision-Language OCR Systems on Historical Uruguayan Documents**：揭示了VLM在历史档案OCR中的幻视模式，可能影响其他专业领域（如医疗、法律）的部署评估标准。
- **CONSISTRE: A Unified Consistency-Aware Framework for Document-Level Relation Extraction with Large Language Models**：统一处理逻辑一致性的框架，可推广至信息抽取下游任务，提升LLM输出可信度。
- **Evidence Attribution in Visual Document Understanding without Coordinates or Region Labels**：提出无需区域标签改善归因的实用方法，降低标注成本，对文档智能系统有直接工程价值。
- **DeCoRAG: Cognitive Decoupling and Semantic-Aware Cropping for Complex Document Understanding**：解决VLM在密集布局中的注意力沉没问题，对RAG系统优化有重要启发。

## 八、论文逐篇解析

### 1. When Low CER is Not Enough: An Analysis of Hallucinations in Vision-Language OCR Systems on Historical Uruguayan Documents

- arXiv: [2607.24077v1](https://arxiv.org/abs/2607.24077v1)
- PDF: [下载链接](https://arxiv.org/pdf/2607.24077v1)
- 作者: Marina Gardella, Camilo Mari{ñ}o, Diego Belzarena, Ignacio Ram{í}rez, Gregory Randall, Jean-Michel Morel
- 发布时间: 2026-07-27T07:19:00Z
- 分类: cs.CV, cs.LG, eess.IV
- 相关性评分: 20
- 主题标签: VLM、历史档案OCR、幻视、评估指标、命名实体

**中文摘要**

> 论文研究了视觉语言模型在乌拉圭历史档案OCR中的应用，发现尽管CER/WER指标优于传统系统，但存在幻视问题（如拼写规范化、虚假内容生成、语义替换），尤其影响命名实体，导致语义失真。表明标准字符级准确率不足以衡量转录保真度。

**核心创新概述**

> 揭示了VLM在历史档案OCR中隐藏的系统性失效模式，挑战了以低CER/WER作为充分性能指标的观点。

**创新点拆解**

- 系统对比VLM与传统OCR在历史档案上的表现
- 定性分析发现VLM独有的幻视错误类型（正交规范化、虚假内容、语义替换）
- 强调命名实体错误对语义保真度的关键影响

**当前局限**

> 仅基于单数据集（Berrutti）分析，对VLM模型种类覆盖有限。

**后续可改进方向**

- 开发超越字符级准确率的评价框架，融合语义可靠性指标
- 针对命名实体设计专门的鲁棒性评估
- 探索抑制VLM幻视觉的系统方法

**工程启发**

> 为历史档案数字化选型/评估标准提供警示，强调不能仅依赖CER/WER指标。

**为什么值得关注**

> 直接关联OCR领域对VLM的评估问题，指出当前主流指标盲区。

**原始摘要**

Optical Character Recognition (OCR) is a key component in the digitization of historical archives.
Recently, Vision-Language Models (VLMs) have emerged as strong alternatives to traditional OCR
systems, achieving state-of-the-art performance on standard benchmarks. However, their suitability
for archival transcription remains insufficiently understood. In this work, we benchmark traditional
OCR systems and VLM-based approaches on the Berrutti dataset, a challenging collection of Uruguayan
dictatorship-era documents derived from microfilm scans. While VLMs consistently outperform
traditional methods in terms of Character Error Rate (CER) and Word Error Rate (WER), we show that
these improvements hide a more complex picture. Through a detailed qualitative analysis, we uncover
systematic failure modes that are invisible to standard metrics, including orthographic
normalization, spurious content generation, and semantic substitutions that preserve fluency while
altering meaning. Errors affecting named entities are particularly critical, as they can introduce
substantial semantic distortions with minimal impact on CER and WER. These findings reveal a
critical gap between quantitative OCR performance and transcription fidelity in real-world archival
settings, and highlight the need for evaluation frameworks that go beyond character-level accuracy
to capture the semantic reliability of generated transcriptions.

---

### 2. CONSISTRE: A Unified Consistency-Aware Framework for Document-Level Relation Extraction with Large Language Models

- arXiv: [2607.24312v1](https://arxiv.org/abs/2607.24312v1)
- PDF: [下载链接](https://arxiv.org/pdf/2607.24312v1)
- 作者: Mingxuan Sun
- 发布时间: 2026-07-27T11:56:29Z
- 分类: cs.CL
- 相关性评分: 16
- 主题标签: DocRE、LLM、一致性约束、知识蒸馏、GRPO

**中文摘要**

> 提出CONSISTRE框架，用于文档级关系抽取中保持三元组的逻辑一致性（如传递性、对称性）。包含两条路径：黑盒LLM推理时通过约束提示和迭代自反思优化；小模型通过知识蒸馏+GRPO对齐，用复合奖励联合优化抽取性能和一致性。在DocRED上超越基线。

**核心创新概述**

> 首次统一处理文档级关系抽取中的逻辑一致性问题，适用于黑盒与可调优场景。

**创新点拆解**

- 提出双轨一致性框架（推理时/训练时）
- 黑盒LLM推理时采用约束感知提示+验证+自反思
- 小模型通过蒸馏+GRPO联合优化抽取与一致性

**当前局限**

> 仅验证于DocRED数据集，未在更多复杂场景测试。

**后续可改进方向**

- 扩展到更多跨领域文档（如法律、医疗）
- 研究更高效的一致性约束形式
- 探索动态约束权重而非固定奖励

**工程启发**

> 可提升LLM在信息抽取领域输出的可靠性与可信度。

**为什么值得关注**

> 文档分析与抽取是OCR下游任务，一致性处理对结构化输出至关重要。

**原始摘要**

Document-level relation extraction (DocRE) aims to extract relations among multiple entities across
extended contexts while maintaining consistency across predicted triples. Although large language
models (LLMs) show remarkable reasoning capabilities in information extraction, their predictions
are typically generated independently for each candidate triple and may violate fundamental
relational constraints such as transitivity, symmetry, and functional uniqueness, leading to
contradictory and unreliable outputs. We propose CONSISTRE, a unified consistency-aware framework
for DocRE that addresses this limitation through two complementary tracks. The first operates at
inference time for black-box LLMs, combining constraint-aware prompting, constraint-based
verification, and iterative self-reflection to refine predictions without task-specific fine-tuning.
The second injects consistency knowledge into smaller open-source models via a knowledge
distillation and reinforcement learning pipeline: reasoning traces from a powerful teacher are
distilled into a student via supervised fine-tuning, followed by GRPO alignment using a composite
reward that jointly optimizes extraction performance and relational consistency. Together, the two
tracks cover both API-accessible and locally deployable scenarios under a unified consistency
formulation. Experiments on DocRED show that both tracks outperform their baselines, with the
inference-time track achieving competitive F1 using off-the-shelf black-box LLMs and the training-
time track substantially narrowing the gap between 7--8B open-source models and state-of-the-art
proprietary LLMs at a fraction of their inference cost. Ablation studies confirm that explicit
consistency modeling mitigates relational contradictions and enhances the reliability of LLM-based
DocRE across both deployment paradigms.

---

### 3. Evidence Attribution in Visual Document Understanding without Coordinates or Region Labels

- arXiv: [2607.24651v1](https://arxiv.org/abs/2607.24651v1)
- PDF: [下载链接](https://arxiv.org/pdf/2607.24651v1)
- 作者: Zhuchenyang Liu, Yao Zhang, Yu Xiao
- 发布时间: 2026-07-27T16:49:36Z
- 分类: cs.CV, cs.CL, cs.IR
- 相关性评分: 11
- 主题标签: 视觉文档理解、证据归因、VLM、GRPO、布局分析

**中文摘要**

> 提出证据归因问题：视觉文档理解中，模型即使回答正确也可能归因到错误区域（归因幻视）。研究比较坐标接口与语言接口（引用原文+检索），表明语言接口证据召回率从≤8提升至26-47且幻视减半。进一步用GRPO训练，无需区域标签即可改善归因。

**核心创新概述**

> 发现坐标接口限制模型表达证据归因能力，提出引用+检索方案并验证有效性。

**创新点拆解**

- 比较坐标接口与语言接口的证据归因性能
- 设计引用-检索管线作为评估和训练框架
- 引入无区域标签的GRPO训练方法

**当前局限**

> 基于CiteVQA子集，可能不完全代表其他文档类型。

**后续可改进方向**

- 扩展到更复杂的布局（如表格、多栏）
- 探索更精细的检索策略
- 研究不同训练方式对归因的影响

**工程启发**

> 提供无需昂贵区域标注即可改善证据归因的实用方法，降低标注成本。

**为什么值得关注**

> 证据归因是文档理解的关键环节，直接关系OCR系统输出的可解释性。

**原始摘要**

Reliable visual document understanding requires a model to attribute each answer to the evidence
regions that support it. Recent benchmarks and systems express this step through a coordinate
interface: the model outputs the coordinates of bounding boxes that mark the evidence regions in the
document. Under this interface, vision-language models often fail to identify the right regions even
when the answer is correct, a failure known as Attribution Hallucination. We present a study that
investigates whether this failure is partially limited by what the model can express through
coordinates. On a verified bilingual CiteVQA subset, we compare the coordinate interface with a
language interface in which the model outputs only text, quoting its evidence verbatim, and a
multimodal retriever returns the location of each quote as a page region proposed by a layout parser
(tables and figures are quoted through their captions or notes); the comparison is repeated over six
open vision-language models. Compared with the coordinate interface, evidence recall rises from at
most 8 points to between 26 and 47 and the hallucination rate roughly halves, with little change in
answer quality. Building on this comparison, we use the same quote-and-retrieve pipeline as a
training scaffold: because region-level evidence labels are expensive to collect for long documents,
we introduce a GRPO recipe whose reward is a judge's reading of the gold answer and crops of the
retrieved regions, training the model to quote better evidence without any region labels and raising
an 8B backbone's strict attributed accuracy from 22.4 to 33.8. These findings indicate a practical
path to improve attribution"without a coordinate interface and without costly region-level
supervision.

---

### 4. DeCoRAG: Cognitive Decoupling and Semantic-Aware Cropping for Complex Document Understanding

- arXiv: [2607.24554v1](https://arxiv.org/abs/2607.24554v1)
- PDF: [下载链接](https://arxiv.org/pdf/2607.24554v1)
- 作者: Shuo Wang, Kai Zhang, Wenyuan Huang, Yizheng Yu, Xia Liao, Junming Su, Qing Wang, Fang Xi
- 发布时间: 2026-07-27T15:28:02Z
- 分类: cs.IR, cs.CV
- 相关性评分: 11
- 主题标签: 多模态RAG、文档理解、注意力机制、图RAG、语义锚点

**中文摘要**

> 提出DeCoRAG，一种多模态图RAG管线，解决复杂文档理解中的“视觉注意力沉没”问题（VLM在高密度布局中语义丢失）。通过认知解耦：先建立宏观语义锚点，再驱动区域感知裁剪，将推理空间从密集背景转换到语义簇。在财务图表等任务上减少幻视和计算开销。

**核心创新概述**

> 揭示VLM在图表等稀疏语义场景的“视觉注意力沉没”机制，并提出认知解耦策略。

**创新点拆解**

- 发现并验证“视觉注意力沉没”现象
- 设计语义锚点+区域感知裁剪（RAP-Crop）
- 提出认知解耦的图RAG管线

**当前局限**

> 主要针对稀疏语义密集布局（如图表），需验证其他类型文档。

**后续可改进方向**

- 扩展至更多布局类型（如表格、多页文档）
- 优化语义锚点生成方式
- 探索混合检索策略提升效率

**工程启发**

> 显著提升RAG在复杂文档上的准确性和效率，减少计算开销。

**为什么值得关注**

> 结合OCR文本与视觉布局，直接提升文档理解系统鲁棒性。

**原始摘要**

Advancing multimodal retrieval-augmented generation (RAG) for complex document understanding
presents a formidable dual dilemma of accuracy and efficiency, particularly in graph RAG. Processing
structurally sparse yet visually dense layouts, such as extracting a tiny data marker from a
financial chart, often incurs computationally prohibitive token overhead while still triggering
catastrophic hallucination. However, multimodal Graph RAG pipelines rely on graph-construction
stages that assume Vision-Language Models (VLMs) can resolve sparse semantics within high-density
layouts. We challenge this assumption, revealing that forcing VLMs to localize visual evidence,
interpret semantics, and extract relations triggers a "Visual Attention Sink," a mechanism driving
catastrophic semantic loss, while full-page processing incurs massive computational overhead.
Controlled interventions verify that this failure is boundary-driven rather than content-specific
and that semantic anchoring mitigates it. To fundamentally correct this flawed paradigm, we
introduce DeCoRAG, a multimodal Graph RAG pipeline that shifts knowledge processing from coupled
visual-semantic reasoning to "Cognitive Decoupling." Rather than passively processing raw pixels,
its graph-construction stage establishes a macroscopic Semantic Anchor to neutralize the attention
sink. This anchor subsequently drives our Region-Aware Pruning and Cropping (RAP-Crop) mechanism,
shifting the reasoning space from dense, noisy backgrounds to purified, intent-driven semantic
clusters. The resulting graph supports hybrid retrieval and answer generation. Across complex
document benchmarks, DeCoRAG improves the semantic pass rate by up to 12.5 percentage points over
the strongest baseline and generalizes to DocVQA. RAP-Crop reduces offline graph-construction prompt
tokens by 40.8% without sacrificing end-to-end accuracy.

---

### 5. FlowCTS: On-policy Continuous Trajectory Supervision of Flow Models

- arXiv: [2607.24522v1](https://arxiv.org/abs/2607.24522v1)
- PDF: [下载链接](https://arxiv.org/pdf/2607.24522v1)
- 作者: Kaiyang Ye, Yuan Ge, Junxiang Zhang, Bei Li, Ziming Zhu, Haishu Zhao, Xiaoqian Liu, Chenglong Wang, Jingbo Zhu, Zhengtao Yu, Tong Xiao
- 发布时间: 2026-07-27T15:03:22Z
- 分类: cs.LG, cs.CV
- 相关性评分: 9
- 主题标签: 流模型、轨迹监督、蒸馏、文本生成、图像生成

**中文摘要**

> 提出FlowCTS，一种流模型连续轨迹监督方法，用于解决流模型后训练中的稀疏奖励和曝光偏差。通过匹配学生与参考轨迹，导出时间加权速度匹配上界。在文本到图像生成任务（GenEval、OCR、PickScore）上优于KL蒸馏和混合奖励基线。

**核心创新概述**

> 首次将连续轨迹监督应用于流模型后训练，优于现有KL蒸馏方法。

**创新点拆解**

- 提出流模型连续轨迹匹配目标（速度匹配上界）
- 多参考设置下单步监督策略
- 识别KL蒸馏中的时间监督错配问题

**当前局限**

> 仅验证于图像生成任务，未在纯文本或OCR任务本身测试。

**后续可改进方向**

- 应用于OCR文本生成等序列任务
- 探索自适应监督步数策略
- 结合更多奖励函数优化

**工程启发**

> 改进流模型蒸馏和训练效率，可提升生成质量。

**为什么值得关注**

> OCR任务常用生成模型，FlowCTS可直接应用于OCR相关的生成模型训练。

**原始摘要**

While on-policy distillation (OPD) effectively addresses sparse rewards and exposure bias in large
language model post-training, its extension to flow models remains underexplored. To this end, we
propose Flow Continuous Trajectory Supervision (FlowCTS), which matches subsequent student and
reference trajectories initialized from the same student-visited state. Using the integral relation
between trajectories and velocity fields, we derive a temporally weighted velocity-matching upper
bound and discretize it into practical objectives parameterized by the number of supervision steps.
Under a multi-reference setup, single-state FlowCTS-OPD outperforms vanilla KL-based OPD with faster
convergence. FlowCTS-OPD improves GenEval from 0.90 to 0.93, OCR from 0.90 to 0.92, and PickScore
from 22.75 to 23.06, while outperforming a mixed-reward RL baseline across all target metrics.
Further analysis reveals a clear temporal supervision mismatch in vanilla KL-based OPD arising from
its auxiliary SDE transition kernels. Beyond on-policy setting,FlowCTS also consistently outperforms
vanilla SFT , particularly on OCR, while increasing supervision steps exhibit a trade-off between
richer trajectory information and greater optimization difficulty.

---

### 6. Token-Region Guided Cross-Attention Fusion for Multimodal Affect Interpretation

- arXiv: [2607.23493v1](https://arxiv.org/abs/2607.23493v1)
- PDF: [下载链接](https://arxiv.org/pdf/2607.23493v1)
- 作者: Musa Tur Farazi, Nufayer Jahan Reza
- 发布时间: 2026-07-26T06:36:44Z
- 分类: cs.CV, cs.AI
- 相关性评分: 9
- 主题标签: 多模态融合、低资源语言、政治意图检测、OCR、注意力机制

**中文摘要**

> 提出多模态交叉注意力融合框架，用于孟加拉语网络迷因中的政治意图检测。先使用VLM提取高保真OCR文本，再通过跨模态多头注意力对齐语义token与视觉区域。在PoliMemeDecode1数据集上达到0.94 Macro-F1。

**核心创新概述**

> 针对低资源语言（孟加拉语）中OCR文本与视觉复杂交互，提出跨模态注意力融合方案。

**创新点拆解**

- 利用VLM提取噪声图像中的OCR文本
- 跨模态多头注意力融合视觉和文本特征
- 整合领域政治词典作为知识先验

**当前局限**

> 仅针对孟加拉语单一数据集，泛化性未知。

**后续可改进方向**

- 扩展到其他低资源语言
- 探索更丰富的多模态融合策略
- 研究无监督域适应方法

**工程启发**

> 为低资源语言的多模态内容分析提供有效方案，助力舆情监测。

**为什么值得关注**

> OCR后的文本理解环节，可直接用于OCR系统的语义分析下游。

**原始摘要**

Automated analysis of multimodal content on social networks has become a critical task for
understanding public sentiment and information diffusion in the digital age. However, classifying
internet memes remains computationally challenging due to the intricate interplay between visual
cues and embedded, often stylized, text, particularly in low-resource languages like Bengali
Language. This paper addresses the detection of political intent in Bengali memes by introducing
Multimodal Cross-Attention Fusion framework. We first leverage a Vision-Language Model to extract
high-fidelity OCR text from noisy meme images. Subsequently, we encode visual and textual features
and synthesize them through a cross-modal multi-head attention mechanism that aligns semantic tokens
with visual regions. We also investigate the integration of a domain-specific political lexicon as a
knowledge prior. Experimental evaluation on the PoliMemeDecode1 dataset shows that our attention-
based fusion significantly outperforms unimodal baselines and standard concatenation methods,
achieving a state-of-the-art Macro-F1 of approximately 0.94. Interpretability analyzes further
confirm that the model effectively learns to ground textual semantics in visual evidence.

---

### 7. From transcription to semantic corpus analysis: unsupervised learning of sentence representations for ancient languages

- arXiv: [2607.24542v1](https://arxiv.org/abs/2607.24542v1)
- PDF: [下载链接](https://arxiv.org/pdf/2607.24542v1)
- 作者: Th{é}otime de la Selle
- 发布时间: 2026-07-27T15:20:13Z
- 分类: cs.CL, cs.DL, cs.IR
- 相关性评分: 8
- 主题标签: 无监督学习、句子表示、古代语言、文本复用识别、ATR/HTR噪声

**中文摘要**

> 本文研究如何从自动文本识别（ATR）产生的古代语言噪声文本中，通过无监督学习获得句子表示以支持下游语义分析（如文本复用识别、对齐和语义搜索）。针对现有方法对古代语言迁移效果差的问题，作者提出了两种无监督策略：TSDAE和对比句子嵌入（CSE），它们仅利用原始句子将专用的token级语言模型适应为语料库特定的句子编码器。在拉丁语和古希腊语的圣经复用场景（包含2935个专家验证的平行文本）上，将复用识别分解为二元检测和对应检索两个任务进行评测。实验表明，自适应编码器在所有基线上均表现出色：TSDAE在大规模领域语料上检测最优，而CSE在检索上领先，且仅需4-8k条领域内原始句子即可达到最优，并在不同作品和作者间具有迁移性，包括直接对含HTR噪声的文本重新训练时也能有效处理噪声。

**核心创新概述**

> 针对古代语言缺乏标注相似性数据的问题，提出完全无监督的句子编码器适应策略，并分解文本复用识别为两个子任务进行系统评估。

**创新点拆解**

- 提出两种无监督句子表示学习方法：TSDAE和对比句子嵌入（CSE），仅利用原始句子适应古代语言模型。
- 将文本复用识别分解为二元检测和对应检索两个评估任务，更全面分析模型表现。
- 在包含HTR噪声和抄写缩写的模拟数据上评估，验证模型对噪声的鲁棒性。

**当前局限**

> 方法仅在圣经复用这一特定场景下验证，对其他类型的古代语言语义分析任务（如主题建模、实体识别）的适用性未知；无监督方法可能无法捕获更细粒度的语义关系。

**后续可改进方向**

- 探索结合部分标注数据或主动学习策略，进一步提升无监督表示的语义质量。
- 将方法扩展到更多古代语言和更广泛的语义分析任务（如语义角色标注、关系抽取）。
- 研究如何更好地处理多种类型的ATR噪声（如字词替换、删除），提高对不同噪声模式的鲁棒性。

**工程启发**

> 为数字人文领域提供了一种低成本、低数据依赖的句子表示方法，可直接应用于大规模古代语言文本的语义分析，减少对手动标注的依赖。

**为什么值得关注**

> 研究聚焦于从OCR/HTR产生的噪声文本中提取语义特征，与文档解析中下游语义理解任务紧密相关，其无监督适应策略可启发类似场景下的句子编码器优化。

**原始摘要**

Automatic Text Recognition (ATR) now supplies digital humanities with large volumes of unstructured,
heterogeneous, and often noisy text in ancient languages. Downstream semantic analysestext reuse
identification, alignment, and semantic search-rely on sentence embeddings, yet existing methods
transfer poorly to ancient languages: generic multilingual encoders underperform, specialized
language models yield anisotropic representation spaces, and labeled similarity data is unavailable.
We study two fully unsupervised strategies - TSDAE and contrastive sentence embedding (CSE) - that
adapt a specialized token-level language model into a corpus-specific sentence encoder using only
raw sentences. On the philologically central case of biblical reuse in patristic literature (2,935
expert-verified parallels in Latin and Ancient Greek, from Augustine, Jerome, and Athanasius), we
decompose reuse identification into two separately evaluated tasks-binary detection and
correspondence retrieval-and benchmark the adapted encoders against multilingual, specialized,
distilled, and supervised fine-tuned baselines, as well as on artificially noised data simulating
HTR artifacts and scribal abbreviations. The adapted encoders outperform all baselines on both
tasks, with complementary profiles: TSDAE leads detection given a large in-domain corpus, while CSE
leads retrieval, reaches its optimum with as few as 4-8k raw in-domain sentences-a few tens of
seconds of training on a laptop GPU-and transfers across works and authors, including to noisy post-
ATR text when retrained directly on it. UMAP atlases relate the geometric effect of each strategy to
the measured gains, and the full pipeline-segmentation, fine-tuning, cross-corpus semantic search-is
made available to non-specialists through the online tool Paraphrasis.

---
