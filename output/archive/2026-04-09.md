# OCR / 文档解析研究日报（2026-04-09）

## 报告说明

- 检索源：arXiv API
- 检索查询：`(all:"document parsing" OR all:"document understanding" OR all:"optical character recognition" OR all:OCR OR all:"layout analysis" OR all:"document layout analysis" OR all:"text recognition" OR all:"table recognition" OR all:"form understanding" OR all:"document intelligence" OR all:"page understanding" OR all:"scene text recognition" OR all:"handwritten text recognition" OR all:"information extraction") AND (cat:cs.CV OR cat:cs.AI OR cat:cs.CL OR cat:eess.IV)`
- 生成时间（UTC）：`2026-04-09 04:05:07`
- 大模型综合分析：`开启`

## 一、今日执行摘要

> 今日研究聚焦于提升OCR与文档解析的准确性、效率及可信度。核心进展包括：通过多阶段验证框架与LLM辅助路径显著提升提取质量（如临床信息提取F1达0.80，失踪人员案例F1达0.8664）；引入字符错误向量（CEV）实现错误源分解，为评估提供新视角；通过查询感知自适应（Q-Zoom）和线性复杂度机制（PoM）优化计算效率，推理加速最高达4.39倍。同时，对抗性走私攻击研究揭示了OCR在安全审核中的脆弱性（攻击成功率>90%），凸显鲁棒性增强的紧迫性。整体趋势显示，研究正从单一精度提升转向精度、效率、可信度与安全的协同优化，并积极探索弱监督与多模态集成方法。

## 二、今日趋势判断

当前研究呈现四大趋势：1）精度与可信度并重：通过多阶段验证、LLM辅助提取与模式验证框架（如Guardian Parser、临床提取框架）提升复杂场景下的提取可靠性与可解释性，减少对人工标注的依赖。2）效率优化成为焦点：采用查询感知自适应（Q-Zoom）、线性复杂度替代注意力（PoM）及动态门控机制，针对长文档或高分辨率输入减少冗余计算，平衡速度与精度。3）评估指标细化：突破传统CER局限，引入可分解错误源的CEV指标，助力定位解析、OCR及交互错误，优化文档理解流水线。4）安全与鲁棒性受关注：对抗性攻击研究（如走私攻击）暴露OCR/MLLM在内容审核中的漏洞，推动防御机制如对抗训练与多模态分析的发展。

## 三、今日论文概览

1. **LLM-based Schema-Guided Extraction and Validation of Missing-Person Intelligence from Heterogeneous Data Sources** | 标签：文档解析、模式验证、LLM辅助提取、多源数据集成、OCR备用
2. **The Character Error Vector: Decomposable errors for page-level OCR evaluation** | 标签：OCR评估、字符错误向量、页面解析、错误分解、文档理解
3. **Q-Zoom: Query-Aware Adaptive Perception for Efficient Multimodal Large Language Models** | 标签：MLLMs、自适应感知、查询感知、文档理解、OCR优化
4. **PoM: A Linear-Time Replacement for Attention with the Polynomial Mixer** | 标签：自注意力替代、多项式混合器、线性复杂度、手写文本识别、令牌混合
5. **Assessing the Added Value of Onboard Earth Observation Processing with the IRIDE HEO Service Segment** | 标签：地球观测、机载处理、服务导向架构、图像分析、遥感
6. **Making MLLMs Blind: Adversarial Smuggling Attacks in MLLM Content Moderation** | 标签：对抗性攻击、内容审核、OCR鲁棒性、MLLMs安全、视觉编码
7. **A Multi-Stage Validation Framework for Trustworthy Large-scale Clinical Information Extraction using Large Language Models** | 标签：临床信息提取、大型语言模型、弱监督验证、多阶段框架、医疗文档解析

## 四、今天 OCR / 文档解析论文里的主要创新点

- 集成LLM辅助提取与规则验证，提升复杂文档的提取精度和模式一致性。
- 采用动态门控或区域提议网络，实现查询感知的自适应处理以减少计算冗余。
- 引入可分解错误源的评估指标（如CEV），细化OCR与解析错误分析。
- 构建多阶段验证框架，结合规则过滤、语义评估和LLM法官降低人工标注需求。
- 探索线性复杂度机制（如PoM）作为自注意力替代，优化长序列处理效率。

## 五、后续 OCR 领域值得推进的改进方向

- 开发轻量化LLM路径优化技术，如模型压缩或并行处理，以降低高精度提取的时间开销。
- 扩展CEV指标到多语言、手写文本或低质量图像场景，提升错误分解的泛化能力。
- 集成对抗训练或测试时增强到OCR模型中，防御针对文本识别的感知盲区攻击。
- 研究实时自适应机制，动态调整文档解析的分辨率或处理区域以减少延迟。
- 探索多模态数据（如时间序列或图像特征）与文本的语义基础融合，增强临床等领域的提取可信度。
- 优化机载处理算法，将其应用于文档图像分析以实现边缘设备的快速OCR。
- 开发自适应规则生成方法，减少多阶段验证框架中的人工规则设计偏差。

## 六、工程落地启发

- 在执法或医疗文档处理中，可部署多阶段验证框架或LLM辅助路径，以高精度提取关键字段（如失踪人员信息或临床诊断）。
- 采用Q-Zoom或类似查询感知机制，优化MLLMs在文档OCR任务中的推理速度，适用于资源受限环境。
- 将CEV集成到OCR评估流水线，帮助识别和优先修复解析或OCR错误，提升整体文档理解质量。
- 在内容审核系统中，加强OCR模型鲁棒性并集成多模态防御，以抵抗对抗性走私攻击。
- 考虑用PoM等线性复杂度机制替换自注意力，降低长文档处理的计算成本，适用于大规模批量处理。

## 七、优先关注论文

- **LLM-based Schema-Guided Extraction and Validation of Missing-Person Intelligence from Heterogeneous Data Sources**：系统集成多引擎提取与LLM辅助路径，在失踪人员调查中实现高精度提取（F1=0.8664），可直接应用于执法机构提升效率。
- **The Character Error Vector: Decomposable errors for page-level OCR evaluation**：CEV指标可分解解析、OCR和交互错误，为评估文档理解流水线提供新工具，有助于针对性优化。
- **Q-Zoom: Query-Aware Adaptive Perception for Efficient Multimodal Large Language Models**：框架通过自适应感知加速MLLMs推理达4.39倍，在文档OCR任务中平衡速度与精度，适合集成到实时系统。
- **Making MLLMs Blind: Adversarial Smuggling Attacks in MLLM Content Moderation**：揭示OCR鲁棒性差距导致的高成功率攻击（>90%），对安全关键应用（如内容审核）有直接警示，需优先防御。
- **A Multi-Stage Validation Framework for Trustworthy Large-scale Clinical Information Extraction using Large Language Models**：框架通过弱监督验证实现大规模临床提取（F1=0.80），减少人工标注，可扩展至其他OCR任务提升可信度。

## 八、论文逐篇解析

### 1. LLM-based Schema-Guided Extraction and Validation of Missing-Person Intelligence from Heterogeneous Data Sources

- arXiv: [2604.06571v1](https://arxiv.org/abs/2604.06571v1)
- PDF: [下载链接](https://arxiv.org/pdf/2604.06571v1)
- 作者: Joshua Castillo, Ravi Mukkamala
- 发布时间: 2026-04-08T01:35:56Z
- 分类: cs.CL, cs.AI, cs.IR, cs.LG
- 相关性评分: 34
- 主题标签: 文档解析、模式验证、LLM辅助提取、多源数据集成、OCR备用

**中文摘要**

> 失踪人员调查依赖异构文档，如结构化表格和海报，其布局和术语差异阻碍分析。本文提出Guardian Parser Pack，一个AI驱动的解析和归一化流水线，将多源文档转换为统一表示。系统集成多引擎PDF文本提取（含OCR备用）、基于规则的源识别、模式优先协调验证，以及可选的LLM辅助提取路径。在75个案例子集上，LLM路径提取质量显著高于确定性路径（F1=0.8664 vs. 0.2578），在517条记录中提高关键字段完整性（96.97% vs. 93.23%），但确定性路径更快（0.03秒/记录 vs. 3.95秒/记录）。

**核心创新概述**

> 提出一个集成多源异构文档解析的系统，结合确定性规则和LLM辅助路径，实现高精度提取和模式验证，特别针对失踪人员调查场景。

**创新点拆解**

- 多引擎PDF文本提取与OCR备用机制
- 基于规则的源识别与源特定解析器
- 模式优先的协调和验证框架
- LLM辅助提取路径，结合验证器引导修复和共享地理编码服务

**当前局限**

> LLM辅助路径运行时间较长，可能不适合实时或大规模处理；系统依赖手动对齐子集进行评估，泛化性未充分验证。

**后续可改进方向**

- 优化LLM路径的效率，如通过模型压缩或并行处理
- 扩展系统到更多文档类型和语言，增强泛化能力
- 集成更先进的OCR技术以减少解析错误

**工程启发**

> 高，系统可直接应用于执法或救援机构的文档处理流程，提高失踪人员调查效率，支持下游空间建模。

**为什么值得关注**

> 涉及OCR作为备用文本提取方法，强调文档解析和归一化，对OCR在异构数据源处理中的应用有参考价值。

**原始摘要**

Missing-person and child-safety investigations rely on heterogeneous case documents, including
structured forms, bulletin-style posters, and narrative web profiles. Variations in layout,
terminology, and data quality impede rapid triage, large-scale analysis, and search-planning
workflows. This paper introduces the Guardian Parser Pack, an AI-driven parsing and normalization
pipeline that transforms multi-source investigative documents into a unified, schema-compliant
representation suitable for operational review and downstream spatial modeling. The proposed system
integrates (i) multi-engine PDF text extraction with Optical Character Recognition (OCR) fallback,
(ii) rule-based source identification with source-specific parsers, (iii) schema-first harmonization
and validation, and (iv) an optional Large Language Model (LLM)-assisted extraction pathway
incorporating validator-guided repair and shared geocoding services. We present the system
architecture, key implementation decisions, and output design, and evaluate performance using both
gold-aligned extraction metrics and corpus-level operational indicators. On a manually aligned
subset of 75 cases, the LLM-assisted pathway achieved substantially higher extraction quality than
the deterministic comparator (F1 = 0.8664 vs. 0.2578), while across 517 parsed records per pathway
it also improved aggregate key-field completeness (96.97\% vs. 93.23\%). The deterministic pathway
remained much faster (mean runtime 0.03 s/record vs. 3.95 s/record for the LLM pathway). In the
evaluated run, all LLM outputs passed initial schema validation, so validator-guided repair
functioned as a built-in safeguard rather than a contributor to the observed gains. These results
support controlled use of probabilistic AI within a schema-first, auditable pipeline for high-stakes
investigative settings.

---

### 2. The Character Error Vector: Decomposable errors for page-level OCR evaluation

- arXiv: [2604.06160v1](https://arxiv.org/abs/2604.06160v1)
- PDF: [下载链接](https://arxiv.org/pdf/2604.06160v1)
- 作者: Jonathan Bourne, Mwiza Simbeye, Joseph Nockels
- 发布时间: 2026-04-07T17:56:06Z
- 分类: cs.CV, cs.LG
- 相关性评分: 29
- 主题标签: OCR评估、字符错误向量、页面解析、错误分解、文档理解

**中文摘要**

> 字符错误率（CER）是评估OCR质量的关键指标，但假设文本完美解析，在页面解析错误时未定义，限制了其使用。本文引入字符错误向量（CEV），一个用于OCR的字符袋评估器，可分解为解析、OCR和交互错误组件。这种可分解性允许从业者关注文档理解流水线中对整体提取质量影响最大的部分。CEV可通过多种方法实现，如SpACER和基于Jensen-Shannon距离的字符分布方法。验证显示CEV是解析指标与CER等局部指标之间的有价值桥梁。在归档报纸数据集上分析发现，传统流水线方法优于端到端模型。CEV需要字符级定位以优化分类，但基于阈值可预测主要错误源（F1=0.91）。

**核心创新概述**

> 提出CEV作为页面级OCR评估的新指标，可分解错误来源，弥补CER在解析错误下的不足，提供更全面的质量分析。

**创新点拆解**

- 字符错误向量（CEV）作为可分解的页面级评估指标
- 错误分解为解析、OCR和交互组件
- 实现方法如SpACER和字符分布方法
- 验证CEV作为解析与局部指标之间的桥梁

**当前局限**

> CEV需要字符级定位数据，可能增加标注成本；在复杂布局或低质量图像上性能未充分测试。

**后续可改进方向**

- 开发更高效的CEV计算算法，减少计算开销
- 扩展CEV到多语言或手写文本场景
- 集成CEV到OCR训练流程，以端到端优化模型

**工程启发**

> 中等，CEV可作为OCR系统评估工具，帮助识别和修复解析与OCR错误，提升文档理解流水线质量。

**为什么值得关注**

> 直接针对OCR评估问题，提出新指标以改进页面级性能分析，对OCR研究和应用有重要意义。

**原始摘要**

The Character Error Rate (CER) is a key metric for evaluating the quality of Optical Character
Recognition (OCR). However, this metric assumes that text has been perfectly parsed, which is often
not the case. Under page-parsing errors, CER becomes undefined, limiting its use as a metric and
making evaluating page-level OCR challenging, particularly when using data that do not share a
labelling schema. We introduce the Character Error Vector (CEV), a bag-of-characters evaluator for
OCR. The CEV can be decomposed into parsing and OCR, and interaction error components. This
decomposability allows practitioners to focus on the part of the Document Understanding pipeline
that will have the greatest impact on overall text extraction quality. The CEV can be implemented
using a variety of methods, of which we demonstrate SpACER (Spatially Aware Character Error Rate)
and a Character distribution method using the Jensen-Shannon Distance. We validate the CEV's
performance against other metrics: first, the relationship with CER; then, parse quality; and
finally, as a direct measure of page-level OCR quality. The validation process shows that the CEV is
a valuable bridge between parsing metrics and local metrics like CER. We analyse a dataset of
archival newspapers made of degraded images with complex layouts and find that state-of-the-art end-
to-end models are outperformed by more traditional pipeline approaches. Whilst the CEV requires
character-level positioning for optimal triage, thresholding on easily available values can predict
the main error source with an F1 of 0.91. We provide the CEV as part of a Python library to support
Document understanding research.

---

### 3. Q-Zoom: Query-Aware Adaptive Perception for Efficient Multimodal Large Language Models

- arXiv: [2604.06912v1](https://arxiv.org/abs/2604.06912v1)
- PDF: [下载链接](https://arxiv.org/pdf/2604.06912v1)
- 作者: Yuheng Shi, Xiaohuan Pei, Linfeng Wen, Minjing Dong, Chang Xu
- 发布时间: 2026-04-08T10:12:30Z
- 分类: cs.CV, cs.AI
- 相关性评分: 17
- 主题标签: MLLMs、自适应感知、查询感知、文档理解、OCR优化

**中文摘要**

> MLLMs需要高分辨率视觉输入以进行细粒度任务，但当前全局分辨率缩放范式在自注意力机制中引入冗余令牌，降低推理吞吐量。本文提出Q-Zoom，一个查询感知的自适应高分辨率感知框架，以粗到细方式操作。首先，轻量级动态门控网络在粗全局特征足够时绕过高分辨率处理；其次，对于需要细粒度感知的查询，自蒸馏区域提议网络从中间特征空间精确定位任务相关区域。通过一致性感知生成策略和自监督蒸馏优化模块。实验显示，在文档和OCR基准上，Q-Zoom加速推理2.52倍，在高分辨率场景加速4.39倍，同时匹配基线峰值精度。

**核心创新概述**

> 提出Q-Zoom框架，通过查询感知自适应机制，动态选择高分辨率处理区域，减少冗余计算，提升MLLMs在文档理解等任务中的效率。

**创新点拆解**

- 查询感知自适应高分辨率感知框架
- 动态门控网络用于安全绕过高分辨率处理
- 自蒸馏区域提议网络精确定位感兴趣区域
- 一致性感知生成和自监督蒸馏优化策略

**当前局限**

> 框架可能增加模型复杂度，需要额外训练；在极端稀疏或密集场景下自适应性能未充分验证。

**后续可改进方向**

- 进一步优化门控网络和区域提议网络的轻量化设计
- 扩展框架到更多MLLM架构和任务类型
- 研究实时自适应机制以减少延迟

**工程启发**

> 高，Q-Zoom可集成到现有MLLMs中，显著提升文档OCR等任务的推理速度，适用于资源受限环境。

**为什么值得关注**

> 涉及文档理解和OCR任务，通过自适应感知减少计算开销，对OCR在MLLMs中的应用有直接优化意义。

**原始摘要**

MLLMs require high-resolution visual inputs for fine-grained tasks like document understanding and
dense scene perception. However, current global resolution scaling paradigms indiscriminately flood
the quadratic self-attention mechanism with visually redundant tokens, severely bottlenecking
inference throughput while ignoring spatial sparsity and query intent. To overcome this, we propose
Q-Zoom, a query-aware adaptive high-resolution perception framework that operates in an efficient
coarse-to-fine manner. First, a lightweight Dynamic Gating Network safely bypasses high-resolution
processing when coarse global features suffice. Second, for queries demanding fine-grained
perception, a Self-Distilled Region Proposal Network (SD-RPN) precisely localizes the task-relevant
Region-of-Interest (RoI) directly from intermediate feature spaces. To optimize these modules
efficiently, the gating network uses a consistency-aware generation strategy to derive deterministic
routing labels, while the SD-RPN employs a fully self-supervised distillation paradigm. A continuous
spatio-temporal alignment scheme and targeted fine-tuning then seamlessly fuse the dense local RoI
with the coarse global layout. Extensive experiments demonstrate that Q-Zoom establishes a dominant
Pareto frontier. Using Qwen2.5-VL-7B as a primary testbed, Q-Zoom accelerates inference by 2.52
times on Document & OCR benchmarks and 4.39 times in High-Resolution scenarios while matching the
baseline's peak accuracy. Furthermore, when configured for maximum perceptual fidelity, Q-Zoom
surpasses the baseline's peak performance by 1.1% and 8.1% on these respective benchmarks. These
robust improvements transfer seamlessly to Qwen3-VL, LLaVA, and emerging RL-based thinking-with-
image models. Project page is available at https://yuhengsss.github.io/Q-Zoom/.

---

### 4. PoM: A Linear-Time Replacement for Attention with the Polynomial Mixer

- arXiv: [2604.06129v1](https://arxiv.org/abs/2604.06129v1)
- PDF: [下载链接](https://arxiv.org/pdf/2604.06129v1)
- 作者: David Picard, Nicolas Dufour, Lucas Degeorge, Arijit Ghosh, Davide Allegro, Tom Ravaud, Yohann Perron, Corentin Sautier, Zeynep Sonat Baltaci, Fei Meng, Syrine Kalleli, Marta López-Rauhut, Thibaut Loiseau, Ségolène Albouy, Raphael Baena, Elliot Vincent, Loic Landrieu
- 发布时间: 2026-04-07T17:40:37Z
- 分类: cs.CV, cs.AI
- 相关性评分: 10
- 主题标签: 自注意力替代、多项式混合器、线性复杂度、手写文本识别、令牌混合

**中文摘要**

> 本文介绍多项式混合器（PoM），一种具有线性复杂度的新颖令牌混合机制，可作为自注意力的即插即用替代品。PoM通过学习多项式函数将输入令牌聚合为紧凑表示，从中每个令牌检索上下文信息。证明PoM满足上下文映射属性，确保配备PoM的Transformer保持通用序列到序列近似能力。在五个领域替换标准自注意力：文本生成、手写文本识别、图像生成、3D建模和地球观测。PoM匹配基于注意力的模型性能，同时大幅减少长序列的计算成本。

**核心创新概述**

> 提出PoM作为线性复杂度的自注意力替代机制，通过多项式聚合实现高效上下文建模，在多个领域验证其性能与注意力相当。

**创新点拆解**

- 多项式混合器（PoM）作为线性复杂度的令牌混合机制
- 证明PoM满足上下文映射属性，保持模型通用性
- 在多个领域（包括手写文本识别）作为自注意力替代品验证性能

**当前局限**

> PoM可能在某些复杂序列任务上性能略低于注意力；多项式函数的学习和优化需要进一步研究。

**后续可改进方向**

- 探索更高效的多项式函数设计和训练策略
- 扩展PoM到更多OCR相关任务，如文档布局分析
- 集成PoM到端到端OCR模型以提升效率

**工程启发**

> 中等，PoM可降低OCR模型在长文档处理时的计算成本，适用于大规模或实时应用，但需验证在特定OCR任务上的泛化性。

**为什么值得关注**

> 涉及手写文本识别作为应用领域，PoM的线性复杂度对OCR模型效率提升有潜在价值，尤其处理长文本序列时。

**原始摘要**

This paper introduces the Polynomial Mixer (PoM), a novel token mixing mechanism with linear
complexity that serves as a drop-in replacement for self-attention. PoM aggregates input tokens into
a compact representation through a learned polynomial function, from which each token retrieves
contextual information. We prove that PoM satisfies the contextual mapping property, ensuring that
transformers equipped with PoM remain universal sequence-to-sequence approximators. We replace
standard self-attention with PoM across five diverse domains: text generation, handwritten text
recognition, image generation, 3D modeling, and Earth observation. PoM matches the performance of
attention-based models while drastically reducing computational cost when working with long
sequences. The code is available at https://github.com/davidpicard/pom.

---

### 5. Assessing the Added Value of Onboard Earth Observation Processing with the IRIDE HEO Service Segment

- arXiv: [2604.07120v1](https://arxiv.org/abs/2604.07120v1)
- PDF: [下载链接](https://arxiv.org/pdf/2604.07120v1)
- 作者: Parampuneet Kaur Thind, Charles Mwangi, Giovanni Varetto, Lorenzo Sarti, Andrea Papa, Andrea Taramelli
- 发布时间: 2026-04-08T14:14:43Z
- 分类: cs.CV, cs.AI, cs.AR, cs.ET
- 相关性评分: 9
- 主题标签: 地球观测、机载处理、服务导向架构、图像分析、遥感

**中文摘要**

> 当前地球观测服务依赖地面处理流水线，受下行链路延迟和带宽限制。IRIDE计划是一个国家地球观测倡议，集成异构传感技术于统一服务导向架构。其中，HEO支持机载数据产品生成，允许在处理链早期提取信息。本文以IRIDE烧毁区域映射服务为例，评估机载处理在操作服务层面的附加值，展示其支持更高空间细节、更小可检测事件和改进系统响应性。

**核心创新概述**

> 评估机载处理在地球观测服务中的附加值，通过IRIDE HEO能力展示其在空间细节和响应性方面的改进，而非替代现有服务。

**创新点拆解**

- 机载数据产品生成，减少地面处理依赖
- 统一服务导向架构集成异构传感技术
- 以烧毁区域映射服务为例展示操作优势

**当前局限**

> 机载处理可能受硬件限制，成本较高；泛化到其他地球观测任务未充分讨论。

**后续可改进方向**

- 开发更高效的机载处理算法，减少计算和存储需求
- 扩展机载处理到更多OCR相关应用，如文档图像分析
- 研究机载与地面处理的协同优化策略

**工程启发**

> 中等，机载处理可提升地球观测服务的实时性，对OCR在遥感图像文本提取中的应用有间接启发，但直接关联较弱。

**为什么值得关注**

> 涉及图像处理和数据分析，机载处理技术可能启发OCR在边缘计算或实时场景的应用，但论文未直接讨论OCR。

**原始摘要**

Current operational Earth Observation (EO) services, including the Copernicus Emergency Management
Service (CEMS), the European Forest Fire Information System (EFFIS), and the Copernicus Land
Monitoring Service (CLMS), rely primarily on ground-based processing pipelines. While these systems
provide mature large-scale information products, they remain constrained by downlink latency,
bandwidth limitations, and limited capability for autonomous observation prioritisation. The
International Report for an Innovative Defence of Earth (IRIDE) programme is a national Earth
observation initiative led by the Italian government to support public authorities through timely,
objective information derived from spaceborne data. Rather than a single constellation, IRIDE is
designed as a constellation of constellations, integrating heterogeneous sensing technologies within
a unified service-oriented architecture. Within this framework, Hawk for Earth Observation (HEO)
enables onboard generation of data products, allowing information extraction earlier in the
processing chain. This paper examines the limitations of ground-only architectures and evaluates the
added value of onboard processing at the operational service level. The IRIDE burnt-area mapping
service is used as a representative case study to demonstrate how onboard intelligence can support
higher spatial detail (sub-three-metre ground sampling distance), smaller detectable events (minimum
mapping unit of three hectares), and improved system responsiveness. Rather than replacing existing
Copernicus services, the IRIDE HEO capability is positioned as a complementary layer providing
image-driven pre-classification to support downstream emergency and land-management workflows. This
work highlights the operational value of onboard intelligence for emerging low-latency EO service
architectures.

---

### 6. Making MLLMs Blind: Adversarial Smuggling Attacks in MLLM Content Moderation

- arXiv: [2604.06950v1](https://arxiv.org/abs/2604.06950v1)
- PDF: [下载链接](https://arxiv.org/pdf/2604.06950v1)
- 作者: Zhiheng Li, Zongyang Ma, Yuntong Pan, Ziqi Zhang, Xiaolei Lv, Bo Li, Jun Gao, Jianing Zhang, Chunfeng Yuan, Bing Li, Weiming Hu
- 发布时间: 2026-04-08T11:13:16Z
- 分类: cs.CV
- 相关性评分: 7
- 主题标签: 对抗性攻击、内容审核、OCR鲁棒性、MLLMs安全、视觉编码

**中文摘要**

> MLLMs越来越多地部署为自动内容审核器。本文揭示关键威胁：对抗性走私攻击。与对抗扰动和越狱不同，走私攻击利用人-AI能力差距，将有害内容编码为人可读但AI不可读的视觉格式，从而逃避自动检测。将走私攻击分类为两条路径：感知盲区（破坏文本识别）和推理阻断（抑制语义理解）。构建SmuggleBench基准，包含1700个攻击实例。评估显示，最先进模型易受攻击，攻击成功率超过90%。通过感知和推理视角分析漏洞根源：视觉编码器能力有限、OCR鲁棒性差距、领域特定对抗样本稀缺。初步探索缓解策略，如测试时缩放和对抗训练。

**核心创新概述**

> 揭示对抗性走私攻击作为MLLMs内容审核的新威胁，通过视觉格式编码逃避检测，构建基准并分析漏洞根源。

**创新点拆解**

- 对抗性走私攻击分类为感知盲区和推理阻断路径
- 构建SmuggleBench基准用于评估攻击
- 分析漏洞根源，包括OCR鲁棒性差距
- 初步探索缓解策略如测试时缩放和对抗训练

**当前局限**

> 缓解策略效果有限，未完全解决攻击问题；攻击可能扩展到更多视觉格式和场景。

**后续可改进方向**

- 开发更鲁棒的OCR模型以抵抗感知盲区攻击
- 集成多模态防御机制，如结合文本和图像分析
- 扩展基准到更多语言和文档类型，提升泛化性

**工程启发**

> 高，研究直接关联OCR安全，对提升MLLMs在内容审核中的鲁棒性有重要应用价值，可指导实际系统设计。

**为什么值得关注**

> 直接涉及OCR作为攻击目标（感知盲区），强调OCR鲁棒性差距，对OCR安全研究和实践有直接相关性。

**原始摘要**

Multimodal Large Language Models (MLLMs) are increasingly being deployed as automated content
moderators. Within this landscape, we uncover a critical threat: Adversarial Smuggling Attacks.
Unlike adversarial perturbations (for misclassification) and adversarial jailbreaks (for harmful
output generation), adversarial smuggling exploits the Human-AI capability gap. It encodes harmful
content into human-readable visual formats that remain AI-unreadable, thereby evading automated
detection and enabling the dissemination of harmful content. We classify smuggling attacks into two
pathways: (1) Perceptual Blindness, disrupting text recognition; and (2) Reasoning Blockade,
inhibiting semantic understanding despite successful text recognition. To evaluate this threat, we
constructed SmuggleBench, the first comprehensive benchmark comprising 1,700 adversarial smuggling
attack instances. Evaluations on SmuggleBench reveal that both proprietary (e.g., GPT-5) and open-
source (e.g., Qwen3-VL) state-of-the-art models are vulnerable to this threat, producing Attack
Success Rates (ASR) exceeding 90%. By analyzing the vulnerability through the lenses of perception
and reasoning, we identify three root causes: the limited capabilities of vision encoders, the
robustness gap in OCR, and the scarcity of domain-specific adversarial examples. We conduct a
preliminary exploration of mitigation strategies, investigating the potential of test-time scaling
(via CoT) and adversarial training (via SFT) to mitigate this threat. Our code is publicly available
at https://github.com/zhihengli-casia/smugglebench.

---

### 7. A Multi-Stage Validation Framework for Trustworthy Large-scale Clinical Information Extraction using Large Language Models

- arXiv: [2604.06028v1](https://arxiv.org/abs/2604.06028v1)
- PDF: [下载链接](https://arxiv.org/pdf/2604.06028v1)
- 作者: Maria Mahbub, Gregory M. Dams, Josh Arnold, Caitlin Rizy, Sudarshan Srinivasan, Elliot M. Fielstein, Minu A. Aghevli, Kamonica L. Craig, Elizabeth M. Oliva, Joseph Erdos, Jodie Trafton, Ioana Danciu
- 发布时间: 2026-04-07T16:23:52Z
- 分类: cs.CL, cs.AI, cs.IR
- 相关性评分: 6
- 主题标签: 临床信息提取、大型语言模型、弱监督验证、多阶段框架、医疗文档解析

**中文摘要**

> 大型语言模型（LLMs）在从非结构化健康记录中提取临床有意义信息方面展现出潜力，但其在现实世界中的应用受到缺乏可扩展和可信验证方法的限制。传统评估方法严重依赖标注密集的参考标准或不完整的结构化数据，限制了在人口规模上的可行性。我们提出了一个基于LLM的临床信息提取的多阶段验证框架，能够在弱监督下进行严格评估。该框架集成了提示校准、基于规则的合理性过滤、语义基础评估、使用独立高能力法官LLM的针对性确认评估、选择性专家评审和外部预测有效性分析，以量化不确定性并描述错误模式，无需详尽的人工标注。我们将此框架应用于从919,783份临床记录中提取11种物质类别的物质使用障碍（SUD）诊断。基于规则的过滤和语义基础移除了14.59%的LLM阳性提取，这些提取未受支持、不相关或结构上不合理。对于高不确定性案例，法官LLM的评估与主题专家评审显示出高度一致性（Gwet's AC1=0.80）。使用法官评估输出作为参考，主要LLM在宽松匹配标准下实现了F1分数0.80。LLM提取的SUD诊断在预测后续参与SUD专科护理方面比结构化数据基线更准确。

**核心创新概述**

> 提出一个多阶段验证框架，用于基于LLM的临床信息提取，通过弱监督方法实现大规模可信评估，减少对人工标注的依赖。

**创新点拆解**

- 多阶段验证框架设计，集成提示校准、规则过滤、语义评估和法官LLM评估
- 弱监督训练范式，利用规则和语义基础减少标注需求
- 数据增强方法，通过外部预测有效性分析量化不确定性
- 架构创新，结合多个LLM（主要LLM和法官LLM）进行协同评估
- 任务定义扩展，从传统提取扩展到可信度评估和错误模式分析

**当前局限**

> 框架依赖规则和语义基础，可能引入偏差；法官LLM的评估能力受其训练数据限制；在更复杂或多样化的临床场景中泛化能力未充分验证。

**后续可改进方向**

- 开发自适应规则生成以减少人工规则设计
- 探索多模态数据（如图像或时间序列）集成以增强语义基础
- 优化法官LLM的训练数据以提高评估准确性
- 扩展框架到其他OCR任务如手写文本或低质量文档提取
- 研究实时验证机制以支持动态临床环境

**工程启发**

> 高，框架提供可扩展的验证方法，适用于大规模临床文档处理，减少人工成本，提升信息提取的可靠性和实用性，支持医疗决策和流行病学研究。

**为什么值得关注**

> 该论文直接涉及OCR/文档解析领域，专注于从非结构化文本中提取信息，并引入验证框架以提高准确性和可信度，对医疗文档处理具有重要应用价值。

**原始摘要**

Large language models (LLMs) show promise for extracting clinically meaningful information from
unstructured health records, yet their translation into real-world settings is constrained by the
lack of scalable and trustworthy validation approaches. Conventional evaluation methods rely heavily
on annotation-intensive reference standards or incomplete structured data, limiting feasibility at
population scale. We propose a multi-stage validation framework for LLM-based clinical information
extraction that enables rigorous assessment under weak supervision. The framework integrates prompt
calibration, rule-based plausibility filtering, semantic grounding assessment, targeted confirmatory
evaluation using an independent higher-capacity judge LLM, selective expert review, and external
predictive validity analysis to quantify uncertainty and characterize error modes without exhaustive
manual annotation. We applied this framework to extraction of substance use disorder (SUD) diagnoses
across 11 substance categories from 919,783 clinical notes. Rule-based filtering and semantic
grounding removed 14.59% of LLM-positive extractions that were unsupported, irrelevant, or
structurally implausible. For high-uncertainty cases, the judge LLM's assessments showed substantial
agreement with subject matter expert review (Gwet's AC1=0.80). Using judge-evaluated outputs as
references, the primary LLM achieved an F1 score of 0.80 under relaxed matching criteria. LLM-
extracted SUD diagnoses also predicted subsequent engagement in SUD specialty care more accurately
than structured-data baselines (AUC=0.80). These findings demonstrate that scalable, trustworthy
deployment of LLM-based clinical information extraction is feasible without annotation-intensive
evaluation.

---
