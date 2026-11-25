# OCR / 文档解析研究日报（2026-11-25）

## 报告说明

- 检索源：arXiv API
- 检索查询：`(all:"document parsing" OR all:"document understanding" OR all:"optical character recognition" OR all:OCR OR all:"layout analysis" OR all:"document layout analysis" OR all:"text recognition" OR all:"table recognition" OR all:"form understanding" OR all:"document intelligence" OR all:"page understanding" OR all:"scene text recognition" OR all:"handwritten text recognition" OR all:"information extraction") AND (cat:cs.CV OR cat:cs.AI OR cat:cs.CL OR cat:eess.IV)`
- 生成时间（UTC）：`2026-11-25 09:49:43`
- 大模型综合分析：`开启`

## 一、今日执行摘要

> 今日论文呈现三条主线：一是紧凑视觉语言识别器通过数据引擎与并行解码实现高精度高通量文档解析，在表格、公式任务上超过大规模通用模型；二是OCR任务边界向意图消解、科学图表数值恢复、退化图像增强等场景延伸，强调对真实世界噪声与人工批注的语义理解；三是多模态MoE可解释性研究表明视觉专属专家并非必要，OCR是唯一依赖图像位置专家的能力，对模型压缩与路由设计有直接提示。低资源文字与手写场景仍受限于专用符号与标注成本。

## 二、今日趋势判断

文档解析正从通用文本识别转向面向真实场景的任务细分：意图感知、图表数值重建、混合退化增强和低资源铭文数字化并行推进。小型专用模型配合可靠监督数据与无损并行解码，在特定基准上已可比肩大规模通用模型，部署性价比成为关注点。同时，多模态MoE损伤实验提示参数效率不等于能力必要性，为模型压缩提供新证据。

## 三、今日论文概览

1. **VenusOCR2.0: Towards Efficient and Effective Document Parsing** | 标签：文档解析、视觉语言模型、表格识别、公式识别、并行解码、推理加速、数据引擎
2. **When Ink Meets Pixel: Intent-Aware OCR with VLMs for Human-Corrected Financial Documents When Ink Meets Pixel: Intent-Aware OCR with VLMs for Human-Corrected Financial Documents** | 标签：意图感知OCR、文档理解、视觉语言模型、金融文档、数据集与基准、人机回路
3. **Trallie: from Free-Form Text to Structured Data with LLMs** | 标签：信息抽取、大语言模型、零样本/少样本、模式归纳、文档结构化
4. **Towards an Armenian Epigraphic Corpus** | 标签：古籍数字化、版面检测、OCR、视觉语言模型、低资源文字、专家校对
5. **ArEssays: Towards Robust Arabic Handwritten Text Understanding in Educational Settings** | 标签：阿拉伯语OCR、手写识别、教育NLP、数据集与基准、视觉语言模型
6. **SciFig2Data: A Workflow for Recovering Structured Data from Scientific Figures** | 标签：科学图表解析、OCR、多模态大模型、版面分析、文献数据挖掘、信息抽取
7. **DocPristine: Content-Aware Document Appearance Enhancement under Real-World Mixed Degradations** | 标签：文档增强、混合退化、内容感知、文档解析、预训练视觉编码器
8. **Lit Up but Not Needed: Scoped Lesions Show Where Multimodal Mixture-of-Experts Depend on Their Experts** | 标签：混合专家、多模态大模型、损伤实验、模型可解释性、OCR依赖
9. **Interactive Neural Computers** | 标签：世界模型、交互式生成、屏幕文本OCR、记忆网络、神经图灵机
10. **DexOPD: Dual-Extrapolation On-Policy Distillation for Diffusion Models** | 标签：扩散模型、在线策略蒸馏、多教师蒸馏、OCR生成、模型融合
11. **What Quality Engineers Need to Know About Generative AI: Structured Data Extraction** | 标签：结构化数据提取、视觉语言模型、质量工程、文档信息抽取、人工验证

## 四、今天 OCR / 文档解析论文里的主要创新点

- 以冻结预训练视觉编码器提供内容或弱点引导信号，降低对人工标注的依赖。
- 将OCR与视觉语言模型串联为多阶段流水线，并通过专家校对或人工核验形成闭环。
- 针对特定领域构建配套数据集与基准，覆盖真实退化、手写变体或人工批注等噪声条件。
- 采用轻量并行解码或残差渲染模块，在保持输出等价的前提下提升推理吞吐。

## 五、后续 OCR 领域值得推进的改进方向

- 在意图感知OCR中引入重叠与冲突批注的置信度估计，并将意图消解与阅读顺序联合建模。
- 将无损并行草稿解码机制移植到其他自回归文档解析模型，验证跨架构加速的通用性与等价性。
- 针对编辑符号、数学表达式和分类字段等高频错误类型构建符号级后处理与专用识别模型。
- 建立科学图表数值重建的定量评测协议，并用OCR与多模态大模型结果交叉验证降低抽取错误。
- 把文档增强作为OCR前置模块，与版面分析和解析器联合优化，量化增强对下游任务的实际增益。
- 基于MoE损伤实验结论设计专家剪枝与路由策略，优先保护文本位置的双用途专家和图像文本阅读能力。
- 在低资源语言、手写与扫描文档上系统评估递归自我改进数据引擎的可迁移性和标注成本。

## 六、工程落地启发

- 1B级专用文档解析模型配合单卡vLLM部署可实现约3倍单请求加速和2.36倍批量吞吐，适合高吞吐流水线优先选型。
- 自动模式归纳的零样本信息抽取框架需前置OCR与版面解析模块，才能覆盖扫描文档和复杂表格。
- 结构化抽取落地必须保留人工核验环节，实测字段级准确率虽高，但分类字段和数学表达式仍易出错。
- 简单按路由频率剪枝多模态MoE专家可能无效，应关注文本位置双用途专家和图像文本阅读路径。
- 文档增强方法可复用冻结文档视觉编码器的多层特征作为引导，降低对退化输入视觉线索的依赖。

## 七、优先关注论文

- **VenusOCR2.0: Towards Efficient and Effective Document Parsing**：紧凑模型在公式与表格基准上超过大规模通用模型且解码无损加速，其RSI数据引擎与PTPv2并行草稿机制值得跟踪复现。
- **When Ink Meets Pixel: Intent-Aware OCR with VLMs for Human-Corrected Financial Documents**：意图感知OCR定义了新任务边界，DocIntent数据集与IntentBench可检验小模型在批注消解上的上限。
- **Lit Up but Not Needed: Scoped Lesions Show Where Multimodal Mixture-of-Experts Depend on Their Experts**：损伤实验结论直接挑战按激活频率剪枝的直觉，OCR是唯一跨模型依赖图像位置专家的能力，对MoE压缩有指导意义。
- **DocPristine: Content-Aware Document Appearance Enhancement under Real-World Mixed Degradations**：提供带解析标注的真实混合退化测试集与内容感知增强框架，可作为移动扫描OCR前处理的评估基准。
- **SciFig2Data: A Workflow for Recovering Structured Data from Scientific Figures**：模块化流水线便于替换组件，但缺少重建精度报告，需跟踪其定量评测与人工校验协议的补充。

## 八、论文逐篇解析

### 1. VenusOCR2.0: Towards Efficient and Effective Document Parsing

- arXiv: [2611.32617v1](https://arxiv.org/abs/2611.32617v1)
- PDF: [下载链接](https://arxiv.org/pdf/2611.32617v1)
- 作者: Lei Li, Zheng Wei, Yi Yuan, Qingbin Liu, Jiang Bian, Zang Li
- 发布时间: 2026-11-24T13:46:00Z
- 分类: cs.CV
- 相关性评分: 21
- 主题标签: 文档解析、视觉语言模型、表格识别、公式识别、并行解码、推理加速、数据引擎

**中文摘要**

> 该文提出VenusOCR2.0，一个1B参数的紧凑视觉语言识别器，面向文本、表格与公式的高精度、高通量文档解析。为在避免自训练崩溃的前提下持续提升识别质量，构建了有界递归自我改进（RSI）数据引擎，模型仅作为弱点探测工具，由外部多专家medoid共识、VLM视觉核验与因子化合成提供可靠监督，覆盖预训练、精调SFT与RLVR。模型采用动态分辨率SigLIP2编码器、2x2空间token合并与Qwen3-0.6B解码器，并使用紧凑原子OTSL token缩短表格序列。为消除自回归解码瓶颈，引入PTPv2轻量解耦并行草稿模块（约67M），结合冻结多层验证器条件、独立学习掩码与块因果全位置预测。在OmniDocBenchv1.6上总分96.45，公式CDM达98.57，超过Gemini-3-Pro与Qwen3-VL-235B；单张H20部署vLLM，单请求加速2.96倍、批量吞吐提升至2.36倍，且与标准自回归解码逐token无损等价。

**核心创新概述**

> 将弱点探测式递归自我改进数据引擎与轻量解耦并行草稿解码结合，在紧凑参数规模下实现高精度文档解析并保持解码无损加速。

**创新点拆解**

- 有界递归自我改进数据引擎：模型仅作弱点探测器，由多专家medoid共识、VLM视觉核验与因子化合成构成可靠监督闭环
- 紧凑原子OTSL表格token表示，显著缩短表格序列并降低结构错误
- PTPv2解耦并行草稿模块：冻结多层验证器条件、独立学习掩码与块因果全位置下一token预测，实现无损并行解码
- 动态分辨率SigLIP2编码器与2x2空间token合并的紧凑VLM架构

**当前局限**

> 摘要未报告除OmniDocBench外的多场景泛化评测，也未说明RSI数据引擎对多专家标注与VLM核验的依赖成本及在低资源语言文档上的表现。

**后续可改进方向**

- 在更多语言、手写与低质量扫描文档上验证RSI数据引擎与OTSL表示的泛化性
- 量化多专家共识与VLM核验的标注成本，探索更低成本的可信监督替代方案
- 将PTPv2并行草稿机制扩展到其他自回归文档解析模型，评估无损加速的通用性
- 结合版面结构与阅读顺序建模，进一步降低复杂多栏、跨页表格的结构错误

**工程启发**

> 1B参数模型在单张H20上实现约3倍单请求加速与2.36倍批量吞吐且无损等价，具备较高部署性价比，适合高吞吐文档解析流水线落地。

**为什么值得关注**

> 直接面向OCR文档解析的效率与精度权衡，涵盖表格/公式结构化输出与推理加速，是OCR日报核心方向的代表性工作。

**原始摘要**

We present VenusOCR2.0, a compact 1B-parameter vision-language recognizer designed for both high-
accuracy and high-throughput document parsing across text, tables, and formulas. To continuously
improve recognition quality without self-training collapse, we build a bounded recursive self-
improvement (RSI) data engine where the model acts strictly as a weakness probe, while external
multi-expert medoid consensus, VLM visual verification, and factorized synthesis supply reliable
supervision across pretraining, curated SFT, and RLVR. VenusOCR2.0 couples a dynamic-resolution
SigLIP2 encoder and 2x2 spatial token merging with a Qwen3-0.6B decoder, adopting compact atomic
OTSL tokens to shorten table sequences and reduce structural errors. To further eliminate the
autoregressive decoding bottleneck, we introduce PTPv2, a lightweight ($\sim$67M) decoupled parallel
draft module that combines frozen multi-layer verifier conditioning, a standalone learned mask, and
block-causal all-position next-token prediction. On OmniDocBenchv1.6, VenusOCR2.0 achieves an
overall score of 96.45 and a state-of-the-art 98.57 formula CDM, substantially outperforming massive
general-purpose VLMs such as Gemini-3-Pro (92.91) and Qwen3-VL-235B (89.78). Deployed in vLLM on a
single H20 GPU, PTPv2 delivers a 2.96x single-request speedup and up to 2.36x higher batched
throughput while guaranteeing lossless, token-for-token equivalence with standard autoregressive
decoding.

---

### 2. When Ink Meets Pixel: Intent-Aware OCR with VLMs for Human-Corrected Financial Documents When Ink Meets Pixel: Intent-Aware OCR with VLMs for Human-Corrected Financial Documents

- arXiv: [2611.32446v1](https://arxiv.org/abs/2611.32446v1)
- PDF: [下载链接](https://arxiv.org/pdf/2611.32446v1)
- 作者: Akshata A Bhat, Daman Deep Singh, Niyati Chhaya
- 发布时间: 2026-11-24T11:43:26Z
- 分类: cs.CL
- 相关性评分: 19
- 主题标签: 意图感知OCR、文档理解、视觉语言模型、金融文档、数据集与基准、人机回路

**中文摘要**

> 该文提出意图感知OCR新任务：在文档原始内容基础上联合推理手写或数字标注所表达的编辑意图（箭头、插入符、删除线、插入文字等），生成经修正的转写结果。现有OCR与文档理解系统将这些标注视为视觉噪声。作者构建DocIntent数据集，含1600份金融文档、5700余处视觉意图标注及版面感知的意图消解OCR目标，并发布216文档的IntentBench基准。基于DocIntent微调3B与7B的DocIntentOCR模型，在IntentBench上F1分别为0.81和0.83，显著优于GPT-4.1（0.626）与LLaMA-3.2-Vision-90B（0.50）。

**核心创新概述**

> 首次将人工批注定义为一类需要消解的语义编辑操作，提出意图感知OCR任务及配套数据、基准与模型。

**创新点拆解**

- 任务定义创新：意图感知OCR，将视觉标注建模为编辑意图而非噪声
- 构建DocIntent多模态金融文档数据集，含版面感知的意图消解转写目标
- 发布IntentBench基准，覆盖多样真实批注条件
- 通过直接意图监督微调，使小参数模型在特定任务上超越大规模通用模型

**当前局限**

> 数据集中于金融文档领域，规模有限（1600份文档），意图类型与语言覆盖可能不足以代表通用文档场景；评测以F1为主，未充分讨论复杂重叠批注与意图歧义情形。

**后续可改进方向**

- 扩展到非金融领域与多语言文档，检验意图感知监督的迁移性
- 研究重叠、冲突或多轮批注的意图消解与置信度估计
- 探索众包或多模态大模型自动生成意图标注以降低数据构建成本
- 将意图消解与版面分析、阅读顺序联合建模，提升复杂版式下的修正准确性

**工程启发**

> 面向金融单据人工批改场景，提供可复现的数据、基准与模型，对表单修正、人工复核流程自动化有直接工程参考价值。

**为什么值得关注**

> 拓展OCR任务边界至人机回路的意图理解，属于文档理解与交互式处理的新方向，与OCR日报主题高度相关。

**原始摘要**

Human annotations on documents (such as arrows, carets, strikethroughs, and insertions) express
corrective intent yet existing OCR and document understanding systems treat these marks as visual
noise rather than semantic edit operations. We introduce intent-aware OCR, the task of generating
corrected transcriptions by jointly reasoning over original document content and visual intent cues
(handwritten or digital) that convey edit intent. To support this setting, we present DocIntent, a
multimodal dataset of 1,600 financial documents with over 5,700 annotated visual intent cues, each
paired with layout-aware, intent-resolved OCR targets. We further introduce IntentBench, a
216-document benchmark designed to evaluate model robustness under diverse real-world annotation
conditions. Leveraging DocIntent, we fine-tune DocIntentOCR, a suite of 3B and 7B parameter vision-
language models, under direct intent supervision on corrected transcriptions. On IntentBench, the
fine-tuned 3B and 7B models achieve F1-scores of 0.81 and 0.83, respectively, substantially
outperforming commercial closed-source (e.g., GPT-4.1 (0.626)), and open-source models (e.g.,
LLaMA-3.2-Vision-90B (0.50)) demonstrating that intent-aware supervision enables compact domain-
specific models to outperform substantially larger general-purpose systems on this task. This work
establishes intent-aware OCR as a novel human-in-the-loop document understanding task and provides
foundational resources (dataset, benchmark, models) to advance research in interactive document
processing.

---

### 3. Trallie: from Free-Form Text to Structured Data with LLMs

- arXiv: [2611.30773v1](https://arxiv.org/abs/2611.30773v1)
- PDF: [下载链接](https://arxiv.org/pdf/2611.30773v1)
- 作者: Vijayasri Iyer, Cristiano De Nobili, Mubashir Hussain Shah, Sébastien Bratières
- 发布时间: 2026-11-23T14:41:32Z
- 分类: cs.CL, cs.DB, cs.IR
- 相关性评分: 17
- 主题标签: 信息抽取、大语言模型、零样本/少样本、模式归纳、文档结构化

**中文摘要**

> Trallie是开源框架，利用大语言模型从自然语言来源中抽取信息，支持有或无用户指导的场景。其目标包括：借助提示式零样本/少样本降低人工标注、灵活解析HTML/PDF/TXT/JSON等格式、自动从文档集合归纳模式以降低非专家使用门槛。在FDA 510(k)文档与SWDE电影及大学网站数据上，使用开放权重LLM进行评估，在给定目标属性时优于此前系统，在需自动发现属性时具竞争力。

**核心创新概述**

> 以零/少样本提示替代领域训练，并将模式自动归纳与多格式解析整合为面向非专家的端到端信息抽取框架。

**创新点拆解**

- 无需大量标注或领域训练的信息抽取流程，依赖LLM提示式零样本与少样本能力
- 自动从文档集合归纳抽取模式并支持人工细化
- 统一支持HTML、PDF、TXT、JSON多格式输入

**当前局限**

> 依赖LLM的推理质量，自动模式归纳在属性发现场景仅具竞争力而非领先；未报告对扫描图像类PDF版面与表格复杂结构的处理能力。

**后续可改进方向**

- 将OCR与版面解析前置模块纳入框架，以覆盖扫描文档与复杂表格
- 研究模式归纳的自动评估与迭代精炼机制，提升属性发现阶段的稳定性
- 引入抽取置信度与人工核验回路，降低LLM幻觉对结构化输出的影响
- 在更多领域与多语言文档上系统评估零样本与少样本设置的边界

**工程启发**

> 开源、易集成，适合作为非专家用户的结构化信息抽取基线，但需依赖外部文档解析能力。

**为什么值得关注**

> 涉及PDF等文档到结构化数据的转换，与OCR下游信息抽取环节衔接紧密。

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

### 4. Towards an Armenian Epigraphic Corpus

- arXiv: [2611.30603v1](https://arxiv.org/abs/2611.30603v1)
- PDF: [下载链接](https://arxiv.org/pdf/2611.30603v1)
- 作者: Chahan Vidal-Gor{è}ne, Arpine Avetisyan, Edita Matevosyan, Seda Kirakosyan, Victoria Khurshudyan, Pollet Samvelian
- 发布时间: 2026-11-23T12:40:28Z
- 分类: cs.CV
- 相关性评分: 17
- 主题标签: 古籍数字化、版面检测、OCR、视觉语言模型、低资源文字、专家校对

**中文摘要**

> 亚美尼亚铭文缺乏类似希腊、拉丁、格鲁吉亚文的数字资源。该文构建Corpus Inscriptionum Armenicarum Electronicum，将十卷本Divan hay vimagrut'yan（约7600条记录）转为开放数字语料。流程包括版面检测、OCR与视觉语言模型生成初读结构，再由专家在校对平台核验。初步修正显示字母识别可靠，残余错误集中在编辑符号上。语料定位为长期铭文记录平台及古典与中古亚美尼亚语银数据来源。

**核心创新概述**

> 针对濒危、仅存于印刷本的亚美尼亚铭文，建立结合版面检测、OCR、VLM与专家校对的开放数字语料及流程。

**创新点拆解**

- 面向亚美尼亚铭文的端到端数字化流水线：版面检测、OCR、VLM初读与专家校对平台
- 将印刷铭文语料转为结构化开放数字资源，并作为古典/中古亚美尼亚语模型银数据

**当前局限**

> 错误集中在编辑符号识别，说明专用符号与标注语义仍是瓶颈；专家校对环节人力依赖明显，摘要未报告整体识别精度与校对吞吐数据。

**后续可改进方向**

- 针对编辑符号与特有用字构建专用识别模型或符号级后处理
- 研究专家校对反馈的主动学习闭环，降低人工核验成本
- 将铭文元数据与语言资源对齐，提升银数据对语言模型训练的可利用性

**工程启发**

> 提供低资源古籍/铭文数字化可复用流程，对文化遗产文档结构化具有参考价值。

**为什么值得关注**

> 属于版面检测、OCR与VLM结合的文献数字化实践，体现低资源文字OCR的真实落地难点。

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

### 5. ArEssays: Towards Robust Arabic Handwritten Text Understanding in Educational Settings

- arXiv: [2611.32211v1](https://arxiv.org/abs/2611.32211v1)
- PDF: [下载链接](https://arxiv.org/pdf/2611.32211v1)
- 作者: Hamdy Mubarak, Anas Madkoor, Ehsaneddin Asgari, Majd Hawasly
- 发布时间: 2026-11-24T08:55:56Z
- 分类: cs.CL, cs.CV
- 相关性评分: 15
- 主题标签: 阿拉伯语OCR、手写识别、教育NLP、数据集与基准、视觉语言模型

**中文摘要**

> 该文提出ArEssays，面向埃及小学至中学学生的真实阿拉伯语手写作文数据集，同时提供逐字转写与语言修正版本。作者基准测试34个视觉语言与OCR模型（含微调系统），发现真实学生手写上的性能差距显著，并开放数据、训练流程与结果，以推动阿拉伯语OCR、文档理解与教育NLP研究。

**核心创新概述**

> 构建覆盖低龄学生真实手写、同时提供逐字与规范化双转写的大规模阿拉伯语教育场景数据集，并系统基准评测34个模型。

**创新点拆解**

- 面向学生手写的高变异性阿拉伯语大规模真实数据集
- 逐字转写与语言修正双版本标注，支持不同下游任务
- 34个VLM/OCR模型的系统基准与微调流程公开

**当前局限**

> 摘要未披露数据集规模与标注一致性细节，评测集中于教育作文，未覆盖表格、公式等其他文档类型，也未讨论模型轻量化部署。

**后续可改进方向**

- 针对儿童手写变异性引入书写者自适应或个性化校准方法
- 结合语言模型纠错与逐字转写的联合建模，提升规范化输出质量
- 扩展至多方言、多学科手写材料并补充标注一致性分析
- 探索小参数模型在教育场景的可部署化微调策略

**工程启发**

> 为阿拉伯语手写教育场景提供数据与评测基线，可用于教育类文档理解系统的模型选型。

**为什么值得关注**

> 属于手写OCR与文档理解的基准与数据集建设，覆盖低资源语言真实场景。

**原始摘要**

Automated understanding of handwritten Arabic student essays remains challenging due to script
complexity and high variability in children's writing. We introduce ArEssays, a large-scale dataset
of authentic essays from primary to secondary students across Egypt, with both verbatim
transcriptions and linguistically corrected versions. We benchmark 34 vision-language and OCR
models, including fine-tuned systems, and find large performance gaps on real student handwriting.
We release the dataset, training pipelines, and results to support research in Arabic OCR, document
understanding, and educational NLP.

---

### 6. SciFig2Data: A Workflow for Recovering Structured Data from Scientific Figures

- arXiv: [2611.31787v1](https://arxiv.org/abs/2611.31787v1)
- PDF: [下载链接](https://arxiv.org/pdf/2611.31787v1)
- 作者: Xinhe Wu, Yicheng Ye, Yadong Jin
- 发布时间: 2026-11-24T01:41:00Z
- 分类: cs.AI
- 相关性评分: 15
- 主题标签: 科学图表解析、OCR、多模态大模型、版面分析、文献数据挖掘、信息抽取

**中文摘要**

> 该文提出SciFig2Data自动化高吞吐工作流，从科学PDF中恢复图表内嵌的测量数据。流程整合多尺度文档元素检测、自适应复合图分解、两阶段基于OCR的语义过滤、Swin图表分类与指令引导的多模态大模型重建，并支持目录级批处理、缓存与结构化日志。在两个生物医学语料（605篇毒理学与药理学文章、551篇脂质纳米颗粒文章）上分别重建468与242个表格化输出，并将重建测量与图注元数据关联，服务AI4Science下游应用。

**核心创新概述**

> 将图表定位、面板分解、OCR语义过滤、图表分类与MLLM数值重建串成文献规模的数据采集工作流，并关联实验上下文。

**创新点拆解**

- 端到端多阶段科学图表数据恢复流水线，支持目录级批处理与缓存
- 两阶段OCR语义过滤与Swin图表分类结合，控制无效图表处理成本
- 利用指令引导MLLM重建数值，并将测量与图注实验元数据对齐

**当前局限**

> 重建输出数量相对语料规模偏低，未报告重建精度与人工核验比例；对复杂多元图表与重叠面板的鲁棒性缺乏量化评估。

**后续可改进方向**

- 建立图表数值重建的定量评测指标与人工校验协议
- 增强复合图分解与多系列图表、误差棒等复杂元素的解析能力
- 将OCR与MLLM重建结果进行一致性交叉验证，降低数值抽取错误
- 扩展至更多学科与图类型，并评估流水线吞吐与失败的分类归因

**工程启发**

> 适合大规模科学文献图表数据挖掘的工程化流水线，模块划分清晰，便于增量替换与部署。

**为什么值得关注**

> 融合OCR、版面检测与多模态模型进行科学图表结构化抽取，属OCR下游高价值应用方向。

**原始摘要**

Scientific measurements reported in scholarly articles are often embedded in compound figures rather
than available as machine-readable data. Recovering these measurements at literature scale requires
an integrated workflow for figure localization, panel decomposition, chart identification, numerical
reconstruction, and experimental context association. We present \textit{SciFig2Data}, an automated,
high-throughput workflow for harvesting structured experimental data from scientific PDF
repositories. The system integrates multi-scale document element detection, adaptive compound figure
decomposition, two-stage OCR-based semantic filtering, Swin-based chart classification, and
instruction-guided multimodal large language model (MLLM) reconstruction. It further incorporates
directory-level batch execution, caching, and structured logging to support large-scale processing.
We demonstrate the workflow on two biomedical literature corpora comprising 605 toxicology and
pharmacology articles and 551 lipid nanoparticle (LNP) articles. The pipeline successfully
reconstructed 468 and 242 tabular outputs from the respective corpora, illustrating its practical
applicability to literature-scale scientific data harvesting. By associating reconstructed
measurements with caption-derived experimental metadata, SciFig2Data provides a workflow for
transforming graphical evidence in scholarly publications into structured, context-enriched data
records for downstream AI4Science applications.

---

### 7. DocPristine: Content-Aware Document Appearance Enhancement under Real-World Mixed Degradations

- arXiv: [2611.32176v1](https://arxiv.org/abs/2611.32176v1)
- PDF: [下载链接](https://arxiv.org/pdf/2611.32176v1)
- 作者: Zihan Huang, Junle Liu, Zhonghao Ye, Yuyi Zhang, Peirong Zhang, Hanlin Li, Yongxin Shi, Lianwen Jin
- 发布时间: 2026-11-24T08:29:21Z
- 分类: cs.CV, cs.AI
- 相关性评分: 9
- 主题标签: 文档增强、混合退化、内容感知、文档解析、预训练视觉编码器

**中文摘要**

> 针对摄像头拍摄文档常出现的混合退化（高光、阴影、模糊）问题，论文提出DocPristine方法。该方法发现预训练文档视觉编码器在退化文档上仍能关注文本区域，提供内容感知引导。为此，DocPristine自适应融合冻结文档视觉编码器的多层特征，并将其注入像素恢复网络，结合自适应多层特征融合（AMFF）、分层门控条件化（HGC）和移位窗口交叉注意力（SWCA）来恢复细粒度文本细节。同时发布了DocACE数据集，包含合成混合退化训练集和真实世界测试集（含人工修复的真值图像和解析标注）。在三个基准上的实验表明，该方法在视觉增强质量和下游文档解析任务上均达到最先进水平。

**核心创新概述**

> 首次利用预训练文档视觉编码器在退化文档上的内容感知注意力作为引导信号，并设计多模块融合机制将多层特征注入像素恢复网络，同时构建了包含真实世界混合退化测试集的新基准。

**创新点拆解**

- 利用冻结的预训练文档视觉编码器的多层特征作为内容感知引导，避免了依赖不可靠的输入视觉线索或缺乏空间指导的LLM诊断。
- 提出自适应多层特征融合（AMFF）与分层门控条件化（HGC），实现编码器特征与像素恢复网络的高效融合。
- 设计移位窗口交叉注意力（SWCA），利用跨窗口边界的结构线索恢复细粒度文本细节。
- 构建DocACE数据集，包含合成混合退化训练集和带人工修复真值与解析标注的真实世界测试集。

**当前局限**

> 方法依赖预训练文档视觉编码器的质量，在极端退化下编码器注意力可能失效；合成训练集与真实退化的分布差异可能影响泛化；未讨论计算开销和实时性。

**工程启发**

> 为摄像头文档增强提供了可落地的内容感知引导框架和公开数据集，有助于提升移动扫描、文档数字化等场景下的OCR前处理质量。

**为什么值得关注**

> 论文直接针对文档外观增强，并明确验证了对下游文档解析（OCR）的提升，与OCR研究高度相关。

**原始摘要**

Camera-captured documents often exhibit mixed degradations, such as highlights, shadows, and blur,
that distort backgrounds and obscure text details. Document appearance enhancement (DAE) aims to
mitigate these degradations and improve readability. Existing document appearance enhancement
methods rely either on input-derived visual cues that can become unreliable under severe degradation
or on LLM-based degradation diagnosis that lacks spatial guidance. Notably, we find that pretrained
document visual encoders continue to attend to text regions in degraded documents, providing
content-aware guidance. Based on this insight, we propose DocPristine, which adaptively fuses multi-
layer features from a frozen document visual encoder and injects them into a pixel restoration
network. To integrate these features into a pixel restoration network, DocPristine combines Adaptive
Multi-Layer Feature Fusion (AMFF), Hierarchical Gated Conditioning (HGC), and Shifted-Window Cross-
Attention (SWCA). Specifically, SWCA draws on structural cues from neighboring locations across
window boundaries to recover fine text details.We also introduce DocACE, with a synthetic mixed-
degradation training set (DocACE-Synthetic) and a real-world test set (DocACE-Real) containing
manually restored ground-truth images and document parsing annotations. Comprehensive experiments
across three benchmarks demonstrate that DocPristine achieves state-of-the-art appearance
enhancement quality and consistently improves downstream document parsing. Code, models, and data
will be publicly available.

---

### 8. Lit Up but Not Needed: Scoped Lesions Show Where Multimodal Mixture-of-Experts Depend on Their Experts

- arXiv: [2611.31576v1](https://arxiv.org/abs/2611.31576v1)
- PDF: [下载链接](https://arxiv.org/pdf/2611.31576v1)
- 作者: Zhixuan Ge, Anqi Li, Kexin Geng, Wei Qiu
- 发布时间: 2026-11-23T21:16:44Z
- 分类: cs.CV
- 相关性评分: 9
- 主题标签: 混合专家、多模态大模型、损伤实验、模型可解释性、OCR依赖

**中文摘要**

> 论文借鉴认知神经科学中“激活图不等于必要性地图”的观点，通过“损伤”实验探究多模态混合专家（MoE）视觉语言模型对专家的依赖。在Qwen3-VL-30B-A3B、Kimi-VL-A3B和Gemma-4-26B-A4B中，发现3%至12%的专家为视觉专属（图像token路由至其的频率高达均匀率的五倍，文本token几乎不路由）。在Qwen3-VL中，这些专家接收四分之一图像token路由，但损伤全部视觉专属专家在八个感知基准和自由形式OCR上平均损失不到1个百分点，与损伤同规模随机专家集相当。局部损伤（仅在图像位置或文本位置移除专家集）显示，模型对专家的依赖主要位于文本位置的双用途专家；图像侧依赖在Qwen3-VL和Kimi-VL中为2至3点，在Gemma-4中为26点。图像中的文本阅读是唯一在每个模型中都需要图像位置专家的能力。视觉专属专家接收信息丰富的图像块，输出规模正常，且在感觉剥夺下保持惰性。

**核心创新概述**

> 首次将损伤实验范式系统性地引入多模态MoE模型分析，区分了专家激活与必要性，揭示了视觉专属专家并非关键、而文本位置双用途专家才是依赖核心的反直觉结论。

**创新点拆解**

- 提出“局部损伤”方法，仅在图像或文本位置移除专家集，以定位模态特异性依赖。
- 发现视觉专属专家虽然激活频繁，但损伤后性能损失与随机损伤相当，表明其非必要性。
- 揭示图像侧依赖主要来自文本位置的双用途专家，且OCR是唯一在所有模型中都需要图像位置专家的能力。
- 系统评估三个主流多模态MoE模型，提供跨模型比较证据。

**当前局限**

> 损伤实验仅覆盖有限模型和基准，结论的普适性需进一步验证；未深入分析视觉专属专家的功能角色；局部损伤可能引入分布偏移。

**工程启发**

> 为多模态MoE模型的专家剪枝、路由优化和高效推理提供实证依据，指出简单依据路由频率剪枝可能无效，需关注文本位置的双用途专家。

**为什么值得关注**

> 论文涉及OCR任务（自由形式OCR）作为评估基准，并揭示OCR对图像位置专家的特殊依赖，对OCR模型设计与压缩有参考价值。

**原始摘要**

Cognitive neuroscience learned that an activation map is not a map of necessity. Regions that light
up during a task are not always needed for it, and only lesions reveal which ones are. Mixture-of-
experts (MoE) vision-language models come with an activation map for free, since the router records
which experts respond to image and text tokens, and recent work reads modality-specialized experts
off this map. We bring the lesion. In Qwen3-VL-30B-A3B, Kimi-VL-A3B and Gemma-4-26B-A4B, 3 to 12% of
the experts are vision-exclusive: image tokens route to them at up to five times the uniform rate
and text tokens almost never. In Qwen3-VL they receive a quarter of all image-token routing, and
lesioning all of them costs less than one percentage point on average over eight perception
benchmarks and free-form OCR, no more than lesioning a random set of the same size. In Kimi-VL and
Gemma-4 the lesion also costs no more than a random set. Scoped lesions, which remove an expert set
only at image positions or only at text positions, then show where the models do depend on their
experts. In Qwen3-VL, silencing every expert at every image position costs 3 points, against 45 at
text positions, where the dependence sits in dual-use experts that text-only tasks need as well.
Across models the image-side dependence is 2 to 3 points in Qwen3-VL and Kimi-VL and 26 in Gemma-4.
Reading text in images is the one ability that needs image-position experts in every model. The
exclusive experts receive informative patches, produce outputs of ordinary size, and stay inert
under sensory deprivation: text-only training recruits them only when load balancing forces it. In
Kimi-VL the balancing bias itself manufactures most of them. Load balancing draws the modality map
in the part of the computation the models depend on least. Expert selection, pruning and skipping
should follow the lesion, not the map.

---

### 9. Interactive Neural Computers

- arXiv: [2611.32811v1](https://arxiv.org/abs/2611.32811v1)
- PDF: [下载链接](https://arxiv.org/pdf/2611.32811v1)
- 作者: Ross Murphy, Marcel Hedman, Gabriel Brostow
- 发布时间: 2026-11-24T15:30:05Z
- 分类: cs.AI, cs.NE, cs.SC
- 相关性评分: 6
- 主题标签: 世界模型、交互式生成、屏幕文本OCR、记忆网络、神经图灵机

**中文摘要**

> 论文提出“交互式神经计算机”（Interactive Neural Computer），将桌面环境视为交互式世界模型，通过生成模型根据历史屏幕和用户鼠标键盘动作预测下一屏幕。为解决无相机位姿下的记忆、精确算术和界面小文本可读性问题，模型采用类神经图灵机结构，包含三个端到端模块：由MEMORY-JEPA监督的惊喜门控槽记忆存储屏幕外内容；探索性查询桥引入预训练VLM的推理；残差渲染器仅预测帧间的潜在变化。在长闭环滚动中，模型以64.2%的召回率回忆被遮挡文件（随机为33.3%），优于循环和滑动窗口基线（最高56.0%），并将终端文本OCR准确率从1.3%提升至50.1%。

**核心创新概述**

> 将桌面计算环境建模为可交互的生成式世界模型，而非训练智能体操作现有计算机，并针对无几何线索的记忆、精确文本渲染和交互帧率等挑战提出结构化解决方案。

**创新点拆解**

- 提出交互式神经计算机范式，用生成模型直接预测屏幕演化，替代传统智能体操作固定界面。
- 设计惊喜门控槽记忆（MEMORY-JEPA监督），在无相机位姿下存储屏幕外内容。
- 引入探索性查询桥，融合预训练VLM的推理能力。
- 采用残差渲染器仅预测潜在变化，提升交互帧率下的文本可读性。

**当前局限**

> 模型在复杂界面和精确算术任务上可能仍有误差；长时程记忆召回率（64.2%）仍有限；计算成本较高，交互帧率下的实时性未充分讨论。

**工程启发**

> 为无障碍交互、自动化测试和新型人机接口提供了可生成、可定制的计算机界面范式，其中提升小文本OCR可读性的方法对屏幕内容识别有借鉴意义。

**为什么值得关注**

> 论文涉及界面小文本的OCR准确率提升（从1.3%到50.1%），与OCR在交互式环境中的应用直接相关。

**原始摘要**

Computers and their interfaces are usually treated as fixed, so a person, or increasingly an AI
agent, must adapt to whatever the operating system presents. This is limiting when someone needs a
different workflow, or an interface suited to hands-free use or a disability. We explore an
overlooked alternative. Rather than training an agent to operate an existing computer, we train a
generative model to be the computer, predicting each next screen from past screens and the user's
mouse and keyboard actions. Treating a desktop as an interactive world model raises problems that
natural-video world models largely avoid. Without a camera pose to index memory, the model must
remember content that has left the screen without any geometric cues. Arithmetic in a terminal has
to be exactly right, not merely plausible. Small interface text must also stay legible at
interactive frame rates. Our Interactive Neural Computer is structured like a Neural Turing Machine
and starts to address these problems with three modules trained end to end from pixels and actions.
A surprise-gated slot memory, supervised by latent next-frame prediction (MEMORY-JEPA), stores what
is off screen. An exploratory query bridge brings in the reasoning of a pretrained VLM, and a
residual renderer predicts only the latent changes between frames. In long closed-loop rollouts, our
model recalls occluded files in 64.2% of trials (chance is 33.3%), compared with at most 56.0% for
recurrent and sliding-window baselines. It also raises terminal-text OCR accuracy from 1.3% to
50.1%. Finally, because the memory is explicit, it can be transplanted at test time to causally
change what the model renders.

---

### 10. DexOPD: Dual-Extrapolation On-Policy Distillation for Diffusion Models

- arXiv: [2611.31969v1](https://arxiv.org/abs/2611.31969v1)
- PDF: [下载链接](https://arxiv.org/pdf/2611.31969v1)
- 作者: Yunchao Ke, Yanzhe Hu, Yi Yang, Jiachun Jin, Zhihong Liu, Zhijie Deng
- 发布时间: 2026-11-24T05:19:50Z
- 分类: cs.AI
- 相关性评分: 6
- 主题标签: 扩散模型、在线策略蒸馏、多教师蒸馏、OCR生成、模型融合

**中文摘要**

> 论文提出DexOPD，一种用于扩散模型的双外推在线策略蒸馏方法。现有多教师在线策略蒸馏通过教师外推构建更强代理教师，但外推方向仅由冻结教师和参考模型定义，未利用学生自身训练进展。DexOPD在保留外推教师监督的同时，利用滞后的历史学生作为参考进行学生自外推，通过共享初始噪声的多自外推增益采样扩大探索，并将任务奖励转化为归一化辅助回归方向。在GenEval、OCR和DrawBench上，统一学生模型SD3.5-Medium分别达到0.9736、0.9515和6.4875的美学分数，超越专家教师及所有评估的OPD和多任务强化学习基线，同时保持单模型推理。

**核心创新概述**

> 首次将学生自身历史模型引入外推参考，形成教师侧与学生侧的双外推机制，使蒸馏过程能利用学生训练轨迹的动态信息。

**创新点拆解**

- 提出双外推在线策略蒸馏框架，同时进行教师外推和学生自外推。
- 利用滞后历史学生作为自外推参考，并基于共享初始噪声采样多个增益以扩大探索。
- 将任务奖励转化为归一化辅助回归方向，指导候选质量差异的学习。
- 在OCR等任务上验证统一学生模型可超越专家教师。

**当前局限**

> 方法依赖多教师专家模型的存在；自外推的参考更新策略和增益选择需调参；在更复杂或低资源任务上的泛化性未充分验证。

**工程启发**

> 为扩散模型的多任务能力融合提供了高效蒸馏方案，可应用于需要统一模型同时处理生成和OCR相关任务的场景，降低部署多个专家模型的成本。

**为什么值得关注**

> 论文在OCR基准上评估蒸馏后模型的性能，表明方法对OCR相关生成任务有效，与OCR研究中的模型压缩和多任务学习相关。

**原始摘要**

Flow-based diffusion models have become a mainstream paradigm for text-to-image generation, where
task-specific post-training produces specialist models with complementary strengths. Multi-teacher
on-policy distillation (OPD) offers an efficient way to consolidate these specialists into a single
unified student. Recent methods strengthen supervision through teacher extrapolation, constructing
stronger proxy teachers that allow distilled students to surpass the original specialists. However,
their extrapolation directions remain defined solely by frozen teacher and reference models, leaving
the student's own training progress unexploited. To address this limitation, we introduce DexOPD, a
dual-extrapolation on-policy distillation method for diffusion models. DexOPD retains extrapolated
teacher supervision while leveraging a lagging historical student as the reference for student self-
extrapolation. Sampling across multiple self-extrapolation gains from shared initial noise broadens
exploration along the student's evolving trajectory, and task rewards convert pairwise differences
in candidate quality into a normalized auxiliary regression direction. Empirically, we evaluate
DexOPD on GenEval, OCR, and DrawBench. The resulting unified SD3.5-Medium student achieves a GenEval
reward of 0.9736, an OCR score of 0.9515, and a DrawBench Aesthetic score of 6.4875, surpassing the
corresponding specialist teachers as well as all evaluated OPD and multi-task reinforcement learning
baselines across these three benchmarks while preserving standard single-model inference.

---

### 11. What Quality Engineers Need to Know About Generative AI: Structured Data Extraction

- arXiv: [2611.30778v1](https://arxiv.org/abs/2611.30778v1)
- PDF: [下载链接](https://arxiv.org/pdf/2611.30778v1)
- 作者: Fadel M. Megahed, Ying-Ju Chen, Yamin Dahwich, Zhao-Wei Chen, Lucas K. Hung, Arthur Carvalho, L. Allison Jones-Farmer, Ibrahim Yousif, Inez M. Zwetsloot
- 发布时间: 2026-11-23T14:44:59Z
- 分类: cs.CE, cs.CL
- 相关性评分: 3
- 主题标签: 结构化数据提取、视觉语言模型、质量工程、文档信息抽取、人工验证

**中文摘要**

> 这是一篇面向质量工程师的说明性论文，介绍如何利用大语言模型（LLM）和视觉语言模型（VLM）进行结构化数据提取。论文从测量系统视角讨论结构化提取，并给出R和Python实现，同时展示两个免费网络应用：从汽车召回通知中提取信息，以及监控arXiv上的质量工程研究。人工评估验证了提取准确性：第一个应用中，四位评审者对30份召回通知的720个字段级评分中98.6%完全正确；第二个应用中，21位作者评估了45篇论文的提取信息，摘要大多被评为基本正确或正确，但分类字段和数学表达式存在一些问题。论文强调验证提取信息的必要性，并公开应用和源代码。

**核心创新概述**

> 从质量工程的测量系统视角系统阐述LLM/VLM结构化数据提取，并提供可复用的开源应用和人工验证结果，强调验证环节的重要性。

**创新点拆解**

- 将结构化数据提取视为测量系统，引入质量工程中的验证理念。
- 提供两个可公开访问的Web应用及R/Python实现，便于领域人员适配。
- 通过人工评估量化提取准确性，并识别分类字段和数学表达式等薄弱环节。

**当前局限**

> 评估规模有限（30份通知、45篇论文），未覆盖多样文档类型；数学表达式和分类字段的提取问题未给出针对性解决方案；主要面向质量工程领域。

**工程启发**

> 为质量工程及更广泛领域的结构化信息提取提供了可操作的工具和验证框架，降低了LLM/VLM应用门槛，并强调人工验证在工程落地中的必要性。

**为什么值得关注**

> 论文涉及使用VLM进行文档信息提取（如召回通知和论文），与OCR后的结构化信息抽取任务直接相关，并讨论了提取准确性问题。

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
