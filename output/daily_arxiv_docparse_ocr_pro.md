# OCR / 文档解析研究日报（2026-08-14）

## 报告说明

- 检索源：arXiv API
- 检索查询：`(all:"document parsing" OR all:"document understanding" OR all:"optical character recognition" OR all:OCR OR all:"layout analysis" OR all:"document layout analysis" OR all:"text recognition" OR all:"table recognition" OR all:"form understanding" OR all:"document intelligence" OR all:"page understanding" OR all:"scene text recognition" OR all:"handwritten text recognition" OR all:"information extraction") AND (cat:cs.CV OR cat:cs.AI OR cat:cs.CL OR cat:eess.IV)`
- 生成时间（UTC）：`2026-08-14 03:29:12`
- 大模型综合分析：`开启`

## 一、今日执行摘要

> 今日3篇论文聚焦文档解析与隐私安全。NaviDC-OCR提出变形感知与内容-结构解耦的端到端解析框架，在数字与相机文档上取得SOTA；另外两篇关注隐私：一篇提出防OCR提取的多层上下文伪装框架，另一篇针对文档MLLM的关系隐私泄露提出去学习框架。整体趋势显示文档解析向复杂场景鲁棒性和隐私保护双线发展。

## 二、今日趋势判断

文档解析研究正从单一数字文档向相机拍摄等复杂场景扩展，强调几何变形鲁棒性；同时，随着文档多模态大模型的应用，隐私泄露问题凸显，促使研究者设计专门的防御与去学习机制；端到端解析与结构化建模深度结合，减少对传统布局分析的依赖。

## 三、今日论文概览

1. **NaviDC-OCR: Navigating Document Parsing Across Digital and Camera-Captured Documents** | 标签：文档解析、视觉语言模型、变形感知、结构建模、布局分析
2. **Multi-Layer Context Camouflaging: A Semantic Superposition and Contextual Lamination Framework for Malpractice-Resilient Online Assessment** | 标签：在线评估、隐私保护、语义叠加、防提取、计算模糊度
3. **Beyond Visual Evidence: Revealing and Mitigating Relational Privacy Leakage in Document MLLMs** | 标签：文档理解、隐私泄露、去学习、关键信息抽取、基准构建

## 四、今天 OCR / 文档解析论文里的主要创新点

- 多篇论文均在框架中引入显式的结构建模或几何感知，以提升复杂文档的解析精度。
- 隐私相关论文均从数学或理论层面定义了攻击模型或泄露度量，增强方案的可证明性。
- 均提出新的评估基准或协议，以系统性地验证方法在特定场景下的效果。

## 五、后续 OCR 领域值得推进的改进方向

- 探索变形感知学习在更多非刚性变形（如弯曲、透视）和低质量图像上的泛化，并优化自适应采样机制的计算效率。
- 将内容-结构解耦策略扩展到表格、公式之外的更多结构化元素（如票据、图表），并研究其在超高分辨率文档上的端到端性能。
- 将防OCR提取的语义叠加框架从理论转向实际系统，评估与不同渲染设备、屏幕类型和光照条件下的兼容性。
- 研究动态去学习框架在更多文档类型（如财务、医疗）和任务（如文档分类、视觉问答）上的泛化性，并降低去学习过程的计算开销。
- 探索隐私保护与解析精度的联合优化，设计自适应机制，根据文档敏感级别动态调整伪装或去学习策略。

## 六、工程落地启发

- NaviDC-OCR可直接用于实际系统，同时支持数字和相机文档，减少预处理依赖。
- 多层上下文伪装框架可用于在线考试或机密文档查看，需验证工程可行性。
- DRUF框架可直接集成到身份文档处理流程，增强隐私保护，且不显著损失KIE性能。
- 构建专门基准（如DocPrivacyBench）有助于评估隐私风险，建议类似实践用于其他敏感领域。
- 引入几何感知和结构解耦时需注意推理速度和计算开销，考虑模型轻量化或蒸馏。

## 七、优先关注论文

- **NaviDC-OCR: Navigating Document Parsing Across Digital and Camera-Captured Documents**：该框架在ICDAR竞赛中排名第一，展示了极强的实际性能，后续可能发布开源代码或模型，值得跟进并应用于联合数字与相机文档的场景。
- **Multi-Layer Context Camouflaging: A Semantic Superposition and Contextual Lamination Framework for Malpractice-Resilient Online Assessment**：该理论框架为防OCR提取提供了新的思路，若后续有原型实现，可能对在线评估和内容安全领域产生重要影响。
- **Beyond Visual Evidence: Revealing and Mitigating Relational Privacy Leakage in Document MLLMs**：该工作揭示了文档MLLM的隐私漏洞，并提出DRUF框架，其基准DocPrivacyBench可能成为后续评估标准，对隐私敏感文档处理具有指导价值。

## 八、论文逐篇解析

### 1. NaviDC-OCR: Navigating Document Parsing Across Digital and Camera-Captured Documents

- arXiv: [2608.12898v1](https://arxiv.org/abs/2608.12898v1)
- PDF: [下载链接](https://arxiv.org/pdf/2608.12898v1)
- 作者: Peng Cai, Zhaofan Zou, Shifa Liu, Yikun Wang, Jiawei Tang, Kaicheng Yang, Meng Tong, Zhongjiang He, Hao Sun
- 发布时间: 2026-08-13T07:34:21Z
- 分类: cs.CV, cs.AI
- 相关性评分: 25
- 主题标签: 文档解析、视觉语言模型、变形感知、结构建模、布局分析

**中文摘要**

> 本文提出NaviDC-OCR，一个统一的文档解析框架，用于处理数字文档和相机拍摄文档。该框架通过变形感知学习将几何感知融入视觉语言模型，并采用自适应采样机制表示复杂布局。此外，还提出了内容-结构解耦学习策略，显式建模公式语法和表格结构。实验表明，NaviDC-OCR在多个基准上达到最先进性能，并在ICDAR 2026挑战赛中排名第一。

**核心创新概述**

> 针对文档解析中相机拍摄文档的几何变形和端到端方法的结构推理不足问题，提出变形感知学习和内容-结构解耦学习，创新性地将几何感知和结构化表示学习结合。

**创新点拆解**

- 引入变形感知学习，使VLM具备几何感知能力
- 提出自适应采样机制，用于复杂布局表示
- 设计内容-结构解耦学习策略，显式建模公式语法和表格结构

**当前局限**

> 本文未明确讨论在极端低质量图像或非常规文档类型上的表现，且未提供与真实场景部署相关的效率分析。

**后续可改进方向**

- 探索将变形感知学习扩展到更多文档类型和更复杂的几何变形
- 研究自适应采样机制在超高分辨率文档上的效率优化
- 结合内容-结构解耦学习，进一步改进表格和公式的细粒度结构建模

**工程启发**

> NaviDC-OCR在多个基准上取得顶尖性能，证明了其在实际文档解析系统中的有效性，可直接用于数字和相机拍摄文档的解析，减少对布局分析的依赖，提高鲁棒性。

**为什么值得关注**

> 该工作针对文档解析中的关键挑战（几何变形和结构推理）提出创新解决方案，性能领先，对OCR和文档解析领域具有重要参考价值。

**原始摘要**

Document parsing aims to transform unstructured documents into structured and machine-readable
representations. Recent advances in Vision-Language Models (VLMs) have significantly advanced
document parsing. However, existing approaches still face two major challenges. First, decoupled
VLM-based methods heavily rely on accurate layout analysis, where geometric distortions in camera-
captured documents can introduce cascading errors. Second, although end-to-end VLM-based methods
alleviate the dependence on explicit layout detection, they often suffer from redundant generation,
hallucinations, and insufficient structural reasoning in high-resolution scenarios. To address these
challenges, we propose NaviDC-OCR, a unified framework for document parsing. NaviDC-OCR introduces
deformation-aware learning to incorporate geometric perception into VLMs and proposes an adaptive
sampling mechanism for complex layout representation. Furthermore, a content-structure decoupled
learning strategy is developed to explicitly model formula grammars and table structures, enabling
more effective structured representation learning. Extensive experiments demonstrate that NaviDC-OCR
achieves state-of-the-art performance across diverse document parsing benchmarks. It obtains overall
scores of 96.87, 88.53 and 78.41 on OmniDocBench v1.6, Wild-OmniDocBench, and PureDocBench,
respectively, and ranks first in the ICDAR 2026 Sci-ImageMiner Challenge. These results validate the
effectiveness and generalization capability of NaviDC-OCR in complex document parsing scenarios.

---

### 2. Multi-Layer Context Camouflaging: A Semantic Superposition and Contextual Lamination Framework for Malpractice-Resilient Online Assessment

- arXiv: [2608.13100v1](https://arxiv.org/abs/2608.13100v1)
- PDF: [下载链接](https://arxiv.org/pdf/2608.13100v1)
- 作者: Gupta Lovi Raj, Kaur Kamalpreet, Dama Sri Ram, Parani Prajithaa
- 发布时间: 2026-08-13T11:25:12Z
- 分类: cs.AI, cs.CY, cs.HC
- 相关性评分: 10
- 主题标签: 在线评估、隐私保护、语义叠加、防提取、计算模糊度

**中文摘要**

> 本文提出一种多层上下文伪装框架，用于在线评估系统，防止考试内容通过截图、屏幕共享、OCR等方式被提取。该框架通过语义叠加将真实内容和合成伪装统一渲染，只有合法考生可恢复。文章建立了理论基础，包括条件熵形式的计算模糊度量化，并提供了渲染算法和评估协议。

**核心创新概述**

> 首次将语义叠加和上下文分层用于防OCR提取，从数学上定义了对抗提取过程，并建立了可证明的安全保证，区别于传统的浏览器锁定等被动防御。

**创新点拆解**

- 提出多层上下文伪装理论，将真实内容与伪装内容语义叠加
- 定义了提取通道运算符和多个耦合构造，如上下文反转算子、分层算子等
- 用条件熵量化计算模糊度，并提供封闭式表达
- 设计渲染算法，保证合法恢复的精确过滤身份

**当前局限**

> 本文主要提供理论框架和算法设计，缺少实际系统实现和真实用户研究，性能验证有限。

**后续可改进方向**

- 实现原型系统，评估在实际设备和环境下的性能
- 研究不同类型内容（如数学公式、图表）的伪装效果差异
- 优化渲染算法以提高计算效率和视觉自然度

**工程启发**

> 该框架可应用于在线考试、机密文档查看等场景，能有效对抗恶意提取，提高内容安全，但需进一步验证工程可行性。

**为什么值得关注**

> 该工作针对OCR提取攻击提出防御策略，与OCR技术的安全应用直接相关，为对抗性OCR场景提供新颖思路。

**原始摘要**

Contemporary online assessment systems rely primarily on browser lockdown, webcam monitoring, and
behavioural analytics, yet remain vulnerable to attacks that extract the assessment content itself
through screenshots, screen sharing, optical character recognition, and automated scraping. This
paper extends the Multi-dimensional Spatio-Temporal Context Camouflaging Model (MSCCM) within the
MARS (Multi-modal Assessment Resilience Suite) by introducing the Multi-Layer Context Camouflaging
Theory (MCCT), a mathematical framework that protects rendered assessment content through semantic
superposition. Authentic assessment content and synthetically generated camouflage are represented
as a unified rendering while remaining recoverable only by legitimate candidates. The framework
models the adversarial extraction process through an explicit extraction-channel operator and
develops six coupled constructs: the Context Inversion Operator, Contextual Lamination Operator,
Separation Channel, Human Readability Functional, Computational Ambiguity Functional, and Context
Camouflage Tensor. Computational ambiguity is formulated using conditional entropy, yielding a
closed-form expression that quantifies uncertainty during unauthorized extraction, while legitimate
recovery is guaranteed through an exact filtering identity. We further establish theoretical
properties governing ambiguity, camouflage density, semantic preservation, multi-observation
leakage, and temporal multiplexing, and present a rendering algorithm with computational complexity
and a pre-registered evaluation protocol. MCCT provides a mathematically rigorous foundation for
behaviorally adaptive, accessibility-aware, and computationally resilient digital assessment by
securing rendered assessment content while preserving readability for legitimate users.

---

### 3. Beyond Visual Evidence: Revealing and Mitigating Relational Privacy Leakage in Document MLLMs

- arXiv: [2608.12911v1](https://arxiv.org/abs/2608.12911v1)
- PDF: [下载链接](https://arxiv.org/pdf/2608.12911v1)
- 作者: Beining Xu, Hairui Wang, Jiaxin Wang, Changsheng Chen, Anirban Chakraborty
- 发布时间: 2026-08-13T07:53:53Z
- 分类: cs.CV, cs.CR, cs.MM
- 相关性评分: 10
- 主题标签: 文档理解、隐私泄露、去学习、关键信息抽取、基准构建

**中文摘要**

> 本文研究了文档理解多模态大模型在身份文档处理中的隐私泄露问题。当输入图像缺乏足够视觉证据时，模型依赖训练数据中的字段关系推断缺失内容，导致多个相关字段泄露。作者提出动态关系去学习框架(DRUF)和评估基准DocPrivacyBench，实验表明DRUF在抑制高危险字段对泄露的同时保持了关键信息抽取性能，优于现有方法。

**核心创新概述**

> 首次针对文档理解MLLM在身份文档处理中的关系隐私泄露问题，提出动态去学习框架，并构建专门评估基准，系统性地评估多种模型的隐私泄露风险。

**创新点拆解**

- 提出动态关系去学习框架(DRUF)，包含关系解耦去学习模块和动态集合更新机制
- 构建DocPrivacyBench基准，模拟缺失视觉证据条件下的隐私泄露评估
- 在多个MLLM上验证了隐私泄露现象，并对比六种去学习方法

**当前局限**

> 本文主要针对身份文档的KIE任务，对其他类型文档的隐私问题未深入探讨，且DRUF的泛化性有待更多模型和场景验证。

**后续可改进方向**

- 扩展DRUF到更多类型的文档和任务，如财务票据、医疗记录
- 研究去学习过程中对模型其他能力的潜在影响，并优化权衡
- 探索动态更新机制的自适应策略，以减少计算开销

**工程启发**

> 该框架可直接用于文档处理系统，增强隐私保护，尤其对于涉及敏感个人信息的身份文档处理，具有重大工程意义。

**为什么值得关注**

> 该工作聚焦文档理解模型的安全隐私问题，与OCR和文档AI的合规应用直接相关，为构建可信文档处理系统提供方法。

**原始摘要**

While the privacy risks of multimodal large language models (MLLMs) have drawn significant
attention, the unique vulnerabilities of domain-specific MLLMs remain largely underexplored.
Focusing on document understanding MLLMs for identity document processing, this paper investigates
the privacy issues inherent in Key Information Extraction (KIE) tasks. We reveal that when input
images lack sufficient visual evidence, these models often rely on memorized field relations from
training data to infer missing content, thereby leaking multiple correlated fields containing
sensitive personal information. To mitigate this risk, we make three key contributions.First, we
propose the Dynamic Relational Unlearning Framework (DRUF) which comprises a Relational Decoupling
Unlearning (RDU) module and a dynamic set update mechanism. It suppresses the leakage of high-risk
field pairs while preserving KIE performance.Second, we introduce DocPrivacyBench, a novel benchmark
to systematically evaluate a model's susceptibility to privacy leakage under conditions of absent or
minimal visual evidence.Third, we evaluate three MLLMs and six unlearning methods using this
benchmark, assessing both post-unlearning leakage suppression and utility preservation.Our results
demonstrate that existing MLLMs consistently exhibit privacy leakage when visual evidence is scarce,
particularly on noisier datasets. In contrast, DRUF outperforms the strongest baseline by improving
leakage suppression by 4.8 percentage points, effectively mitigating privacy risks while maintaining
robust document information extraction performance.

---
