# OCR / 文档解析研究日报（2026-03-12）

## 报告说明

- 检索源：arXiv API
- 检索查询：`(all:"document parsing" OR all:"document understanding" OR all:"optical character recognition" OR all:OCR OR all:"layout analysis" OR all:"document layout analysis" OR all:"text recognition" OR all:"table recognition" OR all:"form understanding" OR all:"document intelligence" OR all:"page understanding" OR all:"scene text recognition" OR all:"handwritten text recognition" OR all:"information extraction") AND (cat:cs.CV OR cat:cs.AI OR cat:cs.CL OR cat:eess.IV)`
- 生成时间（UTC）：`2026-03-12 03:42:28`
- 大模型综合分析：`开启`

## 一、今日执行摘要

> 今日论文清单显示OCR和文档解析研究正朝多模态、领域专用、高效化和隐私保护方向快速发展。核心趋势包括：1）多模态模型融合视觉与语言处理，提升端到端理解能力（如GLM-OCR、Omni Parsing）；2）针对特定领域（金融、医疗、科学）的专用系统涌现，通过定制化算法解决布局不连续、隐私等挑战（Agentar-Fin-OCR、MITRA）；3）模型效率优化成为重点，通过紧凑架构、解码优化和边缘部署平衡性能与资源（GLM-OCR）；4）低资源语言和历史文档的OCR技术持续进步，结合专用管道和语料库发布推动基准建立（Patrologia Graeca、SiDiaC-v.2.0）；5）开源和本地化部署受关注，确保数据隐私和可复现性（MITRA、医疗LLM流水线）。这些进展为工程应用提供了更精准、高效和安全的解决方案。

## 二、今日趋势判断

当前研究呈现五大趋势：一、多模态整合深化，模型统一处理文档、图像和音视频，通过渐进式解析实现结构化知识提取（如Omni Parsing、文档图像翻译竞赛）。二、领域专用化加强，针对金融、医疗、科学等垂直场景开发定制系统，解决跨页解析、隐私保护等特定问题（Agentar-Fin-OCR、MITRA）。三、效率与性能平衡，紧凑模型和多令牌预测等技术创新优化解码速度和资源使用，支持边缘部署（GLM-OCR）。四、低资源语言和历史文档处理进步，通过专用OCR管道和语料库构建提升噪声文本识别能力（Patrologia Graeca、SiDiaC-v.2.0）。五、开源与隐私保护兴起，本地托管框架和开源LLM流水线促进可复现研究并满足敏感数据需求（医疗文本提取、MITRA）。

## 三、今日论文概览

1. **MITRA: An AI Assistant for Knowledge Retrieval in Physics Collaborations** | 标签：检索增强生成、文档解析、隐私保护、科学协作、向量数据库
2. **GLM-OCR Technical Report** | 标签：紧凑模型、多模态、解码优化、文档理解、边缘计算
3. **Agentar-Fin-OCR** | 标签：金融文档、跨页解析、表格识别、课程学习、基准评估
4. **ICDAR 2025 Competition on End-to-End Document Image Machine Translation Towards Complex Layouts** | 标签：文档图像翻译、多模态、竞赛组织、端到端学习、大模型
5. **A Robust Deep Learning Framework for Bangla License Plate Recognition Using YOLO and Vision-Language OCR** | 标签：车牌识别、对象检测、序列生成、鲁棒性评估、孟加拉语OCR
6. **The Patrologia Graeca Corpus: OCR, Annotation, and Open Release of Noisy Nineteenth-Century Polytonic Greek Editions** | 标签：历史文档OCR、多调希腊语、语料库发布、布局检测、噪声文本识别
7. **SiDiaC-v.2.0: Sinhala Diachronic Corpus Version 2.0** | 标签：低资源语言、语料库构建、OCR后处理、历时分析、文本标注
8. **PromptDLA: A Domain-aware Prompt Document Layout Analysis Framework with Descriptive Knowledge as a Cue** | 标签：文档布局分析、提示学习、领域自适应、多域泛化、计算机视觉
9. **Logics-Parsing-Omni Technical Report** | 标签：多模态解析、统一分类法、证据锚定、OCR集成、结构化知识提取
10. **Tracking Cancer Through Text: Longitudinal Extraction From Radiology Reports Using Open-Source Large Language Models** | 标签：临床文本提取、开源LLM、纵向分析、隐私保护、医疗文档解析

## 四、今天 OCR / 文档解析论文里的主要创新点

- 结合多模态模型（如视觉编码器和语言解码器）实现端到端文档理解，提升OCR与布局分析的协同效率。
- 采用领域自适应方法，如提示学习或课程学习，优化模型在特定场景（如金融或医疗文档）下的解析性能。
- 引入高效解码机制，如多令牌预测，减少自回归模型的计算开销并提高吞吐量。
- 设计专用管道处理复杂挑战，如跨页内容整合或噪声文本识别，通过算法改进提升精度。
- 强调隐私保护，通过本地托管或开源框架确保敏感数据（如医疗或科学文档）的安全处理。

## 五、后续 OCR 领域值得推进的改进方向

- 开发更高效的多模态端到端模型，专门针对文档图像翻译任务，降低计算成本并支持更多语言对。
- 优化跨页解析算法，以处理金融、法律等文档中更复杂的布局不连续性和单元格引用问题。
- 增强低资源语言OCR的鲁棒性，通过改进后处理流程和扩展语料库覆盖更多历史文档类型。
- 探索轻量级布局分析框架，结合自动化提示生成，提升模型在边缘设备上的多域泛化能力。
- 集成时序建模技术到文档解析中，支持从临床报告等文本中提取纵向信息并链接跨时间点数据。

## 六、工程落地启发

- 采用双层向量数据库架构（如MITRA）可提高文档检索精度并减少歧义，适用于大型内部知识库。
- 部署紧凑多模态模型（如GLM-OCR）结合多令牌预测，能在资源受限环境中实现高效的文档理解。
- 实现跨页内容整合和标题重建模块（如Agentar-Fin-OCR）可显著提升金融文档的结构化解析质量。
- 利用开源LLM本地流水线（如医疗文本提取）可在隐私敏感场景中安全提取临床数据，避免专有系统依赖。
- 结合YOLO布局检测和CRNN文本识别的专用管道（如Patrologia Graeca）能有效处理噪声历史文档，降低错误率。

## 七、优先关注论文

- **GLM-OCR Technical Report**：紧凑多模态模型通过多令牌预测优化解码效率，适合边缘部署和大规模生产系统，可能成为工业OCR的新标准。
- **Agentar-Fin-OCR**：针对金融文档的跨页解析和表格识别方法具有高精度和审计级可追溯性，对金融科技应用有直接工程价值。
- **PromptDLA: A Domain-aware Prompt Document Layout Analysis Framework with Descriptive Knowledge as a Cue**：领域感知提示框架显著提升布局分析的跨域泛化性能，可优化多类型文档处理流水线。
- **Logics-Parsing-Omni Technical Report**：统一多模态解析框架通过证据锚定机制实现结构化知识提取，为复杂文档和音视频分析提供端到端解决方案。
- **Tracking Cancer Through Text: Longitudinal Extraction From Radiology Reports Using Open-Source Large Language Models**：开源本地部署流水线在医疗文本提取中实现高精度，同时确保隐私，可推广到其他敏感领域的数据处理。

## 八、论文逐篇解析

### 1. MITRA: An AI Assistant for Knowledge Retrieval in Physics Collaborations

- arXiv: [2603.09800v1](https://arxiv.org/abs/2603.09800v1)
- PDF: [下载链接](https://arxiv.org/pdf/2603.09800v1)
- 作者: Abhishikth Mallampalli, Sridhara Dasu
- 发布时间: 2026-03-10T15:28:35Z
- 分类: cs.IR, cs.AI, cs.CL, cs.LG, hep-ex
- 相关性评分: 29
- 主题标签: 检索增强生成、文档解析、隐私保护、科学协作、向量数据库

**中文摘要**

> 本文介绍了MITRA，一个基于检索增强生成（RAG）的系统原型，旨在为大型物理合作（如CERN的CMS）中的内部文档提供上下文感知问答。系统采用自动化管道，使用Selenium从内部数据库检索文档，并通过OCR和布局解析进行高保真文本提取。整个框架（包括嵌入模型和大语言模型）在本地托管，确保敏感数据隐私。引入双层向量数据库架构，先通过摘要识别相关分析，再聚焦完整文档，解决不同分析间的歧义。原型在真实查询中优于基于关键字的基线，并讨论了未来开发全面研究代理的方向。

**核心创新概述**

> 针对大型科学合作中的文档导航挑战，提出一个端到端的RAG系统，结合自动化文档检索、OCR和布局解析，并采用本地托管和双层向量数据库架构以提高隐私和检索精度。

**创新点拆解**

- 自动化文档检索与OCR管道，使用Selenium和布局解析实现高保真文本提取
- 双层向量数据库架构，先基于摘要筛选分析，再检索完整文档，减少歧义
- 全本地托管框架，确保敏感数据隐私，适用于内部协作环境

**当前局限**

> 系统为原型阶段，可能未完全覆盖所有文档类型或复杂查询场景；依赖内部数据库和特定OCR工具，可扩展性有待验证。

**后续可改进方向**

- 扩展系统以处理更多文档格式和语言，提高通用性
- 优化检索算法，支持更复杂的多模态查询和实时更新
- 集成更多领域知识，增强问答的准确性和解释能力

**工程启发**

> 高，为大型科学合作提供了实用的文档检索解决方案，隐私保护和检索效率优势明显，可直接应用于类似内部环境。

**为什么值得关注**

> 涉及OCR和布局解析技术，用于文档文本提取，是文档理解的关键组成部分，与OCR研究直接相关。

**原始摘要**

Large-scale scientific collaborations, such as the Compact Muon Solenoid (CMS) at CERN, produce a
vast and ever-growing corpus of internal documentation. Navigating this complex information
landscape presents a significant challenge for both new and experienced researchers, hindering
knowledge sharing and slowing down the pace of scientific discovery. To address this, we present a
prototype of MITRA, a Retrieval-Augmented Generation (RAG) based system, designed to answer
specific, context-aware questions about physics analyses. MITRA employs a novel, automated pipeline
using Selenium for document retrieval from internal databases and Optical Character Recognition
(OCR) with layout parsing for high-fidelity text extraction. Crucially, MITRA's entire framework,
from the embedding model to the Large Language Model (LLM), is hosted on-premise, ensuring that
sensitive collaboration data remains private. We introduce a two-tiered vector database architecture
that first identifies the relevant analysis from abstracts before focusing on the full
documentation, resolving potential ambiguities between different analyses. We demonstrate the
prototype's superior retrieval performance against a standard keyword-based baseline on realistic
queries and discuss future work towards developing a comprehensive research agent for large
experimental collaborations.

---

### 2. GLM-OCR Technical Report

- arXiv: [2603.10910v1](https://arxiv.org/abs/2603.10910v1)
- PDF: [下载链接](https://arxiv.org/pdf/2603.10910v1)
- 作者: Shuaiqi Duan, Yadong Xue, Weihan Wang, Zhe Su, Huan Liu, Sheng Yang, Guobing Gan, Guo Wang, Zihan Wang, Shengdong Yan, Dexin Jin, Yuxuan Zhang, Guohong Wen, Yanfeng Wang, Yutao Zhang, Xiaohan Zhang, Wenyi Hong, Yukuo Cen, Da Yin, Bin Chen, Wenmeng Yu, Xiaotao Gu, Jie Tang
- 发布时间: 2026-03-11T15:55:47Z
- 分类: cs.CL
- 相关性评分: 28
- 主题标签: 紧凑模型、多模态、解码优化、文档理解、边缘计算

**中文摘要**

> 本文介绍了GLM-OCR，一个高效的0.9B参数紧凑多模态模型，专为现实世界文档理解设计。模型结合0.4B参数的CogViT视觉编码器和0.5B参数的GLM语言解码器，在计算效率和识别性能间取得平衡。针对确定性OCR任务中自回归解码的低效问题，引入多令牌预测机制，每步预测多个令牌，显著提高解码吞吐量，同时通过共享参数保持低内存开销。系统层面采用两阶段管道：PP-DocLayout-V3先进行布局分析，然后并行区域级识别。在公共基准和工业场景的广泛评估中，GLM-OCR在文档解析、文本和公式转录、表格结构恢复及关键信息提取方面达到竞争性或最先进性能，其紧凑架构和结构化生成适合资源受限的边缘部署和大规模生产系统。

**核心创新概述**

> 提出一个紧凑多模态模型，通过多令牌预测机制优化解码效率，结合两阶段管道实现高效的文档理解，在性能和资源使用间取得平衡。

**创新点拆解**

- 多令牌预测机制，提高自回归解码吞吐量，减少内存开销
- 紧凑架构设计，结合CogViT视觉编码器和GLM语言解码器，参数仅0.9B
- 两阶段管道，先布局分析后并行区域识别，提升系统效率

**当前局限**

> 模型可能对某些复杂布局或低质量图像的处理能力有限；紧凑架构可能在极端精度要求场景下性能不足。

**后续可改进方向**

- 进一步优化多令牌预测机制，适应更多OCR任务类型
- 增强模型对噪声图像和多语言文档的鲁棒性
- 探索更高效的训练策略，以降低计算成本

**工程启发**

> 高，紧凑设计和高效解码使其适合边缘部署和大规模应用，在工业场景中具有直接实用价值。

**为什么值得关注**

> 核心为OCR模型，专注于文档理解和文本提取，是OCR技术的前沿进展。

**原始摘要**

GLM-OCR is an efficient 0.9B-parameter compact multimodal model designed for real-world document
understanding. It combines a 0.4B-parameter CogViT visual encoder with a 0.5B-parameter GLM language
decoder, achieving a strong balance between computational efficiency and recognition performance. To
address the inefficiency of standard autoregressive decoding in deterministic OCR tasks, GLM-OCR
introduces a Multi-Token Prediction (MTP) mechanism that predicts multiple tokens per step,
significantly improving decoding throughput while keeping memory overhead low through shared
parameters. At the system level, a two-stage pipeline is adopted: PP-DocLayout-V3 first performs
layout analysis, followed by parallel region-level recognition. Extensive evaluations on public
benchmarks and industrial scenarios show that GLM-OCR achieves competitive or state-of-the-art
performance in document parsing, text and formula transcription, table structure recovery, and key
information extraction. Its compact architecture and structured generation make it suitable for both
resource-constrained edge deployment and large-scale production systems.

---

### 3. Agentar-Fin-OCR

- arXiv: [2603.11044v1](https://arxiv.org/abs/2603.11044v1)
- PDF: [下载链接](https://arxiv.org/pdf/2603.11044v1)
- 作者: Siyi Qian, Xiongfei Bai, Bingtao Fu, Yichen Lu, Gaoyang Zhang, Xudong Yang, Peng Zhang
- 发布时间: 2026-03-11T17:59:42Z
- 分类: cs.CV
- 相关性评分: 27
- 主题标签: 金融文档、跨页解析、表格识别、课程学习、基准评估

**中文摘要**

> 本文提出Agentar-Fin-OCR，一个针对金融领域文档的解析系统，将超长金融PDF转换为语义一致、高精度、结构化的输出，并具备审计级可追溯性。为应对金融特定挑战（如复杂布局、跨页结构不连续和单元格级引用能力），系统结合（1）跨页内容整合算法以恢复页面间连续性，以及文档级标题层次重建模块以构建全局一致的内容目录树，支持结构感知检索；（2）难度自适应课程学习训练策略用于表格解析，以及CellBBoxRegressor模块，使用结构锚令牌从解码器隐藏状态定位表格单元格，无需外部检测器。实验表明，模型在OmniDocBench的表格解析指标上表现优异。为在金融垂直领域进行现实评估，进一步引入FinDocBench基准，包含六个金融文档类别，带有专家验证注释和评估指标（如基于编辑距离的内容目录相似性、跨页拼接TEDS和表格单元格交并比）。在FinDocBench上评估多种最先进模型，评估其在金融文档上的能力和剩余限制。总体而言，Agentar-Fin-OCR和FinDocBench为可靠的下游应用提供了实用基础。

**核心创新概述**

> 针对金融文档的特定挑战，提出跨页内容整合和文档级标题重建方法，结合难度自适应训练和无需外部检测器的单元格定位，实现高精度结构化解析。

**创新点拆解**

- 跨页内容整合算法和文档级标题层次重建模块，处理金融文档的布局不连续性
- 难度自适应课程学习训练策略，优化表格解析性能
- CellBBoxRegressor模块，利用结构锚令牌从解码器状态定位单元格，减少外部依赖

**当前局限**

> 系统可能对非金融文档或极不规则布局的泛化能力有限；FinDocBench基准覆盖范围可能不够全面。

**后续可改进方向**

- 扩展系统以处理更多文档类型和语言，提高通用性
- 优化跨页整合算法，应对更复杂的文档结构
- 增强基准的多样性和评估指标，促进更全面的模型比较

**工程启发**

> 高，为金融领域提供了专门的文档解析解决方案，审计级可追溯性和高精度使其在金融应用中具有重要价值。

**为什么值得关注**

> 涉及OCR和文档解析技术，特别是针对复杂金融文档的处理，是OCR在垂直领域的应用案例。

**原始摘要**

In this paper, we propose Agentar-Fin-OCR, a document parsing system tailored to financial-domain
documents, transforming ultra-long financial PDFs into semantically consistent, highly accurate,
structured outputs with auditing-grade provenance. To address finance-specific challenges such as
complex layouts, cross-page structural discontinuities, and cell-level referencing capability,
Agentar-Fin-OCR combines (1) a Cross-page Contents Consolidation algorithm to restore continuity
across pages and a Document-level Heading Hierarchy Reconstruction (DHR) module to build a globally
consistent Table of Contents (TOC) tree for structure-aware retrieval, and (2) a difficulty-adaptive
curriculum learning training strategy for table parsing, together with a CellBBoxRegressor module
that uses structural anchor tokens to localize table cells from decoder hidden states without
external detectors. Experiments demonstrate that our model shows high performance on the table
parsing metrics of OmniDocBench. To enable realistic evaluation in the financial vertical, we
further introduce FinDocBench, a benchmark that includes six financial document categories with
expert-verified annotations and evaluation metrics including Table of Contents edit-distance-based
similarity (TocEDS), cross-page concatenated TEDS, and Table Cell Intersection over Union (C-IoU).
We evaluate a wide range of state-of-the-art models on FinDocBench to assess their capabilities and
remaining limitations on financial documents. Overall, Agentar-Fin-OCR and FinDocBench provide a
practical foundation for reliable downstream financial document applications.

---

### 4. ICDAR 2025 Competition on End-to-End Document Image Machine Translation Towards Complex Layouts

- arXiv: [2603.09392v1](https://arxiv.org/abs/2603.09392v1)
- PDF: [下载链接](https://arxiv.org/pdf/2603.09392v1)
- 作者: Yaping Zhang, Yupu Liang, Zhiyang Zhang, Zhiyuan Chen, Lu Xiang, Yang Zhao, Yu Zhou, Chengqing Zong
- 发布时间: 2026-03-10T09:04:38Z
- 分类: cs.CV, cs.AI
- 相关性评分: 26
- 主题标签: 文档图像翻译、多模态、竞赛组织、端到端学习、大模型

**中文摘要**

> 本文介绍了ICDAR 2025文档图像机器翻译竞赛，该竞赛旨在通过联合建模文本内容和页面布局，将文档图像中的文本从一种语言翻译到另一种语言，桥接OCR和自然语言处理。DIMT 2025挑战赛推进了端到端文档图像翻译的研究，这是多模态文档理解中快速发展的领域。竞赛包含两个赛道（OCR-free和OCR-based），每个赛道有两个子任务（小模型和大模型）。参赛者提交统一的DIMT系统，可选择结合提供的OCR转录。竞赛从2024年12月10日运行至2025年4月20日，吸引了69个团队和27个有效提交。赛道1有34个团队和13个有效提交，赛道2有35个团队和14个有效提交。本报告介绍了挑战动机、数据集构建、任务定义、评估协议和结果总结。分析表明，大模型方法为翻译复杂布局文档图像建立了有前景的新范式，并突出了未来研究的重大机会。

**核心创新概述**

> 组织首个专注于文档图像机器翻译的竞赛，定义OCR-free和OCR-based赛道，推动端到端多模态翻译研究，并总结大模型在该领域的潜力。

**创新点拆解**

- 定义文档图像机器翻译任务，桥接OCR和NLP，促进多模态研究
- 设计双赛道竞赛结构，区分是否使用OCR，鼓励多样化方法
- 提供大规模数据集和评估协议，为社区建立基准

**当前局限**

> 竞赛结果可能受限于数据集规模和多样性；大模型方法可能计算成本高，不适合资源受限场景。

**后续可改进方向**

- 扩展数据集以包含更多语言和复杂布局类型
- 开发更高效的端到端模型，降低计算需求
- 探索小模型在文档图像翻译中的优化策略

**工程启发**

> 中，竞赛推动了技术前沿，但实际工程应用需进一步模型优化和部署。

**为什么值得关注**

> 直接涉及OCR技术作为文档图像翻译的基础，是OCR在多模态任务中的关键应用。

**原始摘要**

Document Image Machine Translation (DIMT) seeks to translate text embedded in document images from
one language to another by jointly modeling both textual content and page layout, bridging optical
character recognition (OCR) and natural language processing (NLP). The DIMT 2025 Challenge advances
research on end-to-end document image translation, a rapidly evolving area within multimodal
document understanding. The competition features two tracks, OCR-free and OCR-based, each with two
subtasks for small (less than 1B parameters) and large (greater than 1B parameters) models.
Participants submit a single unified DIMT system, with the option to incorporate provided OCR
transcripts. Running from December 10, 2024 to April 20, 2025, the competition attracted 69 teams
and 27 valid submissions in total. Track 1 had 34 teams and 13 valid submissions, while Track 2 had
35 teams and 14 valid submissions. In this report, we present the challenge motivation, dataset
construction, task definitions, evaluation protocol, and a summary of results. Our analysis shows
that large-model approaches establish a promising new paradigm for translating complex-layout
document images and highlight substantial opportunities for future research.

---

### 5. A Robust Deep Learning Framework for Bangla License Plate Recognition Using YOLO and Vision-Language OCR

- arXiv: [2603.10267v1](https://arxiv.org/abs/2603.10267v1)
- PDF: [下载链接](https://arxiv.org/pdf/2603.10267v1)
- 作者: Nayeb Hasin, Md. Arafath Rahman Nishat, Mainul Islam, Khandakar Shakib Al Hasan, Asif Newaz
- 发布时间: 2026-03-10T22:55:59Z
- 分类: cs.CV
- 相关性评分: 25
- 主题标签: 车牌识别、对象检测、序列生成、鲁棒性评估、孟加拉语OCR

**中文摘要**

> 本文提出一个鲁棒的孟加拉车牌识别系统，集成基于深度学习的对象检测模型用于车牌定位和OCR用于文本提取。比较了多种对象检测架构（包括U-Net和多个YOLO变体）用于车牌定位。研究基于YOLOv8架构提出一种新颖的两阶段自适应训练策略，以提高定位性能。所提方法优于现有模型，达到97.83%的准确率和91.3%的交并比。文本识别问题被表述为序列生成问题，采用VisionEncoderDecoder架构，评估了多种编码器-解码器组合。结果表明，ViT + BanglaBERT模型在字符级别表现更好，字符错误率为0.1323，词错误率为0.1068。所提系统在外部数据集上测试也表现一致，该数据集具有与训练样本完全不同的环境和光照条件，表明框架的鲁棒性。总体而言，所提系统为孟加拉车牌识别提供了鲁棒可靠的解决方案。

**核心创新概述**

> 针对孟加拉车牌的复杂字符和布局挑战，提出两阶段自适应训练策略优化YOLOv8定位，并结合VisionEncoderDecoder架构进行文本识别，实现高精度和鲁棒性。

**创新点拆解**

- 两阶段自适应训练策略，基于YOLOv8优化车牌定位性能
- 将文本识别建模为序列生成问题，评估多种编码器-解码器组合
- 使用外部数据集验证鲁棒性，涵盖不同环境和光照条件

**当前局限**

> 系统可能对其他语言或车牌类型的泛化能力有限；依赖特定数据集，实际部署中可能需适应更多变体。

**后续可改进方向**

- 扩展系统以支持多语言车牌识别，提高通用性
- 优化训练策略，减少对标注数据的依赖
- 增强模型对极端天气或遮挡条件的鲁棒性

**工程启发**

> 高，为智能交通管理提供了实用的车牌识别解决方案，高精度和鲁棒性使其适合实际部署。

**为什么值得关注**

> 涉及OCR技术用于文本提取，是OCR在特定垂直领域（车牌识别）的应用案例。

**原始摘要**

An Automatic License Plate Recognition (ALPR) system constitutes a crucial element in an intelligent
traffic management system. However, the detection of Bangla license plates remains challenging
because of the complicated character scheme and uneven layouts. This paper presents a robust Bangla
License Plate Recognition system that integrates a deep learning-based object detection model for
license plate localization with Optical Character Recognition for text extraction. Multiple object
detection architectures, including U-Net and several YOLO (You Only Look Once) variants, are
compared for license plate localization. This study proposes a novel two-stage adaptive training
strategy built upon the YOLOv8 architecture to improve localization performance. The proposed
approach outperforms the established models, achieving an accuracy of 97.83% and an Intersection
over Union (IoU) of 91.3%. The text recognition problem is phrased as a sequence generation problem
with a VisionEncoderDecoder architecture, with a combination of encoder-decoders evaluated. It was
demonstrated that the ViT + BanglaBERT model gives better results at the character level, with a
Character Error Rate of 0.1323 and Word Error Rate of 0.1068. The proposed system also shows a
consistent performance when tested on an external dataset that has been curated for this study
purpose. The dataset offers completely different environment and lighting conditions compared to the
training sample, indicating the robustness of the proposed framework. Overall, our proposed system
provides a robust and reliable solution for Bangla license plate recognition and performs
effectively across diverse real-world scenarios, including variations in lighting, noise, and plate
styles. These strengths make it well suited for deployment in intelligent transportation
applications such as automated law enforcement and access control.

---

### 6. The Patrologia Graeca Corpus: OCR, Annotation, and Open Release of Noisy Nineteenth-Century Polytonic Greek Editions

- arXiv: [2603.09470v1](https://arxiv.org/abs/2603.09470v1)
- PDF: [下载链接](https://arxiv.org/pdf/2603.09470v1)
- 作者: Chahan Vidal-Gorène, Bastien Kindt
- 发布时间: 2026-03-10T10:21:54Z
- 分类: cs.CV
- 相关性评分: 18
- 主题标签: 历史文档OCR、多调希腊语、语料库发布、布局检测、噪声文本识别

**中文摘要**

> 本文介绍了Patrologia Graeca语料库，首个针对19世纪古希腊版本的大规模开放OCR和语言资源。该集合覆盖了Patrologia Graeca剩余未数字化的卷册，这些卷册以复杂的双语（希腊语-拉丁语）布局印刷，并具有高度退化的多调希腊语排版。通过专用管道结合基于YOLO的布局检测和基于CRNN的文本识别，实现了1.05%的字符错误率和4.69%的词错误率，大幅优于现有的多调希腊语OCR系统。所得语料库包含约六百万个词元化和词性标注的令牌，与完整的OCR和布局注释对齐。除了其文献学价值外，该语料库为噪声多调希腊语OCR建立了新基准，并为未来模型（包括大语言模型）提供了训练材料。

**核心创新概述**

> 针对高度退化的多调希腊语文档，提出专用OCR管道，结合YOLO布局检测和CRNN文本识别，实现低错误率，并发布首个大规模开放语料库。

**创新点拆解**

- 专用OCR管道，结合YOLO和CRNN，优化对噪声多调希腊语文档的处理
- 发布大规模开放语料库，包含OCR、布局和语言注释，促进研究
- 为多调希腊语OCR建立新基准，推动技术进展

**当前局限**

> 语料库可能覆盖文档类型有限；管道可能对其他语言或布局的泛化能力不足。

**后续可改进方向**

- 扩展语料库以包含更多历史文档类型和语言
- 优化OCR管道，提高对极端退化文本的识别精度
- 探索利用语料库训练更高效的多模态模型

**工程启发**

> 中，语料库和基准对学术研究有价值，但实际工程应用需进一步模型优化。

**为什么值得关注**

> 核心为OCR技术，专注于噪声文档的文本提取和布局分析，是OCR在历史文档处理中的前沿应用。

**原始摘要**

We present the Patrologia Graeca Corpus, the first large-scale open OCR and linguistic resource for
nineteenthcentury editions of Ancient Greek. The collection covers the remaining undigitized volumes
of the Patrologia Graeca (PG), printed in complex bilingual (Greek-Latin) layouts and characterized
by highly degraded polytonic Greek typography. Through a dedicated pipeline combining YOLO-based
layout detection and CRNN-based text recognition, we achieve a character error rate (CER) of 1.05%
and a word error rate (WER) of 4.69%, largely outperforming existing OCR systems for polytonic
Greek. The resulting corpus contains around six million lemmatized and part-of-speech tagged tokens,
aligned with full OCR and layout annotations. Beyond its philological value, this corpus establishes
a new benchmark for OCR on noisy polytonic Greek and provides training material for future models,
including LLMs.

---

### 7. SiDiaC-v.2.0: Sinhala Diachronic Corpus Version 2.0

- arXiv: [2603.10861v1](https://arxiv.org/abs/2603.10861v1)
- PDF: [下载链接](https://arxiv.org/pdf/2603.10861v1)
- 作者: Nevidu Jayatilleke, Nisansa de Silva, Uthpala Nimanthi, Gagani Kulathilaka, Azra Safrullah, Johan Sofalas
- 发布时间: 2026-03-11T15:10:32Z
- 分类: cs.CL
- 相关性评分: 13
- 主题标签: 低资源语言、语料库构建、OCR后处理、历时分析、文本标注

**中文摘要**

> SiDiaC-v.2.0 是目前最大的僧伽罗语历时语料库，覆盖出版日期从公元1800年到1955年，书写日期从公元5世纪到20世纪。该语料库包含185部文学作品中的24.4万个单词，经过严格筛选、预处理和版权合规检查，并进行广泛后处理。此外，一个包含59份文档、总计7万个单词的子集根据书写日期进行了标注。文本选自斯里兰卡国家图书馆的SiDiaC-v.1.0未筛选列表，使用Google Document AI OCR进行数字化，后处理包括纠正格式问题、处理代码混合、添加特殊标记和修复错误标记。语料库构建借鉴了其他语料库（如FarPaHC、SiDiaC-v.1.0和CCOHA）的做法，特别是在句法标注和文本规范化策略方面，考虑到法罗语和僧伽罗语同为低资源语言的相似性。语料库按体裁分为两层：主要分类为二元（非虚构或虚构），次要分类更详细，包括宗教、历史、诗歌、语言和医学等具体体裁。尽管面临资源有限的挑战，SiDiaC-v.2.0为僧伽罗语NLP提供了全面资源。

**核心创新概述**

> 构建了目前最大的僧伽罗语历时语料库，覆盖广泛历史时期，并引入基于书写日期的标注子集，结合OCR数字化和后处理流程，为低资源语言NLP研究提供标准化数据。

**创新点拆解**

- 大规模历时语料库构建，涵盖多个世纪的历史跨度
- 基于书写日期的标注子集，支持时间序列分析
- 利用Google Document AI OCR进行数字化，结合后处理纠正格式和标记问题
- 借鉴其他低资源语料库的标注和规范化策略，提升数据质量
- 按体裁分层分类，支持多领域NLP任务

**当前局限**

> 语料库规模相对较小（24.4万单词），覆盖时期可能不完整，后处理可能引入人为错误，且依赖特定OCR工具（Google Document AI），通用性受限。

**后续可改进方向**

- 扩展语料库规模，纳入更多历史时期和体裁
- 开发更鲁棒的OCR后处理算法，减少人工干预
- 探索多语言OCR工具比较，提升数字化效率
- 增强标注深度，如句法或语义层面
- 集成更多低资源语言语料库构建最佳实践

**工程启发**

> 为僧伽罗语NLP任务（如文本分类、语言建模）提供基准数据集，支持低资源语言研究，可应用于历史文献数字化和文化遗产保护。

**为什么值得关注**

> 涉及OCR技术在低资源语言文档数字化中的应用，后处理流程对OCR错误纠正有参考价值，语料库构建方法可推广到其他语言。

**原始摘要**

SiDiaC-v.2.0 is the largest comprehensive Sinhala Diachronic Corpus to date, covering a period from
1800 CE to 1955 CE in terms of publication dates, and a historical span from the 5th to the 20th
century CE in terms of written dates. The corpus consists of 244k words across 185 literary works
that underwent thorough filtering, preprocessing, and copyright compliance checks, followed by
extensive post-processing. Additionally, a subset of 59 documents totalling 70k words was annotated
based on their written dates. Texts from the National Library of Sri Lanka were selected from the
SiDiaC-v.1.0 non-filtered list, which was digitised using Google Document AI OCR. This was followed
by post-processing to correct formatting issues, address code-mixing, include special tokens, and
fix malformed tokens. The construction of SiDiaC-v.2.0 was informed by practices from other corpora,
such as FarPaHC, SiDiaC-v.1.0, and CCOHA. This was particularly relevant for syntactic annotation
and text normalisation strategies, given the shared characteristics of low-resource language status
between Faroese and the similar cleaning strategies utilised in CCOHA. This corpus is categorised
into two layers based on genres: primary and secondary. The primary categorisation is binary,
assigning each book to either Non-Fiction or Fiction. The secondary categorisation is more detailed,
grouping texts under specific genres such as Religious, History, Poetry, Language, and Medical.
Despite facing challenges due to limited resources, SiDiaC-v.2.0 serves as a comprehensive resource
for Sinhala NLP, building upon the work previously done in SiDiaC-v.1.0.

---

### 8. PromptDLA: A Domain-aware Prompt Document Layout Analysis Framework with Descriptive Knowledge as a Cue

- arXiv: [2603.09414v1](https://arxiv.org/abs/2603.09414v1)
- PDF: [下载链接](https://arxiv.org/pdf/2603.09414v1)
- 作者: Zirui Zhang, Yaping Zhang, Lu Xiang, Yang Zhao, Feifei Zhai, Yu Zhou, Chengqing Zong
- 发布时间: 2026-03-10T09:30:00Z
- 分类: cs.CV, cs.AI
- 相关性评分: 11
- 主题标签: 文档布局分析、提示学习、领域自适应、多域泛化、计算机视觉

**中文摘要**

> 文档布局分析（DLA）对文档人工智能至关重要，近年来受到关注，涌现了大量公共DLA数据集。现有工作常结合不同领域的数据集以提升DLA泛化能力，但直接合并训练往往导致性能次优，因为忽略了不同领域固有的布局结构差异，如标注风格、文档类型和语言。本文提出PromptDLA，一个领域感知的提示文档布局分析框架，有效利用描述性知识作为线索，将领域先验集成到DLA中。创新的PromptDLA具有独特的领域感知提示器，根据数据域特定属性定制提示，这些提示作为线索引导DLA关注关键特征和结构，增强模型跨域泛化能力。大量实验表明，该方法在DocLayNet、PubLayNet、M6Doc和D$^4$LA数据集上达到最先进性能。

**核心创新概述**

> 提出首个领域感知提示框架PromptDLA，通过定制化提示整合领域先验，解决多域DLA数据集合并训练时的布局结构差异问题，显著提升跨域泛化性能。

**创新点拆解**

- 领域感知提示器设计，基于数据属性动态生成提示
- 利用描述性知识作为线索，引导模型关注关键布局特征
- 集成领域先验到DLA任务，减少多域数据冲突
- 在多个公共数据集上验证SOTA性能
- 开源代码促进可复现性

**当前局限**

> 提示设计可能依赖手动领域知识定义，泛化到未见领域有限，实验数据集主要为英文文档，多语言支持未充分验证。

**后续可改进方向**

- 自动化提示生成，减少人工干预
- 扩展多语言和低资源文档评估
- 集成更复杂的领域自适应技术
- 探索提示与模型架构的协同优化
- 增强对非标准布局（如手写文档）的处理能力

**工程启发**

> 提升文档AI系统的布局分析准确性和泛化能力，适用于多领域文档处理（如学术论文、商业报告），支持下游任务如OCR和内容提取。

**为什么值得关注**

> 直接针对文档布局分析任务，与OCR紧密相关，提示方法可迁移到其他文档解析任务，为多域OCR系统提供新思路。

**原始摘要**

Document Layout Analysis (DLA) is crucial for document artificial intelligence and has recently
received increasing attention, resulting in an influx of large-scale public DLA datasets. Existing
work often combines data from various domains in recent public DLA datasets to improve the
generalization of DLA. However, directly merging these datasets for training often results in
suboptimal model performance, as it overlooks the different layout structures inherent to various
domains. These variations include different labeling styles, document types, and languages. This
paper introduces PromptDLA, a domain-aware Prompter for Document Layout Analysis that effectively
leverages descriptive knowledge as cues to integrate domain priors into DLA. The innovative
PromptDLA features a unique domain-aware prompter that customizes prompts based on the specific
attributes of the data domain. These prompts then serve as cues that direct the DLA toward critical
features and structures within the data, enhancing the model's ability to generalize across varied
domains. Extensive experiments show that our proposal achieves state-of-the-art performance among
DocLayNet, PubLayNet, M6Doc, and D$^4$LA. Our code is available at
https://github.com/Zirui00/PromptDLA.

---

### 9. Logics-Parsing-Omni Technical Report

- arXiv: [2603.09677v1](https://arxiv.org/abs/2603.09677v1)
- PDF: [下载链接](https://arxiv.org/pdf/2603.09677v1)
- 作者: Xin An, Jingyi Cai, Xiangyang Chen, Huayao Liu, Peiting Liu, Peng Wang, Bei Yang, Xiuwen Zhu, Yongfan Chen, Baoyu Hou, Shuzhao Li, Weidong Ren, Fan Yang, Jiangtao Zhang, Xiaoxiao Xu, Lin Qu
- 发布时间: 2026-03-10T13:46:32Z
- 分类: cs.AI
- 相关性评分: 10
- 主题标签: 多模态解析、统一分类法、证据锚定、OCR集成、结构化知识提取

**中文摘要**

> 针对多模态解析中任务定义碎片化和非结构化数据异质性的挑战，本文提出Omni Parsing框架。该框架建立了一个覆盖文档、图像和音视频流的统一分类法，引入渐进式解析范式，连接感知和认知。具体包括三个层次：1）整体检测，实现对象或事件的精确时空定位，为感知建立几何基线；2）细粒度识别，对局部对象进行符号化（如OCR/ASR）和属性提取，完成结构化实体解析；3）多级解释，构建从局部语义到全局逻辑的推理链。关键优势是证据锚定机制，强制高层语义描述与低层事实严格对齐，实现“基于证据”的逻辑归纳，将非结构化信号转换为可定位、可枚举和可追溯的标准化知识。基于此，构建了标准化数据集并发布Logics-Parsing-Omni模型，成功将复杂音视频信号转换为机器可读结构化知识。实验表明细粒度感知与高层认知协同，有效提升模型可靠性。此外，引入OmniParsingBench进行定量评估。

**核心创新概述**

> 提出统一的多模态解析框架Omni Parsing，整合文档、图像和音视频流，通过渐进式解析和证据锚定机制，实现从低层感知到高层认知的端到端结构化知识转换。

**创新点拆解**

- 统一分类法覆盖多模态数据，减少任务碎片化
- 渐进式解析范式，分层处理从检测到解释
- 证据锚定机制，确保语义与事实对齐
- 集成OCR/ASR作为符号化步骤，支持结构化实体解析
- 发布标准化数据集和模型，促进可复现研究

**当前局限**

> 框架复杂度高，可能计算开销大；证据锚定依赖精确的低层检测，错误传播风险；多模态数据融合挑战未完全解决。

**后续可改进方向**

- 优化计算效率，适用于实时应用
- 增强错误容忍机制，减少传播影响
- 扩展更多模态（如3D数据）支持
- 开发更鲁棒的证据对齐算法
- 探索轻量级模型变体

**工程启发**

> 为多模态AI系统提供统一解析框架，适用于文档分析、视频理解和知识图谱构建，提升自动化处理能力。

**为什么值得关注**

> 直接集成OCR作为关键组件，用于文档符号化，框架方法可提升OCR在复杂多模态环境中的性能，支持端到端文档解析。

**原始摘要**

Addressing the challenges of fragmented task definitions and the heterogeneity of unstructured data
in multimodal parsing, this paper proposes the Omni Parsing framework. This framework establishes a
Unified Taxonomy covering documents, images, and audio-visual streams, introducing a progressive
parsing paradigm that bridges perception and cognition. Specifically, the framework integrates three
hierarchical levels: 1) Holistic Detection, which achieves precise spatial-temporal grounding of
objects or events to establish a geometric baseline for perception; 2) Fine-grained Recognition,
which performs symbolization (e.g., OCR/ASR) and attribute extraction on localized objects to
complete structured entity parsing; and 3) Multi-level Interpreting, which constructs a reasoning
chain from local semantics to global logic. A pivotal advantage of this framework is its evidence
anchoring mechanism, which enforces a strict alignment between high-level semantic descriptions and
low-level facts. This enables ``evidence-based'' logical induction, transforming unstructured
signals into standardized knowledge that is locatable, enumerable, and traceable. Building on this
foundation, we constructed a standardized dataset and released the Logics-Parsing-Omni model, which
successfully converts complex audio-visual signals into machine-readable structured knowledge.
Experiments demonstrate that fine-grained perception and high-level cognition are synergistic,
effectively enhancing model reliability. Furthermore, to quantitatively evaluate these capabilities,
we introduce OmniParsingBench. Code, models and the benchmark are released at
https://github.com/alibaba/Logics-Parsing/tree/master/Logics-Parsing-Omni.

---

### 10. Tracking Cancer Through Text: Longitudinal Extraction From Radiology Reports Using Open-Source Large Language Models

- arXiv: [2603.09638v2](https://arxiv.org/abs/2603.09638v2)
- PDF: [下载链接](https://arxiv.org/pdf/2603.09638v2)
- 作者: Luc Builtjes, Alessa Hering
- 发布时间: 2026-03-10T13:13:43Z
- 分类: cs.CL
- 相关性评分: 6
- 主题标签: 临床文本提取、开源LLM、纵向分析、隐私保护、医疗文档解析

**中文摘要**

> 放射学报告捕获了肿瘤负荷、治疗反应和疾病进展的关键纵向信息，但其非结构化叙述格式使自动化分析复杂化。尽管大语言模型（LLMs）推进了临床文本处理，但大多数最先进系统是专有的，限制了在隐私敏感医疗环境中的应用。我们提出一个完全开源、可本地部署的流水线，用于从放射学报告中提取纵向信息，使用llm_extractinator框架实现。系统应用qwen2.5-72b模型，根据RECIST标准提取和链接目标、非目标和新病灶数据跨时间点。在50对荷兰CT胸腹报告对上评估，提取性能高，属性级准确度为目标病灶93.7%、非目标病灶94.9%、新病灶94.0%。该方法表明开源LLMs能在多时间点肿瘤学任务中实现临床意义性能，同时确保数据隐私和可复现性。结果突显了可本地部署LLMs在从常规临床文本中提取结构化纵向数据方面的潜力。

**核心创新概述**

> 开发首个完全开源、可本地部署的流水线，利用开源LLM（qwen2.5-72b）从放射学报告中提取纵向信息，实现高精度临床数据提取，同时解决医疗隐私问题。

**创新点拆解**

- 开源本地部署流水线，避免专有系统限制
- 使用qwen2.5-72b模型，实现高精度多时间点提取
- 遵循RECIST标准，确保临床相关性
- 在隐私敏感环境中验证性能
- 促进可复现和可扩展的医疗文本分析

**当前局限**

> 评估数据集较小（50对报告），可能泛化性有限；模型依赖特定LLM，未比较其他开源模型；多语言支持（如荷兰语）未广泛测试。

**后续可改进方向**

- 扩大数据集规模和多样性，提升泛化能力
- 比较不同开源LLMs的性能
- 扩展多语言和跨机构验证
- 集成更复杂的时序建模技术
- 优化本地部署效率

**工程启发**

> 为医疗AI提供隐私安全的文本提取工具，支持肿瘤学研究和临床决策，降低数据共享风险。

**为什么值得关注**

> 涉及文档解析（放射学报告）和OCR后文本处理，开源方法可迁移到其他文档类型，为OCR系统在医疗领域的应用提供案例。

**原始摘要**

Radiology reports capture crucial longitudinal information on tumor burden, treatment response, and
disease progression, yet their unstructured narrative format complicates automated analysis. While
large language models (LLMs) have advanced clinical text processing, most state-of-the-art systems
remain proprietary, limiting their applicability in privacy-sensitive healthcare environments. We
present a fully open-source, locally deployable pipeline for longitudinal information extraction
from radiology reports, implemented using the llm_extractinator framework. The system applies the
qwen2.5-72b model to extract and link target, non-target, and new lesion data across time points in
accordance with RECIST criteria. Evaluation on 50 Dutch CT Thorax/Abdomen report pairs yielded high
extraction performance, with attribute-level accuracies of 93.7% for target lesions, 94.9% for non-
target lesions, and 94.0% for new lesions. The approach demonstrates that open-source LLMs can
achieve clinically meaningful performance in multi-timepoint oncology tasks while ensuring data
privacy and reproducibility. These results highlight the potential of locally deployable LLMs for
scalable extraction of structured longitudinal data from routine clinical text.

---
