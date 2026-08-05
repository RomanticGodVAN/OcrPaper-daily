# OCR / 文档解析研究日报（2026-08-05）

## 报告说明

- 检索源：arXiv API
- 检索查询：`(all:"document parsing" OR all:"document understanding" OR all:"optical character recognition" OR all:OCR OR all:"layout analysis" OR all:"document layout analysis" OR all:"text recognition" OR all:"table recognition" OR all:"form understanding" OR all:"document intelligence" OR all:"page understanding" OR all:"scene text recognition" OR all:"handwritten text recognition" OR all:"information extraction") AND (cat:cs.CV OR cat:cs.AI OR cat:cs.CL OR cat:eess.IV)`
- 生成时间（UTC）：`2026-08-05 04:28:20`
- 大模型综合分析：`开启`

## 一、今日执行摘要

> 今日OCR与文档解析研究聚焦于基准测试、领域专用系统、VQA及鲁棒性优化。关键进展包括：孟加拉语场景文本基准BanglaWild揭示视觉误识别主导错误；化学文档解析系统MinerU.Chem集成专用模块；教育知识图谱构建利用OCR与VLM实现证据支持；ConfBench首次系统评估文档提取的置信度校准；DocTrace通过证据图提升长文档VQA性能；GUI-Lens利用OCR实现GUI接地；解耦评估框架ZeroSense为视觉-文本压缩提供更可靠度量；层级别鲁棒性分析指导适配器放置；ET-Prune通过证据感知动态预算优化token剪枝；手写识别误差评估新方法适用于无地面真值档案。

## 二、今日趋势判断

今日研究趋势显示：1) 基准测试向多语言、低资源及特定领域（如化学）扩展，并引入细粒度错误分析；2) VLM在文档解析中的置信度评估与校准成为新焦点，旨在提升可靠性；3) 视觉token剪枝与压缩评估强调保留文本关键信息；4) 长文档VQA转向可解释的证据图推理；5) 鲁棒性研究开始关注层级别机制，以指导实际修复策略。

## 三、今日论文概览

1. **BanglaWild: An In-the-Wild Bengali Scene Text Recognition Benchmark for OCR and Vision-Language Models** | 标签：场景文本识别、基准测试、多模态模型
2. **MinerU.Chem: A High-Precision System for Optical Chemical Structure and Reaction Recognition** | 标签：化学文档解析、分子结构识别、文档解析系统
3. **Evidence-Grounded Multimodal Knowledge Graph Construction for Multi-Lecture Educational Reasoning** | 标签：知识图谱、多模态学习、教育技术
4. **Can You Trust the Confidence? ConfBench for Vision-Language Models on Document Extraction** | 标签：置信度校准、文档信息提取、视觉语言模型
5. **DocTrace: Towards Traceable Long Document VQA via Hierarchical Evidence Graph Reasoning** | 标签：视觉问答、证据图、多模态大模型
6. **GUI-Lens: Coarse-to-Fine Cropping for GUI Grounding with General-Purpose VLMs** | 标签：GUI接地、视觉语言模型、OCR应用
7. **Decoupling semantics from vision: A framework for faithful visual-text compression evaluation** | 标签：视觉-文本压缩、评估框架、MLLM、基准测试
8. **Sensitivity, Causality, and Repair Dissociate: A Layer-Wise Analysis of Perturbation Robustness and Its Scaling** | 标签：鲁棒性、层级别分析、扰动、适配器修复
9. **ET-Prune: Evidence-Aware Dynamic Budgeting for Visual Token Pruning in Text-Rich MLLMs** | 标签：视觉token剪枝、多模态LLM、文本密集、证据分配
10. **A machine-readable catalogue of the Tsiolkovsky papers (fond 555, Archive of the Russian Academy of Sciences), and a way to measure how well its handwriting can be read** | 标签：手写识别、档案数字化、OCR评估、无地面真值

## 四、今天 OCR / 文档解析论文里的主要创新点

- 多篇研究在评估中采用细粒度错误分类或分层证据结构，提升可解释性。
- 利用OCR或视觉信息作为辅助参考，增强VLM在特定任务（如GUI接地、教育推理）的定位能力。
- 针对无地面真值或低资源场景，提出创新的评估方法（如手写-打字稿配对比较）。
- 动态预算或证据分配机制用于优化视觉token处理，在保持性能的同时降低计算成本。
- 结合多种模态（视觉、文本、语音）构建知识图谱或基准，实现更全面的文档理解。

## 五、后续 OCR 领域值得推进的改进方向

- 扩展多语言场景文本基准到更多低资源语言，并改进视觉特征提取以减少视觉误识别。
- 开发更精确的化学结构识别模型，提升复杂反应方案解析精度，并扩展到更多格式。
- 优化教育知识图谱的锚点选择和证据验证机制，并验证到更多学科。
- 改进VLM置信度校准方法，探索后处理校准在更多任务上的适用性。
- 增强DocTrace对低质量文档的鲁棒性，优化证据定位算法，扩展文档类型。
- 优化GUI-Lens裁剪策略以减少计算成本，并结合语义信息提升指令跟随能力。
- 完善视觉-文本压缩的解耦评估框架，扩展基准覆盖更多任务和模态。
- 进一步研究扰动传播机制，探索更有效的适配器放置策略。
- 将证据感知动态预算扩展到更大模型和更多下游任务，并进行统计显著性验证。
- 提高手写识别模型精度，并探索其他无地面真值场景下的误差评估方法。

## 六、工程落地启发

- ConfBench的ECARB指标可用于优化人工审核资源分配，降低运营成本。
- DocTrace的分层证据图框架可直接应用于长文档问答系统，提升可追溯性。
- ET-Prune在OCRBench-v2上展示性能优势，适合文本密集场景的推理加速。
- GUI-Lens与GPT-5.5结合实现SOTA，可用于GUI智能体的开发。
- MinerU.Chem作为平台模块，便于集成到现有文档解析流程中。
- 鲁棒性层级别分析规则（如默认最深放置适配器）可直接用于模型修复实践。
- ZeroSense基准为VTC方法提供更可靠的评估，指导压缩算法优化。
- BanglaWild为孟加拉语OCR提供了标准测试平台，便于系统对比。

## 七、优先关注论文

- **BanglaWild: An In-the-Wild Bengali Scene Text Recognition Benchmark for OCR and Vision-Language Models**：首个孟加拉语场景文本基准，揭示VLM和OCR的误差模式，后续可能影响其他低资源语言的基准构建。
- **Can You Trust the Confidence? ConfBench for Vision-Language Models on Document Extraction**：首次系统评估文档提取的置信度校准，提出的ECARB指标对部署可靠性有直接价值。
- **DocTrace: Towards Traceable Long Document VQA via Hierarchical Evidence Graph Reasoning**：通过证据图实现长文档VQA的可追溯性，性能提升明显，或成多模态推理新范式。
- **ET-Prune: Evidence-Aware Dynamic Budgeting for Visual Token Pruning in Text-Rich MLLMs**：动态预算剪枝在文本密集场景中保持质量并降低计算，适合实际部署。
- **Sensitivity, Causality, and Repair Dissociate: A Layer-Wise Analysis of Perturbation Robustness and Its Scaling**：层级别鲁棒性分析提供了适配器放置的具体指导，对模型修复有直接工程价值。

## 八、论文逐篇解析

### 1. BanglaWild: An In-the-Wild Bengali Scene Text Recognition Benchmark for OCR and Vision-Language Models

- arXiv: [2608.03884v1](https://arxiv.org/abs/2608.03884v1)
- PDF: [下载链接](https://arxiv.org/pdf/2608.03884v1)
- 作者: Sadab Shiper, Tawsif Tashwar Dipto, Mir Md Inzamam, Eshat Tanzeem
- 发布时间: 2026-08-04T16:20:53Z
- 分类: cs.CV, cs.CL
- 相关性评分: 29
- 主题标签: 场景文本识别、基准测试、多模态模型

**中文摘要**

> 本文提出了BanglaWild基准，包含2535张孟加拉语场景文本图像，以及逐字转录、类别轴、诊断属性和标准拼写。评估了15个VLM和3个传统OCR系统，采用三种提示策略和LLM作为裁判的评估。发现同一家族中较大模型并不优于较小模型；视觉误识别占强系统错误约60%，连字相关错误不足2%，挑战了传统假设。提示语言影响跨脚本漂移，LoRA可减少弱模型的灾难性失败但不提升强模型上限。

**核心创新概述**

> 首次对孟加拉语场景文本识别进行系统基准测试，同时评估VLM和传统OCR，并引入细粒度错误分类。

**创新点拆解**

- 构建了包含多维度标注的野外孟加拉语场景文本基准
- 同时评估VLM和OCR系统，并采用LLM-as-a-Judge评估
- 提出十五类错误分类体系，揭示视觉误识别主导错误

**当前局限**

> 数据集规模有限，主要针对孟加拉语，可能不适用于其他低资源语言。

**后续可改进方向**

- 扩展基准到更多语言和复杂场景
- 改进视觉特征提取以减少视觉误识别
- 研究结合语言模型进行拼写纠正

**工程启发**

> 为孟加拉语OCR和VLM的性能评估提供了标准基准，有助于开发更鲁棒的场景文本识别系统。

**为什么值得关注**

> 直接涉及场景文本识别基准构建和模型评估，对OCR研究有重要参考价值。

**原始摘要**

In-the-wild Bengali scene text recognition is largely unmeasured: existing resources target
handwritten documents or constrained sign-board parsing, report only aggregate edit-distance
metrics, and evaluate either conventional OCR or VLMs, never both on the same in-the-wild data. To
address this gap, we introduce BANGLAWILD, a benchmark of 2,535 Bengali scene text images, each
paired with a verbatim gold transcription, two categorical axes, four diagnostic attributes, and an
orthographically standard form where the in-image text deviates from canonical spelling. We evaluate
fifteen VLMs and three conventional OCR systems under three prompting strategies, fine-tune 6 open-
source models with LoRA, and complement edit-distance metrics with an LLM-as-a-Judge evaluation. Our
results reveal a persistent gap in which larger models within the same family do not outperform
smaller ones. Our fifteen-class error taxonomy shows that visual mis-recognition accounts for ~60%
of errors in the strongest systems, while conjunct-related errors contribute under 2%, challenging a
long-standing assumption in Bengali OCR research; the same visual dominant profile also holds across
architectures, including the one conventional baseline that reads Bengali reliably. Prompt language
mainly affects cross-script drift and LoRA reduces catastrophic failures in weak models without
lifting the ceiling on already competent ones. Code and data will be publicly released.

---

### 2. MinerU.Chem: A High-Precision System for Optical Chemical Structure and Reaction Recognition

- arXiv: [2608.03525v1](https://arxiv.org/abs/2608.03525v1)
- PDF: [下载链接](https://arxiv.org/pdf/2608.03525v1)
- 作者: Haote Yang, Jiang Wu, Jingchao Wang, Xingjian Wei, Lixin Ma, Linye Li, Chen Zhu, Xiaolong Wu, Yuheng Lu, Ziran Zhu, Junyuan Gao, Lingli Ge, Yuan Xu, Huijie Ao, QianQian Wu, Dechen Lin, Huaiyu Gu, Lu Chen, Shengxin Lu, ShaSha Wang, Yuanyuan Cao, Zhejia Yu, Ruijie Zhang, Zimai Tian, Jiaxing Sun, Yinfan Wang, Jiahe Song, Chuang Wang, Yubin Wang, Rui Nie, Hao Zheng, Bowen Jiang, Hongbin Lai, Yifan He, Chengjin Liu, Tingting Zhang, Liqun Wei, Lijun Wu, Bin Wang, Yuqiang Li, Guangyu Wang, Wei Li, Bowen Zhou, Dahua Lin, Conghui He
- 发布时间: 2026-08-04T12:09:02Z
- 分类: cs.CV
- 相关性评分: 19
- 主题标签: 化学文档解析、分子结构识别、文档解析系统

**中文摘要**

> 本文介绍了MinerU.Chem，一个集成在MinerU平台上的有机化学文献解析系统。它基于通用文档解析流程，增加了五个化学专用模块：化学相关性筛选、分子结构检测、分子标识符提取、分子结构识别和反应方案解析。核心表示CARBON保留视觉布局和化学语义，支持导出MolFile和SMILES格式。在MolRecBench-Wild子集上评估了分子结构识别模块。

**核心创新概述**

> 针对有机化学文献的专用解析系统，结合CARBON表示，能够保留化学结构和语义。

**创新点拆解**

- 集成五个化学专用模块于通用文档解析流程
- 使用CARBON表示支持视觉和语义保存
- 支持标准格式导出，便于下游应用

**当前局限**

> 摘要未给出具体性能数据，可能仅针对特定化学结构类型。

**后续可改进方向**

- 提升复杂反应方案的解析精度
- 扩展对更多化学文档格式的支持
- 引入更强大的化学结构识别模型

**工程启发**

> 为化学知识库构建和AI化学任务提供关键的数据提取工具。

**为什么值得关注**

> 专注于专业文档解析，特别是化学结构识别，是OCR技术的应用扩展。

**原始摘要**

In organic chemistry papers and patents, molecular structures, reaction schemes, and experimental
conditions are often presented as molecular structure depictions, reaction diagrams, and complex
tables or figures. Such information is difficult for general-purpose document parsing systems to
directly convert into machine-readable data. This limits data production for organic chemistry
knowledge base construction and for AI for Chemistry tasks such as reaction prediction,
retrosynthesis, condition recommendation, molecular property prediction, and drug molecule design.
This report introduces MinerU.Chem, a document parsing system for organic chemistry literature
integrated into the MinerU online platform. Built on top of MinerU's general document parsing
pipeline, MinerU.Chem adds five chemistry-specific modules: chemistry relevance filtering, molecular
structure detection, molecule identifier extraction, molecular structure recognition, and reaction
scheme parsing. Together, these modules convert organic-chemistry-related image regions in documents
into a Molecule Summary List and a Reaction Summary List. For molecular structure recognition,
MinerU.Chem uses CARBON (Complex Atomic Representation and Bonding Object Notation) as its core
representation. CARBON enables recognition results to preserve both the visual layout of the
original image and complex chemical semantics, while supporting the export of standard downstream
formats such as MolFile and SMILES. On the SMILES-evaluable subset of MolRecBench-Wild (N=2,392),
MinerU.Chem's molecular structure recognition module achieves a SMILES exact-match accuracy of
93.02%, outperforming the best evaluated comparison system, GPT-5.6-Sol (74.87%), by 18.15
percentage points. The system has been integrated into the MinerU online platform and is available
at https://mineru.net/OpenSourceTools/Extractor .

---

### 3. Evidence-Grounded Multimodal Knowledge Graph Construction for Multi-Lecture Educational Reasoning

- arXiv: [2608.03161v1](https://arxiv.org/abs/2608.03161v1)
- PDF: [下载链接](https://arxiv.org/pdf/2608.03161v1)
- 作者: Sahil Al Farib, Momota Ahsana Meem, Sheikh Redwanul Islam, Md. Tanvir Raihan
- 发布时间: 2026-08-04T05:48:05Z
- 分类: cs.AI, cs.CL
- 相关性评分: 19
- 主题标签: 知识图谱、多模态学习、教育技术

**中文摘要**

> 本文提出了一种基于证据的多模态知识图谱构建流程，用于多讲座教育推理。该流程转录讲座，选择语义锚点，应用OCR，并使用视觉语言模型提取有证据支持的概念和关系。处理了3118帧、756个转录段和559个锚点，保留了1022个概念和312个关系提及，最终得到172个规范概念和282个关系，端点覆盖率达90.38%。初步问答测试达到100%的top-1和top-3准确率。

**核心创新概述**

> 构建了一个可审计的、有证据支持的多模态教育知识图谱，整合了语音、文本和视觉信息。

**创新点拆解**

- 利用OCR和VLM从讲座视频中提取证据支持的知识
- 概念和关系通过证据验证和规范化
- 生成具有来源的知识图谱，确保可追溯性

**当前局限**

> 仅针对神经网络讲座，规模较小，尚未进行大规模验证。

**后续可改进方向**

- 扩展到更多学科和讲座类型
- 优化锚点选择和证据验证机制
- 提升知识图谱的推理能力

**工程启发**

> 为教育内容的结构化提供了自动化方法，可支持智能教育应用。

**为什么值得关注**

> 利用OCR技术从视频中提取文本信息，是OCR在多模态场景中的应用。

**原始摘要**

Lecture videos distribute knowledge across speech, slide text, diagrams, equations, and presentation
order, which transcript-only retrieval does not fully preserve. This paper presents an evidence-
grounded multimodal pipeline that transcribes lectures, selects semantic anchors, applies optical
character recognition (OCR), and uses a vision-language model to extract only concepts and typed
relationships supported by transcript, OCR, or visual evidence. Mentions are validated and
canonicalized into a provenance-rich knowledge graph. On three neural-network lectures, the pipeline
processed 3,118 frames, 756 transcript segments, and 559 anchors. It retained 1,022 concept and 312
relationship mentions, yielding 172 canonical concepts and 282 relationships with 90.38% endpoint
coverage. A preliminary three question retrieval test achieved 100% top-1 and top-3 accuracy and
100% mean top-5 recall. The contribution is an auditable construction method rather than a state-of-
the-art performance claim.

---

### 4. Can You Trust the Confidence? ConfBench for Vision-Language Models on Document Extraction

- arXiv: [2608.01792v1](https://arxiv.org/abs/2608.01792v1)
- PDF: [下载链接](https://arxiv.org/pdf/2608.01792v1)
- 作者: Priyashree Roy, Sujitha Martin, Mohammad Rostami, Spencer Romo, Renhao Xue, Bob Strahan, Diego A. Socolinsky, Boyi Xie, Md Mofijul Islam
- 发布时间: 2026-08-03T07:03:51Z
- 分类: cs.AI, cs.CL
- 相关性评分: 16
- 主题标签: 置信度校准、文档信息提取、视觉语言模型

**中文摘要**

> 本文介绍了ConfBench，第一个用于关键信息提取的校准特定基准。通过20种退化流程生成1346个变体和7万多个实体级评估，覆盖整个准确率谱。评估了四个专有和三个开放权重VLM，使用口头化和对数概率置信度估计。发现OCR+图像模态提供更准确的置信度，模型能力是主导因素，校准质量差异很大，对数概率与第一token聚合表现最佳。提出ECARB指标用于操作节省。

**核心创新概述**

> 首次构建用于校准评估的文档提取基准，系统研究了VLM置信度估计。

**创新点拆解**

- 构建包含多种退化级别的ConfBench基准
- 评估多种置信度估计方法
- 提出ECARB指标衡量操作成本节省

**当前局限**

> 主要针对关键信息提取，可能不适用于其他文档任务。

**后续可改进方向**

- 扩展基准到更多任务和语言
- 改进置信度校准方法
- 研究后处理校准在不同模型上的适用性

**工程启发**

> 帮助开发可靠的自动文档处理系统，优化人工审核资源的分配。

**为什么值得关注**

> 关注文档提取中的置信度评估，对OCR下游应用有重要影响。

**原始摘要**

Intelligent document processing (IDP) with vision-language models (VLMs) hinges on confidence scores
trustworthy enough to route extractions between automation and human review. Existing document
benchmarks are dominated by clean, high-quality samples, leaving low accuracy regions too sparse for
calibration assessment. We introduce ConfBench, the first calibration-specific benchmark for key
information extraction (KIE), built by applying 20 controlled degradation pipelines to a diverse
document set, yielding 1,346 variants and 70K+ entity-level evaluations spanning the full accuracy
spectrum. We evaluate four proprietary and three open-weight VLMs under verbalized and log-
probability confidence estimation methods across three input modalities, and find: (i) OCR+Image
modality results in more accurate confidence estimates; (ii) model capability is the dominant
factor: within the Claude family confidence quality scales monotonically with capability, while
across families parameter count is a poor predictor; (iii) calibration quality varies widely across
models, from near-perfect to severely overconfident, and per-model post-hoc correction rescales
these absolute confidence values for threshold-based routing without altering ranking-based
operational metrics; and (iv) log-probability with first-token aggregation consistently outperforms
mean-token and margin aggregations. We also introduce ECARB, a review-budget metric translating
discriminative gains into operational savings. We release ConfBench publicly to enable systematic
study of confidence estimators and calibration methods for trustworthy IDP application deployment.

---

### 5. DocTrace: Towards Traceable Long Document VQA via Hierarchical Evidence Graph Reasoning

- arXiv: [2608.03292v1](https://arxiv.org/abs/2608.03292v1)
- PDF: [下载链接](https://arxiv.org/pdf/2608.03292v1)
- 作者: Le Xiang, Zhicheng Guan, Hong Chen, Xiaocong Lin, Zhenghua Lei, Teng Hu, Bolei He, Long Zeng
- 发布时间: 2026-08-04T08:04:59Z
- 分类: cs.AI
- 相关性评分: 12
- 主题标签: 视觉问答、证据图、多模态大模型

**中文摘要**

> 本文提出了DocTrace，一个用于长文档视觉问答的分层框架，将问题显式建模为证据图推理问题。框架包括证据定位、结构化文档解析和证据图推理，采用两阶段训练：联合SFT和任务特定GRPO。在MMLongBench-Doc、LongDocURL和SlideVQA上，与Qwen3-VL-8B-Instruct相比，分别提高了14.4、11.3和11.7个百分点，并构建了可追溯的证据图。

**核心创新概述**

> 将长文档VQA转化为显式证据图推理，提高答案准确性和可追溯性。

**创新点拆解**

- 提出分层证据图推理框架DocTrace
- 采用两阶段训练，结合SFT和GRPO
- 生成具有节点级来源的证据图

**当前局限**

> 可能依赖高质量OCR结果，文档类型可能有限。

**后续可改进方向**

- 提高对低质量文档的鲁棒性
- 优化证据定位的准确率
- 扩展支持更多文档类型

**工程启发**

> 为长文档智能问答提供可解释的解决方案，具有实际应用价值。

**为什么值得关注**

> 涉及文档解析和推理，是OCR在多模态大模型中的应用。

**原始摘要**

Long Document Visual Question Answering (LongDocVQA) requires Multimodal Large Language Models
(MLLMs) to locate, integrate, and reason over heterogeneous document elements distributed across
multiple pages. Existing approaches, including end-to-end MLLMs, retrieval-augmented generation
(RAG) pipelines, and document agents, often lack explicit mechanisms to represent and verify how
grounded evidence is progressively composed during reasoning, limiting both answer accuracy and
traceability. In this paper, we cast LongDocVQA as an explicit evidence graph reasoning problem
rather than implicit answer prediction. To this end, we propose DocTrace, a hierarchical framework
that progressively performs evidence localization, structured document parsing, and evidence graph
reasoning to enable explicit evidence provenance. To effectively learn these capabilities, we
develop a two-stage training framework: joint Supervised Fine-Tuning (SFT) first initializes
evidence localization and graph reasoning abilities, followed by task-specific Group Relative Policy
Optimization (GRPO) with dedicated rewards to further optimize these capabilities. Extensive
experiments on MMLongBench-Doc, LongDocURL, and SlideVQA demonstrate that DocTrace consistently
outperforms both existing open-source baselines and proprietary MLLMs. Compared with the
Qwen3-VL-8B-Instruct backbone, DocTrace achieves absolute improvements of 14.4, 11.3, and 11.7
points on the three benchmarks, respectively. Beyond competitive performance, DocTrace constructs
traceable evidence graphs with explicit node-level provenance, enabling transparent and verifiable
reasoning for long document understanding.

---

### 6. GUI-Lens: Coarse-to-Fine Cropping for GUI Grounding with General-Purpose VLMs

- arXiv: [2608.03270v1](https://arxiv.org/abs/2608.03270v1)
- PDF: [下载链接](https://arxiv.org/pdf/2608.03270v1)
- 作者: Zichuan Fu, Shirong Wang, Wenlin Zhang, Guojing Li, Yimin Deng, Jingtong Gao, Junjia Qi, Hanyu Yan, Yefeng Zheng, Xiaopeng Li, Wanyu Wang, Xian Wu, Xiangyu Zhao
- 发布时间: 2026-08-04T07:47:37Z
- 分类: cs.CV, cs.AI
- 相关性评分: 9
- 主题标签: GUI接地、视觉语言模型、OCR应用

**中文摘要**

> 本文提出了GUI-Lens，一个用于GUI接地任务的从粗到细框架。它利用通用视觉语言模型，通过OCR和UI组件检测提供坐标参考，逐步裁剪并放大视图以确定目标。在四个GUI接地基准上，与GPT-5.5配合达到最高24.9个百分点的提升，实现了最先进性能。

**核心创新概述**

> 通过主动观察和迭代裁剪来解决GUI接地中的精确定位问题，而非直接预测点击。

**创新点拆解**

- 提出从粗到细的GUI接地框架
- 利用OCR和UI组件位置作为坐标参考
- 迭代裁剪和放大以增强视觉细节

**当前局限**

> 依赖OCR和UI检测的准确性，可能对小型UI元素不够有效。

**后续可改进方向**

- 优化裁剪策略以减少计算成本
- 结合语义信息提升指令跟随能力
- 适应更多样化的GUI环境

**工程启发**

> 提升GUI智能体的可靠性，推动自动化界面操作的应用。

**为什么值得关注**

> 使用OCR技术提取屏幕文本，实现精确的GUI理解和操作。

**原始摘要**

GUI grounding maps natural-language instructions to click locations and is essential for reliable
GUI agents. The task remains difficult on high-resolution, densely populated interfaces because a
vision-language model (VLM) may recognize a requested control without locating it precisely enough
for interaction. Most existing methods provide various forms of localization assistance, but still
rely on a direct click prediction, allowing visual ambiguity or an inaccurate initial estimate to
propagate to the final result. In this paper, we introduce GUI-Lens, a coarse-to-fine grounding
framework that allows a general-purpose VLM to determine the target through active visual
observations. Specifically, GUI-Lens extracts OCR text and detected UI components from the
screenshot and presents their positions as coordinate references. Using the instruction, the current
view, and these references, the VLM selects the region and scale of the next view, which is cropped
and enlarged to provide finer visual details. This process continues over successively focused views
until the target is determined. Proposed crops and clicks are checked against the instruction
throughout the process, and the final local position is mapped back to the original screen
coordinates. Experiments on four GUI grounding benchmarks and three general-purpose VLM backends
show that GUI-Lens improves overall grounding accuracy by up to 24.9 percentage points and achieves
state-of-the-art performance with GPT-5.5.

---

### 7. Decoupling semantics from vision: A framework for faithful visual-text compression evaluation

- arXiv: [2608.01848v1](https://arxiv.org/abs/2608.01848v1)
- PDF: [下载链接](https://arxiv.org/pdf/2608.01848v1)
- 作者: Yonghan Gao, Zehong Chen, Lijian Xu, Jingzhi Chen, Jingwei Guan, Xingyu Zeng
- 发布时间: 2026-08-03T07:56:43Z
- 分类: cs.CV
- 相关性评分: 9
- 主题标签: 视觉-文本压缩、评估框架、MLLM、基准测试

**中文摘要**

> 针对视觉-文本压缩（VTC）方法（如DeepSeek-OCR）的评估问题，本文指出传统基于下游任务性能的评估无法准确衡量文本保留质量，原因在于多模态大语言模型（MLLMs）强大的语言先验会掩盖压缩损失。为此，提出解耦评估框架及ZeroSense Benchmark，通过降低测试样本的语义相关性，使评估结果纯粹反映VTC质量。实验表明VTC质量与下游任务准确率存在显著差异，证明了解耦评估的必要性。

**核心创新概述**

> 首次提出解耦MLLM语义推理能力与VTC质量评估的框架，并构建低语义相关性的ZeroSense基准，突破传统下游任务评估的局限。

**创新点拆解**

- 提出解耦评估框架，将VTC质量与MLLM语义推理能力分离
- 构建ZeroSense Benchmark，确保测试样本低语义相关性
- 通过多数据集实验揭示VTC质量与下游任务准确率的显著差异

**当前局限**

> ['基准构建可能受限于数据选择，低语义相关性样本的生成难度较高', '解耦框架的有效性依赖基准设计的合理性，需进一步验证其通用性']

**后续可改进方向**

- 扩展基准覆盖更多任务类型和模态，增强评估全面性
- 探索更精细的语义相关性控制方法，提升基准的敏感性

**工程启发**

> 为VTC方法的开发提供更可靠的评估工具，有助于优化压缩算法，推动长上下文多模态建模的工程实践。

**为什么值得关注**

> 直接关系到OCR相关的视觉文本压缩技术质量评估，对提升OCR系统性能具有指导意义。

**原始摘要**

Recent visual-text compression (VTC) methods, typified by DeepSeek-OCR, report impressive high token
compression ratios for long-context modeling tasks by leveraging text-to-image rendering. However,
existing evaluation protocols heavily rely on downstream task performance. Such evaluation metrics
fail to accurately measure text preservation due to the strong inherent linguistic priors of
Multimodal Large Language Models (MLLMs). In this work, we introduce a new evaluation framework that
decouples MLLMs' capabilities to faithfully assess VTC quality. Within this framework, we further
introduce the ZeroSense Benchmark to ensure low semantic correlation of testing samples. By
eliminating textual dependencies, our benchmark guarantees that the evaluation results are purely
reflective of VTC quality, unaffected by the semantic inference capabilities of downstream models.
Extensive experiments across multiple datasets demonstrate that VTC quality and downstream task
accuracy diverge significantly, highlighting the necessity of our decoupled evaluation framework.

---

### 8. Sensitivity, Causality, and Repair Dissociate: A Layer-Wise Analysis of Perturbation Robustness and Its Scaling

- arXiv: [2608.03842v1](https://arxiv.org/abs/2608.03842v1)
- PDF: [下载链接](https://arxiv.org/pdf/2608.03842v1)
- 作者: Nathan Labiosa, David Buff, Ena Nayak, Erica Donno
- 发布时间: 2026-08-04T15:48:55Z
- 分类: cs.CL, cs.LG
- 相关性评分: 6
- 主题标签: 鲁棒性、层级别分析、扰动、适配器修复

**中文摘要**

> 本文从层级别角度分析语言模型对表面扰动（如OCR噪声、拼写错误）的鲁棒性，区分了敏感性、因果性和修复能力三种操作性定义，并发现这三者在层间分布上不一致。通过五模型面板识别出两种传播模式（尖峰-抑制和后期累积），并发现敏感性与因果性存在负相关。提出级联破坏机制解释该现象，并通过层扫描实验确认因果相关早期层放置适配器会损害性能。研究为鲁棒性修复提供了实际指导，如无训练LRD预筛选和默认最深放置规则。

**核心创新概述**

> 首次系统区分并实证敏感性、因果性与修复能力在层级别上的不一致性，提出级联破坏机制解释适配器放置的负面效应。

**创新点拆解**

- 提出三种层级别操作性定义并揭示其不一致性
- 识别两种扰动传播模式（尖峰-抑制和后期累积）
- 发现敏感性-因果性负相关（rho=-0.72至-0.88）
- 提出级联破坏机制解释适配器放置的负面效应

**当前局限**

> ['部分结论基于特定模型和任务，泛化性待验证', '适配器修复的绝对增益较小，实用性受限']

**后续可改进方向**

- 探索更有效的适配器放置策略，缓解级联破坏
- 扩展分析到更多模型家族和任务类型，验证传播模式的普遍性

**工程启发**

> 为OCR噪声等表面扰动的鲁棒性修复提供层级别指导，有助于提升语言模型在实际应用中的稳定性。

**为什么值得关注**

> OCR噪声是常见扰动之一，层级别鲁棒性分析对开发抗噪OCR系统具有参考价值。

**原始摘要**

When a language model fails on surface-perturbed input (typos, OCR noise, homophones), "which layer
is responsible" has three natural operationalizations: where representations diverge most
(sensitivity), where restoring clean activations recovers the prediction (causality), and where a
small adapter can repair the damage (compensatory capacity) - and we show these three layer maps
dissociate. Across a five-model panel we identify two propagation regimes - spike-and-suppress
(Phi-3.5, Gemma-2-9B) and late-accumulation (Llama-3, Mistral, Qwen2.5-7B) - and on the two models
meeting an 80% identity-patch gate, sensitivity and causality are anti-correlated (rho = -0.72 to
-0.88). Within-family scaling on Qwen2.5 (1.5B to 14B) shows the late-accumulation signature
strengthening monotonically with scale, corroborated on a second family. We propose cascade
disruption as the mechanism behind the dissociation: adapters placed at causally implicated early
layers break intact downstream computation, making diagnostic-flagged sites the worst adapter
placements. A fixed-harness layer sweep across four models (3.8-8B) confirms the core prediction on
chain-of-thought GSM8K - the flagged sites are the most damaging adapter windows on every
adjudicable model - and is sign-consistent but strongly attenuated on a multiple-choice control,
consistent with damage that compounds with generation length. The sweep yields practical guidance: a
training-free LRD pre-screen and a default-deepest placement rule, though absolute gains over no-
adapter baselines remain small. Finally, apparent gains from a representation-stability loss reverse
under an adequate generation budget - truncated chain-of-thought had been scored as empty - a
methodological warning for any intervention evaluated on chain-of-thought tasks.

---

### 9. ET-Prune: Evidence-Aware Dynamic Budgeting for Visual Token Pruning in Text-Rich MLLMs

- arXiv: [2608.01979v1](https://arxiv.org/abs/2608.01979v1)
- PDF: [下载链接](https://arxiv.org/pdf/2608.01979v1)
- 作者: Zizhong Ding, Junxian Li, Kai Liu, Shaoqiu Zhang, Xiao Xiao, Linghe Kong, Yulun Zhang
- 发布时间: 2026-08-03T09:42:34Z
- 分类: cs.CV, cs.CL
- 相关性评分: 6
- 主题标签: 视觉token剪枝、多模态LLM、文本密集、证据分配

**中文摘要**

> 针对文本密集型多模态大语言模型中视觉token剪枝的问题，本文提出ET-Prune框架，将剪枝视为证据分配。通过解码器侧部分查询-键块获取问题条件化证据，保护文本类空间区域，并将证据不确定性和密度转换为样本特定token下限。三个渐进中间层事件驱动序列接近该预算，对分散或密集文本证据保留更多token，对集中证据更激进剪枝。实验显示在约一半token下，ET-Prune在六个骨干基准比较中领先或持平，并在OCRBench-v2上取得优势，表明证据感知动态预算的有效性。

**核心创新概述**

> 首次提出证据感知的动态预算机制用于视觉token剪枝，针对文本密集场景优化，区别于固定比例剪枝。

**创新点拆解**

- 提出证据分配视角的剪枝框架，将剪枝转化为证据分配问题
- 设计问题条件化证据提取机制，利用解码器部分查询-键块
- 引入证据不确定性和密度动态确定token预算
- 通过渐进中间层事件实现预算调整

**当前局限**

> ['依赖单次确定性推断，估计可能存在偏差', '实验观察基于点估计，缺乏统计显著性验证']

**后续可改进方向**

- 探索多次采样或不确定性量化，提升估计可靠性
- 扩展至更多下游任务和模型，验证动态预算的普适性

**工程启发**

> 为文本密集场景下的多模态推理提供高效剪枝方案，在保持质量的同时显著降低计算成本，利于实际部署。

**为什么值得关注**

> OCR场景常涉及文本密集图像，该剪枝方法直接提升此类任务的推理效率。

**原始摘要**

Visual token pruning reduces the inference cost of multimodal large language models, but a fixed
token ratio is poorly matched to text-rich inputs. In OCR-centric tasks, decisive evidence can be a
small number, label, or field whose relevance is specified by the question; indiscriminate pruning
can erase that evidence while retaining visually salient but irrelevant regions. We present ET-
Prune, a training-free framework that casts pruning as evidence allocation. It derives question-
conditioned evidence from a decoder-side partial query-key block, safeguards text-like spatial
regions, and converts evidence uncertainty and density into a sample-specific token floor. Three
progressive middle-layer events then move the sequence toward this budget, retaining more tokens for
diffuse or text-dense evidence and pruning concentrated evidence more aggressively. At the observed
point estimates from one deterministic pass per configuration, ET-Prune leads or ties among pruned
methods in all six backbone-benchmark comparisons at roughly half tokens. On OCRBench-v2, it leads
the strongest pruned baselines by 1.80 and 0.68 percentage points on Qwen3-VL-8B and InternVL3.5-8B,
respectively, while retaining about half of the visual tokens; on MMBench v1.1, it reaches 0.8467
circular exact-matching accuracy versus 0.8437 for Vanilla at 54.45% average visual-token retention.
These results show a favorable observed quality-cost trade-off for evidence-aware dynamic budgeting
in text-rich multimodal inference.

---

### 10. A machine-readable catalogue of the Tsiolkovsky papers (fond 555, Archive of the Russian Academy of Sciences), and a way to measure how well its handwriting can be read

- arXiv: [2608.03617v1](https://arxiv.org/abs/2608.03617v1)
- PDF: [下载链接](https://arxiv.org/pdf/2608.03617v1)
- 作者: Vladimir Beskorovainyi
- 发布时间: 2026-08-04T13:08:03Z
- 分类: cs.CL, cs.CV, cs.DL
- 相关性评分: 2
- 主题标签: 手写识别、档案数字化、OCR评估、无地面真值

**中文摘要**

> 本文描述了齐奥尔科夫斯基个人档案（fond 555）的机器可读目录构建，包括2019个文件和51008页扫描的分类、日期标注及手写/打字稿分类，并生成了部分机器转录。由于档案无地面真值，提出利用同一文本的手写稿和打字稿对来评估手写识别误差的方法。通过比较配对转录，中位词级一致率为37%，且在两个有出版版本的档案上验证了误差估计的无偏性和页面排序准确性。该研究为无法获取地面真值的档案手写识别提供了一种评估途径。

**核心创新概述**

> 针对无地面真值档案的手写识别评估，首次提出利用同文本双版本（手写和打字）比较来量化误差。

**创新点拆解**

- 构建了完整的档案机器可读目录，包括文件分类和日期标注
- 提出基于手写-打字稿配对比较的识别误差评估方法
- 在部分档案上验证了方法的无偏性和排序准确性

**当前局限**

> ['评估方法依赖文本的双版本存在，适用范围受限', '转录质量仍较低（词级一致率37%），影响实际使用']

**后续可改进方向**

- 提升手写识别模型精度，扩大转录覆盖
- 探索其他无地面真值场景下的误差评估方法

**工程启发**

> 为历史档案数字化提供数据目录和评估工具，有助于手写文本的检索和分析，对档案管理有实用价值。

**为什么值得关注**

> 涉及手写文本识别（OCR/HTR）的质量评估，对提升特定领域识别应用具有参考意义。

**原始摘要**

The personal archive of Konstantin Tsiolkovsky (1857-1935) is held as fond 555 of the Archive of the
Russian Academy of Sciences. The archive scanned the fond and published the images, but with no
queryable catalogue, no full-text search and no dataset: the holdings can only be browsed one page
at a time. This paper describes a machine-readable catalogue of all 2,019 files and 51,008 scans, a
dating for 1,969 files taken from the archive's own descriptions, a page-level classification of
every scan into handwriting and typescript, and a growing corpus of machine transcriptions
(currently 322 files, 5,454 scans). It also reports a way to measure handwritten-text-recognition
accuracy in an archive with no ground truth. Archives of the typewriter era often preserve one text
twice, as manuscript and as a typed copy; transcribing both and comparing isolates the reading
error, since source and pipeline are identical and only page difficulty differs. Across 294 such
pairs from 27 files, two readings of a handwritten page agree on a median 37% of words. On two files
that also have a published edition the estimate can be checked against ground truth: it is unbiased
to within a percentage point and ranks pages as the truth does (rank correlation 0.92 where the
edition is a faithful witness). This bounds use: two variants of one work here share 19% of words,
below the rate at which two readings of a single page agree, so the redactions cannot be collated
word by word at this quality. That negative result is reported as such, and the constraint is built
into the tool.

---
