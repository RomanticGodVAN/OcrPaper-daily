# OCR / 文档解析研究日报（2026-03-26）

## 报告说明

- 检索源：arXiv API
- 检索查询：`(all:"document parsing" OR all:"document understanding" OR all:"optical character recognition" OR all:OCR OR all:"layout analysis" OR all:"document layout analysis" OR all:"text recognition" OR all:"table recognition" OR all:"form understanding" OR all:"document intelligence" OR all:"page understanding" OR all:"scene text recognition" OR all:"handwritten text recognition" OR all:"information extraction") AND (cat:cs.CV OR cat:cs.AI OR cat:cs.CL OR cat:eess.IV)`
- 生成时间（UTC）：`2026-03-26 04:07:54`
- 大模型综合分析：`开启`

## 一、今日执行摘要

> 今日论文聚焦于OCR和文档解析领域的高效、轻量化和鲁棒性解决方案。PP-OCRv5通过数据中心优化实现轻量级高性能，挑战大模型依赖；PaddleOCR-VL采用粗到细处理提升效率；多篇论文探索端到端解析、数据合成和表格理解，如TDATR和TWT通过细节感知与神经符号推理增强性能。趋势包括轻量化模型、多模态对齐和神经符号融合，工程上强调开源部署和资源优化。未来方向具体指向数据增强、实时处理和复杂布局适应。

## 二、今日趋势判断

当前研究趋势强调轻量化模型设计（如PP-OCRv5的5M参数）与效率优化（如PaddleOCR-VL的粗到细处理），以减少计算成本。多模态学习扩展至表格和视频领域（如TWT和CliPPER），通过神经符号推理和精细对齐提升理解能力。端到端解析和数据合成（如论文3）解决数据稀缺问题，而代理系统（如DUPLEX）结合LLM与符号规划提高可靠性。整体上，研究从单纯规模扩展转向数据质量、架构创新和跨模态应用。

## 三、今日论文概览

1. **PP-OCRv5: A Specialized 5M-Parameter Model Rivaling Billion-Parameter Vision-Language Models on OCR Tasks** | 标签：轻量级模型、数据中心优化、OCR 性能提升、幻觉减少
2. **Boosting Document Parsing Efficiency and Performance with Coarse-to-Fine Visual Processing** | 标签：粗到细处理、视觉令牌优化、文档解析效率、轻量级视觉语言模型
3. **Towards Real-World Document Parsing via Realistic Scene Synthesis and Document-Aware Training** | 标签：端到端文档解析、数据合成、结构感知训练、鲁棒性基准
4. **PaperVoyager : Building Interactive Web with Visual Language Models** | 标签：交互式系统生成、视觉语言模型应用、论文理解、结构化生成
5. **TDATR: Improving End-to-End Table Recognition via Table Detail-Aware Learning and Cell-Level Visual Alignment** | 标签：表格识别、端到端学习、视觉语言对齐、少样本性能
6. **Unlocking Few-Shot Capabilities in LVLMs via Prompt Conditioning and Head Selection** | 标签：少样本学习、视觉语言模型优化、提示工程、分类性能提升
7. **Thinking with Tables: Enhancing Multi-Modal Tabular Understanding via Neuro-Symbolic Reasoning** | 标签：多模态学习、表格理解、神经符号推理、程序辅助方法、信息提取
8. **CliPPER: Contextual Video-Language Pretraining on Long-form Intraoperative Surgical Procedures for Event Recognition** | 标签：视频语言预训练、手术视频分析、多模态对齐、零样本学习、事件识别
9. **DUPLEX: Agentic Dual-System Planning via LLM-Driven Information Extraction** | 标签：神经符号架构、任务规划、信息提取、大语言模型、可靠性提升

## 四、今天 OCR / 文档解析论文里的主要创新点

- 轻量级模型设计或优化策略以减少参数和计算开销。
- 数据中心方法或数据合成技术提升训练数据质量和多样性。
- 多模态对齐或神经符号推理机制增强复杂文档或表格的理解能力。
- 端到端架构或代理系统改进任务性能与可靠性。

## 五、后续 OCR 领域值得推进的改进方向

- 开发高效数据增强或合成方法，以降低对大规模真实标注数据的依赖。
- 优化模型在实时或动态OCR场景中的推理速度和资源使用。
- 研究自适应处理策略，以更好地应对极端文档布局或低质量图像。
- 扩展多模态学习到更多领域，如嵌套表格或长形式视频的事件识别。
- 结合轻量级符号规划器与LLM，提升任务规划的可靠性和效率。

## 六、工程落地启发

- 优先采用轻量级开源模型（如PP-OCRv5）以在资源受限环境中部署。
- 集成粗到细处理或视觉令牌减少机制来提升大规模文档解析的效率。
- 利用数据合成和基准（如Wild-OmniDocBench）增强端到端解析的鲁棒性。
- 在表格识别任务中应用细节感知学习和单元格对齐以提高准确性。
- 探索代理架构（如DUPLEX）将LLM限制于信息提取，避免幻觉问题。

## 七、优先关注论文

- **PP-OCRv5: A Specialized 5M-Parameter Model Rivaling Billion-Parameter Vision-Language Models on OCR Tasks**：展示轻量级模型通过数据中心优化达到高性能，挑战大模型主导，适用于边缘部署。
- **Thinking with Tables: Enhancing Multi-Modal Tabular Understanding via Neuro-Symbolic Reasoning**：系统解决表格多模态理解挑战，通过神经符号推理显著提升性能，填补领域空白。
- **DUPLEX: Agentic Dual-System Planning via LLM-Driven Information Extraction**：创新结合LLM与符号规划，提高任务规划可靠性，避免幻觉，适用于机器人等领域。

## 八、论文逐篇解析

### 1. PP-OCRv5: A Specialized 5M-Parameter Model Rivaling Billion-Parameter Vision-Language Models on OCR Tasks

- arXiv: [2603.24373v1](https://arxiv.org/abs/2603.24373v1)
- PDF: [下载链接](https://arxiv.org/pdf/2603.24373v1)
- 作者: Cheng Cui, Yubo Zhang, Ting Sun, Xueqing Wang, Hongen Liu, Manhui Lin, Yue Zhang, Tingquan Gao, Changda Zhou, Jiaxuan Liu, Zelun Zhang, Jing Zhang, Jun Zhang, Yi Liu
- 发布时间: 2026-03-25T14:54:40Z
- 分类: cs.CV
- 相关性评分: 18
- 主题标签: 轻量级模型、数据中心优化、OCR 性能提升、幻觉减少

**中文摘要**

> PP-OCRv5 是一款轻量级 OCR 系统，仅含 500 万参数，通过数据中心的优化策略，在标准 OCR 基准测试中达到与数十亿参数视觉语言模型相竞争的性能，同时提供更精确的文本定位和减少幻觉。研究强调数据质量、准确性和多样性对传统两阶段 OCR 管道性能的关键作用，挑战了模型规模是唯一提升路径的普遍观念。

**核心创新概述**

> 提出一种轻量级、专门化的 OCR 模型，通过数据中心的优化而非架构扩展，实现与大型视觉语言模型相媲美的性能，这在当前大模型时代中展示了轻量模型的可行性。

**创新点拆解**

- 轻量级模型设计（仅 5M 参数）
- 数据中心的训练范式，量化数据难度、准确性和多样性
- 优化两阶段 OCR 管道，提升定位精度和减少幻觉

**当前局限**

> 依赖于高质量、大规模的训练数据，可能在实际应用中面临数据收集和标注的挑战；未详细探讨模型在极端复杂布局或低质量图像下的鲁棒性。

**后续可改进方向**

- 探索更高效的数据增强或合成方法以降低对真实数据量的依赖
- 研究模型在动态或实时 OCR 场景中的优化
- 结合多模态信息进一步提升在复杂文档中的解析能力

**工程启发**

> 高，提供开源代码和模型，适用于资源受限环境，如移动设备或边缘计算，促进轻量 OCR 系统的实际部署。

**为什么值得关注**

> 直接针对 OCR 任务，挑战大模型主导的趋势，强调数据优化的重要性，为 OCR 研究提供了新的轻量化方向。

**原始摘要**

The advent of "OCR 2.0" and large-scale vision-language models (VLMs) has set new benchmarks in text
recognition. However, these unified architectures often come with significant computational demands,
challenges in precise text localization within complex layouts, and a propensity for textual
hallucinations. Revisiting the prevailing notion that model scale is the sole path to high accuracy,
this paper introduces PP-OCRv5, a meticulously optimized, lightweight OCR system with merely 5
million parameters. We demonstrate that PP-OCRv5 achieves performance competitive with many billion-
parameter VLMs on standard OCR benchmarks, while offering superior localization precision and
reduced hallucinations. The cornerstone of our success lies not in architectural expansion but in a
data-centric investigation. We systematically dissect the role of training data by quantifying three
critical dimensions: data difficulty, data accuracy, and data diversity. Our extensive experiments
reveal that with a sufficient volume of high-quality, accurately labeled, and diverse data, the
performance ceiling for traditional, efficient two-stage OCR pipelines is far higher than commonly
assumed. This work provides compelling evidence for the viability of lightweight, specialized models
in the large-model era and offers practical insights into data curation for OCR. The source code and
models are publicly available at https://github.com/PaddlePaddle/PaddleOCR.

---

### 2. Boosting Document Parsing Efficiency and Performance with Coarse-to-Fine Visual Processing

- arXiv: [2603.24326v1](https://arxiv.org/abs/2603.24326v1)
- PDF: [下载链接](https://arxiv.org/pdf/2603.24326v1)
- 作者: Cheng Cui, Ting Sun, Suyin Liang, Tingquan Gao, Zelun Zhang, Jiaxuan Liu, Xueqing Wang, Changda Zhou, Hongen Liu, Manhui Lin, Yue Zhang, Yubo Zhang, Jing Zhang, Jun Zhang, Xing Wei, Yi Liu, Dianhai Yu, Yanjun Ma
- 发布时间: 2026-03-25T14:08:56Z
- 分类: cs.CV, cs.AI, cs.IR
- 相关性评分: 18
- 主题标签: 粗到细处理、视觉令牌优化、文档解析效率、轻量级视觉语言模型

**中文摘要**

> PaddleOCR-VL 提出一种粗到细的视觉处理架构，通过轻量级有效区域聚焦模块（VRFM）识别语义相关区域并抑制冗余，减少视觉令牌数量，从而提升文档解析的效率和性能。该架构结合一个紧凑的 0.9B 视觉语言模型，在页面级和元素级识别任务中达到最先进水平，同时实现快速推理。

**核心创新概述**

> 引入粗到细的视觉处理策略，通过 VRFM 模块动态聚焦有效区域，解决高分辨率输入带来的计算冗余问题，实现效率与性能的平衡。

**创新点拆解**

- 粗到细的架构设计，包括 VRFM 模块
- 轻量级视觉语言模型（0.9B 参数）
- 动态视觉令牌减少机制

**当前局限**

> VRFM 模块可能依赖于预训练或特定任务的数据，泛化能力未充分验证；在极端文档布局或噪声图像中的鲁棒性需进一步测试。

**后续可改进方向**

- 优化 VRFM 模块以处理更多样化的文档类型
- 探索自适应分辨率调整策略以进一步提升效率
- 集成更多上下文信息以增强复杂文档的理解能力

**工程启发**

> 高，开源实现，适用于大规模文档处理场景，如数字图书馆或自动化办公，能显著降低计算成本。

**为什么值得关注**

> 专注于文档解析的效率提升，通过视觉处理优化减少计算开销，对 OCR 和文档理解任务有直接应用价值。

**原始摘要**

Document parsing is a fine-grained task where image resolution significantly impacts performance.
While advanced research leveraging vision-language models benefits from high-resolution input to
boost model performance, this often leads to a quadratic increase in the number of vision tokens and
significantly raises computational costs. We attribute this inefficiency to substantial visual
regions redundancy in document images, like background. To tackle this, we propose PaddleOCR-VL, a
novel coarse-to-fine architecture that focuses on semantically relevant regions while suppressing
redundant ones, thereby improving both efficiency and performance. Specifically, we introduce a
lightweight Valid Region Focus Module (VRFM) which leverages localization and contextual
relationship prediction capabilities to identify valid vision tokens. Subsequently, we design and
train a compact yet powerful 0.9B vision-language model (PaddleOCR-VL-0.9B) to perform detailed
recognition, guided by VRFM outputs to avoid direct processing of the entire large image. Extensive
experiments demonstrate that PaddleOCR-VL achieves state-of-the-art performance in both page-level
parsing and element-level recognition. It significantly outperforms existing solutions, exhibits
strong competitiveness against top-tier VLMs, and delivers fast inference while utilizing
substantially fewer vision tokens and parameters, highlighting the effectiveness of targeted coarse-
to-fine parsing for accurate and efficient document understanding. The source code and models are
publicly available at https://github.com/PaddlePaddle/PaddleOCR.

---

### 3. Towards Real-World Document Parsing via Realistic Scene Synthesis and Document-Aware Training

- arXiv: [2603.23885v1](https://arxiv.org/abs/2603.23885v1)
- PDF: [下载链接](https://arxiv.org/pdf/2603.23885v1)
- 作者: Gengluo Li, Chengquan Zhang, Yupu Liang, Huawen Shen, Yaping Zhang, Pengyuan Lyu, Weinong Wang, Xingyu Wan, Gangyan Zeng, Han Hu, Can Ma, Yu Zhou
- 发布时间: 2026-03-25T03:19:09Z
- 分类: cs.CV
- 相关性评分: 13
- 主题标签: 端到端文档解析、数据合成、结构感知训练、鲁棒性基准

**中文摘要**

> 提出一种数据训练协同设计框架，通过真实场景合成策略构建大规模、结构多样的全页面端到端监督数据，并结合文档感知训练方法增强结构保真度和解码稳定性。该方法集成到 1B 参数的多模态大语言模型中，在扫描/数字和真实捕获场景中实现优越的准确性和鲁棒性。

**核心创新概述**

> 结合数据合成和训练策略，解决端到端文档解析中数据稀缺和结构不一致问题，通过 Wild-OmniDocBench 基准评估鲁棒性。

**创新点拆解**

- 真实场景合成策略生成大规模端到端数据
- 文档感知训练方法，包括渐进学习和结构令牌优化
- 构建 Wild-OmniDocBench 基准用于鲁棒性评估

**当前局限**

> 数据合成可能无法完全覆盖所有真实世界变异；模型在极端噪声或非标准文档格式下的性能需进一步验证。

**后续可改进方向**

- 扩展数据合成以包括更多真实世界捕获的变体
- 研究更高效的结构感知解码机制
- 探索多任务学习以提升泛化能力

**工程启发**

> 中等至高，提供开源数据和基准，促进端到端文档解析研究，适用于自动化文档处理系统。

**为什么值得关注**

> 针对文档解析的端到端方法，强调数据质量和训练策略，对 OCR 和文档理解任务有重要启示。

**原始摘要**

Document parsing has recently advanced with multimodal large language models (MLLMs) that directly
map document images to structured outputs. Traditional cascaded pipelines depend on precise layout
analysis and often fail under casually captured or non-standard conditions. Although end-to-end
approaches mitigate this dependency, they still exhibit repetitive, hallucinated, and structurally
inconsistent predictions - primarily due to the scarcity of large-scale, high-quality full-page
(document-level) end-to-end parsing data and the lack of structure-aware training strategies. To
address these challenges, we propose a data-training co-design framework for robust end-to-end
document parsing. A Realistic Scene Synthesis strategy constructs large-scale, structurally diverse
full-page end-to-end supervision by composing layout templates with rich document elements, while a
Document-Aware Training Recipe introduces progressive learning and structure-token optimization to
enhance structural fidelity and decoding stability. We further build Wild-OmniDocBench, a benchmark
derived from real-world captured documents for robustness evaluation. Integrated into a 1B-parameter
MLLM, our method achieves superior accuracy and robustness across both scanned/digital and real-
world captured scenarios. All models, data synthesis pipelines, and benchmarks will be publicly
released to advance future research in document understanding.

---

### 4. PaperVoyager : Building Interactive Web with Visual Language Models

- arXiv: [2603.22999v1](https://arxiv.org/abs/2603.22999v1)
- PDF: [下载链接](https://arxiv.org/pdf/2603.22999v1)
- 作者: Dasen Dai, Biao Wu, Meng Fang, Wenhao Wang
- 发布时间: 2026-03-24T09:42:27Z
- 分类: cs.CL
- 相关性评分: 12
- 主题标签: 交互式系统生成、视觉语言模型应用、论文理解、结构化生成

**中文摘要**

> PaperVoyager 提出一种将研究论文转换为可执行交互式网页系统的代理，通过端到端处理包括论文理解、系统建模和网页合成，使用户能操作输入并观察动态行为。引入基准评估，并设计结构化生成框架以显式建模机制和交互逻辑。

**核心创新概述**

> 将视觉语言模型应用于交互式系统生成，超越静态文档转换，实现动态机制和状态转换的可视化。

**创新点拆解**

- 论文到交互式系统的端到端代理
- 结构化生成框架 PaperVoyager
- 引入基准评估交互式系统质量

**当前局限**

> 依赖于论文内容的准确解析，可能受限于复杂机制或非标准格式；交互逻辑的生成可能不够灵活或通用。

**后续可改进方向**

- 增强模型对复杂科学论文的理解能力
- 扩展交互式系统生成以支持更多文档类型
- 优化生成框架以提高效率和可扩展性

**工程启发**

> 中等，为科学论文理解和教育工具提供新范式，但实际部署需考虑用户界面和性能优化。

**为什么值得关注**

> 虽然主要关注交互式系统生成，但基于视觉语言模型的文档理解能力与 OCR 和文档解析相关，提供跨领域应用思路。

**原始摘要**

Recent advances in visual language models have enabled autonomous agents for complex reasoning, tool
use, and document understanding. However, existing document agents mainly transform papers into
static artifacts such as summaries, webpages, or slides, which are insufficient for technical papers
involving dynamic mechanisms and state transitions. In this work, we propose a Paper-to-Interactive-
System Agent that converts research papers into executable interactive web systems. Given a PDF
paper, the agent performs end-to-end processing without human intervention, including paper
understanding, system modeling, and interactive webpage synthesis, enabling users to manipulate
inputs and observe dynamic behaviors. To evaluate this task, we introduce a benchmark of 19 research
papers paired with expert-built interactive systems as ground truth. We further propose
PaperVoyager, a structured generation framework that explicitly models mechanisms and interaction
logic during synthesis. Experiments show that PaperVoyager significantly improves the quality of
generated interactive systems, offering a new paradigm for interactive scientific paper
understanding.

---

### 5. TDATR: Improving End-to-End Table Recognition via Table Detail-Aware Learning and Cell-Level Visual Alignment

- arXiv: [2603.22819v1](https://arxiv.org/abs/2603.22819v1)
- PDF: [下载链接](https://arxiv.org/pdf/2603.22819v1)
- 作者: Chunxia Qin, Chenyu Liu, Pengcheng Xia, Jun Du, Baocai Yin, Bing Yin, Cong Liu
- 发布时间: 2026-03-24T05:45:02Z
- 分类: cs.CV, cs.AI
- 相关性评分: 10
- 主题标签: 表格识别、端到端学习、视觉语言对齐、少样本性能

**中文摘要**

> TDATR 通过表格细节感知学习和单元格级视觉对齐改进端到端表格识别，采用“感知后融合”策略，联合感知表格结构和内容，并集成结构引导的单元格定位模块以增强视觉语言对齐。在七个基准测试中达到最先进或高度竞争性能，无需数据集特定微调。

**核心创新概述**

> 结合表格细节感知学习和单元格级对齐，优化端到端表格识别，减少对大规模数据的依赖，提升在数据受限场景中的性能。

**创新点拆解**

- 表格细节感知学习，联合结构理解和内容识别
- 单元格级视觉对齐模块
- “感知后融合”策略

**当前局限**

> 在极端复杂或非结构化表格中的性能可能受限；模型泛化到新领域表格类型的能力需进一步验证。

**后续可改进方向**

- 扩展模型以处理更多样化的表格布局和格式
- 研究自适应数据增强技术以进一步提升少样本性能
- 集成多模态上下文信息以增强识别准确性

**工程启发**

> 高，适用于文档自动化处理，如财务报表或科学文献解析，提供高效且准确的表格识别解决方案。

**为什么值得关注**

> 直接针对表格识别任务，是文档解析的关键子任务，对 OCR 和文档理解有直接贡献。

**原始摘要**

Tables are pervasive in diverse documents, making table recognition (TR) a fundamental task in
document analysis. Existing modular TR pipelines separately model table structure and content,
leading to suboptimal integration and complex workflows. End-to-end approaches rely heavily on
large-scale TR data and struggle in data-constrained scenarios. To address these issues, we propose
TDATR (Table Detail-Aware Table Recognition) improves end-to-end TR through table detail-aware
learning and cell-level visual alignment. TDATR adopts a ``perceive-then-fuse'' strategy. The model
first performs table detail-aware learning to jointly perceive table structure and content through
multiple structure understanding and content recognition tasks designed under a language modeling
paradigm. These tasks can naturally leverage document data from diverse scenarios to enhance model
robustness. The model then integrates implicit table details to generate structured HTML outputs,
enabling more efficient TR modeling when trained with limited data. Furthermore, we design a
structure-guided cell localization module integrated into the end-to-end TR framework, which
efficiently locates cell and strengthens vision-language alignment. It enhances the interpretability
and accuracy of TR. We achieve state-of-the-art or highly competitive performance on seven
benchmarks without dataset-specific fine-tuning.

---

### 6. Unlocking Few-Shot Capabilities in LVLMs via Prompt Conditioning and Head Selection

- arXiv: [2603.24181v1](https://arxiv.org/abs/2603.24181v1)
- PDF: [下载链接](https://arxiv.org/pdf/2603.24181v1)
- 作者: Adhemar de Senneville, Xavier Bou, Jérémy Anger, Rafael Grompone, Gabriele Facciolo
- 发布时间: 2026-03-25T11:00:22Z
- 分类: cs.CV
- 相关性评分: 9
- 主题标签: 少样本学习、视觉语言模型优化、提示工程、分类性能提升

**中文摘要**

> 研究显示，大型视觉语言模型（LVLMs）在零样本任务中表现优异，但在图像分类任务中性能较差。通过提示条件化和头部选择，引入头部集成分类器（HEC），利用 LVLMs 内部表示提升零样本和少样本分类性能，在 12 个数据集中达到最先进水平。

**核心创新概述**

> 揭示 LVLMs 在分类任务中的潜力，通过提示条件化和头部选择机制，无需训练即可提升性能，挑战 CLIP 类方法的优势。

**创新点拆解**

- 提示条件化以增强视觉特征可分性
- 头部集成分类器（HEC）利用内部表示
- 无训练的分类器设计

**当前局限**

> 依赖于 LVLMs 的预训练表示，可能受模型架构或数据偏差影响；在极端类别不平衡或细粒度分类中的性能未充分探讨。

**后续可改进方向**

- 探索更高效的头部选择策略以降低计算开销
- 研究跨模型泛化能力以应用于更多 LVLMs
- 结合领域自适应技术以提升在特定任务中的性能

**工程启发**

> 中等，为视觉分类任务提供新方法，但实际应用需考虑模型兼容性和部署复杂性。

**为什么值得关注**

> 虽然主要关注图像分类，但基于视觉语言模型的技术与 OCR 中的多模态理解相关，可能启发 OCR 任务的少样本学习策略。

**原始摘要**

Current Large Vision Language Models (LVLMs) excel at many zero-shot tasks like image captioning,
visual question answering and OCR. However, these same models suffer from poor performance at image
classification tasks, underperforming against CLIP-based methods. Notably, this gap is surprising
because many LVLMs use CLIP-pretrained vision encoders. Yet LVLMs are not inherently limited by
CLIP's architecture with independent vision and text encoders. In CLIP, this separation biases
classification toward class-name matching rather than joint visual-text reasoning. In this paper we
show that, despite their poor raw performance, LVLMs can improve visual feature class separability
at inference using prompt conditioning, and LVLMs' internal representations, especially attention
heads, can outperform the model itself at zero-shot and few-shot classification. We introduce Head
Ensemble Classifiers (HEC) to bridge the performance gap between CLIP-based and LVLM-based
classification methods. Inspired by Gaussian Discriminant Analysis, HEC ranks the most
discriminative vision and text heads and combines them into a training-free classifier. We show that
HEC achieves state-of-the-art performance in few-shot and zero-shot classification across 12
datasets.

---

### 7. Thinking with Tables: Enhancing Multi-Modal Tabular Understanding via Neuro-Symbolic Reasoning

- arXiv: [2603.24004v1](https://arxiv.org/abs/2603.24004v1)
- PDF: [下载链接](https://arxiv.org/pdf/2603.24004v1)
- 作者: Kun-Yang Yu, Zhi Zhou, Shi-Yu Tian, Xiao-Wen Yang, Zi-Yi Jia, Ming Yang, Zi-Jian Cheng, Lan-Zhe Guo, Yu-Feng Li
- 发布时间: 2026-03-25T07:07:06Z
- 分类: cs.CL
- 相关性评分: 9
- 主题标签: 多模态学习、表格理解、神经符号推理、程序辅助方法、信息提取

**中文摘要**

> 多模态大语言模型（MLLM）在图像和文本等模态上展现出强大的推理能力，但表格数据作为关键的现实世界模态，在多模态学习中仍相对未被充分探索。本文聚焦于表格视觉多模态理解（TVMU）任务，识别了三个核心挑战：（1）表格的高结构可变性和数据不完整性，（2）隐式和复杂的特征依赖关系，（3）下游任务中问题解决管路的显著异质性。为解决这些问题，我们提出了Thinking with Tables（TWT）。TWT采用基于程序的代码驱动神经符号推理机制，通过与环境交互促进信息提取和元素建模等关键操作。我们在八个代表性数据集上评估TWT，实验结果显示，TWT在准确率上平均优于现有基线10%，在TVMU任务上达到或甚至超越专有商业SOTA LLM的性能。

**核心创新概述**

> 本文针对表格视觉多模态理解（TVMU）任务，首次系统性地识别并解决了表格数据特有的挑战，如结构可变性和特征依赖复杂性，通过引入程序辅助的神经符号推理机制，实现了在多个数据集上的显著性能提升，填补了多模态学习中表格模态的空白。

**创新点拆解**

- 提出TVMU任务定义，明确表格在多模态学习中的核心挑战
- 设计基于程序的代码驱动神经符号推理机制，增强信息提取和元素建模能力
- 通过与环境交互实现动态操作，适应表格的高结构可变性
- 在八个数据集上验证方法，平均准确率提升10%，达到或超越SOTA LLM

**当前局限**

> 方法依赖于外部环境交互，可能增加计算开销；在数据极度不完整或噪声较大的表格上性能可能受限；未深入探讨模型在实时或大规模部署中的效率问题。

**后续可改进方向**

- 优化神经符号推理机制以减少计算成本，提高实时处理能力
- 扩展模型以处理更复杂的表格结构，如嵌套表格或动态表格
- 集成更多模态（如音频或传感器数据）以增强多模态表格理解
- 开发自适应训练策略，针对不同领域表格数据进行微调

**工程启发**

> 高，TWT在表格理解任务上表现优异，可应用于金融分析、医疗数据解析、商业智能等现实场景，提升自动化处理表格数据的准确性和效率。

**为什么值得关注**

> 本文涉及多模态学习和神经符号推理，与OCR/文档解析相关，因为表格是文档中常见元素，方法可启发表格识别和结构理解的技术改进。

**原始摘要**

Multimodal Large Language Models (MLLMs) have demonstrated remarkable reasoning capabilities across
modalities such as images and text. However, tabular data, despite being a critical real-world
modality, remains relatively underexplored in multimodal learning. In this paper, we focus on the
task of Tabular-Vision Multi-Modal Understanding (TVMU) and identify three core challenges: (1) high
structural variability and data incompleteness in tables, (2) implicit and complex feature
dependencies, and (3) significant heterogeneity in problem-solving pipelines across downstream
tasks. To address these issues, we propose Thinking with Tables (TWT). TWT employs a program-aided
code-based neuro-symbolic reasoning mechanism that facilitates key operations, such as information
extraction and element modeling, by interacting with external environments. We evaluate TWT on eight
representative datasets. Experimental results demonstrate that TWT consistently outperforms existing
baselines by an average of 10\% in accuracy, achieving performance comparable to, or even
surpassing, proprietary commercial SOTA LLMs on TVMU tasks. Models and codes are available at
https://github.com/kunyang-YU/Thinking-with-Tables

---

### 8. CliPPER: Contextual Video-Language Pretraining on Long-form Intraoperative Surgical Procedures for Event Recognition

- arXiv: [2603.24539v1](https://arxiv.org/abs/2603.24539v1)
- PDF: [下载链接](https://arxiv.org/pdf/2603.24539v1)
- 作者: Florian Stilz, Vinkle Srivastav, Nassir Navab, Nicolas Padoy
- 发布时间: 2026-03-25T17:14:36Z
- 分类: cs.CV, cs.AI
- 相关性评分: 8
- 主题标签: 视频语言预训练、手术视频分析、多模态对齐、零样本学习、事件识别

**中文摘要**

> 视频语言基础模型在零样本应用中已证明对广泛任务非常有效。一个特别具有挑战性的领域是术中手术程序领域，其中标注数据稀缺，且复杂下游任务通常需要精确的时间理解。为应对这一挑战，我们引入了CliPPER（基于长形式术中手术程序的上下文视频语言预训练用于事件识别），这是一个在手术讲座视频上训练的新型视频语言预训练框架。我们的方法专为细粒度时间视频文本识别设计，并引入了多种新颖的预训练策略以改善长形式手术视频中的多模态对齐。具体来说，我们提出了上下文视频文本对比学习（VTC_CTX）和片段顺序预测（COP）预训练目标，两者都利用时间和上下文依赖关系来增强局部视频理解。此外，我们在同一手术视频内的视频文本匹配中融入了循环一致性对齐，以强制双向一致性并提高整体表示连贯性。而且，我们引入了更精细的对齐损失，帧文本匹配（FTM），以改善视频帧和文本之间的对齐。因此，我们的模型在多个公共手术基准上建立了新的最先进水平，包括阶段、步骤、器械和三联体的零样本识别。

**核心创新概述**

> 本文针对术中手术视频领域，提出CliPPER框架，通过创新的预训练策略（如VTC_CTX和COP）和精细对齐损失（FTM），显著提升了长形式视频中多模态对齐和事件识别的性能，在零样本任务上达到SOTA，解决了标注数据稀缺和精确时间理解的挑战。

**创新点拆解**

- 设计CliPPER框架，专为长形式术中手术视频的细粒度时间理解优化
- 引入上下文视频文本对比学习（VTC_CTX）和片段顺序预测（COP）预训练目标，利用时空依赖
- 提出循环一致性对齐和帧文本匹配（FTM）损失，增强多模态对齐和表示连贯性
- 在多个手术基准上实现零样本事件识别的SOTA性能

**当前局限**

> 方法主要针对手术视频领域，泛化到其他长形式视频任务可能需要调整；预训练依赖于手术讲座视频，数据来源可能有限；未详细讨论模型在实时应用中的延迟问题。

**后续可改进方向**

- 扩展预训练数据源，包括更多类型的长形式视频（如教育或监控视频）
- 优化模型架构以减少计算资源需求，适用于边缘设备部署
- 探索自适应微调策略，以快速适应新手术程序或领域
- 集成更多模态（如音频或传感器数据）以增强多模态理解

**工程启发**

> 高，CliPPER在手术视频事件识别上表现优异，可应用于医疗培训、手术辅助系统和自动化文档生成，提高手术过程的解析效率和准确性。

**为什么值得关注**

> 本文涉及视频语言多模态学习和事件识别，与OCR/文档解析相关，因为视频中的文本和视觉信息提取可启发文档中时序或结构化内容的解析技术。

**原始摘要**

Video-language foundation models have proven to be highly effective in zero-shot applications across
a wide range of tasks. A particularly challenging area is the intraoperative surgical procedure
domain, where labeled data is scarce, and precise temporal understanding is often required for
complex downstream tasks. To address this challenge, we introduce CliPPER (Contextual Video-Language
Pretraining on Long-form Intraoperative Surgical Procedures for Event Recognition), a novel video-
language pretraining framework trained on surgical lecture videos. Our method is designed for fine-
grained temporal video-text recognition and introduces several novel pretraining strategies to
improve multimodal alignment in long-form surgical videos. Specifically, we propose Contextual
Video-Text Contrastive Learning (VTC_CTX) and Clip Order Prediction (COP) pretraining objectives,
both of which leverage temporal and contextual dependencies to enhance local video understanding. In
addition, we incorporate a Cycle-Consistency Alignment over video-text matches within the same
surgical video to enforce bidirectional consistency and improve overall representation coherence.
Moreover, we introduce a more refined alignment loss, Frame-Text Matching (FTM), to improve the
alignment between video frames and text. As a result, our model establishes a new state-of-the-art
across multiple public surgical benchmarks, including zero-shot recognition of phases, steps,
instruments, and triplets. The source code and pretraining captions can be found at
https://github.com/CAMMA-public/CliPPER.

---

### 9. DUPLEX: Agentic Dual-System Planning via LLM-Driven Information Extraction

- arXiv: [2603.23909v1](https://arxiv.org/abs/2603.23909v1)
- PDF: [下载链接](https://arxiv.org/pdf/2603.23909v1)
- 作者: Keru Hua, Ding Wang, Yaoying Gu, Xiaoguang Ma
- 发布时间: 2026-03-25T03:57:44Z
- 分类: cs.AI
- 相关性评分: 4
- 主题标签: 神经符号架构、任务规划、信息提取、大语言模型、可靠性提升

**中文摘要**

> 虽然大语言模型（LLM）为机器人任务规划提供了语义灵活性，但其易产生幻觉和逻辑不一致性限制了在长视野领域中的可靠性。为弥合非结构化环境和严格计划合成之间的差距，我们提出了DUPLEX，一种代理双系统神经符号架构，严格将LLM限制于模式引导的信息提取，而非端到端规划或代码生成。在我们的框架中，前馈快速系统利用轻量级LLM从自然语言中提取实体、关系等，确定性地映射到规划域定义语言（PDDL）问题文件中，供经典符号规划器使用。为解决复杂或未充分指定的场景，慢速系统仅在规划失败时激活，利用求解器诊断驱动高容量LLM进行迭代反思和修复。在12个经典和家庭规划领域的广泛评估表明，DUPLEX在成功率和可靠性上显著优于现有端到端和混合LLM基线。这些结果证实，关键不是让LLM规划得更好，而是将LLM限制在其擅长的部分——结构化语义接地——并将逻辑计划合成留给符号规划器。

**核心创新概述**

> 本文提出DUPLEX架构，通过双系统设计（快速系统用于信息提取，慢速系统用于迭代修复），严格限制LLM在规划任务中的角色，避免幻觉问题，实现了在多个规划领域上的高可靠性和性能提升，创新性地结合了神经和符号方法的优势。

**创新点拆解**

- 设计代理双系统神经符号架构，将LLM严格限制于模式引导的信息提取
- 快速系统使用轻量级LLM进行确定性映射到PDDL，慢速系统在失败时激活进行迭代修复
- 通过求解器诊断驱动高容量LLM，增强复杂场景的处理能力
- 在12个规划领域验证方法，显著提升成功率和可靠性

**当前局限**

> 框架依赖于符号规划器，可能不适用于所有非结构化环境；双系统设计可能增加系统复杂性；未深入探讨模型在实时或动态变化环境中的适应性。

**后续可改进方向**

- 优化双系统交互机制，减少延迟并提高实时响应能力
- 扩展框架以处理更多样化的规划任务和领域，如工业自动化或物流
- 集成自适应学习组件，以动态调整信息提取和规划策略
- 探索轻量级符号规划器以减少计算开销

**工程启发**

> 高，DUPLEX在机器人任务规划中表现出高可靠性，可应用于自动驾驶、智能家居和工业机器人等领域，提升规划系统的准确性和鲁棒性。

**为什么值得关注**

> 本文涉及神经符号推理和自然语言信息提取，与OCR/文档解析相关，因为方法中的结构化语义接地技术可启发文档中实体和关系提取的改进。

**原始摘要**

While Large Language Models (LLMs) provide semantic flexibility for robotic task planning, their
susceptibility to hallucination and logical inconsistency limits their reliability in long-horizon
domains. To bridge the gap between unstructured environments and rigorous plan synthesis, we propose
DUPLEX, an agentic dual-system neuro-symbolic architecture that strictly confines the LLM to schema-
guided information extraction rather than end-to-end planning or code generation. In our framework,
a feed-forward Fast System utilizes a lightweight LLM to extract entities, relations etc. from
natural language, deterministically mapping them into a Planning Domain Definition Language (PDDL)
problem file for a classical symbolic planner. To resolve complex or underspecified scenarios, a
Slow System is activated exclusively upon planning failure, leveraging solver diagnostics to drive a
high-capacity LLM in iterative reflection and repair. Extensive evaluations across 12 classical and
household planning domains demonstrate that DUPLEX significantly outperforms existing end-to-end and
hybrid LLM baselines in both success rate and reliability. These results confirm that The key is not
to make the LLM plan better, but to restrict the LLM to the part it is good at - structured semantic
grounding - and leave logical plan synthesis to a symbolic planner.

---
