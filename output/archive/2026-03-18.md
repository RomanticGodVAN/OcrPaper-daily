# OCR / 文档解析研究日报（2026-03-18）

## 报告说明

- 检索源：arXiv API
- 检索查询：`(all:"document parsing" OR all:"document understanding" OR all:"optical character recognition" OR all:OCR OR all:"layout analysis" OR all:"document layout analysis" OR all:"text recognition" OR all:"table recognition" OR all:"form understanding" OR all:"document intelligence" OR all:"page understanding" OR all:"scene text recognition" OR all:"handwritten text recognition" OR all:"information extraction") AND (cat:cs.CV OR cat:cs.AI OR cat:cs.CL OR cat:eess.IV)`
- 生成时间（UTC）：`2026-03-18 03:50:19`
- 大模型综合分析：`开启`

## 一、今日执行摘要

> 今日论文聚焦于OCR和文档解析领域的多语言基准、效率优化、多模态应用、文本渲染准确性和跨模态学习。SEA-Vision基准填补了东南亚多语言评估的空白，强调低资源语言性能差距。并行令牌预测方法提升解码速度，适用于实时应用。KidsNanny架构展示高效多模态内容审核的潜力。GlyphPrinter通过区域偏好优化提高字形准确性。跨模态学习为减少标注需求提供新思路。整体趋势表明，研究正从单一任务转向综合多语言、多模态和效率驱动方案，工程价值普遍较高，推动实际部署。

## 二、今日趋势判断

当前研究趋势包括：1) 多语言和低资源语言关注度上升，通过基准和数据集构建推动全球覆盖；2) 效率优化成为关键，如并行解码和两阶段架构以减少延迟；3) 多模态集成深化，结合视觉、文本和上下文推理提升任务性能；4) 文本渲染准确性通过偏好学习等新方法得到改进；5) 跨模态和自监督学习减少标注依赖，扩展至OCR相关领域。这些趋势反映从传统OCR向高效、全面、低资源适应的系统演进。

## 三、今日论文概览

1. **SEA-Vision: A Multilingual Benchmark for Comprehensive Document and Scene Text Understanding in Southeast Asia** | 标签：多语言OCR、文档解析、视觉问答、基准数据集、低资源语言
2. **Efficient Document Parsing via Parallel Token Prediction** | 标签：文档解析、视觉语言模型、并行解码、效率优化、数据生成
3. **KidsNanny: A Two-Stage Multimodal Content Moderation Pipeline Integrating Visual Classification, Object Detection, OCR, and Contextual Reasoning for Child Safety** | 标签：内容审核、多模态OCR、儿童安全、效率优化、上下文推理
4. **GlyphPrinter: Region-Grouped Direct Preference Optimization for Glyph-Accurate Visual Text Rendering** | 标签：文本渲染、字形准确性、偏好学习、区域优化、数据集构建
5. **Cross-modal learning for plankton recognition** | 标签：跨模态学习、自监督学习、浮游生物识别、多模态OCR、减少标注需求

## 四、今天 OCR / 文档解析论文里的主要创新点

- 开发混合或高效标注流程以减少人工成本并保持数据质量。
- 构建大规模多语言或多模态数据集以支持全面评估和训练。
- 设计并行或两阶段架构优化处理速度和资源效率。
- 集成OCR与语言模型进行上下文推理以提升任务准确性。
- 采用偏好学习或自监督方法减少对标注数据的依赖。

## 五、后续 OCR 领域值得推进的改进方向

- 扩展多语言基准至非洲或土著语言，覆盖更广泛的低资源书写系统。
- 优化并行解码方法以平衡速度与准确性，并适配边缘设备部署。
- 开发通用多模态内容审核框架，整合OCR与视觉模型用于多领域安全应用。
- 增强文本渲染的字形准确性，针对复杂字符如中文或阿拉伯文进行区域级优化。
- 探索跨模态学习在文档解析中的应用，利用未标记多模态数据减少标注需求。

## 六、工程落地启发

- 采用混合标注流程可降低多语言数据集构建成本，适用于跨境文档处理项目。
- 并行令牌预测方法能集成到现有VLMs中，提升文档解析速度1.6倍以上。
- 两阶段架构分离视觉和文本处理，实现低延迟内容审核，适合实时应用。
- 区域分组DPO技术可改进文本渲染模型，提高OCR输入源的字形准确性。
- 自监督跨模态学习减少标注依赖，适用于低资源OCR场景如专业文档识别。

## 七、优先关注论文

- **SEA-Vision: A Multilingual Benchmark for Comprehensive Document and Scene Text Understanding in Southeast Asia**：作为首个东南亚多语言基准，可能推动全球低资源语言OCR评估标准，影响多语言模型开发。
- **Efficient Document Parsing via Parallel Token Prediction**：并行解码方法显著提升速度，有潜力成为文档解析效率优化的行业参考方案。
- **KidsNanny: A Two-Stage Multimodal Content Moderation Pipeline Integrating Visual Classification, Object Detection, OCR, and Contextual Reasoning for Child Safety**：高效架构展示OCR在多模态安全应用中的价值，可能启发其他实时内容审核系统设计。

## 八、论文逐篇解析

### 1. SEA-Vision: A Multilingual Benchmark for Comprehensive Document and Scene Text Understanding in Southeast Asia

- arXiv: [2603.15409v1](https://arxiv.org/abs/2603.15409v1)
- PDF: [下载链接](https://arxiv.org/pdf/2603.15409v1)
- 作者: Pengfei Yue, Xingran Zhao, Juntao Chen, Peng Hou, Wang Longchao, Jianghang Lin, Shengchuan Zhang, Anxiang Zeng, Liujuan Cao
- 发布时间: 2026-03-16T15:21:12Z
- 分类: cs.CL
- 相关性评分: 21
- 主题标签: 多语言OCR、文档解析、视觉问答、基准数据集、低资源语言

**中文摘要**

> 多语言文档和场景文本理解在搜索、金融和公共服务等应用中至关重要，但现有基准大多关注高资源语言，难以评估真实多语言环境下的模型性能。东南亚地区语言多样、书写系统复杂、文档类型多变，挑战更大。本文提出SEA-Vision基准，联合评估11种东南亚语言的文档解析和以文本为中心的视觉问答（TEC-VQA）。SEA-Vision包含15,234个文档解析页面，来自九种代表性文档类型，标注了页面、块和行级别的层次标签；还提供7,496个TEC-VQA问答对，涵盖文本识别、数值计算、比较分析、逻辑推理和空间理解。为高效实现多语言多任务标注，设计了混合流程，结合自动过滤评分、MLLM辅助标注和轻量级母语者验证，大幅减少人工标注同时保持高质量。评估多个领先多模态模型后，发现低资源东南亚语言性能显著下降，凸显多语言文档和场景文本理解仍有巨大差距。SEA-Vision有望推动该领域全球进展。

**核心创新概述**

> 提出首个针对东南亚多语言环境的综合文档和场景文本理解基准，涵盖文档解析和TEC-VQA任务，并设计高效混合标注流程。

**创新点拆解**

- 方法设计：开发混合标注流程，结合自动化和MLLM辅助，减少人工成本
- 数据：构建大规模多语言数据集，覆盖11种语言和多种文档类型
- 任务定义：联合评估文档解析和TEC-VQA，提供全面基准

**当前局限**

> 基准主要针对东南亚语言，可能未覆盖全球所有低资源语言；标注质量依赖自动化工具和母语者验证，可能存在偏差。

**后续可改进方向**

- 扩展基准至更多语言和文档类型
- 优化标注流程以减少潜在偏差
- 探索更高效的多语言模型训练策略

**工程启发**

> 高，为多语言OCR和文档理解提供标准化评估工具，支持实际应用如跨境文档处理。

**为什么值得关注**

> 直接涉及OCR和文档解析的多语言挑战，提供基准和标注方法，对技术发展有指导意义。

**原始摘要**

Multilingual document and scene text understanding plays an important role in applications such as
search, finance, and public services. However, most existing benchmarks focus on high-resource
languages and fail to evaluate models in realistic multilingual environments. In Southeast Asia, the
diversity of languages, complex writing systems, and highly varied document types make this
challenge even greater. We introduce SEA-Vision, a benchmark that jointly evaluates Document Parsing
and Text-Centric Visual Question Answering (TEC-VQA) across 11 Southeast Asian languages. SEA-Vision
contains 15,234 document parsing pages from nine representative document types, annotated with
hierarchical page-, block-, and line-level labels. It also provides 7,496 TEC-VQA question-answer
pairs that probe text recognition, numerical calculation, comparative analysis, logical reasoning,
and spatial understanding. To make such multilingual, multi-task annotation feasible, we design a
hybrid pipeline for Document Parsing and TEC-VQA. It combines automated filtering and scoring with
MLLM-assisted labeling and lightweight native-speaker verification, greatly reducing manual labeling
while maintaining high quality. We evaluate several leading multimodal models and observe pronounced
performance degradation on low-resource Southeast Asian languages, highlighting substantial
remaining gaps in multilingual document and scene text understanding. We believe SEA-Vision will
help drive global progress in document and scene text understanding.

---

### 2. Efficient Document Parsing via Parallel Token Prediction

- arXiv: [2603.15206v1](https://arxiv.org/abs/2603.15206v1)
- PDF: [下载链接](https://arxiv.org/pdf/2603.15206v1)
- 作者: Lei Li, Ze Zhao, Meng Li, Zhongwang Lun, Yi Yuan, Xingjing Lu, Zheng Wei, Jiang Bian, Zang Li
- 发布时间: 2026-03-16T12:45:34Z
- 分类: cs.CL, cs.CV
- 相关性评分: 15
- 主题标签: 文档解析、视觉语言模型、并行解码、效率优化、数据生成

**中文摘要**

> 文档解析作为基础视觉任务，正被视觉语言模型（VLMs）革新，但自回归解码导致速度瓶颈。本文提出并行令牌预测（PTP），一种可插拔、模型无关的简单有效方法，使VLMs能并行生成多个未来令牌，提高样本效率。具体地，在输入序列中插入可学习令牌，并设计相应训练目标，赋予模型并行解码能力。此外，为支持有效训练，开发了综合数据生成流程，高效生产大规模高质量文档解析训练数据。在OmniDocBench和olmOCR-bench上的实验表明，该方法显著提升解码速度（1.6x-2.2x），减少模型幻觉，并展示强泛化能力。

**核心创新概述**

> 提出并行令牌预测方法，解决VLMs在文档解析中的自回归解码速度瓶颈，并配套数据生成流程。

**创新点拆解**

- 方法设计：引入并行令牌预测，优化解码过程
- 训练范式：设计可学习令牌和训练目标，实现并行解码
- 数据：开发高效数据生成流程，支持大规模训练

**当前局限**

> 方法可能增加训练复杂度；实验主要基于特定基准，需验证在更广泛场景下的有效性。

**后续可改进方向**

- 进一步优化并行解码的准确性和效率
- 扩展方法至其他视觉语言任务
- 探索更轻量级的实现方案

**工程启发**

> 高，提升文档解析速度，减少延迟，适用于实时OCR应用。

**为什么值得关注**

> 针对OCR核心任务文档解析的效率问题，提供创新解码方法，有实际应用价值。

**原始摘要**

Document parsing, as a fundamental yet crucial vision task, is being revolutionized by vision-
language models (VLMs). However, the autoregressive (AR) decoding inherent to VLMs creates a
significant bottleneck, severely limiting parsing speed. In this paper, we propose Parallel-Token
Prediction (PTP), a plugable, model-agnostic and simple-yet-effective method that enables VLMs to
generate multiple future tokens in parallel with improved sample efficiency. Specifically, we insert
some learnable tokens into the input sequence and design corresponding training objectives to equip
the model with parallel decoding capabilities for document parsing. Furthermore, to support
effective training, we develop a comprehensive data generation pipeline that efficiently produces
large-scale, high-quality document parsing training data for VLMs. Extensive experiments on
OmniDocBench and olmOCR-bench demonstrate that our method not only significantly improves decoding
speed (1.6x-2.2x) but also reduces model hallucinations and exhibits strong generalization
abilities.

---

### 3. KidsNanny: A Two-Stage Multimodal Content Moderation Pipeline Integrating Visual Classification, Object Detection, OCR, and Contextual Reasoning for Child Safety

- arXiv: [2603.16181v1](https://arxiv.org/abs/2603.16181v1)
- PDF: [下载链接](https://arxiv.org/pdf/2603.16181v1)
- 作者: Viraj Panchal, Tanmay Talsaniya, Parag Patel, Meet Patel
- 发布时间: 2026-03-17T07:00:43Z
- 分类: cs.CV, cs.CR
- 相关性评分: 13
- 主题标签: 内容审核、多模态OCR、儿童安全、效率优化、上下文推理

**中文摘要**

> 本文提出KidsNanny，一个两阶段多模态内容审核架构，用于儿童安全。第一阶段结合视觉Transformer和对象检测器进行视觉筛选（11.7毫秒）；输出以文本而非原始像素形式路由到第二阶段，应用OCR和基于文本的7B语言模型进行上下文推理（总流程120毫秒）。在UnsafeBench Sexual类别（1,054张图像）上评估两种模式：仅视觉（隔离第一阶段）和多模态（评估完整流程）。第一阶段达到80.27%准确率和85.39% F1，耗时11.7毫秒；仅视觉基线准确率从59.01%到77.04%。完整流程达到81.40%准确率和86.16% F1，耗时120毫秒，优于ShieldGemma-2（64.80%准确率，1,136毫秒）和LlavaGuard（80.36%准确率，4,138毫秒）。为评估文本感知能力，过滤两个子集：文本+视觉子集（257张图像）和仅文本子集（44张图像，安全性主要依赖嵌入文本）。在仅文本图像上，KidsNanny达到100%召回率（25/25正例；小样本）和75.76%精确率；ShieldGemma-2达到84%召回率和60%精确率，耗时1,136毫秒。结果表明，专用OCR推理可能在文本嵌入威胁上提供召回-精确优势且延迟更低，但仅文本子集小限制泛化性。通过记录此架构和评估方法，旨在贡献于高效多模态内容审核研究。

**核心创新概述**

> 提出高效两阶段多模态内容审核架构，结合视觉筛选和OCR推理，针对儿童安全应用优化延迟和性能。

**创新点拆解**

- 架构设计：两阶段流程，分离视觉和文本处理，提高效率
- 方法设计：集成OCR和语言模型进行上下文推理
- 任务定义：专注于儿童安全内容审核，提供新评估方法

**当前局限**

> 仅文本子集样本小，限制结论泛化性；架构可能对复杂多模态场景适应性有限。

**后续可改进方向**

- 扩大数据集以验证文本感知性能
- 优化OCR和语言模型的集成策略
- 扩展至其他内容审核领域

**工程启发**

> 高，提供低延迟内容审核方案，适用于实时安全应用。

**为什么值得关注**

> 涉及OCR在内容审核中的关键作用，展示多模态集成方法，对实际部署有参考价值。

**原始摘要**

We present KidsNanny, a two-stage multimodal content moderation architecture for child safety. Stage
1 combines a vision transformer (ViT) with an object detector for visual screening (11.7 ms);
outputs are routed as text not raw pixels to Stage 2, which applies OCR and a text based 7B language
model for contextual reasoning (120 ms total pipeline). We evaluate on the UnsafeBench Sexual
category (1,054 images) under two regimes: vision-only, isolating Stage 1, and multimodal,
evaluating the full Stage 1+2 pipeline. Stage 1 achieves 80.27% accuracy and 85.39% F1 at 11.7 ms;
vision-only baselines range from 59.01% to 77.04% accuracy. The full pipeline achieves 81.40%
accuracy and 86.16% F1 at 120 ms, compared to ShieldGemma-2 (64.80% accuracy, 1,136 ms) and
LlavaGuard (80.36% accuracy, 4,138 ms). To evaluate text-awareness, we filter two subsets: a
text+visual subset (257 images) and a text-only subset (44 images where safety depends primarily on
embedded text). On text-only images, KidsNanny achieves 100% recall (25/25 positives; small sample)
and 75.76% precision; ShieldGemma-2 achieves 84% recall and 60% precision at 1,136 ms. Results
suggest that dedicated OCR-based reasoning may offer recall-precision advantages on text-embedded
threats at lower latency, though the small text-only subset limits generalizability. By documenting
this architecture and evaluation methodology, we aim to contribute to the broader research effort on
efficient multimodal content moderation for child safety.

---

### 4. GlyphPrinter: Region-Grouped Direct Preference Optimization for Glyph-Accurate Visual Text Rendering

- arXiv: [2603.15616v1](https://arxiv.org/abs/2603.15616v1)
- PDF: [下载链接](https://arxiv.org/pdf/2603.15616v1)
- 作者: Xincheng Shuai, Ziye Li, Henghui Ding, Dacheng Tao
- 发布时间: 2026-03-16T17:59:31Z
- 分类: cs.CV
- 相关性评分: 12
- 主题标签: 文本渲染、字形准确性、偏好学习、区域优化、数据集构建

**中文摘要**

> 生成准确字形对于视觉文本渲染至关重要但具挑战性。现有方法通常通过训练大量高质量场景文本图像来增强文本渲染，但字形变体覆盖有限和过度风格化常损害字形准确性，尤其是复杂或域外字符。一些方法利用强化学习缓解此问题，但其奖励模型通常依赖对细粒度字形错误不敏感的文本识别系统，因此错误字形图像仍可能获得高奖励。受直接偏好优化（DPO）启发，提出GlyphPrinter，一种基于偏好的文本渲染方法，消除对显式奖励模型的依赖。但标准DPO目标仅建模两个样本的整体偏好，不足以处理视觉文本渲染中字形错误通常发生在局部区域的问题。为此，构建GlyphCorrector数据集，带区域级字形偏好标注，并提出区域分组DPO（R-GDPO），一种基于区域的目标，优化标注区域的样本间和样本内偏好，显著提升字形准确性。此外，引入区域奖励指导，一种从最优分布采样以控制字形准确性的推理策略。大量实验表明，GlyphPrinter在字形准确性上优于现有方法，同时保持风格化和精确性的良好平衡。

**核心创新概述**

> 提出基于区域分组DPO的文本渲染方法，消除奖励模型依赖，通过区域级优化提升字形准确性。

**创新点拆解**

- 方法设计：引入区域分组DPO，针对局部字形错误进行优化
- 数据：构建带区域标注的数据集GlyphCorrector
- 训练范式：采用偏好学习，避免强化学习的奖励模型问题

**当前局限**

> 方法可能增加训练和推理复杂度；数据集覆盖范围可能有限。

**后续可改进方向**

- 扩展数据集以覆盖更多字形变体和语言
- 优化区域分组策略以提高效率
- 探索与其他文本渲染技术的结合

**工程启发**

> 中高，提升文本渲染的字形准确性，适用于需要高精度OCR的场景如文档生成。

**为什么值得关注**

> 直接关联OCR中的文本渲染和字形准确性，提供新颖优化方法，对字体识别和生成有贡献。

**原始摘要**

Generating accurate glyphs for visual text rendering is essential yet challenging. Existing methods
typically enhance text rendering by training on a large amount of high-quality scene text images,
but the limited coverage of glyph variations and excessive stylization often compromise glyph
accuracy, especially for complex or out-of-domain characters. Some methods leverage reinforcement
learning to alleviate this issue, yet their reward models usually depend on text recognition systems
that are insensitive to fine-grained glyph errors, so images with incorrect glyphs may still receive
high rewards. Inspired by Direct Preference Optimization (DPO), we propose GlyphPrinter, a
preference-based text rendering method that eliminates reliance on explicit reward models. However,
the standard DPO objective only models overall preference between two samples, which is insufficient
for visual text rendering where glyph errors typically occur in localized regions. To address this
issue, we construct the GlyphCorrector dataset with region-level glyph preference annotations and
propose Region-Grouped DPO (R-GDPO), a region-based objective that optimizes inter- and intra-sample
preferences over annotated regions, substantially enhancing glyph accuracy. Furthermore, we
introduce Regional Reward Guidance, an inference strategy that samples from an optimal distribution
with controllable glyph accuracy. Extensive experiments demonstrate that the proposed GlyphPrinter
outperforms existing methods in glyph accuracy while maintaining a favorable balance between
stylization and precision.

---

### 5. Cross-modal learning for plankton recognition

- arXiv: [2603.16427v1](https://arxiv.org/abs/2603.16427v1)
- PDF: [下载链接](https://arxiv.org/pdf/2603.16427v1)
- 作者: Joona Kareinen, Veikka Immonen, Tuomas Eerola, Lumi Haraguchi, Lasse Lensu, Kaisa Kraft, Sanna Suikkanen, Heikki Kälviäinen
- 发布时间: 2026-03-17T12:04:52Z
- 分类: cs.CV
- 相关性评分: 3
- 主题标签: 跨模态学习、自监督学习、浮游生物识别、多模态OCR、减少标注需求

**中文摘要**

> 本文考虑自监督跨模态协调作为策略，利用多模态和大规模未标记浮游生物数据构建浮游生物识别模型。自动化成像仪器促进大规模连续收集浮游生物图像数据。当前自动浮游生物图像识别方法主要依赖监督方法，需要标注训练集，收集劳动密集。另一方面，一些现代浮游生物成像仪器补充图像信息与光学测量数据，如散射和荧光剖面，目前未广泛用于浮游生物识别。本工作中，探索使用此类测量数据指导学习过程而无需手动标注。受对比语言-图像预训练概念启发，训练两种模态的编码器，仅使用二元监督信息指示给定图像和剖面是否来自同一粒子或不同粒子。对于浮游生物识别，采用小标注已知物种库结合k-NN分类器。此方法产生本质多模态的识别模型，即能利用从图像和剖面数据提取的信息。证明所提方法实现高识别准确性，同时仅需最小数量标注图像。此外，展示该方法优于仅图像自监督...

**核心创新概述**

> 提出自监督跨模态协调方法，结合图像和光学测量数据，用于浮游生物识别，减少标注需求。

**创新点拆解**

- 训练范式：采用自监督跨模态学习，减少对标注数据的依赖
- 方法设计：集成图像和光学剖面数据，提升识别性能
- 数据利用：有效利用未标记多模态数据

**当前局限**

> 方法可能对特定模态数据（如光学剖面）的可用性敏感；实验领域较窄，需验证在其他OCR相关任务的泛化性。

**后续可改进方向**

- 扩展至其他多模态OCR任务，如文档理解
- 优化跨模态对齐策略以提高效率
- 探索更复杂的自监督学习框架

**工程启发**

> 中，为低资源OCR场景提供减少标注需求的方案，但应用领域特定。

**为什么值得关注**

> 涉及OCR中的多模态学习和自监督技术，对数据稀缺场景有借鉴意义。

**原始摘要**

This paper considers self-supervised cross-modal coordination as a strategy enabling utilization of
multiple modalities and large volumes of unlabeled plankton data to build models for plankton
recognition. Automated imaging instruments facilitate the continuous collection of plankton image
data on a large scale. Current methods for automatic plankton image recognition rely primarily on
supervised approaches, which require labeled training sets that are labor-intensive to collect. On
the other hand, some modern plankton imaging instruments complement image information with optical
measurement data, such as scatter and fluorescence profiles, which currently are not widely utilized
in plankton recognition. In this work, we explore the possibility of using such measurement data to
guide the learning process without requiring manual labeling. Inspired by the concepts behind
Contrastive Language-Image Pre-training, we train encoders for both modalities using only binary
supervisory information indicating whether a given image and profile originate from the same
particle or from different particles. For plankton recognition, we employ a small labeled gallery of
known plankton species combined with a $k$-NN classifier. This approach yields a recognition model
that is inherently multimodal, i.e., capable of utilizing information extracted from both image and
profile data. We demonstrate that the proposed method achieves high recognition accuracy while
requiring only a minimal number of labeled images. Furthermore, we show that the approach
outperforms an image-only self-supervised baseline. Code available at
https://github.com/Jookare/cross-modal-plankton.

---
