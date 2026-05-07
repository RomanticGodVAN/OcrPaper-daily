# OCR / 文档解析研究日报（2026-05-07）

## 报告说明

- 检索源：arXiv API
- 检索查询：`(all:"document parsing" OR all:"document understanding" OR all:"optical character recognition" OR all:OCR OR all:"layout analysis" OR all:"document layout analysis" OR all:"text recognition" OR all:"table recognition" OR all:"form understanding" OR all:"document intelligence" OR all:"page understanding" OR all:"scene text recognition" OR all:"handwritten text recognition" OR all:"information extraction") AND (cat:cs.CV OR cat:cs.AI OR cat:cs.CL OR cat:eess.IV)`
- 生成时间（UTC）：`2026-05-07 04:44:57`
- 大模型综合分析：`开启`

## 一、今日执行摘要

> 今日研究涵盖OCR基准、多模态智能体、低资源NER、临床信息提取和多模态搜索智能体，聚焦文档解析与信息提取的实际应用优化。核心趋势是大型模型性能在真实场景下降明显，而以模块化、轻量级和领域特定方案为特征的混合方法成为提升实用性的关键方向。

## 二、今日趋势判断

研究重心从单一模型评测转向系统性能力评估与可复现开源方案；在实际部署中，模块化多智能体架构和自提示优化等轻量级方案受到关注；低资源与隐私敏感场景推动更高效、可本地化的NER方法发展。

## 三、今日论文概览

1. **CC-OCR V2: Benchmarking Large Multimodal Models for Literacy in Real-world Document Processing** | 标签：OCR基准、多模态大模型、文档处理、真实场景评估、文本识别、文档解析、关键信息提取、文档问答
2. **Material Database Agent: A Multimodal Agentic Framework for Scientific Literature Mining** | 标签：文献挖掘、多模态信息提取、智能体系统、科学数据库、PDF处理、材料科学
3. **Self-Prompting Small Language Models for Privacy-Sensitive Clinical Information Extraction** | 标签：临床NER、小型语言模型、提示优化、DPO、隐私保护、信息提取
4. **OpenSearch-VL: An Open Recipe for Frontier Multimodal Search Agents** | 标签：多模态搜索、智能体、强化学习、OCR、图像处理、开源方案
5. **A Hybrid Method for Low-Resource Named Entity Recognition** | 标签：低资源NER、混合方法、规则学习、数据增强、LLM、越南语
6. **Geolocating News about Extreme Climate Events: A Comparative Analysis of Off-the-Shelf Tools for Toponym Identification in German** | 标签：NER比较、地理定位、气候事件、德语、信息提取

## 四、今天 OCR / 文档解析论文里的主要创新点

- 多模态搜索智能体OpenSearch-VL集成OCR、图像处理等多工具，通过强化学习提升多步推理鲁棒性。
- CC-OCR V2基准涵盖5个核心OCR任务，聚焦真实文档处理中的硬例与边界情况。
- 材料数据库代理采用多智能体并行处理PDF文本与图表，自动化构建结构化数据库。
- 自提示小语言模型框架结合自动提示优化与DPO，实现隐私友好的临床NER。
- 混合NER框架利用规则降低标签复杂度，再微调预训练模型，配合LLM数据增强解决低资源问题。

## 五、后续 OCR 领域值得推进的改进方向

- 开发针对真实文档硬例（如模糊、倾斜、复杂版面）的专项训练数据与评估方法。
- 构建模块化多智能体系统，实现文档处理中文本、图表、表格的协同提取。
- 探索自动提示生成与偏好优化结合的微调策略，减少对人工标注的依赖。
- 设计可复现的开源搜索/信息提取智能体，集成视觉与语言工具的协同调用。
- 研究基于规则与深度学习的混合架构，提升低资源语言NER的领域迁移能力。

## 六、工程落地启发

- 企业选型时应采用CC-OCR V2这类真实基准评估模型，而非仅依赖学术基准。
- 材料数据库代理的模块化设计可复用至领域文献挖掘，需并行处理多种输入格式。
- 自提示小模型适合医患数据本地部署，结合QLoRA与DPO可控制性能与隐私。
- OpenSearch-VL的全开源方案为构建多模态搜索智能体提供了可复现基线。
- 低资源NER优化可从规则简化标签体系与LLM数据增强两个方向入手。

## 七、优先关注论文

- **CC-OCR V2: Benchmarking Large Multimodal Models for Literacy in Real-world Document Processing**：提供了最贴近企业实用的OCR基准，后续版本更新和模型在基准上的表现直接影响产品选型。
- **OpenSearch-VL: An Open Recipe for Frontier Multimodal Search Agents**：开源的多模态搜索智能体方案，其训练数据和算法可复用于文档搜索、检索增强生成等场景。

## 八、论文逐篇解析

### 1. CC-OCR V2: Benchmarking Large Multimodal Models for Literacy in Real-world Document Processing

- arXiv: [2605.03903v1](https://arxiv.org/abs/2605.03903v1)
- PDF: [下载链接](https://arxiv.org/pdf/2605.03903v1)
- 作者: Zhipeng Xu, Junhao Ji, Zulong Chen, Zhenghao Liu, Qing Liu, Chunyi Peng, Zubao Qin, Ze Xu, Jianqiang Wan, Jun Tang, Zhibo Yang, Shuai Bai, Dayiheng Liu
- 发布时间: 2026-05-05T15:56:12Z
- 分类: cs.CL
- 相关性评分: 33
- 主题标签: OCR基准、多模态大模型、文档处理、真实场景评估、文本识别、文档解析、关键信息提取、文档问答

**中文摘要**

> 本文提出CC-OCR V2基准测试，用于评估大型多模态模型在真实世界文档处理中的识字能力。该基准涵盖5个OCR核心任务（文本识别、文档解析、文档定位、关键信息提取、文档问答），包含7093个高难度样本。对14个先进LMM的广泛实验表明，现有模型在真实应用场景中性能显著下降，与现有基准上的表现存在较大差距。数据集和评估工具已开源。

**核心创新概述**

> 提出了针对真实世界文档处理的综合性OCR基准，聚焦实际企业文档任务中的硬例和边界情况，填补了现有基准与实际应用之间的差距。

**创新点拆解**

- 设计覆盖5个OCR核心任务的高难度基准，共7093个样本
- 重点关注实际企业文档处理中的硬例和边界情况
- 提供开源数据集和评估工具

**当前局限**

> 当前LMM在真实多样化场景下性能退化严重，离实际应用要求仍有较大差距。

**后续可改进方向**

- 提升模型在多样化采集条件和复杂文档结构下的鲁棒性
- 针对真实文档处理场景中的硬例和边界情况进行专项优化

**工程启发**

> 为企业级文档处理系统选择或评估LMM提供了更贴近实际的测试基准和工具。

**为什么值得关注**

> 直接关注OCR在真实应用中的瓶颈，对提升文档理解系统的实用价值有重要指导意义。

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

### 2. Material Database Agent: A Multimodal Agentic Framework for Scientific Literature Mining

- arXiv: [2605.04278v1](https://arxiv.org/abs/2605.04278v1)
- PDF: [下载链接](https://arxiv.org/pdf/2605.04278v1)
- 作者: Achuth Chandrasekhar, Omid Barati Farimani, Radheesh Sharma Meda, Amir Barati Farimani
- 发布时间: 2026-05-05T20:30:45Z
- 分类: cs.CL
- 相关性评分: 11
- 主题标签: 文献挖掘、多模态信息提取、智能体系统、科学数据库、PDF处理、材料科学

**中文摘要**

> 本文提出材料数据库代理（MDA），一个模块化的多智能体系统架构，用于将科研文献自动转化为结构化数据库。MDA以PDF为输入，并行处理为markdown文件和图表，多个子智能体分别提取信息形成子数据库，最终由智能体合并为单一表格数据库。该方法专为材料科学领域设计，展示了将多模态智能体信息提取用于构建下一代科学数据库的可行性。

**核心创新概述**

> 提出了一种模块化多智能体系统，专门用于将材料科学文献自动转化为结构化数据库，区别于规则方法或单轮管道。

**创新点拆解**

- 多智能体并行处理PDF文献，包括文本和图表
- 分步组装子数据库并合并为统一表格数据库
- 专为材料科学领域的信息提取定制架构

**当前局限**

> 目前局限于材料科学领域，通用性尚未验证；依赖多模态大语言模型的准确性。

**后续可改进方向**

- 扩展到其他科学领域
- 提升对图表中复杂信息的提取精度

**工程启发**

> 可大幅减少人工构建科学数据库的时间和成本，支撑材料科学的数据驱动研究。

**为什么值得关注**

> 展示了多模态信息提取在科学文献自动化处理中的实用价值，与OCR和文档理解技术密切相关。

**原始摘要**

Materials science workflows rely on structured and unstructured data from the vast body of available
scientific literature. However, most of the experimental details remain buried in text, tables,
graphs and figures. Thus, constructing databases that incorporate this data is a manual, time-
consuming, and hard-to-scale process. Multimodal large language models have made it feasible to
extract information from text and scientific figures with high speed and accuracy. This opens the
possibility of an AI system that can create production-scale material databases. Material Database
Agent (MDA) is a modular, multi-agent system architecture for converting research literature into
structured databases. MDA accepts article PDFs as input, which are subsequently processed in
parallel into markdown files and figures. Multiple sub-agents read these markdown files and figures
in parallel to assemble sub-databases for each paper. These sub-databases are then compiled into a
single tabular database by an agent. As opposed to using either a rule-based approach or a single-
pass pipeline for extracting information, MDA is a specialized architecture for transforming the
literature into a database in the field of materials science. More generally, this study provides a
basis for positioning multimodal agentic information extraction as a viable means for constructing
next-generation scientific databases from the primary literature.

---

### 3. Self-Prompting Small Language Models for Privacy-Sensitive Clinical Information Extraction

- arXiv: [2605.04221v1](https://arxiv.org/abs/2605.04221v1)
- PDF: [下载链接](https://arxiv.org/pdf/2605.04221v1)
- 作者: Yao-Shun Chuang, Tushti Mody, Uday Pratap Singh, Shirindokht Shiraz, Chun-Teh Lee, Ryan Brandon, Muhammad F Walji, Xiaoqian Jiang, Bunmi Tokede
- 发布时间: 2026-05-05T19:03:40Z
- 分类: cs.CL, cs.AI
- 相关性评分: 10
- 主题标签: 临床NER、小型语言模型、提示优化、DPO、隐私保护、信息提取

**中文摘要**

> 本文针对牙科记录中隐私敏感的临床命名实体识别问题，提出一个可本地部署的框架，使小型语言模型能够自我生成、验证、优化和评估实体特定提示。使用1200条标注笔记，结合多提示集成推理和基于QLoRA的微调及直接偏好优化（DPO），Qwen2.5-14B-Instruct在DPO后达到micro/macro F1分数0.864/0.837。研究表明自动提示优化与轻量级偏好后训练可支持可扩展的临床信息提取。

**核心创新概述**

> 提出小型语言模型自提示框架，结合自动提示优化与轻量级偏好后训练，用于隐私敏感的临床NER。

**创新点拆解**

- 自生成、验证、优化和评估实体特定提示的流程
- 多提示集成推理与QLoRA微调及DPO结合
- 本地可部署，保护隐私

**当前局限**

> 仅针对牙科领域，模型性能因任务而异，依赖高质量标注数据。

**后续可改进方向**

- 扩展至其他医疗领域
- 减少对标注数据的依赖

**工程启发**

> 提供了一种可本地部署、保护隐私的临床信息提取方案，适用于医疗机构的实际应用。

**为什么值得关注**

> 涉及到非结构化文档（牙科记录）中的信息提取，与OCR和文档解析的后续处理相关。

**原始摘要**

Clinical named entity recognition from dental progress notes is challenging because documentation is
highly unstructured, domain-specific, and often privacy-sensitive. We developed a locally deployable
framework that enables small language models to self-generate, verify, refine, and evaluate entity-
specific prompts for extracting multiple clinical entities from dental notes. Using 1,200 annotated
notes, we evaluated candidate open-weight models with multi-prompt ensemble inference and further
adapted selected models using QLoRA-based supervised fine-tuning and direct preference optimization.
Model performance varied substantially, highlighting the need for task-specific evaluation rather
than reliance on generic benchmarks. Qwen2.5-14B-Instruct achieved the strongest baseline
performance. After DPO, Qwen2.5-14B-Instruct and Llama-3.1-8B-Instruct achieved micro/macro F1
scores of 0.864/0.837 and 0.806/0.797, respectively. These findings suggest that automated prompt
optimization combined with lightweight preference-based post-training can support scalable clinical
information extraction using locally deployed small language models.

---

### 4. OpenSearch-VL: An Open Recipe for Frontier Multimodal Search Agents

- arXiv: [2605.05185v1](https://arxiv.org/abs/2605.05185v1)
- PDF: [下载链接](https://arxiv.org/pdf/2605.05185v1)
- 作者: Shuang Chen, Kaituo Feng, Hangting Chen, Wenxuan Huang, Dasen Dai, Quanxin Shou, Yunlong Lin, Xiangyu Yue, Shenghua Gao, Tianyu Pang
- 发布时间: 2026-05-06T17:50:38Z
- 分类: cs.CV
- 相关性评分: 9
- 主题标签: 多模态搜索、智能体、强化学习、OCR、图像处理、开源方案

**中文摘要**

> 本文提出OpenSearch-VL，一个完全开源的前沿多模态搜索智能体训练方案，包括高质量训练数据构建、多样化工具体系和多轮致命感知GRPO训练算法。该方案在7个基准上平均提升超过10个点，性能可与商业专有模型媲美。数据构建通过Wikipedia路径采样、模糊实体重写和源锚视觉定位减少捷径和一步检索崩溃。工具体系统一了文本搜索、图像搜索、OCR、裁剪、锐化、超分辨率和透视校正。

**核心创新概述**

> 提出了首个完全开源的多模态深度搜索智能体训练方案，包含创新性数据构建和训练算法。

**创新点拆解**

- Wikipedia路径采样与模糊实体重写的数据构建方法
- 源锚视觉定位减少检索捷径
- 多样化工具体系，集成OCR、图像处理等
- 多轮致命感知GRPO算法处理工具级联失败

**当前局限**

> 性能提升显著，但与最先进商业模型仍有差距（原文未明确）。

**后续可改进方向**

- 进一步提升视觉理解能力
- 增强在复杂多步推理中的鲁棒性

**工程启发**

> 提供了可复现的先进多模态搜索智能体训练方案，为实际部署提供开源基础。

**为什么值得关注**

> 集成了OCR作为重要工具，且任务涉及文档图像理解，与OCR的实际应用紧密相关。

**原始摘要**

Deep search has become a crucial capability for frontier multimodal agents, enabling models to solve
complex questions through active search, evidence verification, and multi-step reasoning. Despite
rapid progress, top-tier multimodal search agents remain difficult to reproduce, largely due to the
absence of open high-quality training data, transparent trajectory synthesis pipelines, or detailed
training recipes. To this end, we introduce OpenSearch-VL, a fully open-source recipe for training
frontier multimodal deep search agents with agentic reinforcement learning. First, we curated a
dedicated pipeline to construct high-quality training data through Wikipedia path sampling, fuzzy
entity rewriting, and source-anchor visual grounding, which jointly reduce shortcuts and one-step
retrieval collapse. Based on this pipeline, we curate two training datasets, SearchVL-SFT-36k for
SFT and SearchVL-RL-8k for RL. Besides, we design a diverse tool environment that unifies text
search, image search, OCR, cropping, sharpening, super-resolution, and perspective correction,
enabling agents to combine active perception with external knowledge acquisition. Finally, we
propose a multi-turn fatal-aware GRPO training algorithm that handles cascading tool failures by
masking post-failure tokens while preserving useful pre-failure reasoning through one-sided
advantage clamping. Built on this recipe, OpenSearch-VL delivers substantial performance gains, with
over 10-point average improvements across seven benchmarks, and achieves results comparable to
proprietary commercial models on several tasks. We will release all data, code, and models to
support open research on multimodal deep search agents.

---

### 5. A Hybrid Method for Low-Resource Named Entity Recognition

- arXiv: [2605.04489v1](https://arxiv.org/abs/2605.04489v1)
- PDF: [下载链接](https://arxiv.org/pdf/2605.04489v1)
- 作者: Do Minh Duc, Quan Xuan Truong, Viet Tran Hong, Le Hoang Anh, Mac Thi Minh Tra, Nguyen Van Thuy, Le Hai Ha, Vinh Nguyen Van
- 发布时间: 2026-05-06T04:36:01Z
- 分类: cs.CE, cs.AI, cs.CL
- 相关性评分: 6
- 主题标签: 低资源NER、混合方法、规则学习、数据增强、LLM、越南语

**中文摘要**

> 本文针对低资源语言（越南语）的命名实体识别，提出一种混合神经符号框架，结合规则处理和深度学习模型。该框架采用两阶段流水线：先由规则组件通过分组关系类别降低标签复杂度，再微调预训练语言模型进行高精度提取，最后通过后处理恢复细粒度标签。利用LLM进行数据增强解决数据稀缺问题。在5个特定领域数据集上取得显著提升，F1分数最高提升24个百分点。

**核心创新概述**

> 提出结合规则与深度学习的混合框架，并利用LLM进行数据增强解决低资源NER问题，具有实用性。

**创新点拆解**

- 两阶段混合方法：规则消歧 + 深度学习提取 + 后处理恢复标签
- 利用LLM进行可扩展的数据增强，避免完整重标注
- 针对低资源语言的特定领域设计

**当前局限**

> 依赖规则设计的质量，领域迁移可能需要重新设计规则。

**后续可改进方向**

- 探索更自动化的规则生成方法
- 提升对跨领域标签集合的适应性

**工程启发**

> 为低资源语言在特定领域的NER提供了高效且实用的解决方案，显著提升性能。

**为什么值得关注**

> 低资源NER与文档理解中信息提取相关，尤其对于非英文文档的处理有借鉴意义。

**原始摘要**

Named Entity Recognition (NER) is a critical component of Natural Language Processing with diverse
applications in information extraction and conversational AI. However, NER in specific domains for
low-resource languages faces challenges such as limited annotated data and heterogeneous label sets.
This study addresses these issues by proposing a hybrid neurosymbolic framework that integrates
rule-based processing with deep learning models for Vietnamese NER. The core idea involves a two-
stage pipeline: first, a rule-based component reduces label complexity by grouping relational and
special categories; second, pre-trained language models are fine-tuned for high-precision
extraction. A post-processing module is then utilized to restore fine-grained labels, preserving
expressiveness for application-level usability. To mitigate data scarcity, a scalable data
augmentation strategy leveraging Large Language Models (LLMs) is introduced to expand the label set
without full re-annotation, which is a significant novelty of this work. The effectiveness of this
method was evaluated across five specific-domain datasets, including logistics, wildlife, and
healthcare. Experimental results demonstrate substantial improvements over strong RoBERTa-based
baselines. Specifically, the proposed system achieved F1 scores of 90 percent in Customer Service,
up from 83 percent; 84 percent in GAM, up from 73 percent; 83 percent in AI Fluent, up from 80
percent; 94 percent in PhoNER_Covid19, up from 91 percent; and 60 percent in Rare Wildlife, up from
36 percent. These findings confirm that the hybrid approach effectively captures the linguistic
complexity of Vietnamese and contextual nuances in specialized domains, offering a robust
contribution to low-resource NER research.

---

### 6. Geolocating News about Extreme Climate Events: A Comparative Analysis of Off-the-Shelf Tools for Toponym Identification in German

- arXiv: [2605.03414v1](https://arxiv.org/abs/2605.03414v1)
- PDF: [下载链接](https://arxiv.org/pdf/2605.03414v1)
- 作者: Brielen Madureira, Mariana Madruga de Brito, Andreas Niekler
- 发布时间: 2026-05-05T06:40:26Z
- 分类: cs.CL
- 相关性评分: 4
- 主题标签: NER比较、地理定位、气候事件、德语、信息提取

**中文摘要**

> 本文对三种现有的命名实体识别工具（Flair、Spacy、Stanza）在德语新闻文章中识别极端气候事件地名方面进行了比较分析。通过外在评估方法（确定事件发生国家），展示了不同工具的输出差异如何传播到下游任务，并可能影响关于国家媒体关注度的结论。

**核心创新概述**

> 系统比较了三种NER工具在德语新闻中识别气候事件地名的性能差异及其对下游任务的影响。

**创新点拆解**

- 对三种NER工具进行外在评估，关注下游决策影响
- 量化工具输出差异对地理焦点确定的影响

**当前局限**

> 仅针对德语新闻和极端气候事件，可能不具广泛通用性。

**后续可改进方向**

- 扩展评估至更多语言和事件类型
- 改进NER工具对地理上下文的理解

**工程启发**

> 为用户在选择NER工具用于地理定位任务时提供了实证依据。

**为什么值得关注**

> 涉及文档中地名识别，是OCR后处理（信息提取）的重要步骤。

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
