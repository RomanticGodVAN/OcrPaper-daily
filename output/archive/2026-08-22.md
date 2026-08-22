# OCR / 文档解析研究日报（2026-08-22）

## 报告说明

- 检索源：arXiv API
- 检索查询：`(all:"document parsing" OR all:"document understanding" OR all:"optical character recognition" OR all:OCR OR all:"layout analysis" OR all:"document layout analysis" OR all:"text recognition" OR all:"table recognition" OR all:"form understanding" OR all:"document intelligence" OR all:"page understanding" OR all:"scene text recognition" OR all:"handwritten text recognition" OR all:"information extraction") AND (cat:cs.CV OR cat:cs.AI OR cat:cs.CL OR cat:eess.IV)`
- 生成时间（UTC）：`2026-08-22 02:20:25`
- 大模型综合分析：`开启`

## 一、今日执行摘要

> 今日两份论文分别聚焦对抗性OCR鲁棒性和流匹配偏好优化中的流形漂移问题，前者提出首个对抗性OCR基准与训练框架，后者揭示了偏好优化导致生成样本偏离数据分布的根本原因并提出温度控制解法，均为OCR/文档解析的鲁棒性与生成质量提供了重要技术路径。

## 二、今日趋势判断

当前研究趋势强调从通用OCR能力转向对抗性/鲁棒性评估，并在生成模型的偏好优化中关注分布保持；多模态大模型与流匹配生成模型成为主流，但对训练稳定性与鲁棒性挑战的针对性解决方案正成为热点。

## 三、今日论文概览

1. **ArmorOCR: Grounded Adversarial Visual Perception via Observation-Transferred Self-Distillation** | 标签：对抗性OCR、多模态模型、基准、自蒸馏、强化学习
2. **Manifold Drift in Flow Preference Optimization: A Root Cause of Reward Hacking** | 标签：偏好优化、流匹配、流形漂移、温度控制、文本生成

## 四、今天 OCR / 文档解析论文里的主要创新点

- 利用自蒸馏与组相对策略优化来增强模型对对抗性样本的感知。
- 通过温度控制锚定偏好优化于数据流形，缓解流形漂移。
- 构建细粒度、区域级标注的基准以测量模型在真实困难场景下的表现。
- 将奖励函数设计为任务条件式，以平衡多个OCR子任务。

## 五、后续 OCR 领域值得推进的改进方向

- 扩展对抗性OCR基准到更大规模和更多变体，并考虑动态生成以覆盖长尾。
- 研究将流形距离约束整合进对抗性训练，防止模型提取的特征偏移。
- 在流匹配偏好优化中引入自适应的温度调度，根据任务难度动态调节。
- 探索将对抗性检测与偏好优化结合，使LLM在推理时能感知并修正对抗性输入。
- 开发统一框架同时优化通用OCR能力和对抗性鲁棒性，避免折衷。
- 将流形漂移理论应用于Transformer解码器，验证其对文本生成的影响。

## 六、工程落地启发

- 可借鉴ArmorOCR的两阶段训练策略，先内蒸馏再RL精调以提升鲁棒性。
- 采用任务条件奖励设计，以同时优化检测、识别和VQA等子任务。
- 在部署中引入对抗性样本的检测前处理模块，提高系统安全性。
- 使用ThermoDPO加权变体可显著提升文本生成质量（OCR提升47.5%），适合用于生成式OCR模型。
- 注意偏好优化时对训练数据分布的保持，避免生成结果偏离现实。

## 七、优先关注论文

- **ArmorOCR: Grounded Adversarial Visual Perception via Observation-Transferred Self-Distillation**：首个对抗性OCR基准，可能成为行业标准，其训练方法有望被广泛采用。
- **Manifold Drift in Flow Preference Optimization: A Root Cause of Reward Hacking**：揭示偏好优化中的流形漂移问题，温度控制思路可能被集成到主流生成模型训练框架。

## 八、论文逐篇解析

### 1. ArmorOCR: Grounded Adversarial Visual Perception via Observation-Transferred Self-Distillation

- arXiv: [2608.20122v1](https://arxiv.org/abs/2608.20122v1)
- PDF: [下载链接](https://arxiv.org/pdf/2608.20122v1)
- 作者: Linhan Cao, Siyuan Li, Jun Lan, Liangbo He, Guannan Li, Xiaolei Huang, Jun Jia, Shuheng Zhou, Huijia Zhu, Weiqiang Wang, Wei Sun
- 发布时间: 2026-08-20T14:52:06Z
- 分类: cs.CV
- 相关性评分: 13
- 主题标签: 对抗性OCR、多模态模型、基准、自蒸馏、强化学习

**中文摘要**

> 大型多模态模型在OCR识别上表现强大，但对人类可读但对模型难以定位和识别的对抗性视觉文本仍然脆弱。现有OCR基准主要集中在自然或文档风格文本，对抗性OCR评估在规模、任务覆盖或区域感知评估方面有限。本文将对抗性OCR定义为接地OCR感知任务，并引入AdvSpot，这是第一个用于接地对抗性OCR评估的基准，包含390张图像和区域级标注，涵盖5个主要类别和13种细粒度对抗性OCR类型。为解决此挑战，提出ArmorOCR，一种两阶段训练框架，通过策略内自蒸馏获取缺失的对抗性OCR感知，并通过带任务条件奖励的组相对策略优化细化接地OCR感知。实验表明，ArmorOCR持续提高对抗性OCR感知，同时保持有竞争力的通用OCR能力。

**核心创新概述**

> 首次将对抗性OCR定义为接地OCR感知任务，并创建了首个对抗性OCR基准AdvSpot。

**创新点拆解**

- 提出了AdvSpot，首个接地对抗性OCR评估基准，包含390张图像和区域级标注，覆盖5大类和13种对抗性类型。
- 设计了ArmorOCR框架，包括两阶段训练：策略内自蒸馏和组相对策略优化。
- 在GRPO中采用任务条件奖励，用于定位、识别、完整发现和视觉问答。

**当前局限**

> 基准规模相对较小（390张图像），可能限制泛化性。

**后续可改进方向**

- 扩展对抗性OCR基准的规模和多样性。
- 探索如何将对抗性OCR感知与通用OCR能力更好地平衡。
- 研究更有效的自蒸馏策略以减少计算成本。

**工程启发**

> 为对抗性OCR感知提供了新基准和方法，有助于提升LMM在鲁棒性方面的实际应用。

**为什么值得关注**

> 针对LMM在对抗性文本上的脆弱性，提出新基准和训练方法，对OCR研究方向有直接参考价值。

**原始摘要**

Large multimodal models (LMMs) have demonstrated strong OCR recognition capabilities, yet remain
vulnerable to adversarial visual text that is readable to humans but challenging for models to
localize and recognize. Existing OCR benchmarks mainly focus on natural or document-style text,
while adversarial OCR evaluations remain limited in scale, task coverage, or region-aware
evaluation. In this paper, we formulate adversarial OCR as a \textbf{grounded OCR perception} task
and introduce \textbf{AdvSpot}, the first benchmark for grounded adversarial OCR evaluation. AdvSpot
comprises 390 images with region-level annotations, spanning 5 primary categories and 13 fine-
grained adversarial OCR types. To address this challenge, we propose \textbf{ArmorOCR}, a two-stage
training framework for robust adversarial OCR perception. ArmorOCR first acquires missing
adversarial OCR perception from privileged transformed observations through On-Policy Self-
Distillation (OPSD), and then refines grounded OCR perception through Group Relative Policy
Optimization (GRPO) with task-conditioned rewards for localization, recognition, full spotting, and
visual question answering (VQA). Experiments on our AdvSpot, other adversarial OCR benchmarks, and
general OCR benchmarks demonstrate that ArmorOCR consistently improves adversarial OCR perception
while preserving competitive general OCR capability.

---

### 2. Manifold Drift in Flow Preference Optimization: A Root Cause of Reward Hacking

- arXiv: [2608.20011v1](https://arxiv.org/abs/2608.20011v1)
- PDF: [下载链接](https://arxiv.org/pdf/2608.20011v1)
- 作者: Yansen Han, Shengyi Liao, Yuanxing Zhang, Pengfei Wan, Tao Lin
- 发布时间: 2026-08-20T13:25:24Z
- 分类: cs.AI, cs.CV
- 相关性评分: 9
- 主题标签: 偏好优化、流匹配、流形漂移、温度控制、文本生成

**中文摘要**

> 偏好优化是生成模型的标准对齐方法，但将其扩展到连续时间动力学仍非易事。在流匹配中，奖励驱动的更新会修改传输轨迹，而无需对预训练数据流形强加约束，可能导致终端样本离开预训练支持集。本文将这种失败模式形式化为流形漂移。理论上，最佳流匹配恢复终端数据分布，而偏好更新在诱导的终端位移具有非零法向分量时会使预训练流形偏离。作为补救措施，提出ThermoDPO，一种温度控制目标，将成对偏好优化锚定在偏好样本上。在不同温度范围内，该目标连接了拒绝采样微调和FlowDPO，并控制基于点重建的流形距离代理。为了抵消低温下的信号减弱，进一步引入加权变体ThermoDPO-weighted。在主要玩具基准上，ThermoDPO-weighted的StrictScore为0.899，而FlowDPO为0.629，FlowDPO+RFT为0.857。在SD3.5-M的CFG=4.5时，OCR提高47.5%，四个指标平均值提高16.0%。

**核心创新概述**

> 揭示了流匹配偏好优化中流形漂移的根本原因，并提出温度控制的目标函数以缓解。

**创新点拆解**

- 形式化定义了流匹配中偏好优化的流形漂移问题。
- 提出ThermoDPO目标，通过温度控制锚定偏好样本，将拒绝采样微调和FlowDPO连接起来。
- 引入加权变体ThermoDPO-weighted以增强低温下的信号。

**当前局限**

> 主要在玩具基准上验证，在真实场景中的效果待进一步探索。

**后续可改进方向**

- 在更广泛的数据集上验证ThermoDPO的实用性。
- 研究流形距离代理的更精确估计方法。
- 探索如何将温度控制策略动态调整以适应不同任务。

**工程启发**

> 为流匹配模型的偏好优化提供了新算法，可提高文本生成和OCR等任务的质量。

**为什么值得关注**

> 本研究关注生成模型中的偏好优化，其改进的OCR性能（在SD3.5-M上提升4.7%）对OCR研究有实际价值。

**原始摘要**

Preference optimization is a standard alignment method for generative models, yet extending it to
continuous-time dynamics remains non-trivial. In flow matching, reward-driven updates modify
transport trajectories without an inherent constraint to the pretrained data manifold and can move
terminal samples off the pretrained support. We formalize this failure mode as manifold drift.
Theoretically, we show that optimal flow matching recovers the terminal data distribution, whereas a
preference update leaves the pretrained manifold whenever its induced terminal displacement has a
nonzero normal component. As a remedy, we propose ThermoDPO, a temperature-controlled objective that
anchors pairwise preference optimization on preferred samples. Across temperature regimes, this
objective connects rejection sampling fine-tuning and FlowDPO and controls a pointwise
reconstruction-based surrogate for manifold distance. To counteract diminished signals at low
temperatures, we further introduce a weighted variant, ThermoDPO-weighted. On the main toy
benchmark, ThermoDPO-weighted attains a StrictScore of 0.899, compared with 0.629 for FlowDPO and
0.857 for FlowDPO+RFT. On SD3.5-M at CFG = 4.5, it improves OCR by 47.5% and the average of four
metrics by 16.0%.

---
