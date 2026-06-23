# OCR / 文档解析研究日报（2026-06-23）

## 报告说明

- 检索源：arXiv API
- 检索查询：`(all:"document parsing" OR all:"document understanding" OR all:"optical character recognition" OR all:OCR OR all:"layout analysis" OR all:"document layout analysis" OR all:"text recognition" OR all:"table recognition" OR all:"form understanding" OR all:"document intelligence" OR all:"page understanding" OR all:"scene text recognition" OR all:"handwritten text recognition" OR all:"information extraction") AND (cat:cs.CV OR cat:cs.AI OR cat:cs.CL OR cat:eess.IV)`
- 生成时间（UTC）：`2026-06-23 05:13:42`
- 大模型综合分析：`开启`

## 一、今日执行摘要

> 今日研究集中在文档布局分析、低资源语言OCR、历史文档数字化、长文档高效推理等方向，多项工作引入新架构或数据集，提升了OCR系统的性能、效率或覆盖度。

## 二、今日趋势判断

趋势包括：1) 端到端多任务统一框架；2) 合成数据驱动低资源语言OCR；3) 状态空间模型在文本识别中的探索；4) 注意力机制改进长文档推理；5) 经典架构（如DETR）在新领域（楔形文字）的应用。

## 三、今日论文概览

1. **RT-DocLayout: Real-Time End-to-End Document Layout Analysis with Reading Order in the Wild** | 标签：文档布局分析、端到端、实时、阅读顺序、多任务学习
2. **Koshur Pixel: a large-scale synthetic ocr dataset for kashmiri** | 标签：合成数据集、低资源语言、克什米尔语、OCR、数据增强
3. **Automated sign detection across the Electronic Babylonian Library: A large-scale dataset and end-to-end cuneiform OCR pipeline** | 标签：楔形文字、目标检测、DETR、数字化、历史文档
4. **Scaling State-Space Models from Lines to Paragraphs: An Ablation of Mamba-based OCR** | 标签：状态空间模型、Mamba、OCR、长序列、消融研究
5. **Unlimited OCR Works** | 标签：长文档OCR、注意力机制、高效推理、KV缓存、R-SWA
6. **P-JEPA: Procedural Video Representation Learning via Joint Embedding Predictive Architecture** | 标签：程序性视频、表示学习、JEPA、动作分类、长视频

## 四、今天 OCR / 文档解析论文里的主要创新点

- 通过多任务查询解码器统一布局分析子任务，实现实时端到端处理。
- 构建大规模合成数据集填补低资源语言OCR训练数据空白。
- 将DETR迁移至楔形文字检测并集成完整流程。
- 消融研究揭示Mamba在长序列OCR中数据饥饿特性。
- 提出参考滑动窗口注意力实现恒定KV缓存，支持长文档高效推理。

## 五、后续 OCR 领域值得推进的改进方向

- 研究更高效阅读顺序推理机制，结合文档结构先验扩展至多语言版面。
- 探索混合状态空间模型与注意力架构，缓解数据稀缺下的性能下降。
- 将R-SWA注意力扩展至更多自回归任务，并优化窗口设计以适应更大长度。
- 融合多模态或语言模型辅助历史文档检测，增强对损坏文档的鲁棒性。
- 开展合成数据与真实数据的域适应研究，提升低资源语言OCR真实性。

## 六、工程落地启发

- RT-DocLayout可直接作为文档解析前端，提升下游OCR效率。
- Koshur Pixel数据集降低克什米尔语OCR标注成本。
- 楔形文字检测流程支持大规模历史文档数字化。
- Mamba的快速推理特性适用于数据充足场景。
- Unlimited OCR大幅降低长文档内存占用，适合实际部署。

## 七、优先关注论文

- **RT-DocLayout: Real-Time End-to-End Document Layout Analysis with Reading Order in the Wild**：实时端到端框架潜力大，关注其在复杂版面和多语言扩展上的后续工作。
- **Scaling State-Space Models from Lines to Paragraphs: An Ablation of Mamba-based OCR**：揭示SSM在真实数据上的不足，关注混合架构或训练策略改进。
- **Unlimited OCR Works**：R-SWA机制有广泛应用前景，关注其通用性和窗口优化。

## 八、论文逐篇解析

### 1. RT-DocLayout: Real-Time End-to-End Document Layout Analysis with Reading Order in the Wild

- arXiv: [2606.23344v1](https://arxiv.org/abs/2606.23344v1)
- PDF: [下载链接](https://arxiv.org/pdf/2606.23344v1)
- 作者: Cheng Cui, Tingquan Gao, Xueqing Wang, Changda Zhou, Hongen Liu, Ting Sun, Yubo Zhang, Zelun Zhang, Jiaxuan Liu, Manhui Lin, Yue Zhang, Suyin Liang, Yiqing Xiang, Yi Liu
- 发布时间: 2026-06-22T13:48:39Z
- 分类: cs.CV
- 相关性评分: 30
- 主题标签: 文档布局分析、端到端、实时、阅读顺序、多任务学习

**中文摘要**

> 提出RT-DocLayout，一个33M参数的端到端文档布局分析框架，统一了分类、检测、分割和阅读顺序预测。基于RT-DETR，采用统一多任务查询解码器同时处理多个子任务，在公共基准上达到SOTA性能（132.1 FPS），并提升下游OCR的文档重建质量。

**核心创新概述**

> 将阅读顺序推理与检测分割统一到单个解码器中，实现实时端到端布局分析。

**创新点拆解**

- 统一多任务查询解码器结构
- 联合学习几何与结构表示的多任务优化
- 轻量级33M参数实现实时推理（132.1 FPS）

**当前局限**

> 论文未提及在极端复杂版面（如手写混排）下的性能。

**后续可改进方向**

- 探索更高效的阅读顺序推理机制
- 融入文档结构先验知识（如模板）
- 扩展至多语言场景

**工程启发**

> 可作为文档解析前端，显著提升OCR系统的完整性和效率，适用于智能文档处理等工业场景。

**为什么值得关注**

> 文档布局分析是OCR关键环节，该工作提供了实时统一的解决方案。

**原始摘要**

Accurate document layout analysis remains a critical bottleneck for document parsing systems, due to
the intricate coupling among heterogeneous document layout elements, geometric distortions (\eg,
paper warping and bending, perspective variations), and reading order within diverse layout
structures. Existing approaches typically rely on fragmented multi-stage pipelines or
computationally heavy generative Transformer architectures, leading to error propagation and limited
efficiency. In this paper, we present RT-DocLayout, a highly efficient end-to-end framework for
document layout analysis, designed as a front-end for document parsing tasks. The proposed model
unifies classification, detection, pixel-level segmentation, and reading order prediction for layout
elements within a single 33M-parameter architecture. Built upon the RT-DETR, our key contribution is
a unified multi-task formulation within a single query-based decoder that simultaneously classifies,
regresses bounding box, generates masks, and constructs relationship to reason reading order. By
jointly learning geometric and structural representations, RT-DocLayout introduces multi-task
optimization that substantially improves robustness under real-world document distortions. Extensive
experiments on public benchmarks demonstrate state-of-the-art performance in document layout
analysis while maintaining real-time inference speed(132.1 FPS). When coupled with downstream OCR
engines, RT-DocLayout significantly improves full-document reconstruction quality, providing a
scalable and practical foundation for real-world document intelligence systems.

---

### 2. Koshur Pixel: a large-scale synthetic ocr dataset for kashmiri

- arXiv: [2606.23144v1](https://arxiv.org/abs/2606.23144v1)
- PDF: [下载链接](https://arxiv.org/pdf/2606.23144v1)
- 作者: Haq Nawaz Malik, Faizan Iqbal, Nahfid Nissar
- 发布时间: 2026-06-22T10:42:36Z
- 分类: cs.CV, cs.CL
- 相关性评分: 17
- 主题标签: 合成数据集、低资源语言、克什米尔语、OCR、数据增强

**中文摘要**

> 介绍Koshur Pixel，首个大规模克什米尔语合成OCR数据集，包含613,078个图像-文本对，覆盖多种字体和文本粒度，使用超过25种数据增强模拟真实退化，为低资源语言OCR提供可扩展基础。

**核心创新概述**

> 首次为克什米尔语构建大规模合成OCR数据集。

**创新点拆解**

- 首个克什米尔语OCR数据集构建
- 基于SynthOCR-Gen框架从5百万语料生成数据
- 包含多种字体和文本粒度，增强策略丰富

**当前局限**

> 合成数据与真实场景存在域差异，真实性有限。

**后续可改进方向**

- 结合少量真实标注进行域适应
- 探索更逼真的退化模拟方法
- 扩展至其他低资源语言

**工程启发**

> 为克什米尔语数字化提供训练数据基础，降低人工标注成本。

**为什么值得关注**

> 低资源语言OCR是重要方向，该数据集填补克什米尔语空白。

**原始摘要**

Optical Character Recognition (OCR) for low-resource languages is often constrained by the lack of
annotated training data and the complexity of script-specific rendering. Kashmiri, written primarily
in the Perso-Arabic Nastaliq script, presents additional challenges due to contextual glyph shaping,
dense ligatures, and orthographic variability. We introduce Koshur Pixel, the first large-scale
synthetic OCR dataset for Kashmiri, comprising 613,078 image-text pairs generated from the KS-
PRET-5M corpus using the SynthOCR-Gen framework. The dataset spans multiple fonts and textual
granularities, ranging from individual words to full-page documents, and incorporates more than 25
augmentation strategies that emulate real-world document degradations. Koshur Pixel provides a
scalable and cost-effective alternative to manual annotation, establishing a foundational resource
for training OCR systems, digitizing Kashmiri textual heritage, and advancing language technologies
for a severely under-resourced language.

---

### 3. Automated sign detection across the Electronic Babylonian Library: A large-scale dataset and end-to-end cuneiform OCR pipeline

- arXiv: [2606.22608v1](https://arxiv.org/abs/2606.22608v1)
- PDF: [下载链接](https://arxiv.org/pdf/2606.22608v1)
- 作者: Wentao Che, Esteban Garcés Arias, Asim Niaz, Andreas Bender, Enrique Jiménez
- 发布时间: 2026-06-21T17:31:05Z
- 分类: cs.CV, cs.CL
- 相关性评分: 16
- 主题标签: 楔形文字、目标检测、DETR、数字化、历史文档

**中文摘要**

> 提出基于DETR的楔形文字检测流程，使用最大规模标注数据集（173/106类），集成平板自动提取、行分组和n-gram文本相似度评估，在87,668个碎片上产生290万次检测，相较于先前工作提升28-37%。

**核心创新概述**

> 将DETR应用于楔形文字检测并实现大规模部署。

**创新点拆解**

- 最大规模楔形文字标注数据集
- 基于DETR的检测模型，两类粒度评估
- 集成自动提取、行分组和n-gram评估的完整流程

**当前局限**

> 对平板损坏和布局变化敏感，缺少语言先验。

**后续可改进方向**

- 引入多模态或语言模型辅助
- 增强对损坏文档的鲁棒性
- 扩展至更多历史文字系统

**工程启发**

> 为楔形文字大规模数字化提供可行方案。

**为什么值得关注**

> 展示了目标检测在古文识别领域的应用潜力。

**原始摘要**

Learning to read cuneiform tablets is an extremely demanding task; consequently, of the roughly half
million excavated tablets, only a small fraction has been analysed by Assyriologists. Computer
vision offers a promising avenue for decipherment but requires large, densely annotated datasets. To
address this limitation, the largest annotated cuneiform sign dataset to date is used, and a
Deformable Detection Transformer (DETR)-based object detection model is evaluated under two class
granularities of 173 and 106 classes. The proposed system integrates automatic tablet-side
extraction, heuristic line grouping, and n-gram-based textual similarity evaluation to bridge visual
sign detection and textual structure, and achieves consistent improvements of up to 28-37% over
prior work on COCO-style detection metrics. At inference, the method is applied to 87,668 tablet
fragments from the Electronic Babylonian Library (eBL) corpus, producing nearly 2.9 million sign
detections. Although the approach operates without linguistic priors and remains sensitive to tablet
damage and layout variability, it provides a scalable and interpretable foundation for corpus-wide
cuneiform analysis and supports future integration with multimodal and linguistic modelling
frameworks.

---

### 4. Scaling State-Space Models from Lines to Paragraphs: An Ablation of Mamba-based OCR

- arXiv: [2606.23524v1](https://arxiv.org/abs/2606.23524v1)
- PDF: [下载链接](https://arxiv.org/pdf/2606.23524v1)
- 作者: Merveilles Agbeti-Messan, Pierrick Tranouez, Stéphane Nicolas, Clément Chatelain, Thierry Paquet
- 发布时间: 2026-06-22T16:07:40Z
- 分类: cs.CV
- 相关性评分: 13
- 主题标签: 状态空间模型、Mamba、OCR、长序列、消融研究

**中文摘要**

> 对基于Mamba的OCR识别器从行到段落的缩放行为进行消融研究。识别器在合成段落上保持低于1% CER，速度比Transformer快1.4-4.5倍，但在真实手写段落上CER为10.0%（Transformer为3.5%），表明SSM在数据稀缺时性能下降明显。

**核心创新概述**

> 系统比较SSM与Transformer在长序列OCR中的行为差异。

**创新点拆解**

- Mamba参数（状态维数、扩展因子）对长序列精度的影响分析
- SSM在合成与真实数据上的性能对比实验
- 揭示SSM数据饥饿特性

**当前局限**

> SSM在真实手写数据上性能落后Transformer。

**后续可改进方向**

- 增加训练数据量或采用数据增强
- 探索状态空间模型与注意力的混合架构
- 研究SSM对复杂书写变体的建模能力

**工程启发**

> 为选择SSM作为OCR解码器提供实验依据，适合数据充足时的快速推理。

**为什么值得关注**

> SSM是一种新兴高效序列模型，该工作评估其在OCR中的适用性。

**原始摘要**

End-to-end OCR increasingly relies on autoregressive sequence models, where the quadratic cost of
Transformer attention limits efficient transcription of long, paragraph-level text. State-Space
Models (SSMs) such as Mamba offer linear-time decoding and have recently been shown to match
Transformer accuracy on printed historical lines, but their behavior as sequences grow from short
lines to full paragraphs, and their generalization to handwriting, remain poorly understood. We
study how a Mamba-based OCR recognizer scales from lines to paragraphs. We first conduct a
systematic exploration of its four core hyperparameters (decoder depth, state dimension, expansion
factor, and connector depth) on synthetic paragraphs from 100 to 1,000 characters, identifying the
recurrent state dimension and the expansion factor as the dominant levers for long-sequence
accuracy. We then compare the recognizer against a Transformer baseline trained under an identical
protocol. On clean synthetic paragraphs, both models stay below 1% CER at every length while the SSM
runs 1.4 to 4.5 times faster, the speedup growing with sequence length. On real handwriting,
however, the SSM lags clearly behind: it reaches 8.2% CER on IAM lines and 10.0% on IAM paragraphs,
against 4.2% and 3.5% for the Transformer baseline. Through controlled experiments we show that a
substantial part of this gap stems from data scarcity rather than from an intrinsic architectural
limit: the autoregressive SSM decoder is markedly data-hungry on long sequences. Our study clarifies
when SSMs are a practical choice for large-scale document transcription and when they are not.

---

### 5. Unlimited OCR Works

- arXiv: [2606.23050v1](https://arxiv.org/abs/2606.23050v1)
- PDF: [下载链接](https://arxiv.org/pdf/2606.23050v1)
- 作者: Youyang Yin, Huanhuan Liu, YY, Qunyi Xie, Chaorun Liu, Shiqi Yang, Shaohua Wang, Zhanlong Liu, Hao Zou, Jinyue Chen, Shu Wei, Jingjing Wu, Mingxin Huang, Zhen Wu, Guibin Wang, Tengyu Du, Lei Jia
- 发布时间: 2026-06-22T09:01:29Z
- 分类: cs.CV, cs.CL
- 相关性评分: 11
- 主题标签: 长文档OCR、注意力机制、高效推理、KV缓存、R-SWA

**中文摘要**

> 提出Unlimited OCR，通过参考滑动窗口注意力（R-SWA）替换LLM解码器的全注意力，保持恒定KV缓存，实现单次前向处理数十页文档（32K长度），降低内存消耗且不增加延迟。代码和模型已开源。

**核心创新概述**

> 提出R-SWA注意力机制解决长序列OCR中KV缓存增长问题。

**创新点拆解**

- 参考滑动窗口注意力（R-SWA）代替全注意力
- 解码过程保持恒定KV缓存
- 支持32K长度单次前向处理

**当前局限**

> 论文以DeepSeek OCR为基线，未在更多模型上验证通用性。

**后续可改进方向**

- 将R-SWA扩展到其他AR任务（如ASR）
- 结合更高效编码器进一步压缩长度
- 探索更大的窗口设计

**工程启发**

> 大幅降低长文档OCR的内存和推理成本，适合实际部署。

**为什么值得关注**

> 解决LLM-based OCR长序列推理效率的痛点。

**原始摘要**

Recently, end-to-end OCR models, exemplified by DeepSeek OCR, have once again thrust OCR into the
spotlight. A widely held view is that employing a large language model (LLM) as the decoder allows
the model to leverage the prior distribution of language, leading to improved OCR performance.
However, the downside is equally evident: as the output sequence lengthens, the accumulated KV cache
drives up memory consumption and progressively slows down generation. This stands in stark contrast
to humans, who exhibit no such decline in efficiency during long-horizon copying tasks. In this
technical report, we propose Unlimited OCR, a model designed to emulate human parsing working
memory. Taking DeepSeek OCR as the baseline, we replace all attention layers in the decoder with our
proposed Reference Sliding Window Attention (R-SWA), which reduces attention computation costs while
maintaining a constant KV cache throughout the entire decoding process. By combining the high
compression rate of DeepSeek OCR's encoder with our constant KV cache design, Unlimited OCR can
transcribe dozens of pages of documents in a single forward pass under a standard maximum length of
32K. More importantly, R-SWA is a general-purpose parsing attention mechanism - beyond OCR, it is
equally applicable to tasks such as ASR, translation, etc. Codes and model weights are publicly
available at http://github.com/baidu/Unlimited-OCR.

---

### 6. P-JEPA: Procedural Video Representation Learning via Joint Embedding Predictive Architecture

- arXiv: [2606.23256v1](https://arxiv.org/abs/2606.23256v1)
- PDF: [下载链接](https://arxiv.org/pdf/2606.23256v1)
- 作者: Felix Tristram, Stefano Gasperini, Benjamin Killeen, Marcel Walch, Christian Benz, Nassir Navab, Ghazal Ghazaei
- 发布时间: 2026-06-22T12:38:36Z
- 分类: cs.CV, cs.AI
- 相关性评分: 3
- 主题标签: 程序性视频、表示学习、JEPA、动作分类、长视频

**中文摘要**

> 提出P-JEPA，一种面向程序性视频的表示学习框架，通过将问题简化为密集帧对齐动作空间并预测池化掩码潜向量，支持长达30分钟的视频处理，在EgoExo4D细粒度动作分类上达到SOTA，参数比LLM方法少一个数量级。

**核心创新概述**

> 将JEPA扩展到程序性视频表示学习，处理长程依赖。

**创新点拆解**

- 程序性视频的帧对齐动作空间设计
- 池化掩码潜向量预测框架
- 支持30分钟以上视频的实时处理

**当前局限**

> 依赖预提取特征编码器，未实现端到端训练。

**后续可改进方向**

- 端到端特征学习
- 结合时序建模更精细的动作分割
- 扩展至更多程序性视频数据集

**工程启发**

> 适用于智能辅助系统中的多步骤任务理解。

**为什么值得关注**

> 程序性视频理解是视觉语言融合的重要场景。

**原始摘要**

The increasing maturity of embodied AI platforms has driven a growing interest in procedural video
representation learning to support intelligent assistance systems for complex, multi-step tasks.
Leveraging large-scale latent predictive training, video foundation models capture video dynamics,
enabling downstream tasks such as activity understanding, spatiotemporal localization, and
predictive control. However, procedural videos include actions with long-range dependencies that
these models do not support, due to the quadratic complexity of self-attention. Distinct actions,
for example, may be visually similar despite appearing at different points in the procedure, such as
turning the stove on versus off. Here, we propose a backbone-agnostic approach that learns long-
duration video representations by reducing the problem to a dense, frame-aligned action space and
predicting pooled masked latent vectors. This approach allows our Procedural Joint Embedding
Predictive Architecture (P-JEPA) to ingest videos over 30 minutes long, enabling effective long-form
understanding of procedural steps. We evaluate P-JEPA using features extracted with VJEPA2.1, TSM,
and I3D over the EgoExo4D, EgoProceL, and Assembly101 datasets, finding that it consistently
improves linear separability, streaming inference, and temporal action segmentation performance,
achieving state-of-the-art results on EgoExo4D fine-grained action classification while using an
order of magnitude fewer parameters than LLM-based methods and running in real time.

---
