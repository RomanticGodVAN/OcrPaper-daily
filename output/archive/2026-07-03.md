# OCR / 文档解析研究日报（2026-07-03）

## 报告说明

- 检索源：arXiv API
- 检索查询：`(all:"document parsing" OR all:"document understanding" OR all:"optical character recognition" OR all:OCR OR all:"layout analysis" OR all:"document layout analysis" OR all:"text recognition" OR all:"table recognition" OR all:"form understanding" OR all:"document intelligence" OR all:"page understanding" OR all:"scene text recognition" OR all:"handwritten text recognition" OR all:"information extraction") AND (cat:cs.CV OR cat:cs.AI OR cat:cs.CL OR cat:eess.IV)`
- 生成时间（UTC）：`2026-07-03 04:56:15`
- 大模型综合分析：`开启`

## 一、今日执行摘要

> 今日OCR与文档解析领域研究聚焦于阅读顺序重建、表格结构识别、低资源场景下的VLM应用及多模态持续学习。多篇论文提出免训练或轻量化方案应对复杂版面，强调数据效率与鲁棒性，同时揭示多模态模型在持续学习中的隐藏缺陷。

## 二、今日趋势判断

趋势包括：1) 阅读顺序重建中图框架与LLM混合方法兴起；2) 零样本VLM替代传统OCR管线在特定场景展现潜力；3) 表格结构识别轻量化、数据高效改进；4) 多模态持续学习关注证据保持而非仅准确率。

## 三、今日论文概览

1. **Semantic-Guided Reading Order Reconstruction in Historical Armenian Newspapers with LLMs** | 标签：阅读顺序重建、历史文档、LLM、版面分析、低资源语言
2. **Reading Order Inference for Complex Document Layouts** | 标签：阅读顺序推断、图框架、最大遗憾推理、复杂版面、历史文档
3. **Evaluating Vision-Language Models as a Zero-Shot Learning Alternative to You Only Look Once and Optical Character Recognition for Nigerian License Plate Recognition** | 标签：车牌识别、VLM、零样本学习、YOLO+OCR、字符错误率
4. **ConRTF: Edge-Constrained Boundary Distribution Refinement for Realtime TransFormer Table Structure Recognition** | 标签：表格结构识别、边界定位、实时检测、数据高效、结构不对称
5. **Hidden Forgetting in Continual Multimodal Learning: When Accuracy Survives but Grounding Fails** | 标签：多模态持续学习、隐藏遗忘、证据依赖、RCL框架、反事实干预
6. **DisciplineGen-1M: A Large-Scale Dataset for Multidisciplinary Visual Generation and Editing** | 标签：多学科数据集、视觉生成、图像编辑、OCR、知识驱动生成
7. **Object Aligner: A Configurable JSON Schema Similarity Score for Graphs, Applied to LLM Prompt Optimization** | 标签：JSON相似度、结构对齐、图同构近似、LLM评估
8. **Condensing Large-Scale Datasets Directly with Minimal Information Loss** | 标签：数据集蒸馏、信息损失最小化、分布对齐、图像分类

## 四、今天 OCR / 文档解析论文里的主要创新点

- 多篇论文采用图或混合框架（如语义检测+LLM）解决阅读顺序问题，避免端到端训练的繁重标注
- 表格结构识别引入先验知识（如边界不对称）以轻量训练提升精度
- 零样本VLM评估证明其可替代传统OCR+YOLO方案，降低标注依赖
- 多模态学习关注隐藏遗忘，提出保持证据路径的框架
- 大规模多学科数据集推动知识驱动视觉生成与OCR编辑结合

## 五、后续 OCR 领域值得推进的改进方向

- 探索阅读顺序重建中的多模态图神经网络，同时整合文本语义与版面几何信息
- 将LLM混合方法扩展至生产级文档解析系统，优化推理速度与成本
- 研究VLM在更多地域车牌识别中的零样本迁移性，并微调以适应高精度需求
- 表格结构识别中融入跨列合并等更复杂先验，扩展至弯曲与部分遮挡表格
- 多模态持续学习设计无需回放的证据保持机制，结合参数隔离提升通用性
- 利用DisciplineGen-1M数据集开发学科感知的OCR后校正模型，提升图表数字识别准确性
- 基于Object Aligner开发面向OCR输出结构的自动评估与修复工具
- 将CIM数据集蒸馏方法引入文档图像分类与版面分析任务，实现高效样本压缩

## 六、工程落地启发

- Semantic-Guided Reading Order方法提供低资源场景的标注加速方案，可减少人工干预
- Reading Order Inference图框架无需训练即可部署，适合历史文档复杂版面
- VLM零样本车牌识别方案减少地域适配标注成本，但需注意小数据集局限
- ConRTF的EFL损失轻量高效，可作为现有TSR系统的即插即用模块
- RCL框架阻止多模态模型遗忘证据使用，提升文档图表等场景可靠性
- DisciplineGen-1M数据集可直接用于训练学科图表生成与编辑模型
- Object Aligner提供确定性JSON相似度，可用于LLM输出质量控制
- CIM蒸馏方法在单GPU上80分钟完成ImageNet-1K蒸馏，降低训练数据成本

## 七、优先关注论文

- **Semantic-Guided Reading Order Reconstruction in Historical Armenian Newspapers with LLMs**：混合LLM方法在低资源历史文档阅读顺序重建上取得显著改进，可能推广至其他语言与复杂版面
- **Reading Order Inference for Complex Document Layouts**：免训练图框架在特定版面超越传统方法，易于工程部署，关注其适用范围扩展
- **Evaluating Vision-Language Models as a Zero-Shot Learning Alternative to YOLO+OCR for Nigerian License Plate Recognition**：VLM零样本车牌识别潜力大，但小数据集验证需扩大评估以确认泛化性
- **ConRTF: Edge-Constrained Boundary Distribution Refinement for Realtime TransFormer Table Structure Recognition**：轻量边界损失显著提升表格结构识别，关注其与其他检测器的集成效果
- **Hidden Forgetting in Continual Multimodal Learning**：揭示多模态模型隐藏遗忘问题，RCL框架为持续学习提供新思路，需关注更大规模的验证

## 八、论文逐篇解析

### 1. Semantic-Guided Reading Order Reconstruction in Historical Armenian Newspapers with LLMs

- arXiv: [2607.00596v1](https://arxiv.org/abs/2607.00596v1)
- PDF: [下载链接](https://arxiv.org/pdf/2607.00596v1)
- 作者: Chahan Vidal-Gorène, Nadi Tomeh, Victoria Khurshudyan
- 发布时间: 2026-07-01T08:19:00Z
- 分类: cs.CV
- 相关性评分: 22
- 主题标签: 阅读顺序重建、历史文档、LLM、版面分析、低资源语言

**中文摘要**

> 本文针对历史亚美尼亚报纸中复杂版面与稀缺语言资源的阅读顺序重建问题，引入了一个包含66页的标注数据集，并比较了几何启发式、基于YOLO的版面分析、端到端文档模型ECLAIR以及结合语义区域检测与生成式LLM的混合方法。混合方法将排序错误最多减少76%，且在多页设置和噪声OCR下保持鲁棒性，旨在作为低资源场景下的数据引导策略。

**核心创新概述**

> 针对历史亚美尼亚报纸这一低资源语言与复杂版面场景，提出将语义区域检测与生成式LLM结合的混合方法用于阅读顺序重建，并发布专用Tesseract OCR模型。

**创新点拆解**

- 提出混合方法：语义区域检测+生成式LLM，用于阅读顺序重建
- 构建66页亚美尼亚历史报纸标注数据集
- 训练并公开面向历史亚美尼亚印刷体的专用Tesseract OCR模型

**当前局限**

> 方法并非面向生产环境，而是设计为数据引导策略；数据集规模较小（66页）。

**后续可改进方向**

- 扩展数据集规模和语言多样性
- 探索将混合方法迁移至端到端生产级系统
- 研究LLM在阅读顺序任务中的更高效使用方法

**工程启发**

> 为低资源历史文档的阅读顺序重建提供低成本数据引导方案，可加速标注流程，减少人工干预。

**为什么值得关注**

> 直接解决OCR后处理中的阅读顺序重建难题，特别针对复杂版面与低资源语言场景，具有典型学术价值。

**原始摘要**

This paper addresses reading order reconstruction in historical Armenian newspapers, which combine
complex layouts with limited language resources. We introduce a new annotated dataset of 66 pages
and compare geometric heuristics, YOLO-based layout parsing, an end-to-end document model ECLAIR,
and a hybrid method combining semantic zone detection with a generative LLM. Our hybrid method
achieves the lowest error rates of all evaluated approaches, reducing ordering errors by up to 76%
over the strongest geometric baseline, and remains robust in multi-page settings and under noisy
OCR. Rather than targeting production the method is designed as a data bootstrapping strategy
enabling rapid annotation in highly under-resourced scenarios. Alongside the dataset, we release a
specialized Tesseract OCR model for historical Armenian print.

---

### 2. Reading Order Inference for Complex Document Layouts

- arXiv: [2607.01018v1](https://arxiv.org/abs/2607.01018v1)
- PDF: [下载链接](https://arxiv.org/pdf/2607.01018v1)
- 作者: Iddo Hakim, Sharva Gogawale, Omer Ventura, Gal Grudka, Daria Vasyutinsky-Shapira, Berat Kurar-Barakat, Nachum Dershowitz
- 发布时间: 2026-07-01T14:52:00Z
- 分类: cs.CL, cs.AI, cs.CV, cs.DL
- 相关性评分: 17
- 主题标签: 阅读顺序推断、图框架、最大遗憾推理、复杂版面、历史文档

**中文摘要**

> 本文针对复杂文档版面（如Glossa Ordinaria布局）中的阅读顺序推断，提出一个免训练的基于图的框架。将每个OCR文本行作为节点，构建有向候选转移图，使用因果语言模型条件似然和BERT下一句预测得分加权集成作为边权重，通过最大遗憾推理规则恢复全局阅读顺序。在合成和真实数据集上优于递归XY-cut和LayoutReader。

**核心创新概述**

> 提出免训练的图框架，利用轻量语言模型信号和最大遗憾推理规则，解决非矩形环绕版面的阅读顺序问题，无需额外训练数据。

**创新点拆解**

- 构建基于有向图的候选转移框架
- 提出最大遗憾推理规则避免贪婪边选择的错误累积
- 集成因果语言模型和BERT NSP信号作为边权重

**当前局限**

> 在环绕版面（Glossa）上表现优秀，但对高度不规则或噪声版面可能仍需验证；语言模型信号可能依赖语言质量。

**后续可改进方向**

- 探索更丰富的语言模型信号（如跨模态特征）
- 将框架扩展至多语种或更复杂的版面类型
- 研究结合版面语义信息的端到端方法

**工程启发**

> 提供无需训练的阅读顺序推断方案，易于部署，尤其适用于历史文档和复杂版面数字化。

**为什么值得关注**

> 直接关联OCR阅读顺序推断这一核心问题，提出免训练且高效的解决方案，具有实用参考价值。

**原始摘要**

Reading order inference remains a critical bottleneck in the digitization of complex historical
manuscripts, where pages contain multiple spatially interleaved reading streams, the canonical
example being the Glossa Ordinaria layout, in which a central text is surrounded by commentaries
that wrap around it in non-rectangular, non-convex regions. We present a training-free, graph-based
framework: each OCR text line becomes a node in a directed candidate-transition graph, edges are
scored by a weighted additive ensemble of two lightweight language-model signals (causal language
model conditional likelihood and BERT next-sentence prediction, NSP; a third sentence-embedding
signal was evaluated but did not improve reading order), and the global reading order is recovered
as a degree-constrained directed path cover. To avoid the cascading "edge-theft" failures of greedy
edge selection, we propose a max-regret inference rule that prioritizes commitments with high
opportunity cost. We evaluate on synthetic Glossa Ordinaria grid layouts, on 23 ALTO page geometries
(10 historical source pages plus mirrored and flipped variants), and on a 140-page multi-column
English subset of OmniDocBench, comparing our method against the canonical recursive XY-cut
(PaddleOCR PP-StructureV3) and two LayoutReader variants (layout-only and text+layout) on identical
inputs. On wrap-around Glossa layouts our method recovers 95% of ground-truth successor edges on
average vs. XY-cut's 50%; on the OmniDocBench multi-column subset it reaches 88% macro edge accuracy
versus XY-cut's 75% and LayoutReader's 25%. The LayoutReader baselines transfer poorly due to a
word-level vs. line-level granularity mismatch. We additionally verify mirror-invariance under
horizontal and vertical page reflections: Our method changes by less than 1 percentage point,
classical XY-cut by 2 points, and LayoutReader-T by up to 8 points.

---

### 3. Evaluating Vision-Language Models as a Zero-Shot Learning Alternative to You Only Look Once and Optical Character Recognition for Nigerian License Plate Recognition

- arXiv: [2607.02025v1](https://arxiv.org/abs/2607.02025v1)
- PDF: [下载链接](https://arxiv.org/pdf/2607.02025v1)
- 作者: Ismail Ismail Tijjani, Ahmad Abubakar Mustapaha, Sunusi Ibrahim Muhammad, Muhammad Bashir Aliyu
- 发布时间: 2026-07-02T10:55:24Z
- 分类: cs.CV
- 相关性评分: 16
- 主题标签: 车牌识别、VLM、零样本学习、YOLO+OCR、字符错误率

**中文摘要**

> 本文探索视觉语言模型（VLM）作为零样本学习替代传统YOLO+OCR管线进行尼日利亚车牌识别的可能性。使用88张挑战性真实图像评估了五个VLM，基于字符错误率（CER），Gemini和Qwen在准确性和鲁棒性上显著优于其他模型，展示了VLM在无结构化环境中的优势。

**核心创新概述**

> 系统评估了多个先进VLM在尼日利亚车牌识别上的零样本性能，揭示了VLM相比YOLO+OCR的潜力与局限。

**创新点拆解**

- 首个针对尼日利亚车牌场景评估多个VLM零样本性能
- 使用真实挑战性图像（88张）进行评测
- 直接对比VLM与传统两阶段YOLO+OCR方案

**当前局限**

> 数据集规模较小（88张），仅覆盖尼日利亚场景，且未涉及模型微调或更多语言车牌。

**后续可改进方向**

- 扩大数据集规模和地域多样性
- 探索VLM微调以进一步提升性能
- 研究轻量化VLM在车牌识别中的实时部署可行性

**工程启发**

> 为车牌识别提供零样本VLM方案参考，减少标注依赖，适合快速部署至新地域。

**为什么值得关注**

> 展示VLM在OCR任务（车牌识别）中的零样本潜力，对低资源场景的OCR应用具有启示。

**原始摘要**

License Plate Recognition (LPR) systems are critical tools in traffic monitoring, security
enforcement, and urban mobility management. Traditional LPR systems often rely on a multi-stage
pipeline involving object detection using You Only Look Once (YOLO) and Optical Character
Recognition (OCR), which suffer from limitations such as high resource demands, poor performance in
unstructured environments, and the need for large annotated datasets. This study explores the
potential of Vision-Language Models (VLMs) as a unified, zeroshot learning solution for Nigerian
license plate recognition. Using a curated dataset of 88 challenging real-world images collected in
Nigeria, we evaluate five selected VLMs: Gemini 2.0 Flash Exp (Google DeepMind),
Qwen2.5-VL-7B-Instruct (Alibaba), GPT-4o (OpenAI), Claude 4 Sonnet (Anthropic), and Llama 3.2 Vision
90b (Meta). Results based on Character Error Rate (CER) reveal that Gemini and Qwen significantly
outperform other models in both accuracy and robustness, on the challenging image scenarios. This
work highlights the practical advantages of VLMs over YOLO+OCR, questions the claims by model
providers, and compares the performances of the VLMs.

---

### 4. ConRTF: Edge-Constrained Boundary Distribution Refinement for Realtime TransFormer Table Structure Recognition

- arXiv: [2607.00734v1](https://arxiv.org/abs/2607.00734v1)
- PDF: [下载链接](https://arxiv.org/pdf/2607.00734v1)
- 作者: Eliott Thomas, Tri-Cong Pham, Mickael Coustaty, Aurelie Joseph, Gaspar Deloin, Vincent Poulain d'Andecy, Jean-Marc Ogier, Antoine Doucet
- 发布时间: 2026-07-01T10:18:12Z
- 分类: cs.CV, cs.AI
- 相关性评分: 14
- 主题标签: 表格结构识别、边界定位、实时检测、数据高效、结构不对称

**中文摘要**

> 本文针对表格结构识别（TSR）中的边界定位问题，提出基于边界分布细化的边缘约束损失（EFL），利用表格中行列边界的不对称重要性：行元素强调水平边界，列元素强调垂直边界。在实时检测器D-FINE上实现，仅训练阶段生效，不改变推理管线，在PubTables-1M等数据集上提升+1.6 GriTS。

**核心创新概述**

> 形式化表格结构中行列边界的不对称重要性，并提出边缘约束损失（EFL）在实时检测器中实现精细边界定位，数据高效（2000-3000标注表）。

**创新点拆解**

- 提出边缘约束损失EFL，编码行列边界结构不对称先验
- 在D-FINE实时检测器中集成EFL，训练后推理无开销
- 实现高数据效率（2000-3000标注表即可保持精度）

**当前局限**

> 主要针对边界定位，未涉及极端复杂表格（如部分遮挡、弯曲表格）的评估。

**后续可改进方向**

- 将EFL扩展到其他检测框架或端到端模型
- 结合语义信息处理更多样化的表格样式
- 研究更广泛的边界不对称定义（如跨列合并）

**工程启发**

> 提供轻量化、高效的表格结构识别改进方案，易于集成到现有TSR系统中。

**为什么值得关注**

> 直接提升表格识别核心性能，数据高效且推理无额外开销，实用价值高。

**原始摘要**

Table Structure Recognition (TSR) aims to recover the row and column layout of tables from document
images, a key step in document understanding pipelines. Accurate TSR depends on precise boundary
localization: small errors in row or column boundaries can propagate into incorrect cell assignments
and structural inconsistencies. Yet detection-based approaches treat table elements as generic
objects, ignoring a fundamental property of table layout: rows and columns play structurally
distinct roles and their boundaries carry unequal importance. We propose an Edge-constrained Fine-
grained Localization loss (EFL) that formalizes this structural asymmetry by encoding table-specific
geometric priors into the training objective: row-like elements are supervised with emphasis on
their horizontal boundaries, while column-like elements prioritize vertical boundaries. Implemented
within a real-time detector with distribution-based boundary refinement (D-FINE), EFL operates
during training only and guides boundary refinement toward structurally meaningful adjustments with
no change to the inference pipeline. The proposed approach, ConRTF, is also data-efficient,
maintaining robust accuracy with as few as 2k--3k annotated tables. Experiments on PubTables-1M and
two private datasets show consistent improvements over the optimized baseline and several real-time
detectors including RT-DETRv2 and YOLOv10-11, with gains of up to +1.6 GriTS points at equal
inference speed.

---

### 5. Hidden Forgetting in Continual Multimodal Learning: When Accuracy Survives but Grounding Fails

- arXiv: [2607.02020v1](https://arxiv.org/abs/2607.02020v1)
- PDF: [下载链接](https://arxiv.org/pdf/2607.02020v1)
- 作者: Qianyu Chen, Canran Xiao, Runxuan Tang
- 发布时间: 2026-07-02T10:50:37Z
- 分类: cs.AI
- 相关性评分: 13
- 主题标签: 多模态持续学习、隐藏遗忘、证据依赖、RCL框架、反事实干预

**中文摘要**

> 本文揭示多模态大语言模型（MLLM）持续学习中一种被忽视的失败模式：隐藏的证据使用遗忘，即模型保持答案准确性但逐渐依赖不同或错误的多模态证据。提出RCL框架，冻结旧检查点作为参考，通过反事实通道干预估计师生证据依赖轮廓，联合优化任务学习、预测保持和证据保持，无需推理开销。在多个基准上减少遗忘。

**核心创新概述**

> 首次提出并量化多模态持续学习中的“隐藏证据使用遗忘”，并设计免回放的RCL框架来同时保持答案和证据路径。

**创新点拆解**

- 识别隐藏证据使用遗忘问题：答案准确但证据通道漂移
- 提出RCL框架：反事实通道干预+联合优化保持预测与证据
- 无需回放或增加推理成本

**当前局限**

> 实验基于特定MLLM架构和数据集，通用性需进一步验证；反事实干预计算成本可能随模态增多增加。

**后续可改进方向**

- 扩展到更多模态和更大规模模型
- 探索更高效的证据估计方法
- 结合回放或参数隔离策略对比研究

**工程启发**

> 为多模态连续学习提供保持证据路径的实用框架，提升模型在文档、图表等场景的可靠性。

**为什么值得关注**

> 直接关联OCR在多模态文档理解中的证据使用稳定性，对持续学习环境下的文档分析有重要启示。

**原始摘要**

Multimodal large language models must continually adapt to evolving tasks and domains, yet standard
continual learning metrics mainly measure whether old answers remain correct, leaving the stability
of multimodal grounding largely unexamined. We study this overlooked failure mode and ask whether a
continually adapted MLLM can preserve not only what it answers, but also how it uses visual,
textual, OCR, chart, and document evidence. We identify \emph{hidden evidence-use forgetting}, where
answer accuracy is retained while the model silently shifts toward different or less grounded
evidence channels, and propose \textsc{RCL}, a replay-free reliance-constrained continual learning
framework. \textsc{RCL} freezes the previous checkpoint as a behavioral reference, estimates teacher
and student evidence-reliance profiles through counterfactual channel interventions, and jointly
optimizes task learning, prediction preservation, and reliance preservation without adding
inference-time cost. Across CoIN, COAST, MCITlib, and an evidence-sensitive multimodal stream,
\textsc{RCL} consistently improves final performance and reduces forgetting over replay-free, PEFT,
routing, and memory-assisted baselines, while substantially lowering modality reliance drift,
dominant evidence flips, and hidden forgetting rates. These results suggest that robust continual
multimodal learning requires preserving the evidence path behind correct answers, not merely the
answers themselves.

---

### 6. DisciplineGen-1M: A Large-Scale Dataset for Multidisciplinary Visual Generation and Editing

- arXiv: [2607.02290v1](https://arxiv.org/abs/2607.02290v1)
- PDF: [下载链接](https://arxiv.org/pdf/2607.02290v1)
- 作者: Zhaokai Wang, Mingxin Liu, Zirun Zhu, Ziqian Fan, Yiguo He, Mohan Zhang, Leyao Gu, Xiangyu Zhao, Ning Liao, Shaofeng Zhang, Xuanhe Zhou, Zhihang Zhong, Junchi Yan, Xue Yang
- 发布时间: 2026-07-02T15:07:47Z
- 分类: cs.CV
- 相关性评分: 9
- 主题标签: 多学科数据集、视觉生成、图像编辑、OCR、知识驱动生成

**中文摘要**

> 本文发布DisciplineGen-1M，一个百万级多学科视觉生成与编辑数据集，涵盖数学、物理等10个学科。提出结合矢量图形渲染、OCR编辑等管道构建数据集。基于此，提出学科知情的推理生成模型，在学科基准上显著优于开源基线。

**核心创新概述**

> 构建大规模多学科知识密集型视觉生成数据集，并设计学科推理生成模型，推动图像生成从美学向知识可靠转变。

**创新点拆解**

- 构建120万样本的多学科视觉数据集DisciplineGen-1M
- 设计可扩展的管道：矢量渲染+OCR编辑+程序合成+文本到图像过滤
- 提出学科知情的推理生成模型用于文本到图像生成与编辑

**当前局限**

> 数据集主要覆盖常见学科，可能缺少新兴或交叉学科；生成的图像质量依赖管道各步骤质量。

**后续可改进方向**

- 扩展学科覆盖范围和样本多样性
- 探索更精细的学科事实验证机制
- 结合OCR和版面分析提升图表生成准确性

**工程启发**

> 为多学科文档图表生成提供大规模数据和模型基础，有助于学术可视化、教育材料自动生成。

**为什么值得关注**

> 数据集依赖OCR技术进行构建和编辑，同时涉及图表生成中的文字布局，对文档生成方向有参考。

**原始摘要**

Recent image generation and editing models can produce visually appealing natural images, yet they
remain unreliable when the target image is a knowledge-intensive diagram whose correctness depends
on disciplinary concepts, symbolic structure, and precise spatial relations. We introduce
DisciplineGen-1M, a million-scale multidisciplinary dataset that supports text-to-image generation
and image editing. It contains 1.2M samples spanning mathematics, physics, chemistry, biology,
geography, computer science, economics, history, music, and sports. To construct the dataset, we
design a scalable framework that combines vector-graphics rendering, OCR-based editing, curated
programmatic synthesis, and large-scale text-to-image filtering. These pipelines produce captions,
editing instructions, structured annotations, and paired images with controllable semantic
differences. Building on DisciplineGen-1M, we further introduce a discipline-informed reasoning-
generation model for both text-to-image generation and image editing. Experiments on discipline-
related benchmarks, GenExam and GRADE, show substantial improvements over open-source baselines,
while evaluations on general reasoning-informed benchmarks, WISE and RISE, further indicate broader
transfer. The results suggest that large-scale structured academic visual data is a key ingredient
for moving image generation from aesthetic plausibility toward verifiable knowledge-grounded visual
creation. We will publicly release our dataset, model, and source code of the data curation pipeline
to ensure reproducibility and benefit future research.

---

### 7. Object Aligner: A Configurable JSON Schema Similarity Score for Graphs, Applied to LLM Prompt Optimization

- arXiv: [2607.01972v1](https://arxiv.org/abs/2607.01972v1)
- PDF: [下载链接](https://arxiv.org/pdf/2607.01972v1)
- 作者: Jan Drchal
- 发布时间: 2026-07-02T10:07:34Z
- 分类: cs.CL, cs.AI, cs.LG
- 相关性评分: 6
- 主题标签: JSON相似度、结构对齐、图同构近似、LLM评估

**中文摘要**

> 本文提出Object Aligner，一个开源的Python库，用于确定性地计算两个JSON对象的相似度。它通过递归地对其树结构（无序集合使用匈牙利算法，有序序列使用序列对齐），并在模式声明的粒度上给予部分分数。核心贡献是引用对齐，通过Weisfeiler-Leman颜色细化近似图同构，推断金标准与候选标识符之间的双射，使分数对重新标记不变。该库还提供有序序列对齐和修复建议。

**核心创新概述**

> 提出引用对齐方法，通过Weisfeiler-Leman颜色细化处理图/超图结构的JSON相似度，解决了标识符重新标记导致的分数不稳定问题；配置方式完全基于JSON Schema扩展，无需编码。

**创新点拆解**

- 引用对齐：通过Weisfeiler-Leman颜色细化近似图同构，处理图/超图结构，使相似度分数对标识符重新标记不变
- 可配置性：完全通过JSON Schema扩展配置，无需编写代码即可适应新任务
- 递归对齐：结合匈牙利算法（无序）和序列对齐（有序），在模式声明的粒度上给予部分分数
- 修复建议：对齐过程自动定位不匹配，无额外成本输出排名修复建议

**当前局限**

> 依赖图同构近似，精确恢复标识符双射是NP难问题，近似可能在某些复杂图上失效；仅适用于JSON Schema定义的结构化数据，对自由文本或非结构化数据不适用。

**后续可改进方向**

- 探索更高效的图同构近似方法，提升引用对齐的准确性和扩展性
- 扩展对超图及更复杂结构的支持，例如带权图或动态图
- 集成到LLM生成流程中，作为实时反馈或强化学习奖励信号
- 开发自动Schema推断工具，减少人工标注成本

**工程启发**

> 提供开源、确定性的JSON相似度度量，可直接用于LLM输出验证、信息提取评估、工具调用质量监控等场景，避免昂贵且非确定的LLM裁判，降低工程成本。

**为什么值得关注**

> 直接解决了OCR文档解析中结构化输出（如JSON）与金标准的精确匹配问题，可用于评估解析结果的质量，以及指导解析模型的优化。

**原始摘要**

Large language models (LLMs) are often asked to produce JSON conforming to a fixed schema, powering
information extraction, tool calling, agentic planning, and knowledge-graph construction. Measuring
how closely an output matches a gold reference is essential yet surprisingly hard: exact match is
brittle, text similarity ignores structure, and an LLM judge is expensive, opaque, and non-
deterministic. We address this with Object Aligner (OA), an open-source Python library that scores
two JSON objects deterministically by recursively aligning their trees (the Hungarian algorithm for
unordered collections, sequence alignment for ordered ones) and awarding partial credit at the
granularity the schema declares. The Object Aligner is configured entirely through a set of JSON
Schema extensions, so adapting it to a new task involves annotating a schema rather than writing
code. Complex structured data, however, are rarely flat trees: records may form graphs or
hypergraphs keyed by arbitrary identifiers, breaking the assumptions of prior similarity metrics.
Our central contribution, referential alignment, closes this gap by inferring a bijection between
gold and candidate identifiers and scoring every reference through it, so the score is invariant to
relabeling. Since recovering this bijection exactly is graph isomorphism, the Object Aligner
approximates it with Weisfeiler-Leman color refinement. An order-sensitive sequence regime targets
ranking and planning. Since the same alignment localizes every mismatch, the Object Aligner emits
ranked repair suggestions at no extra cost. Used as a reward inside the GEPA prompt optimizer,
Object Aligner helps or stays neutral across all datasets.

---

### 8. Condensing Large-Scale Datasets Directly with Minimal Information Loss

- arXiv: [2607.00916v1](https://arxiv.org/abs/2607.00916v1)
- PDF: [下载链接](https://arxiv.org/pdf/2607.00916v1)
- 作者: Xinyi Shang, Peng Sun, Bei Shi, Zixuan Wang, Tao Lin
- 发布时间: 2026-07-01T13:21:44Z
- 分类: cs.CV
- 相关性评分: 6
- 主题标签: 数据集蒸馏、信息损失最小化、分布对齐、图像分类

**中文摘要**

> 本文提出CIM框架，通过直接对齐原始数据集与合成数据集的分布，最小化信息损失，取代传统的SQUEEZE-RECOVER-RELABEL三阶段方法。实验表明，CIM在ImageNet-1K上以IPC=10仅需80分钟在单张RTX-4090上蒸馏，ResNet-18 Top-1准确率达48.7%，超过NRR-DD和DELT 2.6%和2.9%。

**核心创新概述**

> 揭示并解决了传统数据集蒸馏中双压缩过程导致的信息损失和分布偏移问题；提出基于度量的框架（CIM）直接优化信息差距，避免模型作为不可靠标签器的问题。

**创新点拆解**

- 直接信息对齐：抛弃双压缩范式，通过最小化原始与合成数据分布之间的信息间隙进行蒸馏
- 度量驱动框架：显式量化并最小化信息损失，确保高保真度浓缩
- 消除RELABEL缺陷：理论证明分布偏移使RELABEL策略失效，新框架自然满足重标记前提
- 高效蒸馏：在单GPU上80分钟完成ImageNet-1K IPC=10蒸馏，达到SOTA准确率

**当前局限**

> 仅在图像分类任务上验证，未探索更复杂的任务（如目标检测、语义分割）；计算开销可能随IPC增加而显著增长；未讨论跨任务迁移能力。

**后续可改进方向**

- 扩展到更复杂的计算机视觉任务，如目标检测、实例分割
- 研究不同IPC设置下的最优策略，平衡效率与保真度
- 探索跨架构泛化能力，提升合成数据在不同模型上的性能
- 融合自监督或无监督方法，进一步减少对原始标签的依赖

**工程启发**

> 显著降低大规模数据集蒸馏的时间和计算成本，单GPU即可完成ImageNet-1K蒸馏，为实际应用中的模型训练提供高效数据压缩方案。

**为什么值得关注**

> 数据集蒸馏技术可应用于OCR文档解析中的训练数据生成，通过压缩真实文档数据集加速模型训练，同时保持解析精度。

**原始摘要**

Recent advancements in scaling dataset distillation rely heavily on decoupled information extraction
pipelines, comprising SQUEEZE, RECOVER, and RELABEL stages. Despite their scalability to large-scale
datasets, these methods suffer from prohibitive computational overhead and poor cross-architecture
generalization. In this paper, we reveal the root cause of these bottlenecks: the implicit dual-
compression process, from data to model and back to images, inherently induces severe information
loss. Crucially, we empirically and theoretically demonstrate that this loss creates a distribution
shift that fundamentally compromises the widely adopted RELABEL strategy, transforming the pre-
trained model into an unreliable labeler that yields sub-optimal labels. To overcome these critical
flaws, we propose CIM, a novel, metric-driven framework that abandons the flawed dual-compression
paradigm. Instead, CIM explicitly quantifies and minimizes the information gap between the original
and synthetic datasets. By directly aligning the data distributions, our approach ensures high-
fidelity information condensation and inherently satisfies the prerequisites for effective
relabeling. Extensive experiments demonstrate that CIM establishes a new state-of-the-art. Notably,
it distills ImageNet-1K at an IPC=10 in merely 80 minutes on a single RTX-4090 GPU, achieving an
unprecedented 48.7% Top-1 accuracy on ResNet-18 and significantly outperforming previous SOTA
approaches, such as NRR-DD and DELT, by 2.6% and 2.9%, respectively. Our code is available at
https://github.com/LINs-lab/CIM.

---
