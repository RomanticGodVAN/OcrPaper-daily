# OCR / 文档解析研究日报（2026-06-25）

## 报告说明

- 检索源：arXiv API
- 检索查询：`(all:"document parsing" OR all:"document understanding" OR all:"optical character recognition" OR all:OCR OR all:"layout analysis" OR all:"document layout analysis" OR all:"text recognition" OR all:"table recognition" OR all:"form understanding" OR all:"document intelligence" OR all:"page understanding" OR all:"scene text recognition" OR all:"handwritten text recognition" OR all:"information extraction") AND (cat:cs.CV OR cat:cs.AI OR cat:cs.CL OR cat:eess.IV)`
- 生成时间（UTC）：`2026-06-25 05:15:30`
- 大模型综合分析：`开启`

## 一、今日执行摘要

> 今日论文集中在OCR鲁棒性评估、艺术字识别、置信度估计、手写识别微调、图像质量门控、多模态推理效率及文档解析加速等方面。核心趋势是向鲁棒性、小样本、低资源、快速推理和可靠置信度发展。

## 二、今日趋势判断

多篇论文关注模型在真实场景中的鲁棒性与可靠性，如OCR-Robust基准、ExtractConf置信度引擎、MagikaDocumentFromPixel模糊门控。同时，针对特定领域（艺术字、中世纪手稿、低资源语言）的数据集和方法创新活跃。此外，推理加速（P-MTP）和高效微调（TrOCR消融）也是重要方向。

## 三、今日论文概览

1. **How Robust is OCR-Reasoning? Evaluating OCR-Reasoning Robustness of Vision-Language Models under Visual Perturbations** | 标签：OCR鲁棒性、视觉扰动、基准测评
2. **Advancing WordArt-Oriented Scene Text Recognition: Datasets and Methods** | 标签：艺术字识别、合成数据、场景文本识别
3. **Beyond Logprobs: A Multi-Signal Confidence Engine for LLM-Based Document Field Extraction** | 标签：置信度估计、文档字段提取、LLM
4. **TrOCR for Medieval HTR: A Systematic Ablation Study with Cross-Dataset Validation** | 标签：手写文本识别、微调策略、中世纪手稿
5. **Edges Before Embeddings: A Confidence-Aware Blur Gate for Vision-Language Pipelines** | 标签：图像质量评估、模糊检测、流水线优化
6. **Latent Visual States for Efficient Multimodal Reasoning** | 标签：多模态推理、潜在表示、端到端优化
7. **L3Cube-MahaPOS: A Marathi Part-of-Speech Tagging Dataset and BERT Models** | 标签：数据集、词性标注、低资源语言、Transformer
8. **Overview of HIPE-2026: Person-Place Relation Extraction from Multilingual Historical Texts** | 标签：关系抽取、历史文档、OCR噪声、多语言、评测
9. **Probabilistic Agents in Deterministic Audits: Evaluating Multi-Agent Systems for Automated Audits Based on the German IT-Grundschutz** | 标签：多智能体系统、检索增强生成、自动化审计、文档处理
10. **WinDOM: Self-Family Distillation for Small-Model GUI Grounding** | 标签：GUI接地、蒸馏、强化学习、数据采集、小模型
11. **P-MTP: Efficient Document Parsing via Multi-Token Prediction with Progressive Depth Scaling** | 标签：文档解析、推理加速、多token预测、视觉语言模型
12. **AI-PAVE-Br: Leveraging Large Language Models for Enhanced Product Attribute Value Extraction through a Golden Set Approach** | 标签：属性抽取、电商、葡萄牙语、大语言模型、数据集

## 四、今天 OCR / 文档解析论文里的主要创新点

- 系统评估视觉扰动对OCR推理的影响并提出新指标（相对损坏保留等）。
- 合成大规模高质量数据集（WATER-S 200万、MahaPOS 3.2万、WinDOM 5.4万）以弥补真实标注不足。
- 融合多信号（不一致性、不确定性、OCR质量）进行置信度估计，无需领域规则。
- 通过消融实验总结微调策略（冻结层、对比度归一化），提供实用指导。
- 将经典图像处理（如拉普拉斯边缘检测）与深度网络结合，提升效率。
- 利用潜在连续表示（Latent_slot tokens）替代离散输出进行多模态推理。
- 提出渐进式多token预测和动态草稿机制加速文档解析推理。

## 五、后续 OCR 领域值得推进的改进方向

- 扩展OCR-Robust基准至语义扰动和对抗样本，结合图像质量门控构建鲁棒流水线。
- 收集真实艺术字标注数据并探索多语言艺术字识别模型的迁移能力。
- 设计无需黑盒模型内部信号的置信度方法，以适应更多API限制。
- 将TrOCR微调策略推广到更多历史文档类型，并研究LoRA等高效微调。
- 将运动模糊门控扩展到高斯模糊和散焦，并嵌入端到端训练。
- 提升潜在多模态表示的可解释性，并压缩序列长度以降低内存。
- 探索跨语言无监督域适应进一步降低低资源语言标注成本。
- 研究OCR噪声对特定关系抽取的影响并设计噪声鲁棒的抽取模型。
- 在更多安全标准和企业场景下验证多智能体自动化审计系统。
- 将P-MTP与硬件优化结合，实现更深展望的多token预测以进一步提升加速比。

## 六、工程落地启发

- 部署OCR系统前应使用OCR-Robust基准评估鲁棒性，优先选择对扰动不敏感的模型。
- 艺术字识别WATERec模型可直接用于设计稿场景，合成数据WATER-S可辅助训练。
- 置信度引擎ExtractConf可集成到文档提取流水线，通过多信号融合降低自动化风险。
- 微调TrOCR时冻结少量编解码器层不影响精度，对比度归一化可被其他预处理替代。
- 使用MagikaDocumentFromPixel作为预处理门控，可快速过滤模糊图像节省下游资源。
- EVA潜在推理框架可替代多模态链式调用，但需注意可解释性。
- 低资源语言POS标注可复用MahaPOS的预处理和模型策略。
- HIPE-2026评测框架可用于历史文档关系抽取系统的性能与效率评估。
- WinDOM数据采集方法可零成本获取GUI接地数据，适合低资源场景。
- P-MTP多token预测可集成到文档解析VLM中，实现最高5倍加速。

## 七、优先关注论文

- **How Robust is OCR-Reasoning? Evaluating OCR-Reasoning Robustness of Vision-Language Models under Visual Perturbations**：首个OCR推理鲁棒性基准，其指标和扰动集可能成为行业标准，后续扩展扰动类型后影响更大。
- **Advancing WordArt-Oriented Scene Text Recognition: Datasets and Methods**：艺术字识别突破性工作，合成数据WATER-S和WATERec模型可直接提升实际应用效果，关注后续真实数据发布。
- **Beyond Logprobs: A Multi-Signal Confidence Engine for LLM-Based Document Field Extraction**：置信度估计是高可靠提取的关键，ExtractConf的创新多信号融合思路可能被广泛应用，关注其黑盒适配版本。
- **P-MTP: Efficient Document Parsing via Multi-Token Prediction with Progressive Depth Scaling**：5倍加速效果明显，若能结合硬件优化将极大提升高吞吐文档解析性能，关注后续稳定性改进。

## 八、论文逐篇解析

### 1. How Robust is OCR-Reasoning? Evaluating OCR-Reasoning Robustness of Vision-Language Models under Visual Perturbations

- arXiv: [2606.26041v1](https://arxiv.org/abs/2606.26041v1)
- PDF: [下载链接](https://arxiv.org/pdf/2606.26041v1)
- 作者: Yuxing Cheng, Yuan Wu, Yi Chang
- 发布时间: 2026-06-24T17:15:42Z
- 分类: cs.CV, cs.CL
- 相关性评分: 22
- 主题标签: OCR鲁棒性、视觉扰动、基准测评

**中文摘要**

> 提出OCR-Robust基准，系统评估视觉语言模型在视觉扰动下的OCR推理鲁棒性。包含812个样本，覆盖文档、场景文本、图表等，选择5种扰动类型、3种严重级别。实验发现高clean准确率不一定意味着强鲁棒性，图表比文档更脆弱。

**核心创新概述**

> 首个针对OCR推理鲁棒性的系统评估基准，定义了相对损坏保留等新指标。

**创新点拆解**

- 构建了包含OCR1.0和OCR2.0两个子集的鲁棒性基准
- 通过预实验筛选出5种代表性扰动和3个严重级别
- 提出相对损坏保留、最坏情况保留和复合鲁棒性指数等新指标

**当前局限**

> 扰动类型有限，仅针对视觉层面扰动，未涉及语义或对抗扰动。

**后续可改进方向**

- 扩展扰动类型覆盖更多真实场景噪声
- 研究模型架构设计对鲁棒性的影响
- 探索鲁棒性增强方法如对抗训练

**工程启发**

> 为OCR系统部署提供鲁棒性评估工具，指导模型选择和优化。

**为什么值得关注**

> 直接关注OCR推理鲁棒性，对实际文档分析系统的可靠性有重要参考价值。

**原始摘要**

Vision-language models (VLMs) have achieved strong performance on OCR-based benchmarks and
increasingly focused on text-rich understanding, but their robustness under controlled visual
degradation remains insufficiently understood. This gap is critical for OCR reasoning, where visual
corruption can induce OCR errors and structural distortions, thereby introducing uncertainty into
the reasoning task. To systematically study this problem, we introduce OCR-Robust, a benchmark
designed for evaluating OCR reasoning robustness under visual perturbations. It contains 812 samples
across two complementary subsets: OCR1.0, covering documents, scene text, receipts, handwriting, and
mathematical content, and OCR2.0, focusing on charts, geometry diagrams, and tables. To enable
efficient yet informative evaluation, we conduct a pilot study over 18 candidate perturbations and
select 5 representative types at 3 severity levels each based on their impact and cross-model
discriminability. We evaluate robustness using clean accuracy, Relative Corruption Retention (RCR),
Worst-Case Retention (WCR), and a composite Corruption Robustness Index (CRI), and benchmark 18
models spanning proprietary systems, open-source VLMs, and OCR+LLM pipelines. Our results show that
higher clean accuracy does not necessarily imply stronger robustness, and that models can suffer
pronounced degradation in the worst case on OCR tasks that are sensitive to structure, and charts
and tables are substantially more fragile than document-like inputs under perturbation.

---

### 2. Advancing WordArt-Oriented Scene Text Recognition: Datasets and Methods

- arXiv: [2606.24484v1](https://arxiv.org/abs/2606.24484v1)
- PDF: [下载链接](https://arxiv.org/pdf/2606.24484v1)
- 作者: Xingsong Ye, Yongkun Du, Jiaxin Zhang, Haojie Zhang, Chong Sun, Chen Li, Jing Lyu, Zhineng Chen
- 发布时间: 2026-06-23T12:18:50Z
- 分类: cs.CV
- 相关性评分: 22
- 主题标签: 艺术字识别、合成数据、场景文本识别

**中文摘要**

> 针对艺术字场景文本识别（WATER）任务，构建200万规模合成数据集WATER-S，并提出WATERec模型，采用支持任意形状输入的视觉编码器和自回归解码器，在WordArt-Bench上达到90.40%准确率，大幅超越通用和OCR专用视觉语言模型。

**核心创新概述**

> 首次系统解决艺术字识别难题，从数据和模型两方面突破固定模板STR瓶颈。

**创新点拆解**

- 构建200万规模艺术字合成数据集WATER-S，含SynthWordArt渲染和VLM生成两种子集
- 提出WATERec模型，采用适应任意形状输入的视觉编码器和自回归解码器
- 结合Qwen3-VL和Z-Image生成多样化真实感数据

**当前局限**

> 主要依赖合成数据，真实艺术字数据的泛化性有待验证。

**后续可改进方向**

- 收集更多真实艺术字标注数据
- 探索轻量化模型结构以适应移动端部署
- 扩展到多语言艺术字识别

**工程启发**

> 显著提升艺术字识别准确率，可直接应用于设计稿、广告等场景。

**为什么值得关注**

> 针对OCR领域难例艺术字，提供数据和方法双重参考。

**原始摘要**

WordArt (artistic text) features highly customized fonts, textures, and layouts, making WordArt-
oriented scene TExt Recognition (WATER) substantially more challenging than general Scene Text
Recognition (STR). Existing STR datasets and methods, typically built around regular scene text and
fixed-template inputs, struggle to scale to WATER. Thus, we aim to advance this task from both data
and model perspectives. On the data side, we construct a 2M synthetic dataset, WATER-S, with the
scale improved by hundreds of times compared to existing artistic text data. WATER-S consists of two
complementary subsets. One rendered by an upgraded rendering pipeline (SynthWordArt), which provides
highly accurate and controllable synthetic WordArt data. The other is generated by combining
Qwen3-VL for prompt mining and Z-Image for image synthesis, which improves the coverage of realistic
and diverse data. On the model side, we propose WATERec. It adopts an visual encoder supporting
arbitrary-shaped inputs and an autoregressive decoder to model complex layouts, structurally
breaking the bottleneck of fixed-template STR on WordArt. Experiments show that this architecture
outperforms prior STR methods, achieving state-of-the-art performance on irregular texts such as
WordArt. Together with WATER-R, carefully reorganized from existing real STR data, our strong
baseline with the new synthetic data and model design reaches 90.40% accuracy on WordArt-Bench,
surpassing both general-purpose and OCR-specialized vision-language models by a large margin. Code
and data are available at https://github.com/YesianRohn/WATER.

---

### 3. Beyond Logprobs: A Multi-Signal Confidence Engine for LLM-Based Document Field Extraction

- arXiv: [2606.24420v1](https://arxiv.org/abs/2606.24420v1)
- PDF: [下载链接](https://arxiv.org/pdf/2606.24420v1)
- 作者: Nitesh Kumar
- 发布时间: 2026-06-23T10:58:08Z
- 分类: cs.CL
- 相关性评分: 21
- 主题标签: 置信度估计、文档字段提取、LLM

**中文摘要**

> 提出ExtractConf，一种跨领域、字段无关的置信度估计引擎，通过双通路（猎人-映射器）的不一致性、LLM内部不确定性、OCR和图像质量等多信号融合，在DocILE上ROC AUC达0.928，将选择性预测风险降低70%。

**核心创新概述**

> 利用双通路不同失效模式的互补性进行置信度估计，无需领域规则或重训练。

**创新点拆解**

- 设计猎人-映射器双通路架构，利用不对称失效模式进行置信度估计
- 融合跨调用不一致性、LLM不确定性、OCR质量等多维信号
- 无需领域规则或重训的场无关置信度分类器

**当前局限**

> 依赖LLM内部不确定性信号，对黑盒模型不适用。

**后续可改进方向**

- 适配更多LLM架构和API
- 扩展到更复杂的嵌套字段提取
- 结合主动学习减少人工审核成本

**工程启发**

> 为高可靠性文档提取系统提供实用置信度评估，减少自动化风险。

**为什么值得关注**

> 解决OCR+LLM文档提取中的置信度估计关键问题，对生产级系统有直接价值。

**原始摘要**

In high-stakes document processing pipelines, including financial reconciliation, compliance
verification, and procurement automation, an LLM extraction that is silently wrong is more dangerous
than one that is visibly absent. The central challenge is not extraction accuracy alone but reliable
confidence estimation: knowing, field by field, whether an extraction can be trusted for automation
or deferred to human review. Token-level log-probabilities, verbalized confidence, and multi-sample
self-consistency all collapse toward all-positive behaviour at practical thresholds, offering no
reliable separation between trustworthy and untrustworthy extractions. We present ExtractConf, a
cross-domain, field-agnostic confidence engine that grounds confidence estimation in two
structurally different readings of the same document. A field-guided Hunter call extracts each field
under schema-slot completion pressure; a document-guided Mapper call scans holistically and surfaces
values grounded in document content. This asymmetry yields different failure modes: Hunter
hallucinates values for absent fields, while Mapper misses visually non-salient ones. Their
disagreement is independently informative. ExtractConf fuses cross-call disagreement, LLM-internal
uncertainty, OCR, image quality, and spatial layout into a classifier requiring no domain-specific
rules or retraining. On DocILE (55-field invoices, 26% failure rate), it achieves 0.928 ROC AUC and
reduces selective prediction risk by 70% over logprob-mean. At 80% coverage, accuracy reaches 99.1%,
enabling a practical human-in-the-loop workflow. Zero-shot transfer to CORD receipts achieves 0.858
AUC; lightweight Lasso recalibration reduces ECE by 89% and Brier by 43%, confirming the signals
generalise across document domains.

---

### 4. TrOCR for Medieval HTR: A Systematic Ablation Study with Cross-Dataset Validation

- arXiv: [2606.24302v1](https://arxiv.org/abs/2606.24302v1)
- PDF: [下载链接](https://arxiv.org/pdf/2606.24302v1)
- 作者: Sachin Sharma, Michele Flammini, Federico Simonetta
- 发布时间: 2026-06-23T08:34:18Z
- 分类: cs.CV, cs.DL
- 相关性评分: 16
- 主题标签: 手写文本识别、微调策略、中世纪手稿

**中文摘要**

> 通过系统消融实验研究TrOCR在手写中世纪手稿识别中对比度归一化、数据增强和层冻结的影响。在13世纪意大利手稿上最佳配置CER为8.03%，发现冻结少量编解码器层不影响精度，对比度归一化可被优化替代。

**核心创新概述**

> 首次对TrOCR在中世纪手稿上的微调策略进行系统性消融和跨数据集验证。

**创新点拆解**

- 系统对比了13种配置下冻结层数的影响
- 发现解码器冻结阈值比编码器更具跨数据集可迁移性
- 使用Grad-CAM和注意力图诊断错误模式

**当前局限**

> 仅在单一手稿和READ-16数据集上验证，推广性有限。

**后续可改进方向**

- 扩展到更多历史文档类型和语言
- 探索更高效的微调方法如LoRA
- 结合无监督域适应减少标注依赖

**工程启发**

> 为手写文本识别微调提供实用指导，减少调参成本。

**为什么值得关注**

> 针对OCR中历史文档识别这一难点，提供微调策略参考。

**原始摘要**

Fine-tuning transformer-based handwritten text recognition (HTR) models on medieval manuscripts is
challenging because these models are pre-trained on modern text and must adapt to a very different
visual domain. This paper studies how three controllable fine-tuning choices (contrast
normalization, data augmentation, and layer freezing) affect recognition accuracy when adapting
TrOCR to small historical datasets. We run controlled experiments on a 13th-century Italian
manuscript (I-CT 91 "Cortonese") and replicate the same experimental grid on the public READ-16
benchmark as robustness evidence. On Cortonese, our best configuration achieves 8.03% character
error rate (CER). Statistical comparisons across 13 configurations show that freezing up to three
encoder layers or six decoder layers does not significantly harm accuracy, while deeper freezing
becomes progressively detrimental. Removing contrast normalization (CLAHE) yields 7.84% CER,
comparable to a domain-specialized baseline, suggesting strong optimization can reduce reliance on
image preprocessing. Cross-dataset validation on READ-16 shows that decoder freezing thresholds
transfer more robustly than encoder thresholds, and combined freezing strategies require dataset-
specific re-validation. Finally, we use Grad-CAM gradient attributions and decoder cross-attention
maps to diagnose error patterns and failure modes revealed by the ablations. Source code is
available at https://github.com/LaudareProject/TrOCR-analysis

---

### 5. Edges Before Embeddings: A Confidence-Aware Blur Gate for Vision-Language Pipelines

- arXiv: [2606.25838v1](https://arxiv.org/abs/2606.25838v1)
- PDF: [下载链接](https://arxiv.org/pdf/2606.25838v1)
- 作者: Duy Tran Thanh
- 发布时间: 2026-06-24T13:51:42Z
- 分类: cs.CV, cs.AI
- 相关性评分: 13
- 主题标签: 图像质量评估、模糊检测、流水线优化

**中文摘要**

> 提出MagikaDocumentFromPixel，一种轻量级CPU友好图像模糊门控，约7ms判定单图清晰/模糊/不确定。通过46配置搜索发现输入分辨率是关键，设计边缘先验模块EPM利用拉普拉斯幅度辅助分类，在GoPro Large上F1=0.9803，模型仅17MB。

**核心创新概述**

> 采用边缘先验模块将经典模糊检测经验引入深度网络，实现高效门控。

**创新点拆解**

- 通过大规模配置搜索确定输入分辨率决定性能，容量仅在≥384px时有效
- 提出边缘先验模块（EPM），将拉普拉斯幅度作为辅助输入通道
- 设计基于选择性预测的置信度感知路由

**当前局限**

> 仅评估运动模糊分布，实验依赖单种子，校准未量化。

**后续可改进方向**

- 扩展到高斯模糊、散焦等多种模糊类型
- 研究跨域迁移性
- 量化校准以实现更可靠的拒绝选项

**工程启发**

> 提供低开销的图像质量门控，可嵌入预处理流水线节省下游计算资源。

**为什么值得关注**

> 直接提升OCR/文档分析系统的鲁棒性，避免无效计算。

**原始摘要**

Production vision pipelines silently degrade on blurry input, wasting compute on downstream OCR,
retrieval, and vision-language model (VLM) calls that cannot recover a usable output. We present
MagikaDocumentFromPixel, a lightweight, CPU-friendly image quality gate that classifies a single
image as sharp, blurred, or uncertain in roughly 7 ms on a single CPU core. The contributions are
(i) a recipe selected from a 46-configuration, 8-sweep empirical search that isolates input
resolution as the dominant lever and shows architecture capacity only pays off at >= 384 px; (ii) a
confidence-aware routing formalism grounded in classical selective prediction; (iii) the Edge Prior
Module (EPM), a Laplacian-magnitude auxiliary input channel that gives the network direct access to
the spectral evidence that classical blur heuristics rely on and that lifts test F1 by +1.3 points
in a matched-env comparison; and (iv) an observation that the gate is one instance of a recurring
design pattern that appears independently in Magika content-type detection, risk-controlled OCR with
VLMs, and DocVLM. The final recipe MobileNetV3-Large with the EPM trained at 384x384 on paired GoPro
Large frames, evaluated with 5-scale test-time augmentation reaches F1 = 0.9803 (AUC 0.9989) with a
17 MB ONNX artifact, improving over our fixed-scale baseline on the same hardware (F1 = 0.9672) by
+1.31 points. We are explicit about limitations: results are on a single motion-blur distribution,
numbers are from a single seed, and calibration is qualitative rather than measured.

---

### 6. Latent Visual States for Efficient Multimodal Reasoning

- arXiv: [2606.24233v1](https://arxiv.org/abs/2606.24233v1)
- PDF: [下载链接](https://arxiv.org/pdf/2606.24233v1)
- 作者: Xiuwei Chen, Wentao Hu, Yongxin Wang, Zisheng Chen, Likui Zhang, Kun Xiang, Jianhua Han, Hui-Ling Zhen, Jingyuan Zou, Hang Xu, Xiaodan Liang
- 发布时间: 2026-06-23T07:22:22Z
- 分类: cs.CV
- 相关性评分: 13
- 主题标签: 多模态推理、潜在表示、端到端优化

**中文摘要**

> 提出EVA框架，原生生成连续潜在视觉表示（Latent_slot tokens）作为中间视觉推理步骤，与文本token端到端训练。为克服过渡窗口策略偏离，提出解耦优化方法D-GSPO，并构建EVA-230K数据集，在多个基准上取得性能提升和效率改进。

**核心创新概述**

> 首次用连续潜在表示代替离散输出进行多模态推理，避免外部工具调用延迟。

**创新点拆解**

- 提出Latent_slot tokens作为连续视觉中间表示
- 开发D-GSPO解耦优化方法解决策略偏离问题
- 构建EVA-230K高质量图文交错CoT数据集

**当前局限**

> 潜在表示的可解释性不足，复杂推理场景下效果待验证。

**后续可改进方向**

- 探索潜在状态的可视化和可解释性
- 扩展到更多模态（如音频）
- 进一步压缩潜在状态序列长度以提升效率

**工程启发**

> 减少多模态推理对离散工具的依赖，提升推理速度和端到端能力。

**为什么值得关注**

> 提出新的多模态推理范式，对OCR+推理场景有启发意义。

**原始摘要**

The integration of visual evidence has significantly enhanced the capabilities of large multimodal
models. However, this integration predominantly relies on generating discrete outputs (etc., code or
box coordinates) to invoke external tools, a process that introduces rigid dependencies and
substantial latency. To overcome these limitations, we propose {EVA} (LatEnt Visual StAtes), a novel
framework that natively generates continuous latent visual representations. These internal
representations manifest as an adaptive sequence of Latent\_slot tokens, serving as intermediate
visual thoughts during the reasoning process. These Latent\_slot tokens are then trained end-to-end
with the discrete text tokens. This co-optimization, notably, causes extreme policy deviation in the
'transition window' following the Latent\_slot tokens. We develop D-GSPO (Decouple-GSPO) to target
this root cause by decoupling the optimization of latent and discrete components. To support SFT, we
construct EVA-230K, a high-quality text-image interleaved CoT dataset encompassing a diverse range
of real-world scenes, documents, charts and OCR tasks. Extensive experiments across multiple
benchmarks confirm that EVA achieves significant performance gains while enhancing inference
efficiency.

---

### 7. L3Cube-MahaPOS: A Marathi Part-of-Speech Tagging Dataset and BERT Models

- arXiv: [2606.24825v1](https://arxiv.org/abs/2606.24825v1)
- PDF: [下载链接](https://arxiv.org/pdf/2606.24825v1)
- 作者: Hariom Ingle, Ronit Ghode, Ishwari Gondkar, Jidnyasa Harad, Raviraj Joshi
- 发布时间: 2026-06-23T17:10:46Z
- 分类: cs.CL, cs.LG
- 相关性评分: 11
- 主题标签: 数据集、词性标注、低资源语言、Transformer

**中文摘要**

> 针对低资源语言马拉地语，构建了包含32,354条人工标注新闻句子的词性标注数据集MahaPOS，采用16标签通用依赖对齐方案。使用HMM、CRF、BiLSTM、BiLSTM+CharCNN、MuRIL及马拉地语专用Transformer MahaBERT-v2进行基准测试，最佳系统达到88.67%的token精度和81.67%的宏F1。

**核心创新概述**

> 首个大规模、高质量、人工标注的马拉地语POS标注数据集，并释放了数据集、标注指南和模型检查点。

**创新点拆解**

- 数据集构建：人工标注32k+新闻句子，16个UD对齐标签。
- 预处理管道：Unicode规范化、天城文感知分词、噪声过滤。
- 全面基准：覆盖传统模型和Transformer，包括马拉地语专属BERT。

**当前局限**

> 数据集仅来自新闻文本，可能缺乏其他领域（如社交媒体、方言）的多样性。

**后续可改进方向**

- 扩展到更多领域和代码混合文本。
- 探索跨语言迁移或无监督方法以进一步降低标注成本。
- 结合更大语言模型提升长尾标签性能。

**工程启发**

> 为马拉地语NLP下游任务（机器翻译、信息抽取）提供标准化评估资源。

**为什么值得关注**

> 展示了OCR/文档解析中低资源语言数据集的构建和评估范式，对多语言文档分析有参考价值。

**原始摘要**

Part-of-Speech (POS) tagging is a foundational NLP task underpinning machine translation,
information extraction, and syntactic parsing. Despite Marathi being spoken by over 83 million
people and ranking among the top twenty most spoken languages worldwide, it remains severely under-
resourced in annotated corpora and standardised evaluation benchmarks. Marathi presents unique
challenges for computational modelling owing to its rich morphology, relatively free word order,
lack of capitalisation conventions, and pervasive code-mixing with Hindi and English. We introduce
L3Cube-MahaPOS, a gold-standard POS tagging dataset for Marathi comprising 32,354 manually annotated
sentences drawn from news text. Annotation was performed entirely manually by a team of Marathi-
proficient annotators following a 16-tag Universal Dependencies-aligned scheme. A structured
preprocessing pipeline covering Unicode normalisation, Devanagari-aware tokenisation, and noise
filtering ensures label consistency across all splits. We benchmark the dataset across six model
families spanning HMM, CRF, BiLSTM, BiLSTM+CharCNN, MuRIL, and the Marathi-specific transformer
MahaBERT-v2. The best system achieves 88.67\% token-level accuracy and a macro-F1 of 81.67% over 15
evaluated tag classes. We release the dataset, annotation guidelines, and trained model checkpoints
to foster further research in Marathi NLP.

---

### 8. Overview of HIPE-2026: Person-Place Relation Extraction from Multilingual Historical Texts

- arXiv: [2606.25935v1](https://arxiv.org/abs/2606.25935v1)
- PDF: [下载链接](https://arxiv.org/pdf/2606.25935v1)
- 作者: Juri Opitz, Maud Ehrmann, Corina Raclé, Andrianos Michail, Matteo Romanello, Simon Clematide
- 发布时间: 2026-06-24T15:09:12Z
- 分类: cs.CL, cs.AI
- 相关性评分: 10
- 主题标签: 关系抽取、历史文档、OCR噪声、多语言、评测

**中文摘要**

> HIPE-2026评测聚焦从含噪历史多语言文档中抽取人物-地点关系（at/isAt），涉及法语、德语、英语，共17支队伍参与。数据集包含19-20世纪报纸和早期现代法语文学文本。评测框架涵盖预测准确性、计算效率、跨领域泛化。结果显示从大规模语言模型到轻量分类器的多种策略，揭示了历史关系抽取在准确率、效率与鲁棒性之间的权衡。

**核心创新概述**

> 首次将实体关系抽取引入历史文档评测，并包含时间约束的关系类型和跨领域泛化评估。

**创新点拆解**

- 任务定义：时间感知的人物-地点关系抽取（at/isAt）。
- 多语言多领域：历史报纸+文学文本，包含OCR噪声和语言变体。
- 三维评估框架：准确性、效率、泛化性。

**当前局限**

> 仅三种语言，泛化到其他历史语言或语域的能力未知。

**后续可改进方向**

- 扩展到更多历史语言和文档类型。
- 探索和缓解OCR噪声对关系抽取的具体影响。
- 设计更高效的模型以处理大规模语料。

**工程启发**

> 为文化遗产领域的大规模历史文档分析提供基准和洞见。

**为什么值得关注**

> 直接处理OCR噪声下的文档解析，特别是关系抽取，对文档理解任务有启发。

**原始摘要**

Was this person ever at that place, and if so, when? Answering such questions from noisy,
multilingual historical documents is the central challenge of HIPE-2026, the third edition of the
HIPE evaluation series. Moving from named entity recognition and linking (HIPE-2020, HIPE-2022) to
reasoning about relationships between entities, HIPE-2026 targets two temporally grounded relation
types: $at$, indicating that a person was present at a location at some point prior to a document's
publication date, and $isAt$, indicating presence contemporaneous with that date. This paper
presents the results of the evaluation campaign, which confronted 17 participating teams with the
challenges of historical language variation, OCR noise, and indirect contextual cues across three
languages: French, German, and English. The datasets include historical newspaper text from the
nineteenth and twentieth centuries, as well as a surprise-domain generalization set drawn from early
modern French literary texts. A distinctive feature of HIPE-2026 is its three-fold evaluation
framework, which assesses predictive accuracy, computational efficiency, and cross-domain
generalization, reflecting the practical demands of large-scale historical document processing in
the cultural heritage domain. Across more than 40 submitted runs, results reveal a wide range of
strategies, from state-of-the-art large language models to lightweight task-specific classifiers,
and highlight the trade-offs between accuracy, efficiency, and robustness inherent to historical
relation extraction at corpus scale. System descriptions, datasets, and findings are presented and
discussed, offering a detailed picture of the current state of temporally grounded relation
extraction for historical documents.

---

### 9. Probabilistic Agents in Deterministic Audits: Evaluating Multi-Agent Systems for Automated Audits Based on the German IT-Grundschutz

- arXiv: [2606.25622v1](https://arxiv.org/abs/2606.25622v1)
- PDF: [下载链接](https://arxiv.org/pdf/2606.25622v1)
- 作者: Lea Roxanne Muth, Marian Margraf
- 发布时间: 2026-06-24T09:31:06Z
- 分类: cs.CR, cs.AI
- 相关性评分: 10
- 主题标签: 多智能体系统、检索增强生成、自动化审计、文档处理

**中文摘要**

> 基于多智能体系统（MAS）和混合检索增强生成（HybridRAG）部分自动化德国IT-Grundschutz（IT-GS）认证，通过假设-验证循环和解耦推理管道减少幻觉并确保合规。利用BSI案例数据集评估结构分析、保护需求评估、建模和IT-GS检查阶段的精确率、召回率和F1。

**核心创新概述**

> 将MAS和HybridRAG技术应用于自动化IT安全认证流程，引入假设-验证循环和知识图谱交叉引用。

**创新点拆解**

- 架构设计：MAS+HybridRAG实现多阶段自动化。
- 假设-验证循环：减少推理中的幻觉。
- 解耦推理管道：分离语义提取和确定性推理。

**当前局限**

> 评估限于一个案例研究，泛化到其他组织或标准需验证。

**后续可改进方向**

- 在不同规模企业上测试系统的鲁棒性。
- 扩展到其他安全框架（如ISO 27001）。
- 优化效率以处理更大文档集。

**工程启发**

> 为安全合规自动化提供可实施的原型，减少人工工作量。

**为什么值得关注**

> 展示了基于大型语言模型的文档分析在安全领域的具体应用，对OCR后处理有参考。

**原始摘要**

The NIS-2 Directive mandates robust Risk Management from thousands of small and medium enterprises.
To ensure compliance, companies rely on established standards such as the German IT-Grundschutz (IT-
GS) of the Federal Office for Information Security. However, IT-GS certification is resource-
intensive and requires a high level of manual effort for documentation, validation, and revision,
making scalable implementation difficult and expensive. Building upon our previous conceptual
framework, this paper presents the technical implementation and empirical evaluation of a Multi-
Agent System (MAS) architecture combined with Hybrid Retrieval Augmented Generation (HybridRAG) for
the partial automation of IT-GS certification. We introduce two novel technical contributions to the
MAS architecture to enforce the compliance rigor. The Hypothesis-Verification Loop in the Structural
Analysis (SA) phase that cross-references agent-inferred dependencies against the Knowledge Graph to
reduce hallucinations, and a Decoupled Reasoning Pipeline that separates agent-driven semantic
extraction from the deterministic protection need inheritance. We utilize the BSI's "RecPlast GmbH"
case study as a human expert-generated reference data set for end-to-end evaluation of the
architecture and to quantify Precision, Recall, and F1-scores. The performance of the system is
investigated across the phases of SA, Protection Needs Assessment (PNA), Modeling, and IT-GS Check.
The empirical results reveal noticeable differences throughout the different steps of IT-GS. While
the MAS demonstrates high efficacy in semantic tasks (SA and Modeling), significantly reducing
manual effort through automated information extraction, quantitative results reveal limitations in
logical reasoning phases (PNA and IT-GS Check) as the probabilistic nature of current LLMs struggles
to meet the deterministic rigor required by IT-GS.

---

### 10. WinDOM: Self-Family Distillation for Small-Model GUI Grounding

- arXiv: [2606.25964v1](https://arxiv.org/abs/2606.25964v1)
- PDF: [下载链接](https://arxiv.org/pdf/2606.25964v1)
- 作者: Chengheng Li-Chen, Zhiqian Zhou, Hao Chen, Nicolas Chauvin
- 发布时间: 2026-06-24T15:35:29Z
- 分类: cs.AI, cs.LG
- 相关性评分: 9
- 主题标签: GUI接地、蒸馏、强化学习、数据采集、小模型

**中文摘要**

> 提出WinDOM（54,425条记录）GUI接地语料库，通过无头Playwright驱动开源Windows 11网页实现，无需OCR或人工标注。提出了自我家族蒸馏（SFD）方法，仅使用教师（EMA或更大模型）初始化，并将饱和深度作为GRPO超参数。在Qwen3.5-2B上，欠饱和冷启动+早期RL比收敛冷启动+RL提升OOD平均5.4个点，EMA模式接近跨尺寸蒸馏效果。

**核心创新概述**

> 无需OCR和标注的GUI接地数据采集方法，以及将蒸馏冷启动深度作为强化学习超参数的新范式。

**创新点拆解**

- 数据采集：无OCR、无标注的DOM直读方法。
- SFD训练：EMA或同族模型作为教师，冷启动后接RL。
- 训练范式：将RL初始器的饱和深度作为超参数。

**当前局限**

> 仅针对Windows 11网页模拟，真实跨平台GUI可能不同；小模型性能仍有限。

**后续可改进方向**

- 扩展到真实操作系统和应用。
- 探索更高效的蒸馏策略以减少教师依赖。
- 结合多模态输入（屏幕截图+DOM）以提升鲁棒性。

**工程启发**

> 为低资源场景下GUI代理训练提供低成本数据采集和高效训练方法。

**为什么值得关注**

> 展示了一种免OCR的文档/界面解析方法，对OCR替代方案有启发。

**原始摘要**

Small ($\sim$2B) GUI-grounding agents are attractive for on-device deployment, accessibility
tooling, and low-cost iteration, but at this scale they face two open recipe questions: how to
obtain bounding-box training data without expensive human annotation, and how to combine supervised
fine-tuning with reinforcement learning. We address both, with the explicit goal of pushing small-
model performance rather than scaling up. WinDOM is a $54{,}425$-record grounding corpus harvested
by driving an open-source Windows 11 web reimplementation under headless Playwright, with bounding
boxes read directly off the DOM and no OCR or human annotation. Self-Family Distillation (SFD) is a
single rejection-sampling cold-start parameterised only by the teacher choice: either an EMA of the
student (no external model) or a frozen larger same-family teacher. We then treat the saturation
depth of the SFD cold-start as an explicit GRPO hyperparameter. On a Qwen3.5-2B student, the under-
saturated cold-start is a better GRPO initialiser than the converged one: SFD-4B with Early-init RL
gains $+5.4$ OOD-mean ($+3.5$ ScreenSpot-Pro, $+7.0$ OSWorld-G, $+5.8$ ScreenSpot-V2) over the base.
The same-size EMA mode lands within roughly one OOD-mean point of the cross-size $4$B variant
($65.2$ vs $66.3$) without an external teacher.

---

### 11. P-MTP: Efficient Document Parsing via Multi-Token Prediction with Progressive Depth Scaling

- arXiv: [2606.24447v1](https://arxiv.org/abs/2606.24447v1)
- PDF: [下载链接](https://arxiv.org/pdf/2606.24447v1)
- 作者: Le Xiang, Chenxi Zhai, Shu Wei, Jingjing Wu, Qunyi Xie, Xiao Tan, Kunbin Chen, Wei He
- 发布时间: 2026-06-23T11:34:28Z
- 分类: cs.CV
- 相关性评分: 9
- 主题标签: 文档解析、推理加速、多token预测、视觉语言模型

**中文摘要**

> 提出P-MTP框架，通过渐进式多token预测（MTP）加速视觉语言模型在文档解析中的推理。引入渐进式课程损失动态调整不同展望深度权重，以及置信度门控动态草稿机制自适应调整推理时的预测长度。在多个基准和架构上实现最高5倍加速，且精度损失可忽略。

**核心创新概述**

> 首次在文档解析领域成功验证大展望深度MTP，并通过渐进式课程学习解决不稳定性。

**创新点拆解**

- 渐进式课程损失：基于路径可靠性和目标一致性动态调整权重。
- 置信度门控动态草稿：自适应调整推理长度，减少计算浪费。
- 方法验证：在多种架构和基准上达到5倍加速。

**当前局限**

> 加速比可能依赖于文档密度和模型架构；极深展望深度下精度仍有下降。

**后续可改进方向**

- 探索更优雅的损失函数以支持更深展望。
- 结合硬件特性优化推理实现。
- 扩展到多语言和复杂版面文档。

**工程启发**

> 显著降低文档解析系统的推理延迟，适用于高吞吐场景。

**为什么值得关注**

> 直接针对OCR/文档解析推理效率瓶颈，提供实用加速方案。

**原始摘要**

Vision-Language Models (VLMs) have revolutionized document parsing by enabling end-to-end mapping
from images to structured text, imposing a significant latency bottleneck, particularly for token-
dense documents. While Multi-Token Prediction (MTP) has emerged as a promising approach for
accelerating inference, its potential is constrained by optimization instability when scaling to
deeper look-ahead depth. In this paper, we propose \textbf{P-MTP}, a framework that leverages
\textbf{Progressive Multi-Token Prediction} with a lightweight MTP module to scale the look-ahead
depth for high-throughput document parsing. Specifically, we introduce Progressive Curriculum Loss
that adaptively re-weights different look-ahead depths using cumulative path reliability and
retrospective target consistency. By effectively suppressing gradient noise in long-range
predictions, P-MTP, facilitates an automated easy-to-hard optimization transition, enabling the
model to master increasingly distant look-ahead depths. Furthermore, we propose Confidence-Gated
Dynamic Drafting to maximize the effective look-ahead depth and acceptance rate by adaptively
calibrating speculative length during inference, thereby minimizing computational waste and further
pushing the boundaries of inference speedup. Experimental results across multiple benchmarks and
architectures demonstrate that P-MTP, achieves up to a $5\times$ speedup with negligible loss in
accuracy, providing the first successful validation of extensive look-ahead MTP in the document
parsing domain.

---

### 12. AI-PAVE-Br: Leveraging Large Language Models for Enhanced Product Attribute Value Extraction through a Golden Set Approach

- arXiv: [2606.24655v1](https://arxiv.org/abs/2606.24655v1)
- PDF: [下载链接](https://arxiv.org/pdf/2606.24655v1)
- 作者: Murilo Gazzola, Hugo Gobato Souto, Samuel Silva, Júlia Schubert Peixoto, Felipe Siqueira, André Luis Pedroso de Morais, Caio Gomes
- 发布时间: 2026-06-23T14:48:37Z
- 分类: cs.CL, cs.AI, cs.LG, cs.PF
- 相关性评分: 6
- 主题标签: 属性抽取、电商、葡萄牙语、大语言模型、数据集

**中文摘要**

> 面向巴西电商葡萄牙语产品描述，构建了AI-PAVE-Br系统用于产品属性值抽取（PAVE），并创建了高质量人工标注的Golden Set数据集。采用大规模语言模型和提示工程，显著优于传统命名实体识别基线。

**核心创新概述**

> 首个针对巴西电商葡萄牙语的LLM-based PAVE系统及附带基准数据集。

**创新点拆解**

- 系统设计：LLM + 提示工程实现高精度属性抽取。
- 数据集：人工标注Portuguese PAVE黄金集，结构包含实体、类别、子类别。
- 实验对比：证明LLM方法远超传统NER。

**当前局限**

> 仅覆盖巴西电商，其他葡萄牙语变体或领域未测试。

**后续可改进方向**

- 扩充数据集涵盖更多品类和语言变体。
- 探索少样本和零样本泛化能力。
- 结合结构化知识（如产品分类）提升抽取一致性。

**工程启发**

> 为巴西电商平台提供可部署的属性抽取方案，节省人工。

**为什么值得关注**

> 展示了大语言模型在文档结构化信息抽取中的优势，对OCR后结构化有参考。

**原始摘要**

The explosive growth and complexity of product data within the dynamic Brazilian e-commerce
landscape demand robust and specialized methods for structured information extraction. Traditional
approaches to Product Attribute Value Extraction (PAVE) often struggle with the linguistic nuances
and sheer diversity of product descriptions in Portuguese. To address this critical gap, this paper
introduces two major contributions. First, we present AI-PAVEBr, a specialized system engineered
with Large Language Models (LLMs) to perform high-accuracy PAVE specifically for Brazilian
e-commerce catalogs. Second, to facilitate reproducible research and provide a definitive benchmark,
we introduce and share the Golden Set, a new, meticulously curated, and manually annotated dataset
for PAVE in Portuguese. We detail the creation process and structure (Entity, Category,
Subcategories) of this high-quality reference set. Our experiments conclusively show that AI-PAVE-
Br, leveraging targeted prompt engineering, dramatically outperforms conventional Named Entity
Recognition (NER) baselines. This work not only delivers a superior, scalable solution for a major
non-English market but also enriches the NLP community with a valuable, publicly available resource
for future PAVE research.

---
