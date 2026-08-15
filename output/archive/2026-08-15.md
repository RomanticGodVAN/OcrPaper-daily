# OCR / 文档解析研究日报（2026-08-15）

## 报告说明

- 检索源：arXiv API
- 检索查询：`(all:"document parsing" OR all:"document understanding" OR all:"optical character recognition" OR all:OCR OR all:"layout analysis" OR all:"document layout analysis" OR all:"text recognition" OR all:"table recognition" OR all:"form understanding" OR all:"document intelligence" OR all:"page understanding" OR all:"scene text recognition" OR all:"handwritten text recognition" OR all:"information extraction") AND (cat:cs.CV OR cat:cs.AI OR cat:cs.CL OR cat:eess.IV)`
- 生成时间（UTC）：`2026-08-15 02:18:29`
- 大模型综合分析：`开启`

## 一、今日执行摘要

> 今日文档解析与OCR领域论文聚焦于三大方向：一是端到端VLM文档解析的鲁棒性与结构推理能力提升，如NaviDC-OCR通过变形感知与内容-结构解耦实现SOTA；二是文档处理中的隐私防护，如DRUF框架抑制关系泄露并配套基准；三是防作弊场景下的内容伪装技术，虽非纯OCR但通过OCR攻击防护与文档安全相关。整体趋势显示，从基础性能优化向高鲁棒性、安全性、隐私合规方向演进，同时兼顾复杂场景泛化。

## 二、今日趋势判断

当前OCR/文档解析研究正从单纯精度竞赛转向多维度能力提升：包括应对相机拍摄畸变的几何鲁棒性、高分辨率下的效率与准确性平衡、结构化信息（如表格、公式）的显式建模，以及与安全隐私的交叉融合。端到端VLM成为主流架构，但集成防御机制（如隐私遗忘、攻击防护）成为新热点。

## 三、今日论文概览

1. **NaviDC-OCR: Navigating Document Parsing Across Digital and Camera-Captured Documents** | 标签：文档解析、视觉语言模型、变形感知、结构推理、OCR
2. **Multi-Layer Context Camouflaging: A Semantic Superposition and Contextual Lamination Framework for Malpractice-Resilient Online Assessment** | 标签：在线评估、防作弊、语义叠加、OCR攻击、安全
3. **Beyond Visual Evidence: Revealing and Mitigating Relational Privacy Leakage in Document MLLMs** | 标签：隐私泄露、文档MLLM、关系遗忘、关键信息提取、安全

## 四、今天 OCR / 文档解析论文里的主要创新点

- 端到端VLM与结构解耦学习结合，摆脱对显式版面分析的依赖，提升端到端泛化能力。
- 嵌入几何感知（如变形感知）和多尺度采样机制，增强对复杂、畸变文档的适应性。
- 引入数学化防御框架（如语义叠加、条件熵），构建可量化的安全防护层。
- 针对隐私泄露设计专门的遗忘机制与基准，推动模型安全性的系统化评估。

## 五、后续 OCR 领域值得推进的改进方向

- 探索自适应采样与稀疏注意力结合，降低高分辨率VLM文档解析的计算冗余，提升推理速度。
- 构建含极端畸变、低质量和混合噪声的标准化基准，促进鲁棒性评估的全面化。
- 研究内容-结构解耦在其他复杂元素（如多级列表、交叉引用）上的泛化，增强结构推理能力。
- 将隐私遗忘与联邦学习或差分隐私融合，实现在线文档处理中的隐私保护与模型持续更新。
- 利用合成数据增强和对抗训练强化伪装框架的泛化能力，同时评估对合法用户体验的影响。

## 六、工程落地启发

- NaviDC-OCR提供统一端到端方案，适合直接集成于OCR系统，但在高分辨率场景需注意计算开销优化。
- DRUF采用动态关系遗忘，可嵌入现有文档MLLM的推理流程，平衡隐私保护与信息提取率。
- MCCT作为理论框架，可以转化为后处理渲染防攻击层，但需额外算法测试以平衡用户体验。
- 工程上应优先支持多种文档格式与拍摄场景，并设计可插拔的隐私保护模块，以增强产品合规性。

## 七、优先关注论文

- **NaviDC-OCR: Navigating Document Parsing Across Digital and Camera-Captured Documents**：首个在多个综合基准上达到SOTA的端到端VLM文档解析框架，其自适应采样与内容-结构解耦的设计思路可能成为后续研究的基础。
- **Beyond Visual Evidence: Revealing and Mitigating Relational Privacy Leakage in Document MLLMs**：首次系统研究文档MLLM的关系隐私泄露问题，并构建专门基准DocPrivacyBench，对行业合规与安全风向有引领作用。

## 八、论文逐篇解析

### 1. NaviDC-OCR: Navigating Document Parsing Across Digital and Camera-Captured Documents

- arXiv: [2608.12898v1](https://arxiv.org/abs/2608.12898v1)
- PDF: [下载链接](https://arxiv.org/pdf/2608.12898v1)
- 作者: Peng Cai, Zhaofan Zou, Shifa Liu, Yikun Wang, Jiawei Tang, Kaicheng Yang, Meng Tong, Zhongjiang He, Hao Sun
- 发布时间: 2026-08-13T07:34:21Z
- 分类: cs.CV, cs.AI
- 相关性评分: 25
- 主题标签: 文档解析、视觉语言模型、变形感知、结构推理、OCR

**中文摘要**

> 文档解析旨在将非结构化文档转换为结构化的机器可读表示。近期视觉语言模型（VLM）的进展显著推进了文档解析，但现有方法仍面临两大挑战：解耦的VLM方法严重依赖准确的版面分析，相机拍摄文档中的几何畸变可能导致级联错误；端到端VLM方法虽减轻了对显式版面检测的依赖，但在高分辨率场景下常出现冗余生成、幻觉和结构推理不足。为此，本文提出NaviDC-OCR，一个统一的文档解析框架。它引入变形感知学习，将几何感知融入VLM；提出自适应采样机制以处理复杂版面表示；并开发内容-结构解耦学习策略，显式建模公式语法和表格结构，以实现更有效的结构表示学习。大量实验表明，NaviDC-OCR在多种文档解析基准上达到最先进性能，在OmniDocBench v1.6、Wild-OmniDocBench和PureDocBench上分别获得96.87、88.53和78.41的总体分数，并在ICDAR 2026 Sci-ImageMiner挑战赛中排名第一，验证了其在复杂文档解析场景中的有效性和泛化能力。

**核心创新概述**

> 提出了一个统一框架，同时处理数字和相机拍摄文档的解析，通过变形感知学习、自适应采样和内容-结构解耦学习，解决了现有方法对版面分析的依赖和结构推理不足的问题。

**创新点拆解**

- 提出变形感知学习，将几何感知能力融入VLM，以应对相机拍摄文档的几何畸变。
- 设计自适应采样机制，用于复杂版面表示，提升高分辨率场景下的解析效果。
- 开发内容-结构解耦学习策略，分别建模公式语法和表格结构，增强结构化表示学习。

**当前局限**

> ['在极端畸变或低质量图像上的性能可能仍有局限。', '自适应采样机制的计算开销可能较高。', '内容-结构解耦学习可能对复杂嵌套结构支持不足。']

**后续可改进方向**

- 进一步优化变形感知学习以应对更复杂的几何变换。
- 探索自适应采样机制的效率提升，降低计算成本。
- 研究更细粒度的结构建模，以支持复杂文档布局。

**工程启发**

> 为文档解析提供统一的端到端解决方案，可直接应用于OCR系统、文档数字化、信息提取等场景；在多个基准上达到SOTA，具有较高的实用价值和部署潜力。

**为什么值得关注**

> 本文直接针对OCR/文档解析中的核心挑战，如几何畸变和结构推理，提出的方法具有创新性和通用性，对相关研究有重要参考价值。

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
- 主题标签: 在线评估、防作弊、语义叠加、OCR攻击、安全

**中文摘要**

> 当代在线评估系统主要依赖浏览器锁定、摄像头监控和行为分析，但仍易受到通过截图、屏幕共享、光学字符识别和自动抓取等方式提取评估内容的攻击。本文扩展了多维时空上下文伪装模型（MSCCM），引入多层上下文伪装理论（MCCT），这是一个通过语义叠加保护渲染的评估内容的数学框架。真实评估内容和合成生成的伪装被表示为统一渲染，但只有合法考生才能恢复。该框架通过显式的提取通道算子建模对抗性提取过程，并开发了六个耦合结构：上下文反转算子、上下文分层算子、分离通道、人类可读性泛函、计算模糊性泛函和上下文伪装张量。计算模糊性使用条件熵公式化，得到量化未授权提取期间不确定性的闭式表达式，而合法恢复通过精确滤波恒等式保证。本文进一步建立了控制模糊度、伪装密度、语义保留、多观测泄漏和时间复用等理论性质，并提出了一种具有计算复杂度的渲染算法和预注册评估协议。

**核心创新概述**

> 首次将语义叠加和上下文分层用于在线评估内容的伪装，数学框架新颖，为防作弊提供了新的理论视角。

**创新点拆解**

- 提出多层上下文伪装理论（MCCT），基于语义叠加保护评估内容。
- 开发六个耦合结构，显式建模对抗提取和合法恢复过程。
- 利用条件熵建立计算模糊性的闭式表达式，量化未授权提取的不确定性。

**当前局限**

> ['理论框架可能未充分验证实际部署的鲁棒性。', '伪装可能影响合法考生的阅读体验或可访问性。', '评估协议是预注册的，尚未进行大规模实证测试。']

**后续可改进方向**

- 在真实在线评估环境中进行更多实验以验证框架的可行性和安全性。
- 优化伪装密度和语义保留之间的平衡，减少对合法用户的影响。
- 探索与现有监控系统的集成，增强整体安全性。

**工程启发**

> 为在线评估提供防截图和OCR攻击的解决方案，可应用于考试系统，提高评估的公正性和安全性。

**为什么值得关注**

> 虽然不直接是OCR研究，但利用OCR攻击的弱点提出防御，与OCR技术的安全应用相关，对文档安全领域有参考价值。

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
- 主题标签: 隐私泄露、文档MLLM、关系遗忘、关键信息提取、安全

**中文摘要**

> 虽然多模态大语言模型（MLLM）的隐私风险已引起广泛关注，但领域特定MLLM的独特漏洞仍未充分探索。本文聚焦于用于身份证件处理的文档理解MLLM，研究关键信息提取（KIE）任务中固有的隐私问题。我们揭示，当输入图像缺乏足够的视觉证据时，这些模型往往依赖训练数据中记忆的字段关系来推断缺失内容，从而泄露多个包含敏感个人信息的相关字段。为缓解这一风险，我们做出三项关键贡献：首先，提出动态关系遗忘框架（DRUF），包含关系解耦遗忘（RDU）模块和动态集更新机制，抑制高风险字段对的泄露，同时保留KIE性能。其次，引入DocPrivacyBench，一个新基准，用于系统评估模型在视觉证据缺失或极少情况下的隐私泄露敏感性。第三，使用该基准评估三个MLLM和六种遗忘方法，评估遗忘后的泄露抑制和效用保留。结果表明，当视觉证据稀少时，现有MLLM一致地表现出隐私泄露，尤其是在噪声较大的数据集上。相比之下，DRUF在泄露抑制上优于最强基线4.8个百分点，有效缓解隐私风险，同时保持稳健的文档信息提取。

**核心创新概述**

> 首次系统研究文档理解MLLM在KIE任务中的关系隐私泄露问题，并提出专门的遗忘框架和基准，填补该领域空白。

**创新点拆解**

- 提出动态关系遗忘框架（DRUF），包含RDU模块和动态集更新机制，针对性抑制高风险字段对泄露。
- 构建DocPrivacyBench基准，专门评估视觉证据缺乏时的隐私泄露风险。
- 评估多个MLLM和遗忘方法，提供系统性实证分析。

**当前局限**

> ['评估的MLLM数量和类型有限，可能不具有广泛代表性。', '遗忘方法可能对模型性能有潜在影响，需要更全面的权衡评估。', 'DocPrivacyBench可能未覆盖所有身份文档类型和场景。']

**后续可改进方向**

- 扩展到更多类型的文档和MLLM，验证DRUF的泛化能力。
- 研究遗忘与模型性能之间的最优平衡，减少效用损失。
- 探索动态更新机制在不同数据分布下的适应性。

**工程启发**

> 为身份文档处理系统提供隐私保护方案，降低隐私泄露风险，同时保持信息提取效率，对合规和安全有重要价值。

**为什么值得关注**

> 涉及文档MLLM的隐私安全，是文档智能处理的重要方面，与OCR技术的安全和伦理问题紧密相关。

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
