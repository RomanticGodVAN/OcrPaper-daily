# OCR / 文档解析研究日报（2026-09-09）

## 报告说明

- 检索源：arXiv API
- 检索查询：`(all:"document parsing" OR all:"document understanding" OR all:"optical character recognition" OR all:OCR OR all:"layout analysis" OR all:"document layout analysis" OR all:"text recognition" OR all:"table recognition" OR all:"form understanding" OR all:"document intelligence" OR all:"page understanding" OR all:"scene text recognition" OR all:"handwritten text recognition" OR all:"information extraction") AND (cat:cs.CV OR cat:cs.AI OR cat:cs.CL OR cat:eess.IV)`
- 生成时间（UTC）：`2026-09-09 05:58:27`
- 大模型综合分析：`关闭`
- 备注：DeepSeek 处理失败：Invalid control character at: line 9 column 34 (char 795)

## 三、今日论文概览

1. **When Superpixels Fail on Documents: A Study of Segmentation for LIME Explanations** | 标签：可解释AI、LIME、文档图像分类、分割
2. **AAS-RAIL: Improving Information Extraction for Asset Administration Shells through Retrieval-Augmented In-Context Learning** | 标签：信息抽取、检索增强、LLM、工业文档
3. **SIFTING: A Novel LLM-Based Framework for Structured and Transparent Information Extraction from Clinical Free-Text Reports, with Application to Tumor Staging in Lung Cancer** | 标签：临床文本、信息抽取、LLM、可追溯性
4. **Beyond Single-Negative Preference: Multi-Negative DPO for LLM-Centric Historical Entity Linking** | 标签：实体链接、历史文档、偏好优化、OCR噪声
5. **BlueprintAgent: Constraint-Triggered Targeted Revisits for Simulation-Ready Generation from Scanned Structural Blueprints** | 标签：蓝图解析、MLLM、约束触发、框架提取
6. **SupGRPO: Enhancing GRPO with Matching-based Online SFT for Text Spotting** | 标签：文本定位、文本识别、强化学习、MLLM
7. **Retrieval-Augmented Multi-Prompt Ensemble for Minor-Grain Breeding Information Extraction** | 标签：信息抽取、大语言模型、提示学习、知识图谱、农业信息化

## 八、论文逐篇解析

### 1. When Superpixels Fail on Documents: A Study of Segmentation for LIME Explanations

- arXiv: [2609.07462v1](https://arxiv.org/abs/2609.07462v1)
- PDF: [下载链接](https://arxiv.org/pdf/2609.07462v1)
- 作者: Quentin Telnoff, Emanuela Boros, Mickaël Coustaty, Robin Jarry, Fabrice Crohas, Antoine Doucet
- 发布时间: 2026-09-07T13:13:36Z
- 分类: cs.CV, cs.AI
- 相关性评分: 17
- 主题标签: 可解释AI、LIME、文档图像分类、分割

**中文摘要**

> 针对文档图像分类中LIME可解释性方法的研究，发现标准超像素分割与文档结构不对齐，导致解释不稳定且不忠实。比较了自然图像超像素（Quickshift、SLIC）与基于OCR和网格的文档感知分割，结果表明文档感知分割能产生更稳定忠实的解释，减少扰动次数，并暴露基于文档识别码的捷径行为。强调分割应视为解释方法的一部分，需要领域感知的可解释表示。

**核心创新概述**

> 首次系统研究分割选择对文档图像分类LIME解释质量的影响，提出文档感知分割的必要性。

**创新点拆解**

- 比较了多种分割方法在文档图像上的解释性能
- 提出基于OCR和规则网格的文档感知分割用于LIME
- 揭示了超像素分割掩盖文档识别码捷径行为的问题

**当前局限**

> 研究仅针对LIME方法，可能不适用于其他解释方法；实验基于RVL-CDIP数据集，结论的通用性有限。

**后续可改进方向**

- 探索其他可解释性方法（如SHAP）与文档感知分割的结合
- 开发自适应分割方法，根据文档类型动态选择分割粒度

**工程启发**

> 为文档图像分析中的可解释AI系统提供了优化方向，可用于提升模型审计的可靠性。

**为什么值得关注**

> OCR系统常涉及文档图像分类，本研究为增强OCR管道中的可解释性提供了实用方法。

**原始摘要**

Post-hoc explanation methods are widely used to inspect image classifiers, but their reliability
depends on design choices that are often treated as implementation details. We study this issue for
LIME on document image classification, focusing on the segmentation step that defines the
interpretable units being perturbed. Standard image-based LIME typically relies on natural-image
superpixels, which are poorly aligned with document structure such as text regions, layout blocks,
and identification codes. Using RVL-CDIP, we compare Quickshift and SLIC with document-aware
segmentations based on OCR bounding boxes and regular grids. Our results show that segmentation
strongly affects explanation consistency, correctness, and local fidelity. Document-aware
segmentations produce more stable and faithful explanations, require fewer perturbations to
converge, and expose shortcut behaviour based on document identification codes, a known RVL-CDIP
bias that superpixel-based LIME often obscures. These findings show that reliable post-hoc
explanation requires domain-aware interpretable representations, and that segmentation should be
treated as part of the explanation method rather than as neutral preprocessing.

---

### 2. AAS-RAIL: Improving Information Extraction for Asset Administration Shells through Retrieval-Augmented In-Context Learning

- arXiv: [2609.07334v1](https://arxiv.org/abs/2609.07334v1)
- PDF: [下载链接](https://arxiv.org/pdf/2609.07334v1)
- 作者: Janek Groß, Jens Heidrich
- 发布时间: 2026-09-07T10:54:00Z
- 分类: cs.AI
- 相关性评分: 12
- 主题标签: 信息抽取、检索增强、LLM、工业文档

**中文摘要**

> 提出了AAS-RAIL，一种检索增强的信息抽取方法，自动从PDF产品数据表生成资产管理壳（AAS）。通过检索与实例相似的AAS示例生成上下文学习样本，使模型适应公司特定术语与格式，无需微调。实验表明该方法优于传统少样本提示，适用于工业文档信息抽取。

**核心创新概述**

> 将检索增强的上下文学习应用于资产管理壳的自动生成，取代静态提示，促进提取行为适应公司特定惯例。

**创新点拆解**

- 提出检索增强的上下文学习（RAIL）用于信息抽取
- 动态选择与实例相似的AAS示例进行提示
- 结合语义检索和结构化信息抽取

**当前局限**

> 未给出具体实验数据，泛化能力需进一步验证；依赖预训练LLM，可能受限于文档类型多样性。

**后续可改进方向**

- 探索利用视觉信息辅助文档布局理解
- 引入主动学习机制以优化检索示例的质量和多样性

**工程启发**

> 可自动化工业资产生命周期管理，减少人工从数据表构建AAS的工作，提高生产效率。

**为什么值得关注**

> 涉及从PDF中提取技术信息，与文档解析和OCR后处理相关，LLM方法可迁移至其他文档理解任务。

**原始摘要**

The Asset Administration Shell (AAS) is a cornerstone of Industry 4.0 and the Digital Product
Passport, providing standardized digital representations of industrial assets. While manufacturers
already maintain extensive technical product documentation, generating AAS instances from existing
product datasheets remains a labor-intensive task because technical information is extracted from
heterogeneous document structures and often involves company-specific terminology and conventions.
In this work, we present AAS-RAIL, a retrieval-augmented information extraction (IE) approach that
automatically generates Asset Administration Shells from PDF product datasheets using large language
models (LLMs). Instead of relying on a fixed set of few-shot examples, the proposed retrieval-
augmented in-context learning (RAIL) approach retrieves LLM-generated extraction helpers from
similar Asset Administration Shells to provide instance-specific in-context learning (ICL). This
enables the model to adapt its extraction behavior to company-specific naming conventions and
formatting styles without fine-tuning. Our core contribution is the dynamic selection of company-
specific AAS examples for each datasheet, replacing static prompting with an extraction pipeline
that adapts to instances and combines semantic retrieval and structured information extraction. The
proposed approach is evaluated on a collection of industrial product datasheets using a selection of
open- and closed-weight LLMs. Experimental results show that RAIL consistently improves extraction
quality over conventional few-shot prompting, yielding relative improvements of 30.4-52.4%. These
results demonstrate that our approach provides an effective improvement for company-specific AAS
generation.

---

### 3. SIFTING: A Novel LLM-Based Framework for Structured and Transparent Information Extraction from Clinical Free-Text Reports, with Application to Tumor Staging in Lung Cancer

- arXiv: [2609.07185v1](https://arxiv.org/abs/2609.07185v1)
- PDF: [下载链接](https://arxiv.org/pdf/2609.07185v1)
- 作者: Mirco Hess, Gerben van Veenendaal, Joris Wakkie, Yiwen Soo, Malcolm H. Lawson, John D. Maclay, Arjun Nair, Neal Navani
- 发布时间: 2026-09-07T08:15:19Z
- 分类: cs.CL
- 相关性评分: 10
- 主题标签: 临床文本、信息抽取、LLM、可追溯性

**中文摘要**

> 介绍了SIFTING，一个基于LLM的框架，用于从临床自由文本报告中提取结构化和可追溯信息。通过分句处理、严格输出控制、引用源文本链接，实现了高准确度（90%）的肺癌T分期提取，同时提供完全可追踪性。采用4比特量化Llama-3.3-70B自托管，性能与专家相当。

**核心创新概述**

> 结合LLM与片段级处理、结构化提示和源文本链接，使提取结果兼具准确性和可追溯性，解决了临床文本提取中的验证难题。

**创新点拆解**

- 提出分句级处理与结构化输出控制结合
- 强制关联提取信息到源文本，增强可追踪性
- 使用量化模型自托管保证数据隐私

**当前局限**

> 仅应用于肺癌T分期，需拓展到其他临床实体；依赖高质量参考标准，可能引入标注偏差。

**后续可改进方向**

- 扩展到医学影像报告、电子病历等多种文本类型
- 集成多模态信息（如影像）提升提取鲁棒性
- 设计专门针对医学领域的分词策略以提高精确度

**工程启发**

> 可应用于临床决策支持，减少医生手动记录负担，确保数据溯源符合法规。

**为什么值得关注**

> 针对医学文档的OCR后处理与信息抽取有直接借鉴，可推动临床NLP应用。

**原始摘要**

Background: Large language models (LLMs) show promise for extracting information from clinical free-
text documents, but their outputs are often unstructured and lack traceability, complicating
validation and adoption in clinical workflows. In this work we introduce SIFTING, an LLM-based
framework designed to address these shortcomings. Methods: SIFTING combines the language
comprehension capabilities of LLMs with segment-level processing and structured prompts with strict
output control, linking findings to the source text to enable both accurate and transparent
information extraction. To demonstrate its capabilities, we applied the framework to the task of
extracting tumor T-stage information from 130 lung cancer radiology reports (SIFTING-T-stage). A
compact 4-bit quantized version of the open-source LLM Llama-3.3-70B (35 GB) was used in a fully
self-hosted setup, providing full control over data and model. Performance was evaluated against a
reference standard created by four clinical experts and compared with a range of LLMs as used in a
conventional single-prompt approach, using bootstrap resampling to estimate confidence intervals.
Results: SIFTING-T-stage achieved an accuracy of 90% (95% CI: 84-95) against the reference standard.
We found its performance to be comparable to even the largest state-of-the-art LLMs with reasoning
capabilities and to be interchangeable with clinical experts (p < 0.001), while at the same time
offering full traceability through source text references. Conclusion: SIFTING enables accurate,
structured, and traceable information extraction from clinical free-text documents. It ensures data
control, reproducibility, and verifiable outputs that can support clinical validation and workflow
integration.

---

### 4. Beyond Single-Negative Preference: Multi-Negative DPO for LLM-Centric Historical Entity Linking

- arXiv: [2609.07379v1](https://arxiv.org/abs/2609.07379v1)
- PDF: [下载链接](https://arxiv.org/pdf/2609.07379v1)
- 作者: Tien Nam Nguyen, Emanuela Boros, Ahmed Hamdi, Adam Jatowt, Mickaël Coustaty, Antoine Doucet
- 发布时间: 2026-09-07T11:57:45Z
- 分类: cs.CL, cs.AI
- 相关性评分: 9
- 主题标签: 实体链接、历史文档、偏好优化、OCR噪声

**中文摘要**

> 提出了多负样本直接偏好优化（MDPO）用于历史实体消解，与仅使用单一负样本的DPO相比，MDPO利用每个提及的所有有效负候选，基于参考的双向目标，保留Bradley-Terry公式但通过掩码、长度归一化序列评分利用完整候选集。在多个语种的历史报纸文本上评估，MDPO显著优于SFT和单负DPO。

**核心创新概述**

> 首次在历史实体消解中利用所有负样本，通过多负样本DPO改进偏好优化，并研究了候选生成与选择错误。

**创新点拆解**

- 提出多负样本DPO目标（MDPO），利用全候选集
- 采用掩码、长度归一化序列评分优化模型
- 在多种语言的历史报纸数据上验证有效性

**当前局限**

> 候选检索仍是瓶颈，端到端性能受限；历史领域独特挑战需专用处理。

**后续可改进方向**

- 改进候选检索模块，结合上下文感知的实体提及识别
- 探索跨语言迁移或知识增强以应对历史语言变异
- 研究多负样本与课程学习结合

**工程启发**

> 对历史文献的数字人文研究有直接帮助，提升命名实体识别与链接的准确性，减少人工校对。

**为什么值得关注**

> 处理OCR噪声是历史实体链接的关键，MDPO在噪声环境下表现强，对OCR后处理有启发。

**原始摘要**

Large language models (LLMs) have recently shown promise for historical entity linking, but
preference optimization for this task is often formulated with only one negative candidate per
training instance. This discards information from the remaining candidates retrieved for the same
mention. We introduce multi-negative direct preference optimisation (MDPO), a reference-based
pairwise objective that compares the correct entity with all valid rejected candidates associated
with each mention. MDPO preserves the Bradley-Terry formulation of DPO while exploiting the complete
candidate set through masked, length-normalised sequence scores. We evaluate MDPO on hipe-2020 and
newseye, covering French, German, English, Swedish, and Finnish historical newspaper text.
Experiments show that MDPO improves over supervised fine-tuning and single-negative DPO, with
particularly strong gains for NIL mentions, semantic ambiguity, OCR noise, and historically
difficult names. Further analyses disentangle candidate-generation and selection errors, showing
that candidate retrieval remains a key bottleneck for end-to-end entity linking. These results
demonstrate that incorporating all within-instance negative candidates is a simple and effective
improvement for LLM-based historical entity linking.

---

### 5. BlueprintAgent: Constraint-Triggered Targeted Revisits for Simulation-Ready Generation from Scanned Structural Blueprints

- arXiv: [2609.07362v1](https://arxiv.org/abs/2609.07362v1)
- PDF: [下载链接](https://arxiv.org/pdf/2609.07362v1)
- 作者: Zhouyuan Xu, Chen Yang, Linhao Wang, Jiansheng Fan, Chen Wang
- 发布时间: 2026-09-07T11:29:29Z
- 分类: cs.CL, cs.AI, cs.CV
- 相关性评分: 9
- 主题标签: 蓝图解析、MLLM、约束触发、框架提取

**中文摘要**

> 提出BlueprintAgent，一个约束触发式多模态代理，从扫描蓝图生成仿真就绪的框架表示。其核心是使工程约束成为可调用验证器，当冲突时触发MLLM对局部区域的定向重访，而非固定管道或自反思。在300张蓝图上取得高F1分数（0.994），显著优于单MLLM和固定管道。

**核心创新概述**

> 创新性地将工程约束作为触发局部重访的验证器，区别于固定流水线和自由形式自修正。

**创新点拆解**

- 实现工程约束为可调用验证器，实体级冲突报告触发局部重访
- MLLM作为主读器，OCR和CV提供证据
- 结合可微分的框架提取与多模态推理

**当前局限**

> 依赖MLLM的阅读和推理能力，对复杂多层图纸可能不足；评估数据有限。

**后续可改进方向**

- 引入更多工程领域知识（如结构力学）进行验证
- 扩展至其他图纸类型（钢结构、机电等）
- 优化触发的局部重访策略以减少计算开销

**工程启发**

> 促进既有建筑数字孪生生成，加速安全评估与改造，节省人力。

**为什么值得关注**

> OCR和视觉理解技术在此系统中作为关键模块，体现了文档解析与领域知识结合的模式。

**原始摘要**

Converting in-service reinforced-concrete (RC) building blueprints into simulation-ready models---
structured frame representations that support deterministic FEM export and qualified-engineer review
---underpins safety assessment and seismic retrofit, but the process remains manual. Direct
prompting of a multimodal large language model (MLLM) over a scanned sheet is unreliable: outputs
often violate engineering constraints on beam--column support, span count, or 3D continuity. We
present BlueprintAgent (BPA), a constraint-triggered multimodal agent for simulation-ready frame
extraction from scanned blueprints. BPA treats the MLLM as the primary reader and decision maker,
with OCR and computer vision supplying localized evidence. Its central mechanism realizes
engineering constraints as callable validators whose entity-level conflict reports trigger targeted
MLLM revisits over the local region---an inference-time control distinct from fixed pipelines and
free-form self-reflection. We evaluate BPA on 300 real scanned blueprint sheets from 20 anonymized
RC frame projects, against five baselines and six ablations. BPA reaches a macro-averaged Beam F1 of
0.994, against 0.301 for single-MLLM zero-shot and 0.820 for a fixed pipeline; removing MLLM-led
axis adjudication collapses Beam and Column F1 on complex multi-sheet projects. For dense technical
drawings, engineering constraints are best deployed as triggers for entity-level targeted revisits
rather than as post-hoc output filters.

---

### 6. SupGRPO: Enhancing GRPO with Matching-based Online SFT for Text Spotting

- arXiv: [2609.07081v1](https://arxiv.org/abs/2609.07081v1)
- PDF: [下载链接](https://arxiv.org/pdf/2609.07081v1)
- 作者: Xudong Xie, Yuzhe Li, Jing Shi, Zhifei Zhang, Curtis Wigington, Zhaowen Wang
- 发布时间: 2026-09-07T06:11:48Z
- 分类: cs.CV
- 相关性评分: 8
- 主题标签: 文本定位、文本识别、强化学习、MLLM

**中文摘要**

> 提出SupGRPO，一种联合训练策略，组合监督微调（SFT）和基于GRPO的强化学习来微调MLLM用于文本识别与检测。发现SFT能更好提升定位，GRPO更好提升识别，通过匹配策略和只对坐标token进行在线SFT来互补。在艺术文本检测数据集上取得新最佳表现，泛化性能强。

**核心创新概述**

> 首次提出将SFT和GRPO联合应用于文本识别模型，动态平衡识别与定位能力。

**创新点拆解**

- 提出结合SFT和GRPO的联合训练方法SupGRPO
- 设计匹配型在线SFT，只对坐标token进行优化
- 构造艺术文本检测数据集ATS，揭示性能差异

**当前局限**

> 仅针对文本识别任务，未扩展到其他OCR或场景；严格依赖MLLM架构，可能计算成本高。

**后续可改进方向**

- 探索在更多任务（如表格结构识别）上验证联合训练的有效性
- 引入多尺度检测头进一步提升定位精度
- 研究GRPO奖励函数的细化以适应不规则文本

**工程启发**

> 改进文本阅读系统在复杂场景下的可靠性，对自动驾驶、辅助视觉等领域的OCR应用有直接帮助。

**为什么值得关注**

> 文本识别与检测是OCR核心，该方法能提升端到端性能，为真实场景OCR提供新范式。

**原始摘要**

Text spotting requires both accurate text recognition and precise spatial localization. Current
specialised spotters excel at predicting tight bounding boxes in natural scenes, but falter on
complex or artistic text, whereas multimodal large language models (MLLMs) possess strong
recognition capabilities yet remain weak at localisation. To equip the text spotter with general and
powerful recognition capabilities and to maximize its localization ability, we explore two MLLM-
based fine-tuning methods: Supervised Fine-Tuning (SFT) and reinforcement learning fine-tuning based
on Group Relative Policy Optimisation (GRPO). An interesting finding is that SFT is less effective
than GRPO at enhancing recognition, while GRPO is less effective than SFT at enhancing detection. To
compensate for each other's shortcomings, we introduce a joint training strategy, SupGRPO, which
simultaneously optimizes the model using both SFT and GRPO. SupGRPO employs the specially designed
reward functions and develops a matching-based online SFT applied solely to coordinate tokens. It
both mitigates the reward sparsity problem of GRPO and avoids the instance order dependency problem
of SFT. To evaluate particularly challenging cases, we curate ATS, a dataset for artistic text
spotting. Experiments demonstrate that SupGRPO improves both text recognition and detection, and
attains superior performance. Our code and dataset will be released at
https://github.com/Psycho-9/SupGRPO.

---

### 7. Retrieval-Augmented Multi-Prompt Ensemble for Minor-Grain Breeding Information Extraction

- arXiv: [2609.07134v1](https://arxiv.org/abs/2609.07134v1)
- PDF: [下载链接](https://arxiv.org/pdf/2609.07134v1)
- 作者: Hang Zhao, Jiahao Wang
- 发布时间: 2026-09-07T07:30:49Z
- 分类: cs.CL
- 相关性评分: 6
- 主题标签: 信息抽取、大语言模型、提示学习、知识图谱、农业信息化

**中文摘要**

> 本文介绍了作者团队在CCL2026-Eval任务5（小杂粮育种信息抽取，MGBIE）中提出的系统。该系统从育种文献中联合抽取12种实体类型和6种关系类型。作者提出了RAME（检索增强多提示集成）框架，这是一种免训练方法，通过在受控多样性下生成多个大语言模型输出，并通过多数投票聚合获得高置信度预测。RAME结合了基于混合BM25-嵌入检索器的检索增强小样本选择、覆盖精度到召回率谱系的三提示集成（严格、宽松、均衡），以及大规模重复采样与多数投票以过滤噪声预测。基于DeepSeek-V4-Flash，RAME在排行榜上取得了0.499的总分（NER 0.730，RE 0.346），排名第一，超越了由GPT-5.5驱动的官方Track-A基线（0.448），相对提升11.4%。代码已公开。

**核心创新概述**

> 提出一种无需训练的检索增强多提示集成方法用于小杂粮育种文献的实体和关系联合抽取，并在竞赛中取得最佳成绩。

**创新点拆解**

- 提出RAME框架，无需微调，通过多提示集成和多数投票提升信息抽取性能。
- 使用混合BM25-嵌入检索器进行少样本选择，增强提示样例质量。
- 设计覆盖不同精度/召回偏好的三提示（严格、宽松、均衡）集成，平衡抽取效果。
- 采用大规模重复采样与多数投票策略，有效过滤噪声预测，提高置信度。

**当前局限**

> 该方法依赖大语言模型的生成能力，对于稀有实体或复杂关系可能存在提取不完整；多数投票可能忽略部分低置信度但正确的预测；整体分数（特别是关系抽取）仍有较大提升空间。

**后续可改进方向**

- 探索针对低资源领域（如育种文献）的轻量级微调或适配方法，以减少对通用LLM的依赖。
- 改进关系抽取的推理策略，例如引入链式思考或结构化约束解码。
- 研究更优的集成投票机制，如置信度加权投票或基于验证集动态调整提示权重。

**工程启发**

> 该框架为小样本、免训练的信息抽取提供了一种实用方案，可快速部署到新领域，对农业文献知识服务有实际应用价值。

**为什么值得关注**

> 本研究针对特定垂直领域的文档信息抽取，展示了如何通过检索增强和提示集成提升LLM的抽取能力，对构建领域知识图谱和智能育种平台具有参考意义。

**原始摘要**

This paper presents our system for CCL2026-Eval Task 5: Minor-Grain Breeding Information Extraction
(MGBIE), which jointly extracts 12 entity types and 6 relation types from minor-grain breeding
literature. We propose RAME (Retrieval-Augmented Multi-Prompt Ensemble), a training-free framework
that elicits multiple LLM outputs under controlled diversity and aggregates them by majority voting
to obtain high-confidence predictions. RAME combines (i) retrieval-augmented few-shot selection via
a hybrid BM25-embedding retriever, (ii) a three-prompt ensemble (Strict, Relaxed, Balanced) spanning
the precision to recall spectrum, and (iii) large-scale repeated sampling with majority voting to
filter noisy predictions. Built on DeepSeek-V4-Flash, RAME achieves a Total Score of 0.499 (NER
0.730, RE 0.346) on the leaderboard, ranking 1st and surpassing the official Track-A baseline
powered by GPT-5.5 (0.448), representing an 11.4% relative improvement. Code is available at
https://github.com/king-wang123/CCL26-RAME.

---
