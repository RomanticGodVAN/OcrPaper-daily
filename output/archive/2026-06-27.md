# OCR / 文档解析研究日报（2026-06-27）

## 报告说明

- 检索源：arXiv API
- 检索查询：`(all:"document parsing" OR all:"document understanding" OR all:"optical character recognition" OR all:OCR OR all:"layout analysis" OR all:"document layout analysis" OR all:"text recognition" OR all:"table recognition" OR all:"form understanding" OR all:"document intelligence" OR all:"page understanding" OR all:"scene text recognition" OR all:"handwritten text recognition" OR all:"information extraction") AND (cat:cs.CV OR cat:cs.AI OR cat:cs.CL OR cat:eess.IV)`
- 生成时间（UTC）：`2026-06-27 05:02:58`
- 大模型综合分析：`开启`

## 一、今日执行摘要

> 今日论文涵盖金融文档解析和视频生成两个领域，其中LLM在证券抵押品资格审核中的应用展示了生成式信息提取的潜力，其保守运行特性对合规场景有重要价值；PhysRAG则通过检索增强生成提升视频的物理合理性。两个方向均体现了从传统模型向更灵活、知识驱动的生成范式的转变。

## 二、今日趋势判断

OCR/文档解析领域正从基于实体的NER向生成式信息提取演进，LLM被用于改善对复杂文档的理解和噪声鲁棒性；同时，检索增强生成成为注入外部知识以提升模型可控性和准确性的通用方法。

## 三、今日论文概览

1. **LLM-Based Examination of Eligibility Criteria from Securities Prospectuses at the German Central Bank** | 标签：文档解析、信息提取、LLM应用、金融合规、评估方法论
2. **PhysRAG: Enhancing Physics-Awareness in Video Generation via Retrieval-Augmented Generation** | 标签：视频生成、物理感知、检索增强生成、数据过滤、知识注入

## 四、今天 OCR / 文档解析论文里的主要创新点

- 采用生成式信息提取流程替代传统序列标注方法，提升了文档级理解的准确性。
- 引入LLM作为裁判对提取结果进行价值评估，替代了依赖位置精度的传统指标。
- 在金融合规场景中实现保守运行特性，优先确保低误接受率以符合监管要求。

## 五、后续 OCR 领域值得推进的改进方向

- 研究OCR噪声对LLM提取性能的鲁棒性，并设计针对噪声文本的提示优化策略。
- 构建面向多语言、多领域文档解析的统一基准测试集，促进通用生成式信息提取模型的发展。
- 探索将LLM生成流程与结构化输出约束（如JSON Schema）结合，以减轻幻觉并提升可解析性。
- 开发支持增量学习和在线更新的文档解析系统，以适应不断变化的法规文档样式。

## 六、工程落地启发

- 德国央行的LLM系统在文档级资格检查上达到91%精确率，证明了生成式流程在金融合规自动化中的工程可行性。
- 生成的提取流程拆解为提取、归一化和解释三个阶段，模块化设计便于独立优化和维护。
- LLM作为裁判的评估方法提供了更符合业务价值的指标，可指导模型迭代方向。

## 七、优先关注论文

- **LLM-Based Examination of Eligibility Criteria from Securities Prospectuses at the German Central Bank**：展示了LLM在金融文档解析中的可行方案，其保守运行特性对高合规要求场景有参考价值，未来工作包括优化召回和抗OCR噪声，值得跟踪其扩展成果。

## 八、论文逐篇解析

### 1. LLM-Based Examination of Eligibility Criteria from Securities Prospectuses at the German Central Bank

- arXiv: [2606.27316v1](https://arxiv.org/abs/2606.27316v1)
- PDF: [下载链接](https://arxiv.org/pdf/2606.27316v1)
- 作者: Serhii Hamotskyi, Akash Kumar Gautam, Christian Hänig
- 发布时间: 2026-06-25T17:29:58Z
- 分类: cs.CL
- 相关性评分: 16
- 主题标签: 文档解析、信息提取、LLM应用、金融合规、评估方法论

**中文摘要**

> 德国央行验证证券抵押品资格是资源密集型任务。传统NER方法受OCR噪声和语言变体影响。本文首次应用LLM进行资格检查，采用生成式信息提取流程，分解为提取、归一化和解释步骤，并引入LLM作为裁判的价值评估方法。结果表明基于LLM的系统在文档级资格上达到91%精确率，具有保守运行特性，减少误接受。

**核心创新概述**

> 首次将LLM用于证券抵押品资格审核，从NER范式转向生成式信息提取，并提出LLM作为裁判的价值评估方法。

**创新点拆解**

- 提出生成式信息提取流程，分解为提取、归一化和解释
- 引入LLM作为裁判的价值评估方法，替代基于位置的指标
- 系统展现出保守运行特性，确保低误接受率

**当前局限**

> 精确率仍有提升空间，未涉及多语言扩展和实时性优化；LLM评估存在潜在偏差。

**后续可改进方向**

- 优化LLM提示策略以提升召回率
- 探索更高效的值归一化方法
- 构建多语言基准测试集
- 研究OCR噪声对LLM提取的鲁棒性影响

**工程启发**

> 为金融机构自动化文档审核提供可行方案，可减少人工成本，提升处理速度和一致性。

**为什么值得关注**

> 展示LLM在文档解析领域的落地应用，针对OCR噪声和复杂模板的泛化能力，对OCR后处理和信息提取有参考价值。

**原始摘要**

Verifying the eligibility of securities as collateral is a key responsibility of the German Central
Bank. However, manually verifying these assets against legal and financial criteria within lengthy,
semi-structured, and often bilingual prospectuses is a resource-intensive task. While previous
efforts utilized traditional Named Entity Recognition (NER) for information extraction, these
methods can struggle with OCR noise, linguistic variance, and rigid span-based constraints, and the
need for manually annotated training data for each relevant annotation type. In this paper, we
present the first case study applying Large Language Models (LLMs) to the eligibility examination
process, shifting the paradigm toward a generative Information Extraction pipeline. Our approach
decomposes the task into extraction, normalization, and interpretation, allowing for greater
flexibility in handling noisy text and interleaved German-English content. We further introduce a
value-based evaluation methodology using LLM-as-a-judge, which offers a more semantic assessment
than location-based metrics. Our results demonstrate that LLM-based systems achieve high precision
(up to 91%) in document-level eligibility, exhibiting a conservative operating profile that
minimizes false acceptance.

---

### 2. PhysRAG: Enhancing Physics-Awareness in Video Generation via Retrieval-Augmented Generation

- arXiv: [2606.26916v1](https://arxiv.org/abs/2606.26916v1)
- PDF: [下载链接](https://arxiv.org/pdf/2606.26916v1)
- 作者: Kexu Cheng, Zicheng Liu, Mingju Gao, Chunhe Song, Hao Tang
- 发布时间: 2026-06-25T11:53:27Z
- 分类: cs.CV
- 相关性评分: 6
- 主题标签: 视频生成、物理感知、检索增强生成、数据过滤、知识注入

**中文摘要**

> 视频生成模型缺乏物理意识。本文提出PhysRAG，通过检索增强生成提升物理感知。设计两阶段数据过滤流水线，从WISA-80K中筛选7K高质量视频。构建物理知识库并利用可学习查询注入物理知识到扩散模型。在PhyGenBench和VBench上达到最先进性能。

**核心创新概述**

> 将检索增强生成引入视频生成以注入物理知识，并设计数据过滤和知识注入机制。

**创新点拆解**

- 提出两阶段数据过滤流水线提升训练数据质量
- 构建物理视频数据库并设计可学习查询注入物理知识
- 实现检索增强生成与视频扩散模型的融合

**当前局限**

> 依赖外部物理数据库，可能限制泛化性；仅覆盖有限物理现象（热、力学、光学）。

**后续可改进方向**

- 扩展物理知识库覆盖更多现象（如流体、电磁）
- 探索无需外部检索的知识蒸馏方法
- 研究跨领域迁移能力
- 优化查询机制以减少检索开销

**工程启发**

> 为视频生成领域提供提升物理合理性的实用方案，可应用于仿真、动画制作等领域。

**为什么值得关注**

> 展示OCR/文档解析中的RAG思路可跨领域迁移至视频生成，强调数据过滤和知识注入的通用方法。

**原始摘要**

Developing physically aware video generation models remains a significant challenge due to the
difficulty in capturing diverse physical phenomena, such as thermal dynamics, mechanics, and optics.
In this work, we introduce PhysRAG, a novel pipeline that enhances physical awareness in video
generation through Retrieval-Augmented Generation (RAG). To address the issue of limited high-
quality data, we design a two-stage data filtering pipeline based on the WISA-80K dataset, resulting
in a curated set of 7K high-quality videos for training. Furthermore, we construct a physical video
database and develop a mechanism to inject physical knowledge into a video diffusion model using
learnable queries. Our method achieves state-of-the-art performance in both visual quality and
physical rule compliance, surpassing existing models in benchmarks such as PhyGenBench and VBench.
We conduct extensive ablation studies to validate the effectiveness of our key components, including
the data filtering pipeline, RAG mechanism, and method for physical information extraction. To
facilitate future research, our code, data, and models are prepared for release at
https://github.com/sediment1024/PhysRAG.

---
