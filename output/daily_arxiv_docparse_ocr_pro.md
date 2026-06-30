# OCR / 文档解析研究日报（2026-06-30）

## 报告说明

- 检索源：arXiv API
- 检索查询：`(all:"document parsing" OR all:"document understanding" OR all:"optical character recognition" OR all:OCR OR all:"layout analysis" OR all:"document layout analysis" OR all:"text recognition" OR all:"table recognition" OR all:"form understanding" OR all:"document intelligence" OR all:"page understanding" OR all:"scene text recognition" OR all:"handwritten text recognition" OR all:"information extraction") AND (cat:cs.CV OR cat:cs.AI OR cat:cs.CL OR cat:eess.IV)`
- 生成时间（UTC）：`2026-06-30 05:17:00`
- 大模型综合分析：`开启`

## 一、今日执行摘要

> 本日研究聚焦于非拉丁文字（僧伽罗语、天城体）OCR的鲁棒性挑战、多模态文档问答的检索编排优化，以及少样本信息抽取中的负样本利用。主要发现：1) 低资源语种OCR需要真实场景数据集和轻量微调，如LightOnOCR-2-1B在僧伽罗语上取得最佳CER 1.05%；2) 天城体OCR压力测试显示合成数据高估性能，专用OCR-VLM在退化下脆弱，多模态大模型如Qwen3-VL和Gemini表现更优；3) 错误驱动演化可自动优化多检索器协同策略，在长文档问答中提升高达+19.6分；4) 负样本引导的上下文学习能有效提升LLM在信息抽取中的鲁棒性。

## 二、今日趋势判断

趋势一是低资源和非拉丁语种OCR从合成数据走向真实场景评测，强调退化文档鲁棒性和跨时间稳定性。趋势二是多模态文档理解从固定流水线转向自适应编排，通过错误驱动或演化学习优化检索与推理策略。趋势三是大型多模态模型在OCR任务上超越专用小模型，但专有模型在特定退化场景下仍有价值。

## 三、今日论文概览

1. **Cross-Temporal Sinhala OCR: Page-Level Adaptation and Diachronic Analysis** | 标签：僧伽罗语OCR、数据集构建、低资源语种、页面级OCR、迁移学习
2. **Hybrid Retriever Evolution for Multimodal Document Reasoning Agents** | 标签：多模态文档问答、检索编排、错误驱动演化、多代理系统、长文档推理
3. **Can OCR-VLMs Read Devanagari? A Stress-Test Benchmark and Post-Correction Study** | 标签：天城体OCR、印地语、压力测试基准、模型鲁棒性、跨脚本迁移
4. **LC-ICL: Label-Guided Contrastive In-Context Learning for Robust Information Extraction** | 标签：少样本信息抽取、上下文学习、负样本利用、NER、关系抽取

## 四、今天 OCR / 文档解析论文里的主要创新点

- 构建真实场景的低资源语种页面级OCR数据集，覆盖时间和退化维度
- 采用QLoRA等参数高效微调方法适配预训练模型以匹配特定语言和领域
- 利用负样本和错误驱动反馈来增强模型鲁棒性和检索推理策略
- 通过跨模态、跨页面的证据组合提升长文档问答的准确率
- 设计压力测试基准以揭示合成数据与实际性能之间的差距

## 五、后续 OCR 领域值得推进的改进方向

- 探索用合成数据或域自适应技术缓解天城体、僧伽罗语等低资源脚本的真实数据稀缺问题
- 分析OCR-VLM灾难性重复失败的根因，设计专用训练策略或输出约束来缓解
- 研究跨语言/脚本的迁移学习，利用英语等丰富资源提升非拉丁语种OCR性能
- 开发更真实的退化文档合成方法，缩小合成训练与真实测试之间的差距
- 将检索编排的演化框架扩展到更多RAG系统和多步推理任务，降低计算开销
- 在信息抽取中自动生成错误原因标签，减少人工标注成本，提升负样本引导的泛化性

## 六、工程落地启发

- 对于低资源语种，优先选择轻量预训练模型（如LightOnOCR-2-1B）并进行QLoRA微调，可快速获得具竞争力的基线
- 天城体等非拉丁OCR部署时，应使用真实扫描测试集而非合成数据来评估模型，并优先考虑多模态大模型（如Gemini、Qwen3-VL）
- 多模态文档问答系统可引入错误驱动演化框架自动优化检索器组合策略，以提升长文档推理的鲁棒性
- 少样本信息抽取中，可集成带错误原因标签的负样本演示来提升LLM的上下文学习效果，作为即插即用的增强模块

## 七、优先关注论文

- **Cross-Temporal Sinhala OCR: Page-Level Adaptation and Diachronic Analysis**：提供了首个真实场景僧伽罗语页面级OCR数据集和基线，其跨时间退化文档评测方法对低资源语种OCR评估具有标杆意义
- **Hybrid Retriever Evolution for Multimodal Document Reasoning Agents**：提出错误驱动的检索编排框架，在长文档问答中取得显著提升，有望推广到更多RAG和文档理解系统
- **Can OCR-VLMs Read Devanagari? A Stress-Test Benchmark and Post-Correction Study**：揭示了OCR-VLM在非拉丁脚本上的脆弱性和合成数据高估问题，其实验发现对模型选型和鲁棒性研究有重要指导价值
- **LC-ICL: Label-Guided Contrastive In-Context Learning for Robust Information Extraction**：创新性地将负样本错误原因标签引入上下文学习，为少样本信息抽取提供可即插即用的增强方案

## 八、论文逐篇解析

### 1. Cross-Temporal Sinhala OCR: Page-Level Adaptation and Diachronic Analysis

- arXiv: [2606.29378v1](https://arxiv.org/abs/2606.29378v1)
- PDF: [下载链接](https://arxiv.org/pdf/2606.29378v1)
- 作者: Avisha Dilhara, Nevidu Jayatilleke
- 发布时间: 2026-06-28T13:01:54Z
- 分类: cs.CL
- 相关性评分: 13
- 主题标签: 僧伽罗语OCR、数据集构建、低资源语种、页面级OCR、迁移学习

**中文摘要**

> 针对僧伽罗语OCR缺乏真实场景页面级数据集的问题，构建了包含1010张立法文本页面图像的数据集（1981-2019年），并基于DeepSeek-OCR等模型微调。LightOnOCR-2-1B取得最低CER（1.05%），显著优于Surya-OCR、Tesseract等开源及商业模型，且在时间跨度和文档退化场景下保持稳定。

**核心创新概述**

> 首次提供真实世界僧伽罗语页面级OCR数据集，覆盖跨年代退化文档，并系统对比多种开源与商业模型在真实场景下的性能。

**创新点拆解**

- 构建了首个真实场景的僧伽罗语页面级OCR数据集（包含多时间段、退化文档）
- 采用QLoRA微调高效适配轻量模型LightOnOCR-2-1B
- 在真实文档上验证跨时间一致性，超越现有开源和商业OCR模型

**当前局限**

> 数据集仅覆盖立法文本领域，字体和版面多样性有限；未探究跨语言迁移能力或模型在极低资源场景下的表现。

**后续可改进方向**

- 扩展到更多域（如手写、历史书籍）和更多语言
- 探索数据增强或合成数据策略以缓解真实数据稀缺问题
- 针对严重退化文档设计专用预处理或后处理模块

**工程启发**

> 为低资源语种OCR提供可复用的标杆数据集和基线模型，直接服务于斯里兰卡数字化档案管理。

**为什么值得关注**

> 开放了真实场景、多时间跨度的OCR数据集，对评估和改进非拉丁语系OCR系统具有重要参考价值。

**原始摘要**

Sinhala is a morphologically rich abugida spoken by roughly 16 million people in Sri Lanka, and to
date, there are no publicly available real-world datasets for page-level Sinhala OCR. All previous
studies for assessing Sinhala OCR models have used artificially generated data. To bridge the gap,
we introduce sinhala-ocr-lk-acts-1010, an annotated dataset of 1,010 page-level images and their
transcriptions collected from Sri Lankan Legislative Acts published between 1981-1989 and 2000-2019,
split into 707 training examples, 101 validation examples, and 202 testing examples. Three models
based on deep learning-based visual language processing, namely DeepSeek-OCR V1, DeepSeek-OCR V2,
and LightOnOCR-2-1B, are fine-tuned using QLoRA in 8 experiments conducted on consumer and cloud
GPUs. LightOnOCR-2-1B is the top performer, achieving a CER of 1.05% across all test examples,
outperforming state-of-the-art open-source OCR models such as Surya-OCR (8.84%) and Tesseract v5
(10.69%), as well as commercially available OCR models such as Google Document AI (2.06%). Our
results suggest that LightOnOCR-2-1B outperforms other baselines on real-world OCR tasks and
maintains consistent performance across all print periods, even when documents are severely
degraded.

---

### 2. Hybrid Retriever Evolution for Multimodal Document Reasoning Agents

- arXiv: [2606.29648v1](https://arxiv.org/abs/2606.29648v1)
- PDF: [下载链接](https://arxiv.org/pdf/2606.29648v1)
- 作者: Bohan Yao, Shruthan Radhakrishna, Vikas Yadav
- 发布时间: 2026-06-28T23:36:34Z
- 分类: cs.CL, cs.AI, cs.LG, cs.MA
- 相关性评分: 12
- 主题标签: 多模态文档问答、检索编排、错误驱动演化、多代理系统、长文档推理

**中文摘要**

> 提出失败驱动的演化框架，让元代理自动发现多步文档问答中如何协调不同检索器（词法、语义、多模态）。演化后的代理学会自适应调度检索器并组合跨模态证据，在MMLongBench-Doc和DocBench上相比未演化基线提升高达+19.6分，超越MACT、MDocAgent等近期系统。

**核心创新概述**

> 将检索编排本身作为推理过程的一部分进行学习，通过错误驱动演化自动优化多检索器协同策略。

**创新点拆解**

- 错误驱动的元代理演化框架，自动诊断并重写任务代理指令
- 自适应检索调度：根据推理步骤动态选择并组合检索器
- 跨模态、跨页面的证据组合能力
- 在长文档多模态问答任务上显著超越固定检索流水线方法

**当前局限**

> 演化过程可能依赖特定任务环境，泛化性有待验证；计算开销可能较高。

**后续可改进方向**

- 研究更轻量的演化或知识蒸馏方案
- 探索跨任务/领域的迁移能力
- 结合强化学习进一步优化演化策略的样本效率

**工程启发**

> 提供一种自动化优化多模态文档理解系统的范式，可集成到现有RAG或文档问答流水线。

**为什么值得关注**

> 展示了动态检索编排在复杂文档推理中的有效性，对提升OCR后文档理解系统的鲁棒性有启发。

**原始摘要**

Different retrievers, including lexical, semantic, and multimodal approaches, provide highly
complementary strengths for multimodal document understanding, yet most systems combine them through
fixed pipelines that cannot adapt to the demands of individual reasoning steps. In this work, we ask
whether retrieval orchestration itself can be learned as part of the reasoning process. We introduce
a failure-driven evolution framework in which a meta-agent autonomously discovers how a tool-using
task agent should coordinate diverse retrievers during multi-step document question answering. The
meta-agent analyzes incorrect reasoning trajectories, actively probes the same tool environment to
diagnose root causes, and iteratively rewrites the task agent's instructions, turning retrieval from
a fixed front-end stage into an adaptive, step-wise reasoning decision. The evolved agent learns
when to invoke each retriever, how to combine them, and how to compose evidence across modalities
and pages. On MMLongBench-Doc and DocBench, the evolved agent achieves gains of up to +19.6 points
over the unevolved baseline and consistently outperforms recent systems including MACT, MDocAgent,
and SimpleDoc. Detailed retrieval analyses confirm that these improvements arise from adaptive
routing and evidence composition rather than reliance on any hard coded retrieval mode, and
evolution dynamics reveal a progressive shift from narrow lexical behavior to rich multi-tool
coordination. These findings establish autonomous multi-agent coordination as a promising paradigm
for multimodal document reasoning.

---

### 3. Can OCR-VLMs Read Devanagari? A Stress-Test Benchmark and Post-Correction Study

- arXiv: [2606.29213v1](https://arxiv.org/abs/2606.29213v1)
- PDF: [下载链接](https://arxiv.org/pdf/2606.29213v1)
- 作者: Aditya Pratap Singh
- 发布时间: 2026-06-28T05:46:05Z
- 分类: cs.CL, cs.CV
- 相关性评分: 10
- 主题标签: 天城体OCR、印地语、压力测试基准、模型鲁棒性、跨脚本迁移

**中文摘要**

> 系统评测10种OCR系统在天城体（印地语）上的表现，包括合成退化条件和真实扫描。发现：合成文本无法区分性能；专门OCR-VLM在退化下最脆弱（如DeepSeek-OCR出现灾难性重复）；真实扫描中多数系统性能骤降（chrF++从90+降到60以下）；强英语OCR不预示印地语表现（如GPT-5.5仅58.5）。Qwen3-VL-8B（75.2）表现优于GPT-5.5，Gemini和Claude领先。

**核心创新概述**

> 首个针对天城体OCR的压力测试基准，揭示合成数据高估实际性能、专门OCR-VLM脆弱性以及跨脚本性能脱节。

**创新点拆解**

- 构建包含合成退化条件和真实扫描的天城体OCR基准
- 发现专用OCR-VLM的灾难性重复失败模式
- 揭示强英语OCR模型在印地语上性能严重下降
- 建议使用中位数和灾难率代替均值来评估

**当前局限**

> 仅覆盖印地语一个脚本；真实扫描数据量有限（300张）；未深入分析模型恢复策略。

**后续可改进方向**

- 扩展到更多印度语言和其他非拉丁脚本
- 针对退化文档设计鲁棒的预训练或微调策略
- 研究灾难性重复失败的根因及缓解方法
- 开发更真实的合成数据生成方法以缩小合成-真实差距

**工程启发**

> 为印地语OCR模型选型提供实证参考，建议优先考虑多模态大模型（如Gemini、Qwen3-VL）而非专门小型OCR-VLM。

**为什么值得关注**

> 揭示了低资源脚本OCR的常见陷阱（合成数据高估、跨脚本迁移失败），对部署非英文OCR系统有直接指导。

**原始摘要**

OCR systems, ranging from classical engines to specialised OCR vision-language models (OCR-VLMs) and
frontier multimodal LLMs, report strong results on English and Chinese document benchmarks, yet
their behaviour on Indic scripts is largely uncharacterised. We benchmark ten systems on Devanagari
(Hindi): classical EasyOCR; open VLMs (Qwen2.5-VL-3B, Qwen3-VL-8B, olmOCR-7B); specialised OCR-VLMs
(DeepSeek-OCR, Unlimited-OCR); and frontier closed models (Gemini 2.5 Flash, Claude Opus 4.7,
GPT-5.5, Mistral OCR), across four synthetic degradation conditions and 300 real printed scans. We
report four findings. First, on clean rendered text all ten cluster within chrF++ 91 to 98, so
synthetic text does not separate them. Second, under degradation the specialised OCR-VLMs are the
most fragile: DeepSeek-OCR suffers rare but catastrophic repetition failures (outputs up to 71 the
reference length) that wreck its corpus mean even though its median is the best of any system, which
is why we report median and catastrophic-rate instead of the mean. Third, on real scans nine of the
ten systems collapse (EasyOCR falls from chrF++ 93.6 to 58.3) and the field spreads across a
76-point range, so synthetic renders badly overstate Devanagari quality. Fourth, strong English OCR
does not predict Indic OCR: GPT-5.5 drops to chrF++ 58.5 (tying classical EasyOCR) and olmOCR-7B,
the model behind olmOCR-Bench, falls to 40.5, while the open Qwen3-VL-8B (75.2, runnable on a single
24 GB GPU) beats GPT-5.5 and approaches Mistral; Gemini and Claude lead at 86.3 and 82.2. An error
taxonomy separates surface errors (numerals, punctuation) from structural ones (conjuncts, matras,
nukta), and a byte-level (ByT5) post-corrector improves a cheap engine on its own error distribution
(chrF++ +1.2 to +1.5) but does not transfer across engines. We release the benchmark, code, and
models.

---

### 4. LC-ICL: Label-Guided Contrastive In-Context Learning for Robust Information Extraction

- arXiv: [2606.29407v1](https://arxiv.org/abs/2606.29407v1)
- PDF: [下载链接](https://arxiv.org/pdf/2606.29407v1)
- 作者: Xiao You, Tianwei Yan, Shan Zhao
- 发布时间: 2026-06-28T14:01:52Z
- 分类: cs.CL, cs.AI
- 相关性评分: 6
- 主题标签: 少样本信息抽取、上下文学习、负样本利用、NER、关系抽取

**中文摘要**

> 提出LC-ICL，一种利用正负样本构建上下文学习演示的少样本信息提取方法。通过标注错误原因标签的负样本暴露错误特征，使LLM理解预测失败原因并在推理中避免重犯。在NER和RE任务上，LC-ICL优于此前少样本上下文学习方法。

**核心创新概述**

> 在上下文学习中引入带错误原因标签的负样本，将失败案例作为学习信号，提升LLM在信息提取中的鲁棒性。

**创新点拆解**

- 使用带错误原因标签的负样本构建上下文演示
- 结合测试样本的最近正邻居和难负样本进行演示选择
- 在NER和RE任务上验证了负样本引导的有效性

**当前局限**

> 错误原因标签需要人工标注或启发式生成，可能引入噪声；方法高度依赖演示质量。

**后续可改进方向**

- 探索自动错误原因标注方法
- 结合主动学习迭代优化负样本质量
- 扩展到更多信息提取任务（如事件抽取）

**工程启发**

> 提供一种即插即用的少样本信息提取增强方案，可快速集成到现有LLM推理流水线。

**为什么值得关注**

> 展示了利用负样本改进上下文学习的通用思路，对提升OCR后信息提取（如实体识别）的鲁棒性有借鉴意义。

**原始摘要**

There has been increasing interest in exploring the capabilities of advanced large language models
(LLMs) in the field of information extraction (IE), specifically focusing on tasks related to named
entity recognition (NER) and relation extraction (RE).Although researchers are exploring the use of
few-shot information extraction through in-context learning with LLMs, they tend to focus only on
using correct or positive examples for demonstration, neglecting the potential value of
incorporating incorrect or negative examples into the learning process.In this paper, we present LC-
ICL a novel few-shot technique that leverages both correct and incorrect sample constructions to
create in-context learning demonstrations. This approach enhances the ability of LLMs to extract
entities and relations by combining positive samples with negative samples annotated by error-cause
labels. These labels expose more detailed error features in erroneous examples, enabling the model
to understand why similar predictions fail and avoid repeating such errors during
inference.Specifically, our proposed method taps into the inherent contextual information and
valuable information in hard negative samples and the nearest positive neighbors to the test and
then applies the in-context learning demonstrations based on LLMs. Our experiments on various
datasets indicate that LC-ICL outperforms previous few-shot in-context learning methods, delivering
substantial enhancements in performance across a broad spectrum of related tasks. These improvements
are noteworthy, showcasing the versatility of our approach in diverse scenarios.

---
