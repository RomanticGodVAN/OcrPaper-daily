# OCR / 文档解析研究日报（2026-04-01）

## 报告说明

- 检索源：arXiv API
- 检索查询：`(all:"document parsing" OR all:"document understanding" OR all:"optical character recognition" OR all:OCR OR all:"layout analysis" OR all:"document layout analysis" OR all:"text recognition" OR all:"table recognition" OR all:"form understanding" OR all:"document intelligence" OR all:"page understanding" OR all:"scene text recognition" OR all:"handwritten text recognition" OR all:"information extraction") AND (cat:cs.CV OR cat:cs.AI OR cat:cs.CL OR cat:eess.IV)`
- 生成时间（UTC）：`2026-04-01 04:22:52`
- 大模型综合分析：`开启`

## 一、今日执行摘要

> 今日论文显示OCR与文档解析研究正朝多模态融合、高效自适应和标准化评估方向发展。视觉语言模型被广泛用于提升转录精度和语义理解，尤其在历史文档和复杂结构（如化学图表）中表现突出。模块化设计和领域自适应方法显著降低计算成本，促进资源受限环境的应用。同时，新基准和数据集（如MDPBench、AutoFormBench）推动模型公平性和现实世界性能评估。工业级模型优化（如Xuanwu）和代理框架（如ChartCynics）增强对抗场景下的鲁棒性。整体趋势强调平衡性能与效率，支持低资源语言和文化遗产数字化。

## 二、今日趋势判断

研究趋势聚焦于多模态集成（视觉、文本、布局联合推理）、轻量级自适应（少样本学习、模块化解耦）和标准化基准构建（多语言、真实场景）。视觉语言模型成为核心，用于端到端任务如转录、实体链接和图表理解。领域自适应通过合成噪声或上下文学习减少标注依赖，提高计算效率。基准数据集推动模型在非拉丁脚本、拍摄文档和表单元素上的公平评估。工业应用注重紧凑架构和对抗训练，以优化部署成本与鲁棒性。

## 三、今日论文概览

1. **Transcription and Recognition of Italian Parliamentary Speeches Using Vision-Language Models** | 标签：视觉语言模型、OCR、实体链接、语义分割、议会文档
2. **Efficient Domain Adaptation for Text Line Recognition via Decoupled Language Models** | 标签：领域自适应、OCR、模块化架构、计算效率、手写体识别
3. **MDPBench: A Benchmark for Multilingual Document Parsing in Real-World Scenarios** | 标签：文档解析基准、多语言处理、开源模型、拍摄文档、性能评估
4. **MarkushGrapher-2: End-to-end Multimodal Recognition of Chemical Structures** | 标签：化学结构识别、多模态融合、OCR、数据集构建、端到端学习
5. **Quid est VERITAS? A Modular Framework for Archival Document Analysis** | 标签：模块化框架、历史文档数字化、布局分析、语义增强、工作流设计
6. **Few-shot Writer Adaptation via Multimodal In-Context Learning** | 标签：手写文本识别、少样本学习、上下文学习、写作者自适应、轻量级模型
7. **L-ReLF: A Framework for Lexical Dataset Creation** | 标签：低资源语言、词汇数据集、OCR、数据标准化、NLP应用
8. **AutoFormBench: Benchmark Dataset for Automating Form Understanding** | 标签：表单理解、目标检测、基准数据集、YOLO、结构化文档
9. **SiPaKosa: A Comprehensive Corpus of Canonical and Classical Buddhist Texts in Sinhala and Pali** | 标签：历史文档、OCR、多语言语料库、文化遗产、语言模型
10. **Xuanwu: Evolving General Multimodal Models into an Industrial-Grade Foundation for Content Ecosystems** | 标签：多模态模型、工业应用、对抗OCR、内容审核、紧凑架构
11. **Navigating the Mirage: A Dual-Path Agentic Framework for Robust Misleading Chart Question Answering** | 标签：图表理解、代理框架、OCR、对抗训练、视觉欺骗
12. **Hydra: Unifying Document Retrieval and Generation in a Single Vision-Language Model** | 标签：视觉语言模型、检索生成统一、LoRA、文档理解、系统优化

## 四、今天 OCR / 文档解析论文里的主要创新点

- 使用视觉语言模型联合推理视觉布局和文本内容，提升转录和分类精度。
- 采用模块化或解耦架构分离视觉检测与语言校正，实现高效领域自适应。
- 构建多语言或特定领域基准数据集，系统评估模型在真实场景下的性能。
- 集成OCR与后期处理流程，为低资源语言或历史文档创建结构化数据集。
- 通过紧凑模型设计和渐进训练，在有限参数下平衡业务对齐与通用能力。

## 五、后续 OCR 领域值得推进的改进方向

- 开发轻量级视觉语言模型，减少计算开销，适用于移动或边缘设备部署。
- 优化合成噪声生成方法，以更好模拟真实文档退化，提升领域自适应泛化能力。
- 扩展多语言基准至更多低资源语言和方言，覆盖非拉丁脚本的复杂拍摄条件。
- 探索多模态融合机制，高效整合视觉、文本和布局信息，用于化学结构或图表识别。
- 研究实时少样本自适应技术，支持手写文本识别在动态环境中的快速部署。

## 六、工程落地启发

- 采用模块化框架（如VERITAS）可灵活集成转录、布局分析和语义增强，提升历史文档数字化效率。
- 利用合成噪声训练校正器，实现无标注领域自适应，降低OCR系统在资源受限环境中的部署成本。
- 集成SPARQL查询和模糊匹配进行实体链接，增强文档解析的语义分析能力，适用于知识库应用。
- 使用紧凑模型架构（如Xuanwu）和LoRA适配器，在工业场景中平衡性能与内存开销，优化内容审核任务。
- 构建标准化基准数据集（如AutoFormBench）可系统评估表单元素检测模型，促进业务流程自动化。

## 七、优先关注论文

- **Transcription and Recognition of Italian Parliamentary Speeches Using Vision-Language Models**：结合视觉语言模型进行端到端转录和实体链接，为历史文档数字化提供高性能解决方案，可能推动语义分析应用。
- **Efficient Domain Adaptation for Text Line Recognition via Decoupled Language Models**：模块化检测-校正框架大幅降低计算需求，适合资源受限环境，可能促进OCR在数字人文等领域的普及。
- **MDPBench: A Benchmark for Multilingual Document Parsing in Real-World Scenarios**：首个多语言文档解析基准，揭示开源模型在非拉丁脚本上的性能瓶颈，对推动模型公平性和包容性有重要影响。
- **Xuanwu: Evolving General Multimodal Models into an Industrial-Grade Foundation for Content Ecosystems**：紧凑架构在对抗OCR场景中表现优异，为工业应用提供高效多模态基础，可能优化内容审核和部署策略。
- **Navigating the Mirage: A Dual-Path Agentic Framework for Robust Misleading Chart Question Answering**：代理框架通过双路径解耦增强图表理解鲁棒性，在对抗场景中提升性能，适用于数据可视化和信息验证任务。

## 八、论文逐篇解析

### 1. Transcription and Recognition of Italian Parliamentary Speeches Using Vision-Language Models

- arXiv: [2603.28103v1](https://arxiv.org/abs/2603.28103v1)
- PDF: [下载链接](https://arxiv.org/pdf/2603.28103v1)
- 作者: Luigi Curini, Alfio Ferrara, Giovanni Pagano, Sergio Picascia
- 发布时间: 2026-03-30T07:06:49Z
- 分类: cs.DL, cs.AI, cs.IR
- 相关性评分: 27
- 主题标签: 视觉语言模型、OCR、实体链接、语义分割、议会文档

**中文摘要**

> 本文提出了一种基于视觉语言模型的管道，用于意大利议会演讲的自动转录、语义分割和实体链接。该管道采用专门的OCR模型提取文本并保持阅读顺序，随后使用大规模视觉语言模型通过联合推理视觉布局和文本内容进行转录精炼、元素分类和发言人识别。提取的发言人通过SPARQL查询和多策略模糊匹配程序链接到众议院知识库。评估显示在转录质量和发言人标记方面有显著改进。

**核心创新概述**

> 将视觉语言模型应用于议会演讲转录，结合OCR和语义分析，实现端到端的转录、分类和实体链接，超越传统OCR方法。

**创新点拆解**

- 使用视觉语言模型联合推理视觉布局和文本内容进行转录精炼和元素分类
- 集成SPARQL查询和多策略模糊匹配进行实体链接
- 专门OCR模型提取文本并保持阅读顺序

**当前局限**

> 依赖大规模视觉语言模型，计算资源需求较高；实体链接可能受知识库覆盖范围限制。

**后续可改进方向**

- 优化模型以减少计算开销
- 扩展知识库以提高实体链接覆盖率
- 探索更多语言或文档类型的应用

**工程启发**

> 高，为历史文档数字化提供自动化解决方案，提升转录准确性和语义分析能力。

**为什么值得关注**

> 涉及OCR、视觉语言模型和文档解析，对多模态文档处理有直接贡献。

**原始摘要**

Parliamentary proceedings represent a rich yet challenging resource for computational analysis,
particularly when preserved only as scanned historical documents. Existing efforts to transcribe
Italian parliamentary speeches have relied on traditional Optical Character Recognition pipelines,
resulting in transcription errors and limited semantic annotation. In this paper, we propose a
pipeline based on Vision-Language Models for the automatic transcription, semantic segmentation, and
entity linking of Italian parliamentary speeches. The pipeline employs a specialised OCR model to
extract text while preserving reading order, followed by a large-scale Vision-Language Model that
performs transcription refinement, element classification, and speaker identification by jointly
reasoning over visual layout and textual content. Extracted speakers are then linked to the Chamber
of Deputies knowledge base through SPARQL queries and a multi-strategy fuzzy matching procedure.
Evaluation against an established benchmark demonstrates substantial improvements both in
transcription quality and speaker tagging.

---

### 2. Efficient Domain Adaptation for Text Line Recognition via Decoupled Language Models

- arXiv: [2603.28028v1](https://arxiv.org/abs/2603.28028v1)
- PDF: [下载链接](https://arxiv.org/pdf/2603.28028v1)
- 作者: Arundhathi Dev, Justin Zhan
- 发布时间: 2026-03-30T04:39:26Z
- 分类: cs.CV, cs.LG
- 相关性评分: 20
- 主题标签: 领域自适应、OCR、模块化架构、计算效率、手写体识别

**中文摘要**

> 本文提出了一种模块化的检测-校正框架，用于文本行识别的高效领域自适应。该方法将轻量级视觉字符检测（领域无关）与使用预训练序列模型（如T5、ByT5、BART）的领域特定语言校正解耦。通过在合成噪声上训练校正器，实现无需标注目标图像的领域自适应。评估显示，该框架在保持接近SOTA准确性的同时，将计算需求减少约95%。

**核心创新概述**

> 通过解耦视觉检测和语言校正，实现资源高效的领域自适应，减少计算开销，同时保持高准确性。

**创新点拆解**

- 模块化检测-校正框架，解耦视觉和语言组件
- 使用合成噪声训练校正器，实现无标注领域自适应
- 识别T5和ByT5在不同文档类型上的Pareto前沿

**当前局限**

> 合成噪声可能无法完全模拟真实文档复杂性；对预训练模型依赖较强。

**后续可改进方向**

- 改进合成噪声生成以更好模拟真实场景
- 探索更多轻量级模型以进一步降低计算成本
- 扩展到更多低资源语言或手写体

**工程启发**

> 高，为资源受限环境提供可行的OCR解决方案，促进数字人文等领域的应用。

**为什么值得关注**

> 涉及OCR领域自适应、计算效率优化和模块化架构，对实际部署有重要意义。

**原始摘要**

Optical character recognition remains critical infrastructure for document digitization, yet state-
of-the-art performance is often restricted to well-resourced institutions by prohibitive
computational barriers. End-to-end transformer architectures achieve strong accuracy but demand
hundreds of GPU hours for domain adaptation, limiting accessibility for practitioners and digital
humanities scholars. We present a modular detection-and-correction framework that achieves near-SOTA
accuracy with single-GPU training. Our approach decouples lightweight visual character detection
(domain-agnostic) from domain-specific linguistic correction using pretrained sequence models
including T5, ByT5, and BART. By training the correctors entirely on synthetic noise, we enable
annotation-free domain adaptation without requiring labeled target images. Evaluating across modern
clean handwriting, cursive script, and historical documents, we identify a critical "Pareto
frontier" in architecture selection: T5-Base excels on modern text with standard vocabulary, whereas
ByT5-Base dominates on historical documents by reconstructing archaic spellings at the byte level.
Our results demonstrate that this decoupled paradigm matches end-to-end transformer accuracy while
reducing compute by approximately 95%, establishing a viable, resource-efficient alternative to
monolithic OCR architectures.

---

### 3. MDPBench: A Benchmark for Multilingual Document Parsing in Real-World Scenarios

- arXiv: [2603.28130v1](https://arxiv.org/abs/2603.28130v1)
- PDF: [下载链接](https://arxiv.org/pdf/2603.28130v1)
- 作者: Zhang Li, Zhibo Lin, Qiang Liu, Ziyang Zhang, Shuo Zhang, Zidun Guo, Jiajun Song, Jiarui Zhang, Xiang Bai, Yuliang Liu
- 发布时间: 2026-03-30T07:47:46Z
- 分类: cs.CV, cs.AI
- 相关性评分: 18
- 主题标签: 文档解析基准、多语言处理、开源模型、拍摄文档、性能评估

**中文摘要**

> 本文介绍了多语言文档解析基准MDPBench，首个针对多语言数字和拍摄文档解析的基准。该基准包含3,400张文档图像，覆盖17种语言、多样脚本和不同拍摄条件。评估显示，开源模型在非拉丁脚本和真实拍摄文档上性能显著下降，而闭源模型相对稳健。结果揭示了跨语言和条件的性能不平衡。

**核心创新概述**

> 创建首个多语言文档解析基准，系统评估模型在多样脚本和拍摄条件下的性能，揭示开源与闭源模型的差距。

**创新点拆解**

- 构建包含多语言、多脚本和拍摄条件的文档解析基准
- 采用专家模型标注、人工校正和验证的高质量标注流程
- 揭示开源模型在非拉丁脚本和拍摄文档上的性能瓶颈

**当前局限**

> 基准规模有限，可能未覆盖所有低资源语言；闭源模型细节不透明，影响可复现性。

**后续可改进方向**

- 扩展基准以包含更多低资源语言和文档类型
- 推动开源模型在非拉丁脚本和拍摄文档上的优化
- 开发更公平的评估指标以减少数据泄露风险

**工程启发**

> 中高，为文档解析研究提供标准化评估工具，促进模型公平性和包容性。

**为什么值得关注**

> 涉及文档解析基准、多语言处理和模型评估，对OCR系统部署有指导作用。

**原始摘要**

We introduce Multilingual Document Parsing Benchmark, the first benchmark for multilingual digital
and photographed document parsing. Document parsing has made remarkable strides, yet almost
exclusively on clean, digital, well-formatted pages in a handful of dominant languages. No
systematic benchmark exists to evaluate how models perform on digital and photographed documents
across diverse scripts and low-resource languages. MDPBench comprises 3,400 document images spanning
17 languages, diverse scripts, and varied photographic conditions, with high-quality annotations
produced through a rigorous pipeline of expert model labeling, manual correction, and human
verification. To ensure fair comparison and prevent data leakage, we maintain separate public and
private evaluation splits. Our comprehensive evaluation of both open-source and closed-source models
uncovers a striking finding: while closed-source models (notably Gemini3-Pro) prove relatively
robust, open-source alternatives suffer dramatic performance collapse, particularly on non-Latin
scripts and real-world photographed documents, with an average drop of 17.8% on photographed
documents and 14.0% on non-Latin scripts. These results reveal significant performance imbalances
across languages and conditions, and point to concrete directions for building more inclusive,
deployment-ready parsing systems. Source available at https://github.com/Yuliang-Liu/MultimodalOCR.

---

### 4. MarkushGrapher-2: End-to-end Multimodal Recognition of Chemical Structures

- arXiv: [2603.28550v1](https://arxiv.org/abs/2603.28550v1)
- PDF: [下载链接](https://arxiv.org/pdf/2603.28550v1)
- 作者: Tim Strohmeyer, Lucas Morin, Gerhard Ingmar Meijer, Valéry Weber, Ahmed Nassar, Peter Staar
- 发布时间: 2026-03-30T15:11:17Z
- 分类: cs.CV
- 相关性评分: 17
- 主题标签: 化学结构识别、多模态融合、OCR、数据集构建、端到端学习

**中文摘要**

> 本文提出MarkushGrapher-2，一种用于文档中化学结构多模态识别的端到端方法。该方法使用专用OCR模型提取文本，通过视觉-文本-布局编码器和光学化学结构识别视觉编码器联合编码文本、图像和布局信息，并采用两阶段训练策略融合编码以自回归生成Markush结构表示。为解决数据缺乏问题，引入了自动构建大规模真实世界Markush结构数据集的管道。

**核心创新概述**

> 端到端多模态化学结构识别方法，结合视觉、文本和布局信息，并构建大规模数据集和基准。

**创新点拆解**

- 视觉-文本-布局编码器联合编码多模态信息
- 两阶段训练策略有效融合编码
- 自动构建大规模真实世界Markush结构数据集

**当前局限**

> 多模态融合可能增加模型复杂性；数据集构建依赖自动流程，可能存在噪声。

**后续可改进方向**

- 优化多模态融合机制以提高效率
- 扩展数据集以覆盖更多化学结构类型
- 探索轻量级模型部署

**工程启发**

> 高，为化学文献分析提供自动化工具，提升化学结构识别精度。

**为什么值得关注**

> 涉及OCR、多模态融合和化学文档解析，对特定领域OCR应用有贡献。

**原始摘要**

Automatically extracting chemical structures from documents is essential for the large-scale
analysis of the literature in chemistry. Automatic pipelines have been developed to recognize
molecules represented either in figures or in text independently. However, methods for recognizing
chemical structures from multimodal descriptions (Markush structures) lag behind in precision and
cannot be used for automatic large-scale processing. In this work, we present MarkushGrapher-2, an
end-to-end approach for the multimodal recognition of chemical structures in documents. First, our
method employs a dedicated OCR model to extract text from chemical images. Second, the text, image,
and layout information are jointly encoded through a Vision-Text-Layout encoder and an Optical
Chemical Structure Recognition vision encoder. Finally, the resulting encodings are effectively
fused through a two-stage training strategy and used to auto-regressively generate a representation
of the Markush structure. To address the lack of training data, we introduce an automatic pipeline
for constructing a large-scale dataset of real-world Markush structures. In addition, we present
IP5-M, a large manually-annotated benchmark of real-world Markush structures, designed to advance
research on this challenging task. Extensive experiments show that our approach substantially
outperforms state-of-the-art models in multimodal Markush structure recognition, while maintaining
strong performance in molecule structure recognition. Code, models, and datasets are released
publicly.

---

### 5. Quid est VERITAS? A Modular Framework for Archival Document Analysis

- arXiv: [2603.28108v1](https://arxiv.org/abs/2603.28108v1)
- PDF: [下载链接](https://arxiv.org/pdf/2603.28108v1)
- 作者: Leonardo Bassanini, Ludovico Biancardi, Alfio Ferrara, Andrea Gamberini, Sergio Picascia, Folco Vaglienti
- 发布时间: 2026-03-30T07:14:51Z
- 分类: cs.DL, cs.AI, cs.IR
- 相关性评分: 17
- 主题标签: 模块化框架、历史文档数字化、布局分析、语义增强、工作流设计

**中文摘要**

> 本文提出VERITAS，一种模块化、模型无关的框架，将历史文档数字化重新概念化为包含转录、布局分析和语义增强的集成工作流。管道分为预处理、提取、精炼和增强四个阶段，采用模式驱动架构允许研究者声明式指定提取目标。评估显示，在转录错误率和处理时间方面相比商业OCR基线有显著改进。

**核心创新概述**

> 模块化框架整合转录、布局分析和语义增强，采用模式驱动架构提供灵活性和可扩展性。

**创新点拆解**

- 四阶段模块化工作流涵盖文档数字化全流程
- 模式驱动架构支持声明式提取目标指定
- 集成检索增强生成系统支持下游历史查询

**当前局限**

> 框架通用性可能受特定文档类型限制；语义增强依赖外部知识源。

**后续可改进方向**

- 扩展框架以支持更多文档类型和语言
- 优化语义增强模块以提高准确性
- 降低部署复杂度以促进广泛应用

**工程启发**

> 高，为历史文档数字化提供系统化解决方案，提升转录质量和分析能力。

**为什么值得关注**

> 涉及OCR、布局分析和语义增强，对文档解析工作流设计有参考价值。

**原始摘要**

The digitisation of historical documents has traditionally been conceived as a process limited to
character-level transcription, producing flat text that lacks the structural and semantic
information necessary for substantive computational analysis. We present VERITAS (Vision-Enhanced
Reading, Interpretation, and Transcription of Archival Sources), a modular, model-agnostic framework
that reconceptualises digitisation as an integrated workflow encompassing transcription, layout
analysis, and semantic enrichment. The pipeline is organised into four stages - Preprocessing,
Extraction, Refinement, and Enrichment - and employs a schema-driven architecture that allows
researchers to declaratively specify their extraction objectives. We evaluate VERITAS on the
critical edition of Bernardino Corio's Storia di Milano, a Renaissance chronicle of over 1,600
pages. Results demonstrate that the pipeline achieves a 67.6% relative reduction in word error rate
compared to a commercial OCR baseline, with a threefold reduction in end-to-end processing time when
accounting for manual correction. We further illustrate the downstream utility of the pipeline's
output by querying the transcribed corpus through a retrieval-augmented generation system,
demonstrating its capacity to support historical inquiry.

---

### 6. Few-shot Writer Adaptation via Multimodal In-Context Learning

- arXiv: [2603.29450v1](https://arxiv.org/abs/2603.29450v1)
- PDF: [下载链接](https://arxiv.org/pdf/2603.29450v1)
- 作者: Tom Simon, Stephane Nicolas, Pierrick Tranouez, Clement Chatelain, Thierry Paquet
- 发布时间: 2026-03-31T08:55:11Z
- 分类: cs.CV, cs.AI
- 相关性评分: 16
- 主题标签: 手写文本识别、少样本学习、上下文学习、写作者自适应、轻量级模型

**中文摘要**

> 本文提出一种基于多模态上下文学习的新型手写文本识别框架，实现无需参数更新的少样本写作者自适应。该框架设计紧凑的8M参数CNN-Transformer，结合上下文驱动和标准OCR训练策略。实验显示，在IAM和RIMES数据集上达到低字符错误率，超越所有写作者无关HTR模型。

**核心创新概述**

> 利用多模态上下文学习实现少样本写作者自适应，无需推理时参数更新，降低计算成本。

**创新点拆解**

- 多模态上下文学习框架实现少样本自适应
- 紧凑CNN-Transformer设计降低模型复杂度
- 结合上下文驱动和标准训练策略获得互补改进

**当前局限**

> 上下文长度可能影响自适应效果；对少数样本的依赖可能导致泛化能力有限。

**后续可改进方向**

- 优化上下文选择策略以提高自适应效率
- 扩展框架到更多手写风格或语言
- 探索实时自适应应用场景

**工程启发**

> 中高，为手写文本识别提供轻量级自适应方案，适合资源受限环境。

**为什么值得关注**

> 涉及手写文本识别、少样本学习和上下文学习，对OCR个性化应用有推进作用。

**原始摘要**

While state-of-the-art Handwritten Text Recognition (HTR) models perform well on standard
benchmarks, they frequently struggle with writers exhibiting highly specific styles that are
underrepresented in the training data. To handle unseen and atypical writers, writer adaptation
techniques personalize HTR models to individual handwriting styles. Leading writer adaptation
methods require either offline fine-tuning or parameter updates at inference time, both involving
gradient computation and backpropagation, which increase computational costs and demand careful
hyperparameter tuning. In this work, we propose a novel context-driven HTR framework3 inspired by
multimodal in-context learning, enabling inference-time writer adaptation using only a few examples
from the target writer without any parameter updates. We further demonstrate the impact of context
length, design a compact 8M-parameter CNN-Transformer that enables few-shot in-context adaptation,
and show that combining context-driven and standard OCR training strategies leads to complementary
improvements. Experiments on IAM and RIMES validate our approach with Character Error Rates of 3.92%
and 2.34%, respectively, surpassing all writer-independent HTR models without requiring any
parameter updates at inference time.

---

### 7. L-ReLF: A Framework for Lexical Dataset Creation

- arXiv: [2603.29346v1](https://arxiv.org/abs/2603.29346v1)
- PDF: [下载链接](https://arxiv.org/pdf/2603.29346v1)
- 作者: Anass Sedrati, Mounir Afifi, Reda Benkhadra
- 发布时间: 2026-03-31T07:19:00Z
- 分类: cs.CL
- 相关性评分: 16
- 主题标签: 低资源语言、词汇数据集、OCR、数据标准化、NLP应用

**中文摘要**

> 本文介绍了L-ReLF（低资源词汇框架），一种新颖、可重复的方法，用于为资源不足的语言创建高质量、结构化的词汇数据集。以摩洛哥达里语为例，标准化术语的缺乏在维基百科等平台中构成了知识公平的关键障碍，常迫使编辑依赖不一致的临时方法创建新词。研究详细阐述了克服这些挑战的技术流程，系统解决了低资源数据处理的困难，包括源识别、利用光学字符识别（OCR）尽管其偏向现代标准阿拉伯语，以及严格的后期处理以纠正错误和标准化数据模型。生成的结构化数据集完全兼容Wikidata Lexemes，作为重要的技术资源。L-ReLF方法设计具有通用性，为其他语言社区提供了构建下游NLP应用（如机器翻译和形态分析）基础词汇数据的清晰路径。

**核心创新概述**

> 提出了一种针对低资源语言的词汇数据集创建框架，强调可重复性和通用性，通过结合OCR和后期处理解决数据标准化问题。

**创新点拆解**

- 方法设计：开发了系统化的技术流程，包括源识别、OCR处理和后期标准化
- 数据：专注于资源不足语言（如摩洛哥达里语）的词汇数据创建
- 架构：生成的结构化数据集兼容Wikidata Lexemes，便于集成和扩展

**当前局限**

> OCR处理可能受限于对现代标准阿拉伯语的偏见，影响低资源语言的准确性；框架在通用性方面可能需针对不同语言特性进行定制调整。

**后续可改进方向**

- 优化OCR算法以减少对特定语言的偏见，提高低资源语言的识别精度
- 扩展框架以支持更多语言类型和方言，增强适应性
- 集成更多自动化工具以减少手动后期处理需求

**工程启发**

> 高，为低资源语言社区提供了实用的词汇数据创建工具，可促进NLP应用开发，支持知识公平。

**为什么值得关注**

> 涉及OCR在低资源语言数据处理中的应用，对文档解析和语言资源构建有直接贡献。

**原始摘要**

This paper introduces the L-ReLF (Low-Resource Lexical Framework), a novel, reproducible methodology
for creating high-quality, structured lexical datasets for underserved languages. The lack of
standardized terminology, exemplified by Moroccan Darija, poses a critical barrier to knowledge
equity in platforms like Wikipedia, often forcing editors to rely on inconsistent, ad-hoc methods to
create new words in their language. Our research details the technical pipeline developed to
overcome these challenges. We systematically address the difficulties of working with low-resource
data, including source identification, utilizing Optical Character Recognition (OCR) despite its
bias towards Modern Standard Arabic, and rigorous post-processing to correct errors and standardize
the data model. The resulting structured dataset is fully compatible with Wikidata Lexemes, serving
as a vital technical resource. The L-ReLF methodology is designed for generalizability, offering
other language communities a clear path to build foundational lexical data for downstream NLP
applications, such as Machine Translation and morphological analysis.

---

### 8. AutoFormBench: Benchmark Dataset for Automating Form Understanding

- arXiv: [2603.29832v1](https://arxiv.org/abs/2603.29832v1)
- PDF: [下载链接](https://arxiv.org/pdf/2603.29832v1)
- 作者: Gaurab Baral, Junxiu Zhou
- 发布时间: 2026-03-31T14:53:26Z
- 分类: cs.CV
- 相关性评分: 15
- 主题标签: 表单理解、目标检测、基准数据集、YOLO、结构化文档

**中文摘要**

> 本文介绍了AutoFormBench，一个包含407个标注真实世界表单的基准数据集，涵盖政府、医疗和企业领域，用于训练和评估表单元素检测模型。研究系统比较了经典OpenCV方法和四种YOLO架构（YOLOv8、YOLOv11、YOLOv26-s和YOLOv26-l）在定位和分类可填写表单元素（特别是复选框、输入线和文本框）方面的性能。YOLOv11在所有元素类别和容忍度级别上均表现出一致的优越性能，在F1分数和Jaccard准确度方面领先。

**核心创新概述**

> 创建了一个多领域真实世界表单的基准数据集，并系统评估了不同目标检测方法在表单元素识别任务上的表现。

**创新点拆解**

- 数据：构建了涵盖政府、医疗和企业领域的标注表单数据集，增强现实世界适用性
- 方法设计：系统比较了经典计算机视觉方法和多种YOLO架构
- 任务定义：专注于表单元素（如复选框、输入线）的检测和分类，针对结构化文档处理

**当前局限**

> 数据集规模相对较小（407个表单），可能不足以覆盖所有表单变体；评估主要基于YOLO架构，未广泛涵盖其他先进检测方法。

**后续可改进方向**

- 扩展数据集以包含更多表单类型和布局变体，提高模型泛化能力
- 探索更多检测架构（如Transformer-based模型）以全面评估性能
- 集成上下文理解以处理复杂表单逻辑和关系

**工程启发**

> 高，为表单自动化处理提供了基准和实用模型，可应用于文档数字化和业务流程优化。

**为什么值得关注**

> 直接涉及文档解析中的表单元素检测，对OCR和视觉文档理解有重要应用价值。

**原始摘要**

Automated processing of structured documents such as government forms, healthcare records, and
enterprise invoices remains a persistent challenge due to the high degree of layout variability
encountered in real-world settings. This paper introduces AutoFormBench, a benchmark dataset of 407
annotated real-world forms spanning government, healthcare, and enterprise domains, designed to
train and evaluate form element detection models. We present a systematic comparison of classical
OpenCV approaches and four YOLO architectures (YOLOv8, YOLOv11, YOLOv26-s, and YOLOv26-l) for
localizing and classifying fillable form elements. specifically checkboxes, input lines, and text
boxes across diverse PDF document types. YOLOv11 demonstrates consistently superior performance in
both F1 score and Jaccard accuracy across all element classes and tolerance levels.

---

### 9. SiPaKosa: A Comprehensive Corpus of Canonical and Classical Buddhist Texts in Sinhala and Pali

- arXiv: [2603.29221v1](https://arxiv.org/abs/2603.29221v1)
- PDF: [下载链接](https://arxiv.org/pdf/2603.29221v1)
- 作者: Ranidu Gurusinghe, Nevidu Jayatilleke
- 发布时间: 2026-03-31T03:36:46Z
- 分类: cs.CL
- 相关性评分: 13
- 主题标签: 历史文档、OCR、多语言语料库、文化遗产、语言模型

**中文摘要**

> 本文介绍了SiPaKosa，一个包含僧伽罗语和巴利语教义文本的综合语料库，约78.6万句子和925万词，整合了16个版权清晰的历史佛教文档以及完整的网络爬取三藏经典文本。语料库通过使用Google Document AI对历史手稿进行高质量OCR创建，结合系统网络爬取经典库，并进行严格质量控制和元数据标注。语料库按语言特定子库组织：僧伽罗语和混合僧伽罗-巴利语。研究评估了十种预训练语言模型的性能，困惑度分数在1.09到189.67之间，显示专有模型显著优于开源替代品三到六倍。该语料库支持领域适应语言模型的预训练，促进历史语言分析，并有助于佛教学术信息检索系统的开发，同时保护僧伽罗文化遗产。

**核心创新概述**

> 构建了一个大规模、多语言的佛教文本语料库，结合OCR和网络爬取技术，专注于低资源语言和文化遗产保护。

**创新点拆解**

- 数据：整合历史手稿OCR和网络爬取数据，创建大规模多语言语料库
- 方法设计：采用高质量OCR和系统质量控制流程
- 任务定义：支持语言模型预训练和历史语言分析，针对特定领域（佛教）

**当前局限**

> OCR质量可能受历史手稿条件限制；语料库主要聚焦佛教文本，泛化到其他领域可能有限；专有模型性能优势可能源于数据或计算资源差异。

**后续可改进方向**

- 优化OCR技术以提高历史文档的识别准确率，特别是对退化文本
- 扩展语料库以涵盖更多语言和领域，增强通用性
- 开发开源模型以缩小与专有模型的性能差距

**工程启发**

> 高，为低资源语言和文化遗产数字化提供了实用资源，支持NLP研究和应用开发。

**为什么值得关注**

> 涉及OCR在历史文档处理中的应用，对文档解析和语料库构建有直接贡献。

**原始摘要**

SiPaKosa is a comprehensive corpus of Sinhala and Pali doctrinal texts comprising approximately 786K
sentences and 9.25M words, incorporating 16 copyright-cleared historical Buddhist documents
alongside the complete web-scraped Tripitaka canonical texts. The corpus was created through high-
quality OCR using Google Document AI on historical manuscripts, combined with systematic web
scraping of canonical repositories, followed by rigorous quality control and metadata annotation.
The corpus is organised into language-specific subcorpora: Sinhala and Mixed Sinhala-Pali. We
evaluate the performance of language models using ten pretrained models, with perplexity scores
ranging from 1.09 to 189.67 on our corpus. This analysis shows that proprietary models significantly
outperform open-source alternatives by factors of three to six times. This corpus supports the
pretraining of domain-adapted language models, facilitates historical language analysis, and aids in
the development of information retrieval systems for Buddhist scholarship while preserving Sinhala
cultural heritage.

---

### 10. Xuanwu: Evolving General Multimodal Models into an Industrial-Grade Foundation for Content Ecosystems

- arXiv: [2603.29211v1](https://arxiv.org/abs/2603.29211v1)
- PDF: [下载链接](https://arxiv.org/pdf/2603.29211v1)
- 作者: Zhiqian Zhang, Xu Zhao, Xiaoqing Xu, Guangdong Liang, Weijia Wang, Xiaolei Lv, Bo Li, Jun Gao
- 发布时间: 2026-03-31T03:27:49Z
- 分类: cs.AI, cs.CL, cs.CV
- 相关性评分: 9
- 主题标签: 多模态模型、工业应用、对抗OCR、内容审核、紧凑架构

**中文摘要**

> 本文介绍了Xuanwu VL-2B作为一个案例研究，展示如何将通用多模态模型发展为内容生态系统的工业级基础模型。模型采用紧凑的InternViT-300M + MLP + Qwen3 1.7B架构，在约20亿参数预算内平衡细粒度视觉感知、语言语义对齐和部署成本。为平衡业务专业化与通用能力保留，开发了数据迭代和筛选机制，并通过渐进式三阶段流程（预训练、中训练和后训练）训练模型。消融研究和离线业务评估显示，Xuanwu VL-2B在七个OpenCompass多模态指标上平均得分67.90（对比InternVL 3.5 2B的64.27），在七个独立业务审核任务上平均召回率94.38%，在挑战性对抗OCR场景中政策违规文本的加权总体召回率82.82%，优于Gemini-2.5-Pro（76.72%）。结果表明，在有限参数预算下，Xuanwu VL-2B在业务对齐、视觉感知、通用能力保留和部署成本间实现了实用平衡。

**核心创新概述**

> 提出了一种工业级多模态模型优化方法，通过紧凑架构和渐进训练流程，在对抗场景中实现高性能。

**创新点拆解**

- 架构设计：采用紧凑模型组合（InternViT-300M + MLP + Qwen3 1.7B）以平衡性能和成本
- 训练范式：开发渐进式三阶段训练流程和数据迭代机制
- 任务定义：针对内容审核和对抗OCR场景进行优化，强调业务对齐

**当前局限**

> 模型性能可能受限于参数预算，在更复杂任务上可能不如更大模型；评估主要基于特定业务场景，泛化到其他领域需验证。

**后续可改进方向**

- 探索更高效的架构以在相同参数下提升性能
- 扩展训练数据以覆盖更多对抗场景和长尾噪声
- 优化部署策略以减少推理开销，提高实时性

**工程启发**

> 高，为工业应用提供了高效的多模态解决方案，特别适用于内容审核和OCR相关任务。

**为什么值得关注**

> 涉及多模态模型在OCR和文档解析中的应用，对视觉文档理解和业务部署有重要价值。

**原始摘要**

In recent years, multimodal large models have continued to improve on general benchmarks. However,
in real-world content moderation and adversarial settings, mainstream models still suffer from
degraded generalization and catastrophic forgetting because of limited fine-grained visual
perception and insufficient modeling of long-tail noise. In this paper, we present Xuanwu VL-2B as a
case study of how general multimodal models can be developed into an industrial-grade foundation
model for content ecosystems. The model adopts a compact InternViT-300M + MLP + Qwen3 1.7B
architecture, balancing fine-grained visual perception, language-semantic alignment, and deployment
cost within an approximately 2B-parameter budget. To balance business specialization with the
retention of general capabilities, we developed a data iteration and curation mechanism and trained
the model through a progressive three-stage pipeline: pre-training, mid-training, and post-training.
Ablation studies and offline business evaluations show that Xuanwu VL-2B achieves an average score
of 67.90 across seven OpenCompass multimodal metrics (vs. 64.27 for InternVL 3.5 2B), an average
recall of 94.38% over seven independent business moderation tasks, and a weighted overall recall of
82.82% on policy-violating text in challenging adversarial OCR scenarios, outperforming
Gemini-2.5-Pro (76.72%). These results show that, under a limited parameter budget, Xuanwu VL-2B
achieves a practical balance among business alignment, visual perception, general capability
retention, and deployment cost.

---

### 11. Navigating the Mirage: A Dual-Path Agentic Framework for Robust Misleading Chart Question Answering

- arXiv: [2603.28583v1](https://arxiv.org/abs/2603.28583v1)
- PDF: [下载链接](https://arxiv.org/pdf/2603.28583v1)
- 作者: Yanjie Zhang, Yafei Li, Rui Sheng, Zixin Chen, Yanna Lin, Huamin Qu, Lei Chen, Yushi Sun
- 发布时间: 2026-03-30T15:32:24Z
- 分类: cs.CV, cs.AI, cs.MM
- 相关性评分: 9
- 主题标签: 图表理解、代理框架、OCR、对抗训练、视觉欺骗

**中文摘要**

> 本文介绍了ChartCynics，一个代理双路径框架，旨在通过“怀疑”推理范式揭示误导性图表的视觉欺骗。与整体模型不同，ChartCynics将感知与验证解耦：诊断视觉路径通过战略ROI裁剪捕捉结构异常（如倒置轴），而OCR驱动数据路径确保数值基础。为解决跨模态冲突，引入了代理总结器，通过两阶段协议优化：Oracle-Informed SFT用于推理蒸馏和Deception-Aware GRPO用于对抗对齐。该流程有效惩罚视觉陷阱并强制逻辑一致性。在两个基准上的评估显示，ChartCynics达到74.43%和64.55%准确率，相比Qwen3-VL-8B骨干提供约29%的绝对性能提升，优于最先进的专有模型。结果表明，专业化代理工作流可以使较小开源模型获得优越鲁棒性，为可信图表解释建立新基础。

**核心创新概述**

> 提出了一种针对误导性图表的代理框架，通过双路径解耦和对抗训练增强模型鲁棒性。

**创新点拆解**

- 方法设计：开发双路径架构（诊断视觉路径和OCR驱动数据路径）以解耦感知和验证
- 训练范式：引入两阶段优化协议（Oracle-Informed SFT和Deception-Aware GRPO）
- 任务定义：专注于误导性图表理解，强调对抗场景下的鲁棒性

**当前局限**

> 框架可能依赖于特定图表类型，泛化到其他视觉欺骗形式需调整；OCR路径的准确性可能受图表质量影响。

**后续可改进方向**

- 扩展框架以处理更多图表类型和视觉欺骗模式
- 优化OCR组件以提高数值提取的准确性和鲁棒性
- 集成更多上下文信息以增强逻辑推理能力

**工程启发**

> 高，为图表解释提供了鲁棒解决方案，可应用于数据可视化和信息验证场景。

**为什么值得关注**

> 涉及OCR在图表数据提取中的应用，对文档解析和视觉理解有直接贡献。

**原始摘要**

Despite the success of Vision-Language Models (VLMs), misleading charts remain a significant
challenge due to their deceptive visual structures and distorted data representations. We present
ChartCynics, an agentic dual-path framework designed to unmask visual deception via a "skeptical"
reasoning paradigm. Unlike holistic models, ChartCynics decouples perception from verification: a
Diagnostic Vision Path captures structural anomalies (e.g., inverted axes) through strategic ROI
cropping, while an OCR-Driven Data Path ensures numerical grounding. To resolve cross-modal
conflicts, we introduce an Agentic Summarizer optimized via a two-stage protocol: Oracle-Informed
SFT for reasoning distillation and Deception-Aware GRPO for adversarial alignment. This pipeline
effectively penalizes visual traps and enforces logical consistency. Evaluations on two benchmarks
show that ChartCynics achieves 74.43% and 64.55% accuracy, providing an absolute performance boost
of ~29% over the Qwen3-VL-8B backbone, outperforming state-of-the-art proprietary models. Our
results demonstrate that specialized agentic workflows can grant smaller open-source models superior
robustness, establishing a new foundation for trustworthy chart interpretation.

---

### 12. Hydra: Unifying Document Retrieval and Generation in a Single Vision-Language Model

- arXiv: [2603.28554v1](https://arxiv.org/abs/2603.28554v1)
- PDF: [下载链接](https://arxiv.org/pdf/2603.28554v1)
- 作者: Athos Georgiou
- 发布时间: 2026-03-30T15:17:41Z
- 分类: cs.CV, cs.AI, cs.IR
- 相关性评分: 3
- 主题标签: 视觉语言模型、检索生成统一、LoRA、文档理解、系统优化

**中文摘要**

> 视觉文档理解通常需要独立的检索和生成模型，增加内存和系统复杂性。本文介绍了Hydra，一种双头方法，从单一视觉语言模型（VLM）提供ColBERT风格后期交互检索和自回归生成。单一LoRA适配器仅训练用于检索，在推理时切换：启用时产生多向量嵌入；禁用时恢复基础模型的生成质量——在10,500个贪婪和随机样本中100%字节相同输出，在四个VQA基准（三个信息性；ChartQA在贪婪解码下对两个模型均接近零）上15,301个样本的最大delta-ANLS = 0.0044，与独立基础模型流程相比。识别了三个工程要求（注意力模式恢复、lm_head保留、KV缓存感知解码），其省略会无声破坏生成尽管权重恢复正确。在ViDoRe V1上，Hydra（4B）在单次训练运行中与受控单头基线相差1个百分点以内，在V2和V3上具有更高聚合分数，集中在子集任务上；需要多种子实验确认这些趋势。单模型设计将峰值GPU内存减少41%，尽管适配器切换在并发服务负载下引入吞吐量开销。消融显示，GritLM风格联合训练在LoRA基础（r=16）训练机制内无益。对Qwen2.5-Omni-3B的概念验证扩展表明机制泛化到音频检索...

**核心创新概述**

> 提出了一种单模型双头架构，通过LoRA适配器切换实现检索和生成功能的统一，减少系统复杂性。

**创新点拆解**

- 架构设计：开发单模型双头方法，结合检索和生成功能
- 训练范式：使用LoRA适配器进行高效训练和切换
- 工程优化：识别关键工程要求以确保生成质量恢复

**当前局限**

> 适配器切换可能引入推理延迟，影响实时性能；机制在更复杂任务或模型上的泛化性需进一步验证。

**后续可改进方向**

- 优化适配器切换机制以减少吞吐量开销，提高推理效率
- 扩展架构以支持更多任务类型（如分类、摘要）
- 探索更高效的训练方法以进一步提升性能

**工程启发**

> 高，为文档理解提供了紧凑的解决方案，降低部署成本，适用于资源受限环境。

**为什么值得关注**

> 涉及视觉文档理解中的检索和生成任务，对OCR和文档解析系统集成有应用价值。

**原始摘要**

Visual document understanding typically requires separate retrieval and generation models, doubling
memory and system complexity. We present Hydra, a dual-head approach that provides both ColBERT-
style late-interaction retrieval and autoregressive generation from a single vision-language model
(VLM). A single LoRA adapter, trained only for retrieval, is toggled at inference: enabling it
produces multi-vector embeddings; disabling it recovers the base model's generation quality -- byte-
identical outputs in 100% of 10,500 greedy and stochastic samples, with max delta-ANLS = 0.0044
across 15,301 samples on four VQA benchmarks (three informative; ChartQA is near-zero for both
models under greedy decoding) when compared against an independent base-model pipeline. We identify
three engineering requirements (attention-mode restoration, lm_head preservation, KV-cache-aware
decoding) whose omission silently breaks generation despite correct weight recovery. On ViDoRe V1,
Hydra (4B) is within 1 percentage point of a controlled single-head baseline in a single training
run, with higher aggregate scores on V2 and V3 that are concentrated on a subset of tasks; multi-
seed experiments are needed to confirm these trends. The single-model design reduces peak GPU memory
by 41%, though adapter switching introduces throughput overhead under concurrent serving loads. An
ablation shows that GritLM-style joint training provides no benefit within the LoRA-based (r=16)
training regime. A proof-of-concept extension to Qwen2.5-Omni-3B demonstrates that the mechanism
generalizes to audio retrieval and video embedding, with speech generation.

---
