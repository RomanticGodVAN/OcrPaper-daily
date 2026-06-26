# OCR / 文档解析研究日报（2026-06-26）

## 报告说明

- 检索源：arXiv API
- 检索查询：`(all:"document parsing" OR all:"document understanding" OR all:"optical character recognition" OR all:OCR OR all:"layout analysis" OR all:"document layout analysis" OR all:"text recognition" OR all:"table recognition" OR all:"form understanding" OR all:"document intelligence" OR all:"page understanding" OR all:"scene text recognition" OR all:"handwritten text recognition" OR all:"information extraction") AND (cat:cs.CV OR cat:cs.AI OR cat:cs.CL OR cat:eess.IV)`
- 生成时间（UTC）：`2026-06-26 05:21:35`
- 大模型综合分析：`开启`

## 一、今日执行摘要

> 今日的OCR/文档解析论文围绕多模态大模型鲁棒性、LLM驱动的信息抽取、图像质量门控、合成数据生成、历史文档关系抽取、多智能体审计系统等展开。核心发现包括：视觉语言模型的OCR推理易受常见图像扰动影响，分类准度不代表鲁棒性；LLM在金融文档理解中可达91%精度；轻量级模糊检测门控可有效提升预处理质量；合成数据及自家族蒸馏为实现小模型GUI推理提供了新路径。

## 二、今日趋势判断

从传统的OCR识别转向更全面的文档理解与推理，强调鲁棒性、效率与泛化能力。亮点包括：对多模态模型在扰动下行为评估的重视；基于LLM的生成式抽取管线替代传统NER；轻量级图像预处理模块（如模糊门控）走俏；自动化数据集构建（如WinDOM）与多智能体协作成为降低成本的关键方向。

## 三、今日论文概览

1. **How Robust is OCR-Reasoning? Evaluating OCR-Reasoning Robustness of Vision-Language Models under Visual Perturbations** | 标签：OCR鲁棒性、视觉扰动、视觉语言模型、评估基准
2. **LLM-Based Examination of Eligibility Criteria from Securities Prospectuses at the German Central Bank** | 标签：LLM、信息抽取、文档审核、OCR后处理
3. **Edges Before Embeddings: A Confidence-Aware Blur Gate for Vision-Language Pipelines** | 标签：图像质量评估、模糊检测、OCR预处理、轻量级模型
4. **ProfileFoundry: A Synthetic Person-Object Substrate for Privacy, Memory, and Tool-Use Evaluation in LLM Agent** | 标签：合成数据、人物对象、隐私评估、文档理解
5. **Overview of HIPE-2026: Person-Place Relation Extraction from Multilingual Historical Texts** | 标签：关系抽取、历史文档、OCR噪声、跨域泛化
6. **Probabilistic Agents in Deterministic Audits: Evaluating Multi-Agent Systems for Automated Audits Based on the German IT-Grundschutz** | 标签：多智能体系统、混合RAG、文档自动化、合规检查
7. **WinDOM: Self-Family Distillation for Small-Model GUI Grounding** | 标签：GUI grounding、数据集构建、知识蒸馏、强化学习、小型模型
8. **PhysRAG: Enhancing Physics-Awareness in Video Generation via Retrieval-Augmented Generation** | 标签：视频生成、物理感知、检索增强生成、数据过滤、扩散模型

## 四、今天 OCR / 文档解析论文里的主要创新点

- 将经典图像处理特征（如边缘检测）融入深度学习模型以提升鲁棒性或效率。
- 利用LLM进行生成式信息抽取，将复杂任务分解为多个子步骤以降低幻觉。
- 通过合成数据或自动标注方法减少对人工标注的依赖，如WinDOM和ProfileFoundry。
- 引入检索增强生成（RAG）为模型提供外部结构化知识。
- 采用多视角评估（准确率、效率、跨域泛化）来全面衡量系统性能。

## 五、后续 OCR 领域值得推进的改进方向

- 研究轻量化鲁棒增强方法，例如在模型输入前端加入自适应图像净化模块。
- 开发针对文档结构敏感的鲁棒性增强技术，以应对PDF排版变化。
- 将LLM与结构化约束（如知识图谱）结合，减少金融文档抽取中的幻觉。
- 探索跨语言、跨文档的生成式抽取泛化能力，尤其针对历史文本。
- 设计统一的图像质量门控协议，支持多种模糊类型和置信度校准。
- 提升合成数据的逼真度和多样性，使其能够替代真实数据用于下游微调。
- 发展无需外部模型的同家族蒸馏框架，简化小模型训练流程。
- 构建端到端的多智能体文档审核系统，提高全流程自动化率。
- 为视频或动态文档引入物理感知和时间推理能力。

## 六、工程落地启发

- 可直接在OCR管道前集成MagikaDocumentFromPixel（7ms/图）来过滤模糊图像，降低后续处理开销。
- 金融机构可借鉴论文2的LLM-based管线实现证券文档自动化审核。
- HIPE-2026的评估框架可用于衡量历史文档处理系统的跨域泛化能力。
- WinDOM-SFD方法适用于资源受限设备的GUI grounding，无需GPU即可生成训练数据。
- PhysRAG的RAG机制可以改进文档解析中的物理常识注入（如发票表格中的逻辑关系）。

## 七、优先关注论文

- **How Robust is OCR-Reasoning? Evaluating OCR-Reasoning Robustness of Vision-Language Models under Visual Perturbations**：系统评估了视觉扰动对VLM OCR推理的影响，提出的基准和指标可成为团队评估自研模型鲁棒性的标准工具。
- **WinDOM: Self-Family Distillation for Small-Model GUI Grounding**：创新性地利用DOM解析自动构建GUI定位数据，结合自家族蒸馏和RL，实现了无需人工/OCR的小模型训练，对部署在边缘设备有直接价值。
- **ProfileFoundry: A Synthetic Person-Object Substrate for Privacy, Memory, and Tool-Use Evaluation in LLM Agent**：提供了一种安全可控的合成人物数据生成方案，可用于评估模型在文档理解等任务中的隐私保护能力。

## 八、论文逐篇解析

### 1. How Robust is OCR-Reasoning? Evaluating OCR-Reasoning Robustness of Vision-Language Models under Visual Perturbations

- arXiv: [2606.26041v1](https://arxiv.org/abs/2606.26041v1)
- PDF: [下载链接](https://arxiv.org/pdf/2606.26041v1)
- 作者: Yuxing Cheng, Yuan Wu, Yi Chang
- 发布时间: 2026-06-24T17:15:42Z
- 分类: cs.CV, cs.CL
- 相关性评分: 22
- 主题标签: OCR鲁棒性、视觉扰动、视觉语言模型、评估基准

**中文摘要**

> 提出OCR-Robust基准，评估视觉语言模型在视觉扰动下的OCR推理鲁棒性，涵盖文档、场景文本、图表等8种类型，发现高准确率不一定意味着强鲁棒性，图表类比文档类更脆弱。

**核心创新概述**

> 首个系统研究视觉扰动对OCR推理鲁棒性的工作，构建包含多种扰动类型和严重等级的基准，提出CRI等复合指标。

**创新点拆解**

- 构建OCR-Robust基准，包含OCR1.0和OCR2.0两个子集共812样本
- 通过预实验从18种扰动中筛选5种代表性类型
- 提出相对损坏保留率、最差保留率和复合损坏鲁棒性指数等评估指标

**当前局限**

> 扰动类型和严重等级有限，未覆盖所有实际场景；模型泛化性有待验证。

**后续可改进方向**

- 扩展扰动类型和数据集规模
- 研究模型架构层面提升鲁棒性的方法
- 开发针对结构敏感任务的专用鲁棒性增强技术

**工程启发**

> 为OCR系统部署提供鲁棒性评估工具，指导模型选择和训练策略。

**为什么值得关注**

> 直接关注OCR推理的鲁棒性问题，对实际OCR应用中的图像质量退化有启示。

**原始摘要**

Vision-language models (VLMs) have achieved strong performance on OCR-based benchmarks and
increasingly focused on text-rich understanding, but their robustness under controlled visual
degradation remains insufficiently understood. This gap is critical for OCR reasoning, where visual
corruption can induce OCR errors and structural distortions, thereby introducing uncertainty into
the reasoning task. To systematically study this problem, we introduce OCR-Robust, a benchmark
designed for evaluating OCR reasoning robustness under visual perturbations. It contains 812 samples
across two complementary subsets: OCR1.0, covering documents, scene text, receipts, handwriting, and
mathematical content, and OCR2.0, focusing on charts, geometry diagrams, and tables. To enable
efficient yet informative evaluation, we conduct a pilot study over 18 candidate perturbations and
select 5 representative types at 3 severity levels each based on their impact and cross-model
discriminability. We evaluate robustness using clean accuracy, Relative Corruption Retention (RCR),
Worst-Case Retention (WCR), and a composite Corruption Robustness Index (CRI), and benchmark 18
models spanning proprietary systems, open-source VLMs, and OCR+LLM pipelines. Our results show that
higher clean accuracy does not necessarily imply stronger robustness, and that models can suffer
pronounced degradation in the worst case on OCR tasks that are sensitive to structure, and charts
and tables are substantially more fragile than document-like inputs under perturbation.

---

### 2. LLM-Based Examination of Eligibility Criteria from Securities Prospectuses at the German Central Bank

- arXiv: [2606.27316v1](https://arxiv.org/abs/2606.27316v1)
- PDF: [下载链接](https://arxiv.org/pdf/2606.27316v1)
- 作者: Serhii Hamotskyi, Akash Kumar Gautam, Christian Hänig
- 发布时间: 2026-06-25T17:29:58Z
- 分类: cs.CL
- 相关性评分: 16
- 主题标签: LLM、信息抽取、文档审核、OCR后处理

**中文摘要**

> 使用LLM从德国央行证券招募说明书中提取资格标准，采用生成式信息抽取管线，分解为抽取、归一化和解释步骤，利用LLM-as-a-judge进行语义评估，达到91%精度。

**核心创新概述**

> 首个将LLM应用于证券资格审核的案例，从NER转向生成式信息抽取，并引入语义评估方法。

**创新点拆解**

- 提出基于LLM的生成式信息抽取管线
- 将任务分解为抽取、归一化和解释三个子任务
- 引入LLM-as-a-judge进行基于语义的评估

**当前局限**

> 依赖LLM输出质量，可能存在幻觉；评估方法仍有主观性。

**后续可改进方向**

- 结合结构化约束减少幻觉
- 探索跨语言和跨文档的泛化能力
- 改进评估方法的自动化与客观性

**工程启发**

> 为金融机构自动化文档审核提供可行方案，降低人力成本。

**为什么值得关注**

> 处理带OCR噪声的多语言文档，涉及信息抽取与筛选，对OCR后处理有借鉴意义。

**原始摘要**

Verifying the eligibility of securities as collateral is a key responsibility of the German Central
Bank. However, manually verifying these assets against legal and financial criteria within lengthy,
semi-structured, and often bilingual prospectuses is a resource-intensive task. While previous
efforts utilized traditional Named Entity Recognition (NER) for information extraction, these
methods can struggle with OCR noise, linguistic variance, and rigid span-based constraints, and the
need for manually annotated training data for each relevant annotation type. In this paper, we
present the first case study applying Large Language Models (LLMs) to the eligibility examination
process, shifting the paradigm toward a generative Information Extraction pipeline. Our approach
decomposes the task into extraction, normalization, and interpretation, allowing for greater
flexibility in handling noisy text and interleaved German-English content. We further introduce a
value-based evaluation methodology using LLM-as-a-judge, which offers a more semantic assessment
than location-based metrics. Our results demonstrate that LLM-based systems achieve high precision
(up to 91%) in document-level eligibility, exhibiting a conservative operating profile that
minimizes false acceptance.

---

### 3. Edges Before Embeddings: A Confidence-Aware Blur Gate for Vision-Language Pipelines

- arXiv: [2606.25838v1](https://arxiv.org/abs/2606.25838v1)
- PDF: [下载链接](https://arxiv.org/pdf/2606.25838v1)
- 作者: Duy Tran Thanh
- 发布时间: 2026-06-24T13:51:42Z
- 分类: cs.CV, cs.AI
- 相关性评分: 13
- 主题标签: 图像质量评估、模糊检测、OCR预处理、轻量级模型

**中文摘要**

> 提出MagikaDocumentFromPixel，一个轻量级CPU图像质量门控，7毫秒内分类图像为清晰、模糊或不确定，采用MobileNetV3-Large加边缘先验模块，F1达0.9803。

**核心创新概述**

> 设计了高效的图像质量门控，结合经典模糊检测特征和深度学习，并指出该模式在多个系统中独立出现。

**创新点拆解**

- 边缘先验模块，将拉普拉斯幅度作为辅助输入通道
- 通过经验搜索确定输入分辨率是关键杠杆
- 置信度感知路由形式化，基于选择性预测理论

**当前局限**

> 仅在单一运动模糊分布上评估，校准是定性的。

**后续可改进方向**

- 扩展到多种模糊类型（散焦、高斯等）
- 量化校准并集成到更广泛的OCR管线
- 探索更轻量或更准确的架构

**工程启发**

> 可直接用于OCR预处理阶段，节省计算资源，提高下游质量。

**为什么值得关注**

> OCR流程中图像质量检测模块，直接影响OCR输入质量。

**原始摘要**

Production vision pipelines silently degrade on blurry input, wasting compute on downstream OCR,
retrieval, and vision-language model (VLM) calls that cannot recover a usable output. We present
MagikaDocumentFromPixel, a lightweight, CPU-friendly image quality gate that classifies a single
image as sharp, blurred, or uncertain in roughly 7 ms on a single CPU core. The contributions are
(i) a recipe selected from a 46-configuration, 8-sweep empirical search that isolates input
resolution as the dominant lever and shows architecture capacity only pays off at >= 384 px; (ii) a
confidence-aware routing formalism grounded in classical selective prediction; (iii) the Edge Prior
Module (EPM), a Laplacian-magnitude auxiliary input channel that gives the network direct access to
the spectral evidence that classical blur heuristics rely on and that lifts test F1 by +1.3 points
in a matched-env comparison; and (iv) an observation that the gate is one instance of a recurring
design pattern that appears independently in Magika content-type detection, risk-controlled OCR with
VLMs, and DocVLM. The final recipe MobileNetV3-Large with the EPM trained at 384x384 on paired GoPro
Large frames, evaluated with 5-scale test-time augmentation reaches F1 = 0.9803 (AUC 0.9989) with a
17 MB ONNX artifact, improving over our fixed-scale baseline on the same hardware (F1 = 0.9672) by
+1.31 points. We are explicit about limitations: results are on a single motion-blur distribution,
numbers are from a single seed, and calibration is qualitative rather than measured.

---

### 4. ProfileFoundry: A Synthetic Person-Object Substrate for Privacy, Memory, and Tool-Use Evaluation in LLM Agent

- arXiv: [2606.26403v1](https://arxiv.org/abs/2606.26403v1)
- PDF: [下载链接](https://arxiv.org/pdf/2606.26403v1)
- 作者: Sriram Selvam, Anneswa Ghosh
- 发布时间: 2026-06-24T21:43:36Z
- 分类: cs.CL
- 相关性评分: 10
- 主题标签: 合成数据、人物对象、隐私评估、文档理解

**中文摘要**

> 提出PROFILEFOUNDRY，一种确定性合成人物对象生成器，发布10万个跨八个地区的合成人物数据，包含快照、家庭、雇主、事件和关系，用于基础模型的内存、隐私、文档理解等评估。

**核心创新概述**

> 提供具有跨字段和时间一致性的合成人物数据，作为负责任的下游评估基础层。

**创新点拆解**

- 确定性生成器保证可复现性
- 生成包含当前快照、家庭、雇主、事件和关系链的复杂人物对象
- 提供完整的生成出处和交叉引用检查

**当前局限**

> 不是群体保真度模型，也不是正式隐私机制，合成数据与真实数据仍有差距。

**后续可改进方向**

- 提高合成数据的真实性和多样性
- 集成隐私保护机制
- 扩展到更多地区和场景

**工程启发**

> 为隐私、记忆、工具使用等评估提供安全可控的合成数据源，避免真实数据风险。

**为什么值得关注**

> 涉及文档理解和记录关联，合成人物数据可用于OCR文档理解任务的评估。

**原始摘要**

Foundation-model research increasingly needs data about people: user state, personal histories,
relationships, contact-like fields, documents, and longitudinal updates. Real user data is difficult
to share, perturb, audit, or redistribute responsibly, while independently generated fake fields
rarely preserve the cross-field and temporal consistency needed for controlled evaluation. We
present PROFILEFOUNDRY, a deterministic generator and fixed reference release of 100,000 adult
synthetic Person Objects across eight locales. Each object combines a typed current snapshot,
household, family, and employer links, snapshot-aligned events, normalized relational views, and
generation provenance. The release contains 709,228 events, 40,338 households, 52,491 employers, and
518,564 directed relationship edges. We report evidence in separate categories: selected population-
marginal comparisons, per-object invariant checks, release-wide referential and temporal closure,
and coincidence/provenance screens. PROFILEFOUNDRY is not a population-fidelity model, a rendered-
text corpus, or a formal privacy mechanism. Instead, it is a responsible synthetic source layer for
constructing downstream foundation-model evaluations involving memory, privacy, document
understanding, record linkage, and agent state while keeping the synthetic person behind each
artifact inspectable

---

### 5. Overview of HIPE-2026: Person-Place Relation Extraction from Multilingual Historical Texts

- arXiv: [2606.25935v1](https://arxiv.org/abs/2606.25935v1)
- PDF: [下载链接](https://arxiv.org/pdf/2606.25935v1)
- 作者: Juri Opitz, Maud Ehrmann, Corina Raclé, Andrianos Michail, Matteo Romanello, Simon Clematide
- 发布时间: 2026-06-24T15:09:12Z
- 分类: cs.CL, cs.AI
- 相关性评分: 10
- 主题标签: 关系抽取、历史文档、OCR噪声、跨域泛化

**中文摘要**

> HIPE-2026评测任务聚焦从多语言历史文本中提取人物-地点关系，涉及时间推理，17支队伍参与，采用三方面评估（准确率、效率、跨域泛化），揭示了LLM和轻量分类器之间的权衡。

**核心创新概述**

> 从命名实体识别转向实体间关系推理，引入时间维度，并结合跨领域泛化评估。

**创新点拆解**

- 定义两种时间锚定关系类型：at和isAt
- 三面评估框架：预测准确率、计算效率、跨域泛化
- 包含历史语言变体、OCR噪声和间接上下文线索

**当前局限**

> 历史文本资源有限，跨域泛化挑战大，评估成本高。

**后续可改进方向**

- 结合LLM和轻量模型优势
- 发展更鲁棒的跨语言和时间推理方法
- 处理OCR噪声和历史语言变化

**工程启发**

> 为文化遗产机构大规模处理历史文档提供关系抽取方案。

**为什么值得关注**

> 直接处理OCR噪声和历史文档，涉及实体关系抽取，对OCR后理解任务有参考价值。

**原始摘要**

Was this person ever at that place, and if so, when? Answering such questions from noisy,
multilingual historical documents is the central challenge of HIPE-2026, the third edition of the
HIPE evaluation series. Moving from named entity recognition and linking (HIPE-2020, HIPE-2022) to
reasoning about relationships between entities, HIPE-2026 targets two temporally grounded relation
types: $at$, indicating that a person was present at a location at some point prior to a document's
publication date, and $isAt$, indicating presence contemporaneous with that date. This paper
presents the results of the evaluation campaign, which confronted 17 participating teams with the
challenges of historical language variation, OCR noise, and indirect contextual cues across three
languages: French, German, and English. The datasets include historical newspaper text from the
nineteenth and twentieth centuries, as well as a surprise-domain generalization set drawn from early
modern French literary texts. A distinctive feature of HIPE-2026 is its three-fold evaluation
framework, which assesses predictive accuracy, computational efficiency, and cross-domain
generalization, reflecting the practical demands of large-scale historical document processing in
the cultural heritage domain. Across more than 40 submitted runs, results reveal a wide range of
strategies, from state-of-the-art large language models to lightweight task-specific classifiers,
and highlight the trade-offs between accuracy, efficiency, and robustness inherent to historical
relation extraction at corpus scale. System descriptions, datasets, and findings are presented and
discussed, offering a detailed picture of the current state of temporally grounded relation
extraction for historical documents.

---

### 6. Probabilistic Agents in Deterministic Audits: Evaluating Multi-Agent Systems for Automated Audits Based on the German IT-Grundschutz

- arXiv: [2606.25622v1](https://arxiv.org/abs/2606.25622v1)
- PDF: [下载链接](https://arxiv.org/pdf/2606.25622v1)
- 作者: Lea Roxanne Muth, Marian Margraf
- 发布时间: 2026-06-24T09:31:06Z
- 分类: cs.CR, cs.AI
- 相关性评分: 10
- 主题标签: 多智能体系统、混合RAG、文档自动化、合规检查

**中文摘要**

> 实现并评估基于多智能体系统和混合RAG的IT-Grundschutz认证部分自动化方案，提出假设验证循环和解耦推理管线，在案例研究中取得一定效果。

**核心创新概述**

> 将多智能体系统与混合RAG结合用于IT安全认证自动化，提出了减少幻觉和保证合规的技术贡献。

**创新点拆解**

- 假设验证循环，通过知识图谱交叉引用减少幻觉
- 解耦推理管线，分离语义提取和确定性保护需求继承
- 利用HybridRAG提升检索质量

**当前局限**

> 不同认证阶段性能有差异，完全自动化仍有挑战。

**后续可改进方向**

- 优化智能体协作机制
- 提高跨阶段一致性
- 整合更多结构化知识源

**工程启发**

> 为中小企业降低IT安全认证成本，提高效率。

**为什么值得关注**

> 涉及文档理解、信息抽取和自动推理，可应用于复杂的OCR后处理场景。

**原始摘要**

The NIS-2 Directive mandates robust Risk Management from thousands of small and medium enterprises.
To ensure compliance, companies rely on established standards such as the German IT-Grundschutz (IT-
GS) of the Federal Office for Information Security. However, IT-GS certification is resource-
intensive and requires a high level of manual effort for documentation, validation, and revision,
making scalable implementation difficult and expensive. Building upon our previous conceptual
framework, this paper presents the technical implementation and empirical evaluation of a Multi-
Agent System (MAS) architecture combined with Hybrid Retrieval Augmented Generation (HybridRAG) for
the partial automation of IT-GS certification. We introduce two novel technical contributions to the
MAS architecture to enforce the compliance rigor. The Hypothesis-Verification Loop in the Structural
Analysis (SA) phase that cross-references agent-inferred dependencies against the Knowledge Graph to
reduce hallucinations, and a Decoupled Reasoning Pipeline that separates agent-driven semantic
extraction from the deterministic protection need inheritance. We utilize the BSI's "RecPlast GmbH"
case study as a human expert-generated reference data set for end-to-end evaluation of the
architecture and to quantify Precision, Recall, and F1-scores. The performance of the system is
investigated across the phases of SA, Protection Needs Assessment (PNA), Modeling, and IT-GS Check.
The empirical results reveal noticeable differences throughout the different steps of IT-GS. While
the MAS demonstrates high efficacy in semantic tasks (SA and Modeling), significantly reducing
manual effort through automated information extraction, quantitative results reveal limitations in
logical reasoning phases (PNA and IT-GS Check) as the probabilistic nature of current LLMs struggles
to meet the deterministic rigor required by IT-GS.

---

### 7. WinDOM: Self-Family Distillation for Small-Model GUI Grounding

- arXiv: [2606.25964v1](https://arxiv.org/abs/2606.25964v1)
- PDF: [下载链接](https://arxiv.org/pdf/2606.25964v1)
- 作者: Chengheng Li-Chen, Zhiqian Zhou, Hao Chen, Nicolas Chauvin
- 发布时间: 2026-06-24T15:35:29Z
- 分类: cs.AI, cs.LG
- 相关性评分: 9
- 主题标签: GUI grounding、数据集构建、知识蒸馏、强化学习、小型模型

**中文摘要**

> 提出WinDOM数据集和自家族蒸馏(SFD)方法，用于训练小规模(约2B参数)GUI定位智能体。WinDOM通过无头Playwright驱动开源Windows 11网页实现自动收集标注数据，无需人工或OCR。SFD采用拒绝采样冷启动，教师模型可选学生EMA或无外部模型的同家族大模型。利用SFD冷启动后的饱和度作为GRPO超参数，欠饱和冷启动比收敛冷启动更适合作为GRPO初始值，在Qwen2.5-2B上取得OOD平均提升+5.4。

**核心创新概述**

> 提出无需人工标注的GUI grounding数据集自动构建方法，以及结合蒸馏与强化学习的自家族蒸馏框架，并创新性利用冷启动饱和度作为RL初始化超参数。

**创新点拆解**

- 提出WinDOM数据集，通过DOM解析直接获取边界框，无需OCR或人工标注
- 提出自家族蒸馏(SFD)方法，通过拒绝采样冷启动，教师可选择EMA或同家族大模型
- 将SFD冷启动的饱和度作为GRPO超参数，发现欠饱和冷启动优于收敛冷启动
- 在2B级小模型上实现跨大小教师的实用蒸馏，EMA模式无外部教师时性能接近跨大小变体

**当前局限**

> 数据仅基于Windows 11网页实现，可能泛化到其他操作系统或原生应用时存在域差异；冷启动饱和度选择依赖于经验调参。

**后续可改进方向**

- 探索跨平台、跨应用的GUI grounding泛化能力
- 自动化选择冷启动饱和度准则以减少人工调参
- 研究不同教师模型大小与蒸馏策略的trade-off

**工程启发**

> 为资源受限设备的GUI grounding提供低成本、高质量的数据生成和监督训练范式，减少对大规模人工标注的依赖。

**为什么值得关注**

> 涉及OCR-free的GUI元素定位，通过DOM结构替代文本检测，可直接用于自动化测试和无障碍工具。

**原始摘要**

Small ($\sim$2B) GUI-grounding agents are attractive for on-device deployment, accessibility
tooling, and low-cost iteration, but at this scale they face two open recipe questions: how to
obtain bounding-box training data without expensive human annotation, and how to combine supervised
fine-tuning with reinforcement learning. We address both, with the explicit goal of pushing small-
model performance rather than scaling up. WinDOM is a $54{,}425$-record grounding corpus harvested
by driving an open-source Windows 11 web reimplementation under headless Playwright, with bounding
boxes read directly off the DOM and no OCR or human annotation. Self-Family Distillation (SFD) is a
single rejection-sampling cold-start parameterised only by the teacher choice: either an EMA of the
student (no external model) or a frozen larger same-family teacher. We then treat the saturation
depth of the SFD cold-start as an explicit GRPO hyperparameter. On a Qwen3.5-2B student, the under-
saturated cold-start is a better GRPO initialiser than the converged one: SFD-4B with Early-init RL
gains $+5.4$ OOD-mean ($+3.5$ ScreenSpot-Pro, $+7.0$ OSWorld-G, $+5.8$ ScreenSpot-V2) over the base.
The same-size EMA mode lands within roughly one OOD-mean point of the cross-size $4$B variant
($65.2$ vs $66.3$) without an external teacher.

---

### 8. PhysRAG: Enhancing Physics-Awareness in Video Generation via Retrieval-Augmented Generation

- arXiv: [2606.26916v1](https://arxiv.org/abs/2606.26916v1)
- PDF: [下载链接](https://arxiv.org/pdf/2606.26916v1)
- 作者: Kexu Cheng, Zicheng Liu, Mingju Gao, Chunhe Song, Hao Tang
- 发布时间: 2026-06-25T11:53:27Z
- 分类: cs.CV
- 相关性评分: 6
- 主题标签: 视频生成、物理感知、检索增强生成、数据过滤、扩散模型

**中文摘要**

> 提出PhysRAG框架，通过检索增强生成(RAG)增强视频生成模型对物理规则的理解。构建两阶段数据过滤管道，从WISA-80K中筛选7K高质量视频；建立物理视频数据库并利用可学习查询注入物理知识。在PhyGenBench和VBench上达到最优视频质量和物理合规性。

**核心创新概述**

> 首次将RAG引入视频生成以增强物理感知，并设计可学习查询机制实现物理知识注入。

**创新点拆解**

- 提出RAG增强视频生成的物理感知框架PhysRAG
- 设计两阶段数据过滤管道，从大规模数据中筛选高质量物理相关视频
- 构建物理视频数据库并开发基于可学习查询的物理知识注入机制
- 在多个基准上实现视觉质量和物理合规性的SOTA

**当前局限**

> 依赖预定义的物理数据库，可能覆盖的物理现象有限；可学习查询的注入机制在复杂场景下的有效性有待验证。

**后续可改进方向**

- 扩展物理数据库覆盖面，包括更多动态物理现象
- 探索更灵活的物理知识表示与注入方式，如自适应查询
- 研究无外部数据库的在线物理知识检索方法

**工程启发**

> 为视频生成模型提供系统性的物理知识增强方案，可直接用于教育、仿真和内容创作等需要物理真实感的领域。

**为什么值得关注**

> 涉及视频生成中的物理规则理解，可通过检索文本知识增强模型对物理现象的建模能力，与多模态文档理解相关。

**原始摘要**

Developing physically aware video generation models remains a significant challenge due to the
difficulty in capturing diverse physical phenomena, such as thermal dynamics, mechanics, and optics.
In this work, we introduce PhysRAG, a novel pipeline that enhances physical awareness in video
generation through Retrieval-Augmented Generation (RAG). To address the issue of limited high-
quality data, we design a two-stage data filtering pipeline based on the WISA-80K dataset, resulting
in a curated set of 7K high-quality videos for training. Furthermore, we construct a physical video
database and develop a mechanism to inject physical knowledge into a video diffusion model using
learnable queries. Our method achieves state-of-the-art performance in both visual quality and
physical rule compliance, surpassing existing models in benchmarks such as PhyGenBench and VBench.
We conduct extensive ablation studies to validate the effectiveness of our key components, including
the data filtering pipeline, RAG mechanism, and method for physical information extraction. To
facilitate future research, our code, data, and models are prepared for release at
https://github.com/sediment1024/PhysRAG.

---
