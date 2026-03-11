# OCR / 文档解析研究日报（2026-03-11）

## 报告说明

- 检索源：arXiv API
- 检索查询：`(all:"document parsing" OR all:"document understanding" OR all:"optical character recognition" OR all:OCR OR all:"layout analysis" OR all:"document layout analysis" OR all:"text recognition" OR all:"table recognition" OR all:"form understanding" OR all:"document intelligence" OR all:"page understanding" OR all:"scene text recognition" OR all:"handwritten text recognition" OR all:"information extraction") AND (cat:cs.CV OR cat:cs.AI OR cat:cs.CL OR cat:eess.IV)`
- 生成时间（UTC）：`2026-03-11 03:35:46`
- 大模型综合分析：`开启`

## 一、今日执行摘要

> 今日OCR/文档解析研究呈现多领域融合与专业化趋势。核心进展包括：1）针对特定领域（物理、医疗、古籍）的本地化、高精度解析系统开发，强调数据隐私与专用流程；2）多模态与端到端任务（如文档图像翻译、数学表达式识别）的基准建立与模型创新，推动布局理解与内容识别协同；3）框架级探索，如统一多模态解析、领域自适应布局分析，旨在解决泛化性与结构化知识转换挑战。研究普遍关注大模型应用、计算效率与工程部署，为实际场景提供多样化解决方案。

## 二、今日趋势判断

研究趋势聚焦于：1）领域专业化：从通用OCR转向物理、医疗、古籍等垂直场景，结合领域知识提升精度（如MITRA、Patrologia Graeca、医疗报告提取）；2）多模态集成：强化布局解析、图像翻译、数学符号识别等多模态任务，推动端到端学习（如ICDAR竞赛、数学表达式识别）；3）框架标准化：通过统一分类法、渐进式解析、共识机制等构建可泛化框架（如Omni Parsing、PromptDLA、多LLM管道）；4）工程友好性：强调本地化部署、开源模型、结构化输出，以平衡性能、隐私与成本（如MITRA、医疗管道、OfficeQA Pro）。

## 三、今日论文概览

1. **MITRA: An AI Assistant for Knowledge Retrieval in Physics Collaborations** | 标签：检索增强生成、OCR布局解析、本地化部署、科学文档处理、向量数据库
2. **ICDAR 2025 Competition on End-to-End Document Image Machine Translation Towards Complex Layouts** | 标签：文档图像翻译、多模态理解、ICDAR竞赛、端到端学习、布局建模
3. **The Patrologia Graeca Corpus: OCR, Annotation, and Open Release of Noisy Nineteenth-Century Polytonic Greek Editions** | 标签：多调希腊语OCR、古文献数字化、布局检测、嘈杂文本识别、语料库构建
4. **A Hybrid Vision Transformer Approach for Mathematical Expression Recognition** | 标签：数学表达式识别、视觉变换器、2D位置编码、覆盖注意力、文档分析
5. **OfficeQA Pro: An Enterprise Benchmark for End-to-End Grounded Reasoning** | 标签：文档推理基准、大语言模型评估、表格数据处理、结构化表示、企级AI
6. **PromptDLA: A Domain-aware Prompt Document Layout Analysis Framework with Descriptive Knowledge as a Cue** | 标签：文档布局分析、提示学习、领域自适应、多领域泛化、结构理解
7. **Logics-Parsing-Omni Technical Report** | 标签：多模态解析、统一分类法、证据锚定、结构化知识转换、OCR
8. **A Consensus-Driven Multi-LLM Pipeline for Missing-Person Investigations** | 标签：多LLM管道、共识机制、QLoRA微调、信息提取、结构化处理
9. **Tracking Cancer Through Text: Longitudinal Extraction From Radiology Reports Using Open-Source Large Language Models** | 标签：开源LLM、纵向信息提取、医疗文本处理、结构化数据、隐私保护

## 四、今天 OCR / 文档解析论文里的主要创新点

- 结合布局检测与文本识别的专用OCR流程以处理复杂或退化文档（如古籍、科学文档）。
- 采用本地化或开源部署的RAG/LLM管道，确保数据隐私并支持敏感领域应用（如物理合作、医疗报告）。
- 引入多模态或端到端学习框架，整合OCR、NLP与视觉理解以处理文档翻译、数学表达式等任务。
- 设计领域自适应或提示学习机制，提升模型在多样化文档布局上的泛化性能。
- 构建大规模基准或语料库，推动文档解析、推理任务的标准化评估与模型训练。

## 五、后续 OCR 领域值得推进的改进方向

- 开发更鲁棒的OCR模块，专门针对复杂科学符号、多调古文字或严重退化文本的识别。
- 优化端到端文档图像翻译系统，集成布局建模与多语言支持，并研究小模型的高效替代方案。
- 扩展多模态解析框架，支持图表、表格等非文本元素的自动化理解与结构化转换。
- 研究自适应学习机制，使文档解析系统能动态处理数据更新或新领域，减少人工标注依赖。
- 提升企级文档推理能力，通过增强表格数据处理、检索精度和结构化表示来支持大规模异构语料库。

## 六、工程落地启发

- 在隐私敏感场景（如医疗、科研）优先采用本地化部署的RAG或开源LLM管道，确保数据安全。
- 针对特定文档类型（如古籍、科学报告）设计专用OCR流程，结合布局解析以提升提取精度。
- 利用领域自适应提示或共识机制，增强文档布局分析和信息提取系统在多场景下的泛化能力。
- 集成结构化输出和证据锚定机制，提升文档解析结果的可靠性、可审计性和下游应用价值。
- 参考现有基准（如OfficeQA Pro、ICDAR竞赛）评估系统性能，并优化计算效率以支持实时或大规模部署。

## 七、优先关注论文

- **MITRA: An AI Assistant for Knowledge Retrieval in Physics Collaborations**：展示了本地化RAG系统在科学文档处理中的完整工程管道，包括自动化检索、OCR布局解析和双层向量数据库，对私有知识管理有借鉴意义。
- **PromptDLA: A Domain-aware Prompt Document Layout Analysis Framework with Descriptive Knowledge as a Cue**：将提示学习引入文档布局分析，通过领域自适应提升泛化性能，为多样化文档处理提供可扩展的解决方案。
- **Logics-Parsing-Omni Technical Report**：提出统一的多模态解析框架，通过证据锚定实现结构化知识转换，可能推动OCR与视频/音频解析的标准化集成。
- **The Patrologia Graeca Corpus: OCR, Annotation, and Open Release of Noisy Nineteenth-Century Polytonic Greek Editions**：提供了嘈杂多调希腊语OCR的高质量语料库和低错误率流程，为古文献数字化和退化文本识别设立新基准。
- **Tracking Cancer Through Text: Longitudinal Extraction From Radiology Reports Using Open-Source Large Language Models**：演示了开源LLM在医疗文本纵向提取中的高精度应用，强调隐私保护和可部署性，适合推广到其他文档OCR任务。

## 八、论文逐篇解析

### 1. MITRA: An AI Assistant for Knowledge Retrieval in Physics Collaborations

- arXiv: [2603.09800v1](https://arxiv.org/abs/2603.09800v1)
- PDF: [下载链接](https://arxiv.org/pdf/2603.09800v1)
- 作者: Abhishikth Mallampalli, Sridhara Dasu
- 发布时间: 2026-03-10T15:28:35Z
- 分类: cs.IR, cs.AI, cs.CL
- 相关性评分: 29
- 主题标签: 检索增强生成、OCR布局解析、本地化部署、科学文档处理、向量数据库

**中文摘要**

> 本文提出MITRA，一个基于检索增强生成（RAG）的系统，旨在为大型物理合作项目（如CERN的CMS）中的内部文档提供上下文感知问答。系统采用自动化流程，使用Selenium从内部数据库检索文档，并结合OCR与布局解析进行高保真文本提取。整个框架（包括嵌入模型和大语言模型）均部署在本地，确保敏感数据隐私。采用双层向量数据库架构，先通过摘要识别相关分析，再聚焦完整文档，以解决不同分析间的歧义。原型在真实查询中优于基于关键字的基线，并讨论了未来开发全面研究代理的方向。

**核心创新概述**

> 针对大规模科学合作中的内部文档导航挑战，提出首个专为物理分析设计的本地化RAG系统，结合自动化文档检索与OCR布局解析，并引入双层向量数据库以提升检索精度。

**创新点拆解**

- 自动化文档检索与OCR布局解析的集成管道
- 完全本地化部署的RAG框架确保数据隐私
- 双层向量数据库架构（先摘要后全文）以解决分析歧义
- 针对物理合作场景的上下文感知问答设计

**当前局限**

> 原型阶段，未全面评估在更广泛文档类型或动态更新数据上的性能；依赖特定内部数据库结构，可能限制泛化能力。

**后续可改进方向**

- 扩展支持更多文档格式和动态数据源
- 优化OCR模块对复杂科学符号的识别
- 集成多模态理解以处理图表等非文本内容
- 开发自适应学习机制以应对文档更新

**工程启发**

> 高，为大型科学合作提供可部署的私有知识检索工具，提升研究效率，具有实际应用潜力。

**为什么值得关注**

> 涉及OCR与布局解析用于文档文本提取，是文档理解的关键步骤；RAG系统依赖高质量OCR输出，直接影响检索性能。

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

### 2. ICDAR 2025 Competition on End-to-End Document Image Machine Translation Towards Complex Layouts

- arXiv: [2603.09392v1](https://arxiv.org/abs/2603.09392v1)
- PDF: [下载链接](https://arxiv.org/pdf/2603.09392v1)
- 作者: Yaping Zhang, Yupu Liang, Zhiyang Zhang, Zhiyuan Chen, Lu Xiang, Yang Zhao, Yu Zhou, Chengqing Zong
- 发布时间: 2026-03-10T09:04:38Z
- 分类: cs.CV, cs.AI
- 相关性评分: 26
- 主题标签: 文档图像翻译、多模态理解、ICDAR竞赛、端到端学习、布局建模

**中文摘要**

> 本文介绍ICDAR 2025文档图像机器翻译（DIMT）竞赛，旨在推动端到端文档图像翻译研究，该领域结合OCR与NLP以处理文本内容和页面布局。竞赛设OCR-free和OCR-based两个赛道，各包含小模型（<1B参数）和大模型（>1B参数）子任务，共吸引69支团队参与。报告概述挑战动机、数据集构建、任务定义、评估协议及结果总结，分析表明大模型方法为复杂布局文档图像翻译建立了新范式，并指出未来研究机会。

**核心创新概述**

> 首个针对文档图像机器翻译的ICDAR竞赛，系统化定义OCR-free与OCR-based端到端任务，推动多模态文档理解研究，并展示大模型在该领域的潜力。

**创新点拆解**

- 端到端文档图像翻译的竞赛框架设计
- OCR-free与OCR-based双赛道对比评估
- 针对复杂布局的多模态任务定义
- 大模型作为翻译新范式的实证分析

**当前局限**

> 竞赛结果可能受数据集特定性和评估指标限制；未深入探讨模型在低资源语言或极端布局上的表现。

**后续可改进方向**

- 开发更鲁棒的布局建模方法以处理多样化文档格式
- 优化OCR与翻译模块的协同训练策略
- 扩展数据集涵盖更多语言和布局复杂度
- 研究小模型的高效替代方案

**工程启发**

> 中高，竞赛推动实际DIMT系统开发，为多语言文档处理提供基准，促进工业应用。

**为什么值得关注**

> 直接关联OCR作为文档图像翻译的基础组件；竞赛任务强调布局与文本的联合建模，是OCR进阶应用。

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

### 3. The Patrologia Graeca Corpus: OCR, Annotation, and Open Release of Noisy Nineteenth-Century Polytonic Greek Editions

- arXiv: [2603.09470v1](https://arxiv.org/abs/2603.09470v1)
- PDF: [下载链接](https://arxiv.org/pdf/2603.09470v1)
- 作者: Chahan Vidal-Gorène, Bastien Kindt
- 发布时间: 2026-03-10T10:21:54Z
- 分类: cs.CV
- 相关性评分: 18
- 主题标签: 多调希腊语OCR、古文献数字化、布局检测、嘈杂文本识别、语料库构建

**中文摘要**

> 本文发布Patrologia Graeca Corpus，首个针对19世纪古希腊语版本的大规模开放OCR与语言资源。该语料库覆盖Patrologia Graeca未数字化卷册，包含复杂双语（希腊语-拉丁语）布局和高度退化的多调希腊语排版。通过结合YOLO布局检测与CRNN文本识别的专用流程，实现1.05%字符错误率和4.69%词错误率，显著优于现有多调希腊语OCR系统。语料库包含约六百万词元化和词性标注的词汇，对齐完整OCR与布局注释，为嘈杂多调希腊语OCR设立新基准，并提供未来模型训练材料。

**核心创新概述**

> 首个针对嘈杂多调希腊语的大规模开放OCR语料库，采用专用布局检测与文本识别流程，在退化排版上实现低错误率，为古文献数字化设立新标准。

**创新点拆解**

- YOLO与CRNN结合的专用OCR流程用于嘈杂多调希腊语
- 大规模双语布局文档的完整OCR与标注发布
- 极低错误率（CER 1.05%, WER 4.69%）在退化文本上
- 语料库包含词元化和词性标注，支持语言学与OCR研究

**当前局限**

> 流程可能依赖特定排版特征，泛化到其他古语言或更严重退化文本时性能未知；未评估实时处理能力。

**后续可改进方向**

- 扩展流程支持更多古语言和排版风格
- 集成深度学习增强的图像预处理以处理更严重退化
- 开发端到端模型以减少流程复杂性
- 优化布局检测对非标准文档结构的适应性

**工程启发**

> 高，为古文献数字化提供可靠工具和基准数据集，促进文化遗产保存与学术研究。

**为什么值得关注**

> 核心聚焦OCR技术，特别是针对嘈杂、多调文本的识别，是OCR在挑战性场景下的前沿应用。

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

### 4. A Hybrid Vision Transformer Approach for Mathematical Expression Recognition

- arXiv: [2603.07929v1](https://arxiv.org/abs/2603.07929v1)
- PDF: [下载链接](https://arxiv.org/pdf/2603.07929v1)
- 作者: Anh Duy Le, Van Linh Pham, Vinh Loi Ly, Nam Quan Nguyen, Huu Thang Nguyen, Tuan Anh Tran
- 发布时间: 2026-03-09T03:49:57Z
- 分类: cs.CV
- 相关性评分: 17
- 主题标签: 数学表达式识别、视觉变换器、2D位置编码、覆盖注意力、文档分析

**中文摘要**

> 本文提出一种混合视觉变换器方法用于数学表达式识别，该任务因二维结构和符号尺寸差异而比文本识别更复杂。方法使用带2D位置编码的混合视觉变换器作为编码器，以提取图像中符号间的复杂关系，并采用覆盖注意力解码器以更好跟踪注意力历史，处理解析不足和过度解析问题。实验在IM2LATEX-100K数据集上进行，显示方法有效性，达到89.94 BLEU分数，优于当前最先进方法。

**核心创新概述**

> 首次将混合视觉变换器与2D位置编码结合用于数学表达式识别，引入覆盖注意力解码器以改善解析问题，在标准数据集上实现SOTA性能。

**创新点拆解**

- 混合视觉变换器编码器结合2D位置编码以捕捉二维结构
- 覆盖注意力解码器用于管理注意力历史
- 利用ViT的[CLS]令牌作为解码器初始嵌入
- 在数学表达式识别任务上达到SOTA BLEU分数

**当前局限**

> 方法在更复杂或手写数学表达式上的泛化能力未验证；计算成本可能较高，适合实时应用。

**后续可改进方向**

- 优化模型效率以支持实时或移动端部署
- 扩展数据集涵盖手写和更复杂表达式
- 研究多模态输入（如结合LaTeX序列）以提升准确性
- 增强对模糊或低质量图像的鲁棒性

**工程启发**

> 中高，为数学文档自动化处理提供先进识别技术，适用于教育、科研和出版领域。

**为什么值得关注**

> 数学表达式识别是文档分析的重要子任务，依赖OCR式图像到序列转换，是OCR在结构化内容识别上的延伸。

**原始摘要**

One of the crucial challenges taken in document analysis is mathematical expression recognition.
Unlike text recognition which only focuses on one-dimensional structure images, mathematical
expression recognition is a much more complicated problem because of its two-dimensional structure
and different symbol size. In this paper, we propose using a Hybrid Vision Transformer (HVT) with 2D
positional encoding as the encoder to extract the complex relationship between symbols from the
image. A coverage attention decoder is used to better track attention's history to handle the under-
parsing and over-parsing problems. We also showed the benefit of using the [CLS] token of ViT as the
initial embedding of the decoder. Experiments performed on the IM2LATEX-100K dataset have shown the
effectiveness of our method by achieving a BLEU score of 89.94 and outperforming current state-of-
the-art methods.

---

### 5. OfficeQA Pro: An Enterprise Benchmark for End-to-End Grounded Reasoning

- arXiv: [2603.08655v1](https://arxiv.org/abs/2603.08655v1)
- PDF: [下载链接](https://arxiv.org/pdf/2603.08655v1)
- 作者: Krista Opsahl-Ong, Arnav Singhvi, Jasmine Collins, Ivan Zhou, Cindy Wang, Ashutosh Baheti, Owen Oertell, Jacob Portes, Sam Havens, Erich Elsen, Michael Bendersky, Matei Zaharia, Xing Chen
- 发布时间: 2026-03-09T17:34:53Z
- 分类: cs.AI, cs.CL, cs.IR
- 相关性评分: 15
- 主题标签: 文档推理基准、大语言模型评估、表格数据处理、结构化表示、企级AI

**中文摘要**

> 本文介绍OfficeQA Pro，一个用于评估AI代理在大型异构文档语料库上进行基于文档的推理的基准。语料库包含近100年的美国财政部公报，共89,000页和超过2600万个数值。基准包含133个需要精确文档解析、检索和分析推理的问题，涉及非结构化文本和表格数据。前沿大语言模型在仅依赖参数知识时准确率低于5%，附加网络访问后低于12%，即使直接访问文档语料库，平均准确率也仅34.1%。提供由Databricks ai_parse_document生成的结构化文档表示可使性能相对提升16.1%。分析表明，在企级基于文档的推理任务上，代理可靠性仍有显著提升空间。

**核心创新概述**

> 首个针对企级多文档推理的基准，聚焦大规模数值和表格数据，系统评估前沿大语言模型在基于文档任务上的局限性，并量化结构化表示的价值。

**创新点拆解**

- 大规模异构文档语料库的构建与基准设计
- 针对数值和表格数据的精确推理问题
- 实证展示大语言模型在基于文档任务上的性能瓶颈
- 结构化文档表示对性能提升的量化分析

**当前局限**

> 基准规模相对较小（133问题），可能未覆盖所有推理类型；依赖特定文档源（财政部公报），泛化性待验证。

**后续可改进方向**

- 开发更高效的文档解析与检索模块以支持大规模语料库
- 优化表格数据表示与推理方法
- 集成多模态理解以处理图表等非文本元素
- 研究小样本或零样本学习以降低标注成本

**工程启发**

> 高，为企级文档AI系统提供评估标准，推动自动化决策和数据分析工具开发。

**为什么值得关注**

> 基准依赖文档解析作为基础步骤，涉及OCR或类似技术用于文本提取；结构化表示生成可借鉴OCR布局分析。

**原始摘要**

We introduce OfficeQA Pro, a benchmark for evaluating AI agents on grounded, multi-document
reasoning over a large and heterogeneous document corpus. The corpus consists of U.S. Treasury
Bulletins spanning nearly 100 years, comprising 89,000 pages and over 26 million numerical values.
OfficeQA Pro consists of 133 questions that require precise document parsing, retrieval, and
analytical reasoning across both unstructured text and tabular data. Frontier LLMs including Claude
Opus 4.6, GPT-5.4, and Gemini 3.1 Pro Preview achieve less than 5% accuracy on OfficeQA Pro when
relying on parametric knowledge, and less than 12% with additional access to the web. When provided
directly with the document corpus, frontier agents still struggle on over half of questions, scoring
34.1% on average. We find that providing agents with a structured document representation produced
by Databricks' ai_parse_document yields a 16.1% average relative performance gain across agents. We
conduct additional ablations to study the effects of model selection, table representation,
retrieval strategy, and test-time scaling on performance. Despite these improvements, significant
headroom remains before agents can be considered reliable at enterprise-grade grounded reasoning.

---

### 6. PromptDLA: A Domain-aware Prompt Document Layout Analysis Framework with Descriptive Knowledge as a Cue

- arXiv: [2603.09414v1](https://arxiv.org/abs/2603.09414v1)
- PDF: [下载链接](https://arxiv.org/pdf/2603.09414v1)
- 作者: Zirui Zhang, Yaping Zhang, Lu Xiang, Yang Zhao, Feifei Zhai, Yu Zhou, Chengqing Zong
- 发布时间: 2026-03-10T09:30:00Z
- 分类: cs.CV, cs.AI
- 相关性评分: 11
- 主题标签: 文档布局分析、提示学习、领域自适应、多领域泛化、结构理解

**中文摘要**

> 本文提出PromptDLA，一个领域感知的提示文档布局分析框架，利用描述性知识作为线索整合领域先验。现有工作常合并不同领域数据以提升DLA泛化，但忽略布局结构差异，导致次优性能。PromptDLA采用独特领域感知提示器，根据数据域特定属性定制提示，作为线索引导DLA关注关键特征和结构。大量实验显示，在DocLayNet、PubLayNet、M6Doc和D$^4$LA数据集上达到最先进性能。

**核心创新概述**

> 首次将提示学习引入文档布局分析，设计领域感知提示器以自适应整合领域知识，解决多领域数据合并时的性能下降问题，在多个基准上实现SOTA。

**创新点拆解**

- 领域感知提示器用于定制化提示生成
- 利用描述性知识作为线索引导布局分析
- 自适应整合多领域先验以提升泛化
- 在多个公共DLA数据集上达到SOTA性能

**当前局限**

> 提示设计可能依赖领域标注，在无标签或新领域上应用受限；未深入探讨计算开销与实时性能。

**后续可改进方向**

- 开发自动化提示生成以减少人工干预
- 扩展框架支持更多文档类型和语言
- 优化模型效率以用于大规模部署
- 研究零样本或小样本迁移学习能力

**工程启发**

> 高，为文档AI提供可泛化的布局分析工具，适用于多样化文档处理场景，如出版、法律和金融。

**为什么值得关注**

> 文档布局分析是OCR后处理的关键步骤，直接影响文本提取和结构理解；提示学习为DLA提供新范式。

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

### 7. Logics-Parsing-Omni Technical Report

- arXiv: [2603.09677v1](https://arxiv.org/abs/2603.09677v1)
- PDF: [下载链接](https://arxiv.org/pdf/2603.09677v1)
- 作者: Xin An, Jingyi Cai, Xiangyang Chen, Huayao Liu, Peiting Liu, Peng Wang, Bei Yang, Xiuwen Zhu, Yongfan Chen, Baoyu Hou, Shuzhao Li, Weidong Ren, Fan Yang, Jiangtao Zhang, Xiaoxiao Xu, Lin Qu
- 发布时间: 2026-03-10T13:46:32Z
- 分类: cs.AI
- 相关性评分: 10
- 主题标签: 多模态解析、统一分类法、证据锚定、结构化知识转换、OCR

**中文摘要**

> 针对多模态解析中任务定义碎片化和非结构化数据异质性的挑战，本文提出了Omni Parsing框架。该框架建立了一个涵盖文档、图像和音视频流的统一分类法，引入了一种连接感知与认知的渐进式解析范式。具体包括三个层次：1）整体检测，实现对象或事件的精确时空定位，为感知建立几何基线；2）细粒度识别，对定位对象进行符号化（如OCR/ASR）和属性提取，完成结构化实体解析；3）多级解释，构建从局部语义到全局逻辑的推理链。框架的关键优势是证据锚定机制，强制高层语义描述与低层事实严格对齐，实现基于证据的逻辑归纳，将非结构化信号转化为可定位、可枚举、可追溯的标准化知识。在此基础上，构建了标准化数据集并发布了Logics-Parsing-Omni模型，成功将复杂音视频信号转换为机器可读的结构化知识。实验表明细粒度感知与高层认知协同作用，有效提升模型可靠性。此外，引入OmniParsingBench进行定量评估。

**核心创新概述**

> 提出统一的多模态解析框架，通过渐进式解析范式连接感知与认知，并引入证据锚定机制确保语义与事实对齐，实现非结构化数据的标准化知识转换。

**创新点拆解**

- 统一分类法覆盖文档、图像和音视频流
- 渐进式解析范式连接感知与认知
- 证据锚定机制强制语义与事实对齐
- 构建标准化数据集和模型Logics-Parsing-Omni
- 引入OmniParsingBench进行定量评估

**当前局限**

> 未具体讨论框架在不同领域或低资源场景下的泛化能力，以及计算开销和实时性限制。

**后续可改进方向**

- 扩展框架到更多模态或跨语言任务
- 优化计算效率以支持实时应用
- 增强在噪声数据或小样本下的鲁棒性
- 探索与其他AI技术（如强化学习）的集成

**工程启发**

> 高，框架提供标准化解析流程，可应用于文档OCR、视频分析等领域，提升数据处理的自动化和可靠性。

**为什么值得关注**

> 直接涉及OCR作为细粒度识别的一部分，强调符号化和结构化解析，对文档处理技术有重要参考价值。

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

### 8. A Consensus-Driven Multi-LLM Pipeline for Missing-Person Investigations

- arXiv: [2603.08954v1](https://arxiv.org/abs/2603.08954v1)
- PDF: [下载链接](https://arxiv.org/pdf/2603.08954v1)
- 作者: Joshua Castillo, Ravi Mukkamala
- 发布时间: 2026-03-09T21:40:17Z
- 分类: cs.AI, cs.CL, cs.DC, cs.IR, cs.LG
- 相关性评分: 9
- 主题标签: 多LLM管道、共识机制、QLoRA微调、信息提取、结构化处理

**中文摘要**

> 失踪人员调查的前72小时对成功找回至关重要。Guardian是一个端到端系统，旨在支持失踪儿童调查和早期搜索规划。本文介绍了Guardian LLM Pipeline，一个多模型系统，其中LLMs用于智能信息提取和处理与失踪人员搜索操作相关的信息。该管道协调跨任务专用LLM模型的端到端执行，并调用共识LLM引擎比较多个模型输出并解决分歧。通过使用精心策划的数据集进行QLoRA微调，进一步强化管道。设计符合先前关于弱监督和LLM辅助标注的工作，强调保守、可审计地使用LLMs作为结构化提取器和标注器，而非不受约束的端到端决策者。

**核心创新概述**

> 提出基于共识驱动的多LLM管道，用于失踪人员调查的信息提取，结合QLoRA微调和共识机制提升系统可靠性和可审计性。

**创新点拆解**

- 多LLM管道协调任务专用模型
- 共识LLM引擎解决输出分歧
- QLoRA微调优化模型性能
- 强调LLMs作为结构化提取器和标注器的保守使用

**当前局限**

> 系统依赖高质量标注数据，可能在实际应用中面临数据稀缺或隐私限制；共识机制可能增加计算开销。

**后续可改进方向**

- 集成更多模态数据（如图像或视频）
- 开发自适应微调方法以减少数据依赖
- 优化共识算法以提高效率
- 扩展应用到其他紧急响应场景

**工程启发**

> 中高，系统在失踪人员调查中提供自动化信息处理，但需确保数据隐私和实时性，适合特定领域部署。

**为什么值得关注**

> 涉及LLMs在信息提取和结构化处理中的应用，与OCR相关任务（如文档解析）有间接关联，强调可审计性和可靠性。

**原始摘要**

The first 72 hours of a missing-person investigation are critical for successful recovery. Guardian
is an end-to-end system designed to support missing-child investigation and early search planning.
This paper presents the Guardian LLM Pipeline, a multi-model system in which LLMs are used for
intelligent information extraction and processing related to missing-person search operations. The
pipeline coordinates end-to-end execution across task-specialized LLM models and invokes a consensus
LLM engine that compares multiple model outputs and resolves disagreements. The pipeline is further
strengthened by QLoRA-based fine-tuning, using curated datasets. The presented design aligns with
prior work on weak supervision and LLM-assisted annotation, emphasizing conservative, auditable use
of LLMs as structured extractors and labelers rather than unconstrained end-to-end decision makers.

---

### 9. Tracking Cancer Through Text: Longitudinal Extraction From Radiology Reports Using Open-Source Large Language Models

- arXiv: [2603.09638v1](https://arxiv.org/abs/2603.09638v1)
- PDF: [下载链接](https://arxiv.org/pdf/2603.09638v1)
- 作者: Luc Builtjes, Alessa Hering
- 发布时间: 2026-03-10T13:13:43Z
- 分类: cs.CL
- 相关性评分: 6
- 主题标签: 开源LLM、纵向信息提取、医疗文本处理、结构化数据、隐私保护

**中文摘要**

> 放射学报告捕获了肿瘤负荷、治疗反应和疾病进展的关键纵向信息，但其非结构化叙述格式使自动化分析复杂化。尽管大语言模型（LLMs）在临床文本处理方面取得进展，但大多数最先进系统仍是专有的，限制了在隐私敏感的医疗环境中的适用性。我们提出了一个完全开源、可本地部署的管道，用于从放射学报告中提取纵向信息，使用\texttt{llm\_extractinator}框架实现。该系统应用\texttt{qwen2.5-72b}模型根据RECIST标准提取和链接目标、非目标和新病灶数据跨时间点。在50对荷兰CT胸腹报告上的评估显示高提取性能，属性级准确度为目标病灶93.7%、非目标病灶94.9%、新病灶94.0%。该方法证明开源LLMs可以在多时间点肿瘤学任务中实现临床有意义的性能，同时确保数据隐私和可重复性。这些结果突显了可本地部署LLMs在从常规临床文本中提取结构化纵向数据的可扩展潜力。

**核心创新概述**

> 开发开源、可本地部署的LLM管道，用于从放射学报告中提取结构化纵向数据，在隐私敏感医疗环境中实现高精度信息提取。

**创新点拆解**

- 完全开源和可本地部署的管道
- 使用\texttt{qwen2.5-72b}模型进行多时间点提取
- 基于RECIST标准的结构化数据链接
- 高属性级准确度（>93%）

**当前局限**

> 评估数据规模较小（50对报告），可能限制泛化性；未讨论模型在不同语言或医疗中心间的适应性。

**后续可改进方向**

- 扩大数据集以增强模型鲁棒性
- 探索多语言或跨机构适配
- 集成更多临床模态（如影像数据）
- 优化管道以降低计算资源需求

**工程启发**

> 高，管道在医疗领域提供隐私保护的数据提取方案，可推广到其他文档OCR任务，促进自动化临床分析。

**为什么值得关注**

> 直接涉及LLMs在文本提取和结构化处理中的应用，与OCR技术（如从文档中提取信息）高度相关，强调开源和可部署性。

**原始摘要**

Radiology reports capture crucial longitudinal information on tumor burden, treatment response, and
disease progression, yet their unstructured narrative format complicates automated analysis. While
large language models (LLMs) have advanced clinical text processing, most state-of-the-art systems
remain proprietary, limiting their applicability in privacy-sensitive healthcare environments. We
present a fully open-source, locally deployable pipeline for longitudinal information extraction
from radiology reports, implemented using the \texttt{llm\_extractinator} framework. The system
applies the \texttt{qwen2.5-72b} model to extract and link target, non-target, and new lesion data
across time points in accordance with RECIST criteria. Evaluation on 50 Dutch CT Thorax/Abdomen
report pairs yielded high extraction performance, with attribute-level accuracies of 93.7\% for
target lesions, 94.9\% for non-target lesions, and 94.0\% for new lesions. The approach demonstrates
that open-source LLMs can achieve clinically meaningful performance in multi-timepoint oncology
tasks while ensuring data privacy and reproducibility. These results highlight the potential of
locally deployable LLMs for scalable extraction of structured longitudinal data from routine
clinical text.

---
