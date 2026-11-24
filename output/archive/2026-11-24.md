# OCR / 文档解析研究日报（2026-11-24）

## 报告说明

- 检索源：arXiv API
- 检索查询：`(all:"document parsing" OR all:"document understanding" OR all:"optical character recognition" OR all:OCR OR all:"layout analysis" OR all:"document layout analysis" OR all:"text recognition" OR all:"table recognition" OR all:"form understanding" OR all:"document intelligence" OR all:"page understanding" OR all:"scene text recognition" OR all:"handwritten text recognition" OR all:"information extraction") AND (cat:cs.CV OR cat:cs.AI OR cat:cs.CL OR cat:eess.IV)`
- 生成时间（UTC）：`2026-11-24 10:54:00`
- 大模型综合分析：`开启`

## 一、今日执行摘要

> 今日论文覆盖了OCR与文档解析的多个层面：应用端出现面向低资源文字、历史文献和领域文档的开源工具与高质量专用模型；方法端针对视觉语言模型在关键信息抽取和视觉定位中的解码效率瓶颈提出非自回归和并行解码方案；分析端则关注光学上下文压缩在推理VLM中的真实成本以及小模型推理的适用条件。整体趋势是从单纯追求精度转向兼顾效率、成本与可验证性，并越来越重视低资源场景的数据构建与人机协同。

## 二、今日趋势判断

今日研究显示三个并行趋势：一是专用OCR模型在特定字体/手写场景仍能显著优于通用VLM，且小模型经微调和量化后可低成本部署；二是文档信息抽取正从自回归序列生成转向利用模式结构先验的并行/非自回归解码，以固定前向次数换取吞吐；三是VLM推理成本分析开始区分预填充与解码开销，推动按工作负载动态选择图像或文本表示。

## 三、今日论文概览

1. **Trallie: from Free-Form Text to Structured Data with LLMs** | 标签：信息抽取、大语言模型、零样本学习、少样本学习、文档解析、模式归纳、开源框架
2. **Towards an Armenian Epigraphic Corpus** | 标签：OCR、版面检测、视觉语言模型、文化遗产数字化、低资源语言、人机协同、语料库构建
3. **PinGround: Pinning Queries to Points for Parallel Grounding in Vision-Language Models** | 标签：视觉语言模型、并行解码、目标定位、OCR、版面分析、强化学习、前缀树
4. **When Does Optical Context Compression Pay Off? A Decode-Aware Cost Analysis of Reasoning VLMs** | 标签：视觉语言模型、光学上下文压缩、推理成本、解码税、OCR、文档理解、成本分析
5. **DictaRashi: A State-of-the-Art OCR Model For Rashi Script** | 标签：OCR、Tesseract、希伯来语、Rashi字体、历史文献、低资源文字、基准数据集
6. **Meddies-PII: A Multilingual Framework for Personally Identifiable Information Extraction in Clinical De-identification** | 标签：PII抽取、临床文本、多语言、去标识化、合成数据、序列标注、信息抽取
7. **Fill in the Blanks: Non-Autoregressive Schema-Parallel Key Information Extraction with CTC Decoding** | 标签：关键信息抽取、非自回归解码、CTC、视觉语言模型、投机解码、文档理解
8. **Escriba-OCR: A 1B Vision-Language Model for Error-Preserving Transcription of Handwritten Portuguese Essays** | 标签：手写文本识别、错误保留、视觉语言模型、教育技术、基准构建、模型量化
9. **When Does Reasoning Help Entity Disambiguation? Small LLMs In-Domain and Under Shift** | 标签：实体消歧、小语言模型、推理、域偏移、零样本、信息抽取
10. **What Quality Engineers Need to Know About Generative AI: Structured Data Extraction** | 标签：结构化数据抽取、LLM应用、质量工程、人工验证、开源工具

## 四、今天 OCR / 文档解析论文里的主要创新点

- 利用结构先验（模式或空间锚点）将无序集合或结构化输出转化为可并行解码的形式，减少自回归步数。
- 构建低资源或领域特定的高质量数据集与基准，并公开生成流水线或人工校正数据以支持复现。
- 引入人机协同校验流程，将专家校对作为数字化流水线的必要环节而非事后修补。
- 关注小模型和量化部署，在精度与推理成本之间寻找可落地的平衡点。
- 从测量系统或成本核算视角评估抽取与压缩方案，强调人工验证和价格加权指标。

## 五、后续 OCR 领域值得推进的改进方向

- 将非自回归CTC解码与模式并行抽取扩展到更复杂的嵌套模式、自由文本值和多页文档，并在更多布局和领域上验证零样本鲁棒性。
- 研究生成前可预测的解码税信号，例如基于输入压缩比、任务类型和模型族特征训练轻量回归器，用于动态路由图像或文本输入。
- 把并行空间锚定定位（PinGround）与OCR流水线中的文本行检测、表格区域定位结合，评估锚点生成策略对密集版面任务F1和延迟的联合影响。
- 针对低资源文字和铭文，开发编辑符号与特殊标记的专门识别模块，并在人机协同校对平台中引入主动学习以减少专家校正量。
- 探索错误保留转录的通用框架，将编辑标记识别从手写作文扩展到表格修改、批注文档和校对稿，并建立跨语言错误保留基准。
- 研究小模型在信息抽取不同子任务（实体消歧、关系抽取、字段抽取）中推理收益的边界条件，并利用不确定性信号实现按样本动态路由。
- 将光学上下文压缩的成本核算从推理VLM扩展到文档解析专用模型，量化图像化输入对版面理解、表格还原和OCR后处理的影响。

## 六、工程落地启发

- 在批量文档KIE场景可优先评估非自回归模式并行解码，以固定前向次数规划资源并降低延迟。
- 部署VLM文档理解时应将输出token成本纳入核算，对高压缩比输入可尝试图像优先策略并设置回退文本的阈值。
- 特定字体或手写场景下，微调小专用OCR模型（1B级+量化）可在CPU上运行，适合本地化或隐私敏感部署。
- 构建文档抽取流水线时应把人工验证环节设计为可度量的测量系统，字段级准确率比整体主观评价更能暴露薄弱环节。
- 低资源文字数字化可采用版面检测+OCR+VLM结构化+专家校对的组合流水线，并将校对结果回流为银数据。
- 密集实例定位任务可关注并行解码加速方案，但需先评估锚点质量对召回的影响，避免为速度牺牲过多F1。

## 七、优先关注论文

- **Fill in the Blanks: Non-Autoregressive Schema-Parallel Key Information Extraction with CTC Decoding**：非自回归KIE与投机解码草稿模型的结合可能直接改变文档抽取的推理成本结构，需关注其向复杂模式和自由文本值的扩展。
- **When Does Optical Context Compression Pay Off? A Decode-Aware Cost Analysis of Reasoning VLMs**：解码税和汇率条件为文档理解中输入表示选择提供了可操作的量化框架，后续若出现生成前预测信号将影响流水线设计。
- **PinGround: Pinning Queries to Points for Parallel Grounding in Vision-Language Models**：并行空间锚定在密集OCR和版面定位任务上加速显著，锚点生成策略的鲁棒性是其落地关键。
- **Escriba-OCR: A 1B Vision-Language Model for Error-Preserving Transcription of Handwritten Portuguese Essays**：错误保留转录揭示了通用VLM的系统性规范化偏差，其基准和量化部署方案对教育及校对类产品有参考价值。
- **DictaRashi: A State-of-the-Art OCR Model For Rashi Script**：专用Tesseract模型在特定字体上显著优于前沿LLM，提示低资源文字场景中专用模型仍具成本与精度优势。

## 八、论文逐篇解析

### 1. Trallie: from Free-Form Text to Structured Data with LLMs

- arXiv: [2611.30773v1](https://arxiv.org/abs/2611.30773v1)
- PDF: [下载链接](https://arxiv.org/pdf/2611.30773v1)
- 作者: Vijayasri Iyer, Cristiano De Nobili, Mubashir Hussain Shah, Sébastien Bratières
- 发布时间: 2026-11-23T14:41:32Z
- 分类: cs.CL, cs.DB, cs.IR
- 相关性评分: 17
- 主题标签: 信息抽取、大语言模型、零样本学习、少样本学习、文档解析、模式归纳、开源框架

**中文摘要**

> Trallie 是一个开源框架，利用大语言模型（LLM）从自然语言源中进行信息抽取（IE），支持有或无用户指导。与依赖大量标注数据集或领域特定训练的传统方法不同，Trallie 能以极少或无需代表性示例将非结构化数据转换为结构化格式。该框架有三个关键目标：(i) 通过基于提示的零样本和少样本能力减少人工标注；(ii) 灵活解析多种文档格式（HTML、PDF、TXT 和 JSON）；(iii) 通过从文档集合自动归纳模式提高非专家用户的可访问性。作者在 FDA 510(k) 文档以及 SWDE 的电影和大学网站上用开放权重 LLM 评估 Trallie，在提供目标属性进行文本抽取时优于先前报告的系统，在必须自动发现模式属性时具有竞争力。

**核心创新概述**

> 提出一个开源、端到端的信息抽取框架 Trallie，整合 LLM 零样本/少样本提示、多格式文档解析和自动模式归纳，降低对标注数据和领域训练的依赖。

**创新点拆解**

- 基于提示的零样本和少样本信息抽取范式，减少人工标注需求。
- 支持 HTML、PDF、TXT 和 JSON 多种文档格式的统一解析流程。
- 自动从文档集合中归纳抽取模式（schema），并允许用户细化，提升非专家可用性。
- 开源框架设计，便于复现和扩展。

**当前局限**

> 在自动发现模式属性时性能仅具竞争力，未超越现有系统；评估主要基于开放权重 LLM 和有限数据集（FDA 510(k)、SWDE），泛化性需进一步验证。

**工程启发**

> 为快速构建文档信息抽取流水线提供开源工具，降低标注和领域适配成本，适用于监管文档、网页结构化等场景。

**为什么值得关注**

> 该工作直接涉及 OCR/文档解析后的结构化信息抽取，利用 LLM 实现端到端文本到结构化数据的转换，与文档智能和 OCR 应用密切相关。

**原始摘要**

Trallie is an open-source framework that leverages large language models (LLMs) to perform
information extraction (IE) from natural language sources with or without user guidance. Unlike
conventional approaches that rely on extensive labeled datasets or domain-specific training, Trallie
enables the conversion of unstructured data into structured formats with minimal or no
representative examples. The framework is designed with three key objectives: (i) reducing manual
annotation by harnessing prompt-based zero-shot and few-shot capabilities of modern LLMs, (ii)
flexibly parsing diverse document formats (i.e., HTML, PDF, TXT, and JSON), and (iii) improving
accessibility for non-expert users by automatically inducing schemas from document collections,
which can then be refined for extraction. We evaluate Trallie with open-weight LLMs on FDA 510(k)
documents and on movie and university websites from SWDE. It outperforms previously reported systems
when the target attributes are provided for text extraction and is competitive when it must discover
attributes for the schema automatically. The project is available at
https://github.com/PiSchool/trallie

---

### 2. Towards an Armenian Epigraphic Corpus

- arXiv: [2611.30603v1](https://arxiv.org/abs/2611.30603v1)
- PDF: [下载链接](https://arxiv.org/pdf/2611.30603v1)
- 作者: Chahan Vidal-Gor{è}ne, Arpine Avetisyan, Edita Matevosyan, Seda Kirakosyan, Victoria Khurshudyan, Pollet Samvelian
- 发布时间: 2026-11-23T12:40:28Z
- 分类: cs.CV
- 相关性评分: 17
- 主题标签: OCR、版面检测、视觉语言模型、文化遗产数字化、低资源语言、人机协同、语料库构建

**中文摘要**

> 本文介绍 Corpus Inscriptionum Armenicarum Electronicum，将十卷亚美尼亚铭文印刷目录 Divan hay vimagrut'yan（1960-2017，近7600条记录）转化为开放数字语料库。流程包括版面检测、OCR 和视觉语言模型生成每条记录的首个结构化读取结果，随后专家在校对平台上检查。初步校正表明字母识别可靠，残余错误集中在编辑符号。该语料库旨在成为记录亚美尼亚铭文的持久平台，并为语言模型和计算语言学提供古典和中古亚美尼亚语的银数据。

**核心创新概述**

> 构建首个亚美尼亚铭文开放数字语料库，结合版面检测、OCR 和视觉语言模型实现结构化读取，并引入专家校对平台。

**创新点拆解**

- 针对亚美尼亚铭文这一低资源文字遗产，设计端到端数字化流水线：版面检测、OCR、视觉语言模型结构化。
- 引入专家校对平台，形成人机协同的数据校验流程。
- 将语料库设计为可复用的银数据源，服务于语言模型和计算语言学研究。

**当前局限**

> 残余错误集中在编辑符号，说明对特殊符号和版面复杂结构的处理仍不完善；仅以初步校正结果报告，未给出完整定量评估；语料库规模有限（约7600条记录）。

**工程启发**

> 为文化遗产数字化提供可复用的 OCR+视觉语言模型流水线及专家校对平台，适用于其他低资源文字和铭文文献。

**为什么值得关注**

> 涉及 OCR、版面检测和视觉语言模型在历史文献数字化中的集成应用，与文档解析和文化遗产 OCR 直接相关。

**原始摘要**

The Divan hay vimagrut'yan (1960-2017), the printed corpus of Armenian inscriptions, comprises
nearly 7,600 records; a growing number of the inscriptions they describe, damaged or destroyed in
recent decades, survive only in its pages. Armenian epigraphy nevertheless lacks a digital resource
of the kind available for Greek, Latin or Georgian. This paper presents the Corpus Inscriptionum
Armenicarum Electronicum, which turns the ten volumes of the Divan into an open digital corpus.
Layout detection, OCR and a vision-language model produce a first structured reading of each record,
which specialists then check on a proofreading platform. First corrections show that letters are
read reliably and that residual errors concentrate in the editorial signs. The corpus is designed as
a lasting platform for documenting Armenian inscriptions and as a source of silver data in Classical
and Middle Armenian for language models and computational linguistics.

---

### 3. PinGround: Pinning Queries to Points for Parallel Grounding in Vision-Language Models

- arXiv: [2611.30304v1](https://arxiv.org/abs/2611.30304v1)
- PDF: [下载链接](https://arxiv.org/pdf/2611.30304v1)
- 作者: Shuxuan Li, Jialiang Kang, Yanghao Zhou, Ziye Zhu, Zhilin Zhao, Xiao Yang
- 发布时间: 2026-11-23T08:55:01Z
- 分类: cs.CV
- 相关性评分: 13
- 主题标签: 视觉语言模型、并行解码、目标定位、OCR、版面分析、强化学习、前缀树

**中文摘要**

> 视觉语言模型（VLM）通过文本接口进行定位，以单一序列逐个写出边界框，但查询实例是无序集合，解码步数随实例数增长，密集场景成本最高。并行解码可避免增长，但互不可见的流会重复或遗漏实例。本文提出 PinGround，在查询中写入单个点作为空间锚点，要求模型在局部半径内返回最近匹配实例或 none。给定图像，锚定查询相互独立，可作为前缀树的叶子并行解码，模型在同一树上训练。粗到细锚点仅细化发现实例的区域，重复抑制保持每实例一框，集合级强化学习优化集合 F1。仅改变提示和注意力掩码，不改变架构。在三种 VLM 和 12 个基准（检测、OCR、布局和指代）上，PinGround 最多比同数据训练的序列解码低 5.5 F1，加速随实例密度增长，密集场景达 21.9 倍。

**核心创新概述**

> 提出 PinGround，将查询锚定为空间点，实现并行解码实例集合，在不改变模型架构的前提下大幅提升密集场景下的定位效率。

**创新点拆解**

- 查询锚定机制：在查询中写入空间点作为锚点，将无序集合解码转化为独立并行解码。
- 前缀树并行解码：利用共享图像和查询的前缀树结构，实现叶子级并行生成。
- 粗到细锚点细化与重复抑制：仅细化包含实例的区域，保持每实例一个框。
- 集合级强化学习：直接优化集合 F1 指标，适配无序集合预测。

**当前局限**

> 相比序列解码仍存在最多 5.5 F1 的性能差距；方法依赖锚点质量，对锚点生成策略敏感；仅在三种 VLM 上验证，泛化性需进一步测试。

**工程启发**

> 显著提升密集场景下的定位解码速度（21.9 倍），对 OCR 中的文本行检测、版面区域定位等高密度实例任务具有直接工程价值。

**为什么值得关注**

> 该工作针对视觉语言模型在 OCR、布局和指代定位中的解码效率问题，提出并行定位方法，与 OCR 和文档解析中的文本行/区域检测高度相关。

**原始摘要**

Vision-language models (VLMs) can localize through their text interface, grounding open-vocabulary
objects, complex referring expressions, text lines and layout regions with strong semantic
understanding. They write the boxes one after another as a single sequence, although the instances
of a query, unlike the words of a sentence, form an unordered set with no sequential dependence. The
number of decoding steps therefore grows with the number of instances, which makes dense scenes the
most expensive. Decoding the instances in parallel avoids this growth, but streams that cannot see
each other duplicate some instances and miss others. We propose \method, which writes a single point
into each query as a spatial anchor and asks for the matching instance nearest to that point within
a local radius, or \none. Given the image, the anchored queries are independent, so they are decoded
in parallel as leaves of a prefix tree that shares the image and the query, and the model is trained
on the same tree. Coarse-to-fine anchors refine only the regions where instances are found,
duplicate suppression keeps one box per instance, and set-level reinforcement learning optimizes the
set F1. Only the prompt and the attention mask change, not the architecture. On three different VLMs
and 12 benchmarks covering detection, OCR, layout and referring, \method is at most 5.5 F1 below
sequential decoding trained on the same data, while its speedup grows with instance density and
reaches 21.9$\times$ on dense scenes.

---

### 4. When Does Optical Context Compression Pay Off? A Decode-Aware Cost Analysis of Reasoning VLMs

- arXiv: [2611.30130v1](https://arxiv.org/abs/2611.30130v1)
- PDF: [下载链接](https://arxiv.org/pdf/2611.30130v1)
- 作者: Ziqing Ge
- 发布时间: 2026-11-23T06:40:44Z
- 分类: cs.AI, cs.CL
- 相关性评分: 13
- 主题标签: 视觉语言模型、光学上下文压缩、推理成本、解码税、OCR、文档理解、成本分析

**中文摘要**

> 将长文本渲染为图像可让视觉语言模型（VLM）用更少输入 token 阅读文档，评估常主要计算这些预填充 token。本文表明对推理模型而言这种核算不完整。在五个模型和两个长上下文基准上，阅读渲染文档使模型思考更久：四个通用 VLM 的解码长度增长 1.5-3.5 倍，在典型输出定价下，该解码税使两个模型在 QuALITY 上图像输入比文本更贵。中等压缩下不可恢复信息损失不足以解释该税：Qwen 对同图像 OCR 恢复 98.7% 单词，将 Kimi-K3 自己的转录作为文本输入可恢复文本模式推理长度和准确率。压缩是否划算归结为汇率 (1-1/c)/(r-1) 是否超过工作负载的价格加权输出输入 token 比；该核算分解解释了 Kimi-K3 和 DeepSeek-V4.1-Flash 可受益而 Qwen 和 GLM 不能。无训练免费信号能在生成前预测该税。作为实用启发式，图像优先策略仅将每输入压缩比至少 1.6 的输入发送为图像，一旦图像模式推理成本等于输入预填充节省则回退文本，在 Kimi-K3 和 DeepSeek-V4.1-Flash 上账单降低 6-14%，准确率代价 0.3-1.2 点；在 QuALITY 上，两条路径均要求推理预算更强。

**核心创新概述**

> 揭示推理 VLM 中光学上下文压缩的“解码税”现象，提出基于汇率条件的成本分析框架，并给出图像优先的实用启发式策略。

**创新点拆解**

- 提出解码感知的成本分析，将输出 token 增长纳入光学压缩的经济性评估。
- 推导压缩划算的汇率条件 (1-1/c)/(r-1)，解释不同模型受益差异。
- 设计图像优先启发式策略，基于每输入压缩比动态选择图像或文本路径。
- 通过 OCR 转录恢复实验分离信息损失与解码税的影响。

**当前局限**

> 启发式策略仅在两个模型上验证账单降低，准确率仍有 0.3-1.2 点损失；未找到生成前预测解码税的无训练信号；结论依赖特定定价假设。

**工程启发**

> 为文档理解系统中图像输入与文本输入的成本权衡提供量化框架和实用策略，有助于在 OCR 流水线中动态选择表示形式以降低推理成本。

**为什么值得关注**

> 该工作分析 OCR/文档图像输入对 VLM 推理成本的影响，直接关联 OCR 在文档理解中的经济性部署决策。

**原始摘要**

Rendering long text as images lets a vision-language model (VLM) read a document with fewer input
tokens, and evaluations often count mainly these prefill tokens. We show that for reasoning models
this accounting is incomplete. Across five models and two long-context benchmarks, reading the
rendered document makes the model think longer: decode length grows by 1.5-3.5x on the four general-
purpose VLMs tested, and under typical output pricing this decode tax makes image input more
expensive than text for two of the five models on QuALITY. Unrecoverable information loss is not
sufficient to explain the tax at moderate compression: Qwen's OCR of the same images recovers 98.7%
of words, and feeding Kimi-K3 its own transcription as text restores text-mode reasoning length and
accuracy. Whether compression pays off reduces to an exchange rate, (1-1/c)/(r-1), that must exceed
the workload's price-weighted ratio of output to input tokens; this accounting decomposition shows
why Kimi-K3 and DeepSeek-V4.1-Flash can benefit and Qwen and GLM cannot. None of the training-free
signals we test predicts the tax before generation. As a practical heuristic, an image-first policy
that sends only inputs with a per-input compression ratio of at least 1.6 to images and falls back
to text once image-mode reasoning costs as much as the input's prefill saving cuts the bill by 6-14%
on Kimi-K3 and DeepSeek-V4.1-Flash at an accuracy cost of 0.3-1.2 points; on QuALITY, asking for a
reasoning budget on both paths is a stronger lever.

---

### 5. DictaRashi: A State-of-the-Art OCR Model For Rashi Script

- arXiv: [2611.29760v1](https://arxiv.org/abs/2611.29760v1)
- PDF: [下载链接](https://arxiv.org/pdf/2611.29760v1)
- 作者: Ometz Shmidman, Yonah Taurog, Aryeh Sanders, Shlomo Bluth, Moshe Koppel, Joshua Geudalia, Avi Shmidman
- 发布时间: 2026-11-22T20:49:18Z
- 分类: cs.CV
- 相关性评分: 13
- 主题标签: OCR、Tesseract、希伯来语、Rashi字体、历史文献、低资源文字、基准数据集

**中文摘要**

> 本文发布 DictaRashi，一个用于扫描希伯来语书籍中所谓“Rashi”字体的 Tesseract OCR 模型。训练数据超过一百万条人工校正文本行，来自100多本拉比和后拉比文学书籍。在1,120条人工转录的 Rashi 字体扫描页保留集上，DictaRashi 达到字符错误率（CER）0.86% 和词错误率（WER）3.38%，为公开 Tesseract 模型的新最优。与31个其他公开希伯来语 Tesseract 模型比较，最佳者 CER 2.98%、WER 11.86%。进一步证明 DictaRashi 在该 OCR 任务上优于当前前沿 LLM。发布测试集作为基准，模型和测试集以 CC BY NC 4.0 许可发布。

**核心创新概述**

> 针对 Rashi 字体希伯来语书籍，发布大规模人工校正训练的高性能 Tesseract OCR 模型，并建立公开基准。

**创新点拆解**

- 构建超过一百万条人工校正文本行的 Rashi 字体训练集，覆盖100多本书籍。
- 发布首个公开的 Rashi 字体 Tesseract OCR 模型，CER 0.86%、WER 3.38%，显著优于31个现有模型。
- 证明专用 OCR 模型在特定字体任务上优于前沿 LLM。
- 公开测试集和模型，建立可复现基准。

**当前局限**

> 仅针对 Rashi 字体，未覆盖其他希伯来语字体或更广泛的历史文献；基于 Tesseract 传统架构，可能难以处理复杂版面或低质量扫描；测试集规模有限（1,120行）。

**工程启发**

> 为历史希伯来语文献数字化提供可直接部署的高精度 OCR 模型和基准，降低拉比文学数字化的门槛。

**为什么值得关注**

> 该工作直接发布针对特定字体的 OCR 模型和基准，属于 OCR 核心领域，对低资源文字识别有参考价值。

**原始摘要**

We release DictaRashi, a Tesseract OCR model for scanned Hebrew books printed in the so-called
"Rashi" font. We trained DictaRashi on over one million manually corrected lines of text from over
100 different books of Rabbinic and post-Rabbinic literature. On a held-out set of 1,120 manually
transcribed lines from scanned Rashi-script pages, DictaRashi reaches a character error rate (CER)
of 0.86% and a word error rate (WER) of 3.38%, setting a new state-of-the-art for publicly-available
Tesseract models. We provide a full comparison of our results to those of the 31 other publicly
available Hebrew Tesseract models; the best of those models achieves a 2.98% CER and 11.86% WER. We
further demonstrate that DictaRashi outperforms the current frontier LLMs on this OCR task. We
release the test set of Rashi-script documents so that it may be used as a benchmark for future work
in this area. We are pleased to release the model and test set to the community under a CC BY NC 4.0
license.

---

### 6. Meddies-PII: A Multilingual Framework for Personally Identifiable Information Extraction in Clinical De-identification

- arXiv: [2611.29491v1](https://arxiv.org/abs/2611.29491v1)
- PDF: [下载链接](https://arxiv.org/pdf/2611.29491v1)
- 作者: Le Linh Uyen, Christian Hoang, Ho Dinh Tri, Huy Hoang Ha
- 发布时间: 2026-11-22T13:59:37Z
- 分类: cs.CL
- 相关性评分: 10
- 主题标签: PII抽取、临床文本、多语言、去标识化、合成数据、序列标注、信息抽取

**中文摘要**

> 临床文本中的多语言个人可识别信息（PII）抽取受限于稀缺的受治理数据和构建记录稀少的合成语料库。本文提出 Meddies-PII，一个覆盖17种语言（包括7种东南亚语言）和9个PII标签的大型多语言数据集，并详细记录生成流水线，发布完整提示、目录、检查和标签映射。一个紧凑的350M参数 BIOES 标记分类器在该资源上训练，在全部15个公开基准上取得最高分，其中14个显著领先四个公开系统中最强者的平均精确匹配 F1 为0.827对0.672。未经适配在多语言基准上测试，包括两个人工标注的德语和西班牙语临床风格语料库，在标注约定对齐后与最佳公开系统竞争，并在 MultiGraSCCo 十种语言中的四种上最佳。分析发现几乎无近重复，训练与任何评估集无文本重叠。数据集、基准、模型、生成框架和评估代码计划在录用后公开。

**核心创新概述**

> 构建覆盖17种语言的大规模多语言临床 PII 数据集，并提供可复现的合成数据生成流水线和紧凑高效模型。

**创新点拆解**

- 17种语言（含7种东南亚语言）和9个PII标签的大规模多语言临床数据集。
- 完整公开的合成数据生成流水线（提示、目录、检查、标签映射），提升可复现性。
- 350M 紧凑 BIOES 标记分类器在15个公开基准上取得最高分，显著优于公开系统。
- 验证跨语言迁移能力，在德语和西班牙语人工标注语料库上具有竞争力。

**当前局限**

> 依赖合成数据生成，虽无近重复但真实临床文本的分布差异仍需验证；模型为350M参数，可能受限于更复杂的临床实体；部分基准上仅与最佳系统竞争而非全面领先；数据尚未公开。

**工程启发**

> 为临床文本去标识化提供多语言数据资源和高效紧凑模型，可直接用于隐私保护流水线，降低多语言部署成本。

**为什么值得关注**

> 涉及从临床文本中抽取结构化PII信息，与文档解析和信息抽取相关，且OCR后的临床文档处理常需去标识化。

**原始摘要**

Multilingual PII extraction in clinical text is limited by scarce governed data and by synthetic
corpora whose construction is thinly documented. We present a large multilingual dataset covering
seventeen languages, including seven Southeast Asian languages, and nine PII labels. We also
document a detailed generation pipeline and release the complete prompts, catalogues, checks and
label maps. A compact 350M-parameter BIOES token classifier trained on the resource achieves the
highest score on all fifteen public benchmarks, significantly ahead of the strongest of four public
systems on fourteen of them, with a mean exact-match F1 of 0.827 against 0.672 for the strongest
system. We also tested it, without adaptation, on multilingual benchmarks, including two human-
annotated German and Spanish clinical-style corpora, where it is competitive with the best public
systems once annotation conventions are aligned, and is best in four of ten MultiGraSCCo languages;
the results show that performance transfers across public benchmarks. We also analyse the data and
find almost no near-duplicates and no text overlap between training and any evaluation set. The
dataset, benchmark, model, generation framework and evaluation code are planned for public release
upon acceptance.

---

### 7. Fill in the Blanks: Non-Autoregressive Schema-Parallel Key Information Extraction with CTC Decoding

- arXiv: [2611.29460v1](https://arxiv.org/abs/2611.29460v1)
- PDF: [下载链接](https://arxiv.org/pdf/2611.29460v1)
- 作者: Shaked Perek, Avihu Dekel, Ben Wiesel, Sivan Harary, Eli Schwartz
- 发布时间: 2026-11-22T13:01:05Z
- 分类: cs.CV
- 相关性评分: 10
- 主题标签: 关键信息抽取、非自回归解码、CTC、视觉语言模型、投机解码、文档理解

**中文摘要**

> 针对视觉语言模型在关键信息抽取（KIE）中自回归生成JSON导致解码步数随答案长度增长的问题，提出非自回归提取器。利用模式已知的结构信息直接写入结构，通过计数遍确定列表长度，并行预测所有值，每个值用CTC在独立槽位块中解码以避免长度预测，固定前向次数不随文档增长。在VAREX、CORD、FUNSD零样本实验中，4B模型比扩散VLM平均快3.5倍（最高5.6倍）且更准确，每文档仅需4-6次前向。该方法还可作为投机解码的草稿模型，比自回归解码快8.3倍（最高10.4倍）且精度差距在0.4点内，比投机扩散解码快3.3倍且准确率高13.0点。

**核心创新概述**

> 首次将非自回归CTC解码与模式驱动的结构生成结合用于KIE，利用模式先验消除序列长度依赖，并扩展为投机解码草稿模型。

**创新点拆解**

- 提出模式并行非自回归KIE框架，直接根据模式写入键、嵌套和列表结构，仅并行预测值。
- 采用计数遍确定每个列表的长度，避免自回归逐步生成列表元素。
- 为每个值分配独立CTC解码槽位块，无需预测值长度，块内未闭合值自动获得更大令牌预算。
- 将提取器同时作为自回归基模型的投机解码草稿，实现加速且保持精度。

**当前局限**

> 零样本评估仅在三个数据集（VAREX、CORD、FUNSD）上验证，未涵盖更复杂的文档布局或模式；CTC解码对值内部顺序敏感，可能限制对自由文本值的建模；模型规模4B，未探索更小模型可行性；未与更多非自回归KIE方法对比。

**工程启发**

> 为文档KIE提供高吞吐、低延迟的推理方案，适合批量处理场景；投机解码加速可降低部署成本；固定前向次数有利于资源规划；开源模型和代码促进工业落地。

**为什么值得关注**

> 直接针对OCR下游关键信息抽取任务，提出非自回归并行解码方法，显著提升推理效率并保持精度，与文档解析中的结构化输出需求高度相关。

**原始摘要**

Vision-language models (VLMs) extract structured data from documents by generating the requested
JSON one token at a time, so their sequential steps grow with the length of the answer. Yet in key
information extraction (KIE) the schema already fixes the answer's structure: keys, nesting and
lists are known before decoding, and only the values are unknown. We exploit this with a non-
autoregressive extractor that writes the structure from the schema, sizes every list with a count
pass, and predicts all values in parallel, in a fixed number of passes that does not grow with the
document. Each value is decoded with connectionist temporal classification (CTC) in its own block of
slots, so its length never has to be predicted, and a value that is still open after its block gets
a larger token budget. Zero-shot on VAREX, CORD and FUNSD, our 4B extractor is 3.5$\times$ faster
than the diffusion-VLM competition on average (up to 5.6$\times$) and more accurate, with 4--6
forward passes per document where block diffusion needs 12--74. The same extractor also drafts for
speculative decoding with its own autoregressive base: it runs 8.3$\times$ faster than
autoregressive decoding (up to 10.4$\times$) within 0.4 points of its accuracy, and 3.3$\times$
faster than speculative diffusion decoding while 13.0 points more accurate. We release the model and
code.

---

### 8. Escriba-OCR: A 1B Vision-Language Model for Error-Preserving Transcription of Handwritten Portuguese Essays

- arXiv: [2611.29874v1](https://arxiv.org/abs/2611.29874v1)
- PDF: [下载链接](https://arxiv.org/pdf/2611.29874v1)
- 作者: Tardelli Ronan Coelho Stekel
- 发布时间: 2026-11-23T01:08:48Z
- 分类: cs.CL, cs.CV, cs.CY
- 相关性评分: 8
- 主题标签: 手写文本识别、错误保留、视觉语言模型、教育技术、基准构建、模型量化

**中文摘要**

> 针对手写作文转录需要保留学生原始错误（拼写错误、划掉、插入等）的需求，指出现有视觉语言模型倾向于将手写内容改写为正确语言。在BRESSAY的1000篇巴西葡萄牙语手写作文上建立基准，除CER外增加错误保留、虚构错误、编辑标记精确率/召回率和行结构指标。评估22个开源基线，最佳Qwen3-VL 235B-A22B达到5.6% CER但无一可靠复现编辑标记，所有模型将39-78%的非词典词替换为词典词。在单GPU上85分钟微调LightOnOCR-3-1B得到Escriba-OCR-1B，CER降至2.06%，比最佳基线低3.5点，ICDAR 2024指标下CER为2.1%，恢复67%插入和77%不可辨认删除，97%页面行结构正确，但仍规范化60%可能拼写错误。4比特量化后普通CPU约一分钟每页。

**核心创新概述**

> 首次系统评估并解决VLM在手写作文转录中的错误规范化问题，提出错误保留基准和微调的小型专用模型。

**创新点拆解**

- 构建BRESSAY错误保留基准，在CER外引入错误保留率、虚构错误、编辑标记精确率/召回率和行结构等指标。
- 揭示所有开源VLM普遍将非词典词替换为词典词的系统性偏差。
- 通过单GPU微调1B模型实现错误保留转录，显著降低CER并部分恢复编辑标记。
- 模型可4比特量化在CPU运行，满足学校本地部署需求。

**当前局限**

> 仍规范化60%的可能拼写错误，错误保留能力不完整；仅针对巴西葡萄牙语手写作文，语言和场景单一；编辑标记恢复率有限（插入67%、删除77%）；未探索更大规模或更多样化的手写数据。

**工程启发**

> 为教育反馈工具提供可本地部署的小型错误保留转录模型，量化后CPU可运行，降低学校硬件门槛；基准和指标可指导后续产品评估。

**为什么值得关注**

> OCR在手写教育场景中的应用，强调错误保留而非规范化，与文档解析中忠实转录的需求直接相关，且模型轻量化具有工程参考价值。

**原始摘要**

Feedback tools and research on learner writing need transcriptions of handwritten essays that keep
exactly what the student wrote: misspellings, line breaks, struck-through words and insertions.
Vision-language models (VLMs) read handwriting well, but they also tend to rewrite it into correct
language. We measure this on BRESSAY, 1,000 handwritten Brazilian Portuguese essays, with a
benchmark that adds error preservation, invented errors, edit-markup precision and recall and line
structure to the character error rate (CER) and uses paired bootstrap confidence intervals. We
restrict the study to open-weight models that schools can run on their own hardware. Of 22 open
baselines, the best, Qwen3-VL 235B-A22B, reaches 5.6% CER on the 199 test pages; none reproduces the
edit markup reliably, and every VLM replaces 39-78% of the words absent from a Portuguese dictionary
with dictionary words. We fine-tune LightOnOCR-3-1B on the 647 training pages in 85 minutes on one
GPU. The resulting Escriba-OCR-1B reaches 2.06% CER, 3.5 points below the best baseline (95% CI
[-4.2, -2.9]); under the ICDAR 2024 competition metric it reaches 2.1% CER, below the best published
page-level results (2.2-2.4%). It recovers 67% of insertions and 77% of illegible deletions, and
reproduces the line structure of 97% of the pages, but still normalises 60% of likely misspellings.
Three seeds agree within 0.04 CER points, and quantised to 4 bits the model runs on an ordinary CPU
at about one minute per page. On 40 letters of another corpus it matches its base model (without
that model's appended comments) but misreads unseen words more often; weight interpolation recovers
half the gap. A teacher's review finds that 45% of the judgeable apparent corrections are errors in
the BRESSAY ground truth, so dictionary-based scores likely understate preservation. We release the
model, the benchmark code and the review data.

---

### 9. When Does Reasoning Help Entity Disambiguation? Small LLMs In-Domain and Under Shift

- arXiv: [2611.30334v1](https://arxiv.org/abs/2611.30334v1)
- PDF: [下载链接](https://arxiv.org/pdf/2611.30334v1)
- 作者: Samy Haffoudhi, Fabian M Suchanek, Nils Holzenberger
- 发布时间: 2026-11-23T09:11:54Z
- 分类: cs.CL
- 相关性评分: 6
- 主题标签: 实体消歧、小语言模型、推理、域偏移、零样本、信息抽取

**中文摘要**

> 研究小规模LLM在实体消歧（ED）中推理何时有益。在经典粗到细ED流程中比较逐点、列表和基于推理的候选选择组件，覆盖经典、少样本和真零样本设置，推理范式采用蒸馏和强化学习训练。发现推理收益随域偏移增大：域内可忽略，真零样本下决定性。两个因素起作用：重排器对候选的不确定性定位范式分歧点，域偏移决定分歧时哪方正确。

**核心创新概述**

> 系统分析小规模LLM在实体消歧中推理范式的收益条件，揭示域偏移与重排器不确定性的交互机制。

**创新点拆解**

- 在统一粗到细ED管道中对比逐点、列表和推理候选选择，覆盖三种监督设置。
- 采用蒸馏和强化学习训练小规模推理ED模型。
- 提出重排器不确定性定位范式分歧、域偏移决定正确性的分析框架。

**当前局限**

> 仅研究实体消歧任务，未推广至其他信息抽取任务；小模型规模未明确；推理成本分析可能不全面；未探索推理与检索增强的结合。

**工程启发**

> 为小模型部署ED提供成本-收益指导：域内可用轻量重排，域外切换推理；不确定性信号可用于动态路由。

**为什么值得关注**

> 实体消歧是信息抽取的基础步骤，与OCR后的文档理解与知识图谱构建相关；小模型推理成本分析对实际部署有参考意义。

**原始摘要**

Entity disambiguation (mapping ambiguous mentions in text to entities in a knowledge base) is a
foundational step in tasks such as knowledge graph construction, question answering, and information
extraction. Recent work has applied LLMs to this problem, achieving stateof-the-art performance.
Notably, reasoning LLMs have been shown to perform entity disambiguation in a true zero-shot
fashion, generalizing across knowledge bases and domains. However, it is unclear whether this
capability survives, or remains competitive, with smaller LLMs, where entity disambiguation has
typically relied on reranking rather than reasoning. We ask when reasoning is worth its cost at
small scale. We compare pointwise, listwise, and reasoning-based candidate-selection components
within a classical coarse-to-fine entity disambiguation pipeline, across the classical, few-shot and
true zero-shot settings. The reasoning paradigm is trained with distillation and reinforcement
learning recipes. The benefit of reasoning grows with domain shift: negligible in-domain, decisive
in the true zero-shot setting. We show that two distinct factors are at work: the reranker's
uncertainty over the candidates locates where the paradigms disagree, while shift governs which is
right when they do.

---

### 10. What Quality Engineers Need to Know About Generative AI: Structured Data Extraction

- arXiv: [2611.30778v1](https://arxiv.org/abs/2611.30778v1)
- PDF: [下载链接](https://arxiv.org/pdf/2611.30778v1)
- 作者: Fadel M. Megahed, Ying-Ju Chen, Yamin Dahwich, Zhao-Wei Chen, Lucas K. Hung, Arthur Carvalho, L. Allison Jones-Farmer, Ibrahim Yousif, Inez M. Zwetsloot
- 发布时间: 2026-11-23T14:44:59Z
- 分类: cs.CE, cs.CL
- 相关性评分: 3
- 主题标签: 结构化数据抽取、LLM应用、质量工程、人工验证、开源工具

**中文摘要**

> 面向质量工程师的说明性论文，介绍如何使用LLM和VLM进行结构化数据抽取。从测量系统视角讨论结构化抽取，提供R和Python实现，并展示两个免费Web应用：从汽车召回通知中抽取信息、监控arXiv上质量工程研究。人工评估验证：第一个应用4名评审对30份召回通知的720个字段级评分中98.6%完全正确；第二个应用21名作者评估45篇论文的抽取摘要，所有摘要被评为大部分正确或正确，但分类字段和数学表达式存在问题。强调实际潜力与验证必要性，公开应用和源码。

**核心创新概述**

> 从质量工程测量系统视角系统阐述LLM/VLM结构化抽取的实施与验证流程，提供可复用的开源应用。

**创新点拆解**

- 将结构化抽取视为测量系统，强调准确度验证与人工评估。
- 提供R和Python双语言实现及两个领域专用Web应用。
- 通过领域专家人工评估量化抽取可靠性，揭示分类和数学表达式等薄弱环节。

**当前局限**

> 属于说明性/应用性论文，未提出新模型或算法；评估规模有限（30份通知、45篇论文）；仅涉及两个应用领域；对数学表达式等复杂内容抽取效果不佳。

**工程启发**

> 为工业质量工程场景提供可落地的LLM/VLM结构化抽取方案和开源代码，降低实施门槛；强调人工验证流程，对生产部署有指导意义。

**为什么值得关注**

> 直接涉及文档结构化抽取（召回通知、论文元数据），与OCR后的信息抽取应用相关，且提供工程实践视角。

**原始摘要**

In this expository paper, we explain how quality engineers can use large language models (LLMs) and
vision-language models (VLMs) for structured data extraction. We introduce the relevant concepts,
discuss structured extraction from a measurement-system perspective, and demonstrate its
implementation in R and Python. We then present two freely available web-based applications (apps):
(a) extracting information from automotive recall notices and (b) monitoring quality engineering
research on arXiv. To ensure the accuracy of our AI-driven structured extraction, human evaluators
validated the results. In the first app, four reviewers assessed information extracted from 30
recall notices using two models, with 98.6% of the 720 field-level ratings judged fully correct. In
the second app, 21 authors evaluated information extracted from 45 of their arXiv papers. All paper
summaries were rated mostly correct or correct, although the evaluations identified problems with
some classification fields and mathematical expressions. These results demonstrate the practical
potential of structured data extraction while emphasizing the need to validate the extracted
information. We make both apps and their source code publicly available so that readers can adapt
the approach to their own applications.

---
