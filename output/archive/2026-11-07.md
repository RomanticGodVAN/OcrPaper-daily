# OCR / 文档解析研究日报（2026-11-07）

## 报告说明

- 检索源：arXiv API
- 检索查询：`(all:"document parsing" OR all:"document understanding" OR all:"optical character recognition" OR all:OCR OR all:"layout analysis" OR all:"document layout analysis" OR all:"text recognition" OR all:"table recognition" OR all:"form understanding" OR all:"document intelligence" OR all:"page understanding" OR all:"scene text recognition" OR all:"handwritten text recognition" OR all:"information extraction") AND (cat:cs.CV OR cat:cs.AI OR cat:cs.CL OR cat:eess.IV)`
- 生成时间（UTC）：`2026-11-07 07:05:07`
- 大模型综合分析：`开启`

## 一、今日执行摘要

> 今日两篇论文分别聚焦临床领域多语言NER与中世纪阿拉伯语手稿HTR。CardioLM通过机器翻译+标注投影构建7语种心脏病学病例报告语料并发布多语NER套件，发现领域继续预训练对困惑度收益大但严格span F1提升有限（≤0.04），多语言联合训练优于单语系统，残差错误集中在实体边界；ATHAAR则填补科学阿拉伯语手稿HTR数据空白，提出校勘学转写标注指南，并揭示当前视觉语言模型在跨文字、跨章节、跨专著迁移上的明显局限。两者共同说明领域数据与标注规范是当前文档解析性能的关键约束，模型架构并非主要瓶颈。

## 二、今日趋势判断

研究正从通用OCR/HTR基准转向高价值垂直领域（临床病例、历史科学手稿）的数据与标注体系建设；低资源语言与历史文字通过翻译投影、校勘学规范等方式扩展标注；视觉语言模型被用于手写历史文档转写，但跨域泛化仍不稳定；对领域预训练收益的评估趋于严格，强调严格span F1与人工临床评分等下游可用性指标。

## 三、今日论文概览

1. **CardioLM: A multilingual suite of small language models for the cardiology domain** | 标签：临床NER、多语言、心脏病学、标注投影、领域预训练、小语言模型、病例报告
2. **ATHAAR: A Medieval Scientific Arabic Manuscript Dataset for Handwritten Text Recognition** | 标签：手写文本识别、阿拉伯语手稿、历史文档数字化、视觉语言模型、数据集构建、标注指南、跨域迁移

## 四、今天 OCR / 文档解析论文里的主要创新点

- 以领域专家参与的标注规范或审核流程提升数据质量，而非单纯堆叠通用数据。
- 系统评估领域继续预训练与多语言/跨域联合训练的实际收益边界。
- 将残差错误分析细化到实体边界或字形/变音符号等具体层面。
- 构建覆盖多种语言、书法风格或文本见证版本的可迁移性评测设置。

## 五、后续 OCR 领域值得推进的改进方向

- 针
- 对
- O
- C
- R
- /
- H
- T
- R
- 中
- 实
- 体
- 边
- 界
- 与
- 字
- 符
- 边
- 界
- 错
- 误
- ，
- 设
- 计
- 边
- 界
- 感
- 知
- 解
- 码
- 或
- 跨
- 度
- 修
- 正
- 模
- 块
- ，
- 并
- 在
- 药
- 物
- 实
- 体
- 和
- 阿
- 拉
- 伯
- 语
- 连
- 字
- 变
- 音
- 符
- 号
- 上
- 做
- 专
- 项
- 验
- 证
- ；
- 在
- 标
- 注
- 投
- 影
- 流
- 程
- 中
- 引
- 入
- 主
- 动
- 学
- 习
- 与
- 人
- 工
- 复
- 核
- 优
- 先
- 级
- 排
- 序
- ，
- 量
- 化
- 翻
- 译
- 质
- 量
- 对
- 下
- 游
- N
- E
- R
- F
- 1
- 的
- 敏
- 感
- 性
- ；
- 将
- 多
- 语
- 言
- 联
- 合
- 训
- 练
- 与
- 语
- 言
- 特
- 定
- 继
- 续
- 预
- 训
- 练
- 结
- 合
- 为
- 两
- 阶
- 段
- 策
- 略
- ，
- 在
- 低
- 资
- 源
- 语
- 言
- 收
- 益
- 与
- 高
- 资
- 源
- 语
- 言
- 精
- 度
- 之
- 间
- 做
- 消
- 融
- ；
- 为
- 阿
- 拉
- 伯
- 语
- 手
- 稿
- 设
- 计
- 连
- 写
- 与
- 变
- 音
- 符
- 号
- 感
- 知
- 的
- 视
- 觉
- 编
- 码
- 或
- 字
- 符
- 级
- 对
- 齐
- 预
- 训
- 练
- 目
- 标
- ，
- 并
- 测
- 试
- 风
- 格
- 归
- 一
- 化
- 与
- 手
- 稿
- 特
- 定
- 微
- 调
- ；
- 建
- 立
- 跨
- 书
- 法
- 风
- 格
- 、
- 跨
- 专
- 著
- 、
- 跨
- 文
- 本
- 见
- 证
- 版
- 本
- 的
- 统
- 一
- 迁
- 移
- 评
- 估
- 协
- 议
- ，
- 报
- 告
- 细
- 粒
- 度
- 错
- 误
- 类
- 型
- 分
- 布
- ；
- 扩
- 展
- 临
- 床
- 实
- 体
- 到
- 剂
- 量
- 、
- 检
- 验
- 值
- 、
- 时
- 间
- 表
- 达
- 式
- 与
- 关
- 系
- 标
- 注
- ，
- 评
- 估
- 跨
- 语
- 言
- 迁
- 移
- 一
- 致
- 性
- ；
- 开
- 发
- 与
- 历
- 史
- 文
- 本
- 校
- 勘
- 流
- 程
- 衔
- 接
- 的
- 转
- 写
- 后
- 处
- 理
- 工
- 具
- 链
- ，
- 并
- 公
- 开
- 可
- 复
- 现
- 的
- 错
- 误
- 分
- 析
- 与
- 标
- 注
- 指
- 南
- 。

## 六、工程落地启发

- 临
- 床
- 自
- 由
- 文
- 本
- 结
- 构
- 化
- 优
- 先
- 选
- 用
- 多
- 语
- 言
- 联
- 合
- 训
- 练
- 的
- 编
- 码
- 器
- （
- 如
- X
- L
- M
- -
- R
- -
- l
- a
- r
- g
- e
- 多
- 语
- 微
- 调
- ）
- ，
- 其
- 严
- 格
- F
- 1
- 可
- 高
- 于
- 最
- 强
- 单
- 语
- 系
- 统
- 0
- .
- 1
- 3
- ；
- 领
- 域
- 继
- 续
- 预
- 训
- 练
- 可
- 降
- 低
- 困
- 惑
- 度
- 但
- 不
- 应
- 单
- 独
- 作
- 为
- N
- E
- R
- 性
- 能
- 提
- 升
- 依
- 据
- ，
- 需
- 以
- 严
- 格
- s
- p
- a
- n
- F
- 1
- 和
- 临
- 床
- 医
- 生
- 评
- 分
- 验
- 收
- ；
- 部
- 署
- 时
- 预
- 留
- 松
- 弛
- 匹
- 配
- 评
- 估
- ，
- 疾
- 病
- /
- 操
- 作
- /
- 症
- 状
- 可
- 恢
- 复
- 0
- .
- 1
- 0
- –
- 0
- .
- 2
- 3
- F
- 1
- ，
- 但
- 药
- 物
- 实
- 体
- 边
- 界
- 问
- 题
- 严
- 重
- ，
- 需
- 专
- 门
- 后
- 处
- 理
- ；
- 古
- 籍
- 阿
- 拉
- 伯
- 语
- H
- T
- R
- 项
- 目
- 应
- 直
- 接
- 采
- 用
- 校
- 勘
- 学
- 转
- 写
- 标
- 注
- 指
- 南
- ，
- 并
- 对
- 跨
- 风
- 格
- 、
- 跨
- 专
- 著
- 迁
- 移
- 做
- 单
- 独
- 评
- 测
- ，
- 不
- 能
- 假
- 设
- 通
- 用
- 视
- 觉
- 语
- 言
- 模
- 型
- 可
- 直
- 接
- 迁
- 移
- ；
- 标
- 注
- 扩
- 展
- 流
- 程
- 需
- 记
- 录
- 翻
- 译
- 投
- 影
- 噪
- 声
- 并
- 设
- 置
- 人
- 工
- 复
- 核
- 优
- 先
- 级
- 。

## 七、优先关注论文

- **CardioLM: A multilingual suite of small language models for the cardiology domain**：提供可直接部署的7语种心脏病学NER模型与CardioCCC语料，其多语言联合训练优于单语的结论对临床NLP选型有直接参考价值，且边界错误分析明确了后续优化点。
- **ATHAAR: A Medieval Scientific Arabic Manuscript Dataset for Handwritten Text Recognition**：首个科学阿拉伯语手稿HTR标注指南与数据集，跨文字、跨章节、跨专著迁移实验揭示了当前视觉语言模型在历史手写文档上的泛化短板，是古籍数字化方向的关键基准。

## 八、论文逐篇解析

### 1. CardioLM: A multilingual suite of small language models for the cardiology domain

- arXiv: [2611.07940v1](https://arxiv.org/abs/2611.07940v1)
- PDF: [下载链接](https://arxiv.org/pdf/2611.07940v1)
- 作者: Manuela-Daniela Danu, Miguel Rodríguez-Ortega, Alberto Becerra-Tome, Pablo Arancibia, Fernando Gallego-Donoso, Lorenzo Pratesi, Xi Bai, Andrei-Damian Dinescu, Salvador Lima-López, Andrea Guala, Saskia Haitjema, Jonas Mack, Michele Miranda, Wesam Al Nabki, Jan Rodríguez-Miret, Vasile George Marica, Vladimír Kincl, Kateřina Dostálová, Michael Andrej, Alicia Ujil, Corinne Allaart, Machteld Boonstra, Malin Overmars, Anoop Shah, Giovanna Ceroni, Jonathan Kossoff, Domenico D'Amario, Renzo Laborante, Antonio Iaconelli, Isabella Fumarulo, Jacopo Lenkowicz, Livia Lilli, Emma Weiss, Alex Scafa, Felix Lindberg, Milou Gamage, Eulàlia Farré-Maduell, Sébastien Bratières, Martin Krallinger, Bram van Es
- 发布时间: 2026-11-05T12:41:19Z
- 分类: cs.CL, cs.AI
- 相关性评分: 10
- 主题标签: 临床NER、多语言、心脏病学、标注投影、领域预训练、小语言模型、病例报告

**中文摘要**

> 该文提出两个资源：CardioCCC（508篇西班牙语心脏病学病例报告，经机器翻译、标注投影与临床医生审核扩展到捷克语、荷兰语、英语、意大利语、罗马尼亚语和瑞典语，标注疾病、症状、操作和药物四类实体）和CardioLM（含基于心脏病学与生物医学语料继续预训练的语言特定编码器CardioBERTa，以及在CardioCCC上微调的NER模型CardioNER）。实验显示，领域继续预训练可将伪困惑度降低至多8倍，但严格span级F1变化不超过0.04，收益集中在缺乏生物医学覆盖的骨干语言上；联合训练的多语言XLM-RoBERTa-large在几乎所有语言和实体类型上取得最佳严格F1，最高超过最强单语系统0.13。残差错误多与边界检测有关，松弛匹配可为疾病、操作和症状恢复0.10–0.23 F1，而药物仅恢复0.01–0.07。临床医生对CardioNER的评分显著高于规则和词典基线。

**核心创新概述**

> 构建了心脏病学专用、多语言、实体覆盖较广的病例报告语料与配套小模型套件，并以机器翻译加标注投影和临床医生审核的方式扩展低资源语言标注；同时系统比较了领域继续预训练与多语言联合训练在临床NER上的实际收益。

**创新点拆解**

- 提出CardioCCC多语言心脏病学病例报告语料，覆盖7种语言和疾病、症状、操作、药物四类实体
- 采用机器翻译、标注投影与临床医生审核相结合的低资源语言标注扩展流程
- 构建CardioBERTa语言特定编码器，在心脏病学与生物医学语料上继续预训练
- 发布CardioNER多语言NER模型套件，并系统评估领域预训练与多语言联合训练的相对贡献
- 引入临床医生人工评分，与规则和词典基线进行可用性对比

**当前局限**

> 领域继续预训练虽大幅降低伪困惑度，但对严格span级F1提升有限（不超过0.04），说明语言模型适配与实体识别性能之间并不直接对应；标注扩展依赖机器翻译与投影，可能引入翻译偏差；残差错误集中在实体边界检测，松弛匹配下药物类提升很小，表明药物实体识别仍较困难；语料规模相对有限（508篇源报告）。

**后续可改进方向**

- 针对实体边界问题设计边界感知的解码或跨度修正模块，重点改善药物类实体的边界与修饰语归属
- 在标注投影流程中引入主动学习或人工复核优先级排序，降低机器翻译投影带来的标注噪声
- 探索将多语言联合训练与语言特定继续预训练结合的两阶段策略，以兼顾低资源语言收益与高资源语言精度
- 扩展实体类型与关系标注（如剂量、检验值、时间表达式），并评估跨语言迁移的一致性
- 在更大规模心脏病学文本上验证领域预训练的收益边界，并报告翻译质量对NER性能的敏感性分析

**工程启发**

> 提供了可直接用于心脏病学临床文本处理的多语言NER模型与标注语料，适合作为临床自由文本结构化、病例报告实体抽取和跨语言临床NLP系统的基础组件；其多语言联合训练优于单语系统的结论对实际部署中的模型选型有参考价值。

**为什么值得关注**

> 该工作面向临床文档的命名实体识别，涉及多语言语料构建、标注投影、领域预训练和边界错误分析，与OCR/文档解析后接的临床文本结构化环节直接相关，其边界检测发现对OCR输出噪声下的实体抽取亦有借鉴意义。

**原始摘要**

Background: Cardiovascular care generates large volumes of clinical free-text documentation in local
languages. However, clinical natural language processing (NLP) resources remain concentrated in
English, and no existing benchmark is cardiology-specific, multilingual, and broad in entity
coverage. Methods: We present two contributions. The first is CardioCCC, a corpus of 508 cardiology
case reports originally published in Spanish and extended to Czech, Dutch, English, Italian,
Romanian, and Swedish through machine translation, annotation projection, and clinician review, with
annotations covering diseases, symptoms, procedures, and medications. The second is CardioLM,
comprising CardioBERTa, a set of language-specific encoders obtained by continued pretraining on
cardiology and biomedical corpora, and CardioNER, a set of named entity recognition (NER) models
fine-tuned on CardioCCC. Results: Cardiology-specific pretraining reduced pseudo-perplexity by up to
a factor of eight, yet changed strict span-level F1 by at most 0.04, with benefits concentrated in
languages whose backbones lacked biomedical coverage. The jointly trained multilingual XLM-RoBERTa-
large models achieved the best strict F1 in nearly every language and entity type, exceeding the
strongest monolingual system by up to 0.13 F1. A large share of residual errors concerned boundary
detection: relaxed matching recovered 0.10-0.23 F1 for disease, procedure, and symptom, but only
0.01-0.07 for medication. Clinicians rated CardioNER well above a rule- and dictionary-based
baseline, with the mean rating across entity types rising from 26% to 73%. Conclusions: Specialty-
specific pretraining is not the decisive factor for downstream entity recognition, whereas
multilingual joint training yields the strongest results in nearly all settings and a simpler
deployment path for multi-country clinical information extraction.

---

### 2. ATHAAR: A Medieval Scientific Arabic Manuscript Dataset for Handwritten Text Recognition

- arXiv: [2611.08091v1](https://arxiv.org/abs/2611.08091v1)
- PDF: [下载链接](https://arxiv.org/pdf/2611.08091v1)
- 作者: Ismail El Jamiy, Khadija Msalek, Guillaume Loizelet, Farah Benamara, Nabil Hathout
- 发布时间: 2026-11-05T14:36:16Z
- 分类: cs.CV, cs.CL
- 相关性评分: 7
- 主题标签: 手写文本识别、阿拉伯语手稿、历史文档数字化、视觉语言模型、数据集构建、标注指南、跨域迁移

**中文摘要**

> 针对中世纪阿拉伯语科学手稿因连写连字、变音符号多变且缺乏训练数据而难以被当前视觉语言模型识别的问题，该文提出首个面向科学阿拉伯语手稿转写的标注指南（借鉴校勘学），并据此人工标注构建数据集ATHAAR。该数据集在文本见证版本、书法风格和内容（文本与数字）上均有变化，区别于既有资源。作者基于先进视觉语言模型设计实验，研究模型跨文字、跨章节和跨专著的迁移，发现当前系统在古科学文本特性面前存在明显局限。

**核心创新概述**

> 首次将校勘学思想引入科学阿拉伯语手稿转写标注指南，并构建同时覆盖同一文本不同见证、不同书法风格以及文本与数字内容的 medieval 科学阿拉伯语手稿数据集。

**创新点拆解**

- 提出面向科学阿拉伯语手稿转写的标注指南，借鉴文本校勘学方法规范转写
- 构建ATHAAR数据集，同时覆盖同一文本的不同见证版本、多种书法风格以及文本和数字内容
- 基于先进视觉语言模型开展跨文字、跨章节、跨专著的迁移实验，系统刻画古科学文本识别难点
- 填补中世纪阿拉伯语科学手稿HTR训练数据缺失的空白

**当前局限**

> 数据集规模未在摘要中给出，可能受人工标注成本限制；实验表明当前视觉语言模型在古科学文本上仍表现有限，跨文字、跨章节和跨专著迁移存在明显退化；摘要未报告具体识别指标与错误类型分布，难以判断瓶颈主要来自字形、变音符号还是版式。

**后续可改进方向**

- 扩大标注规模并公开细粒度错误分析，区分连字、变音符号、数字和版式因素对识别错误的影响
- 针对阿拉伯语连写与变音符号设计专门的视觉编码或字符级对齐预训练目标
- 探索校勘学标注指南与弱监督/半监督结合，利用未标注手稿扩充训练数据
- 研究跨书法风格和跨专著的领域自适应方法，如风格归一化或手稿特定微调
- 建立与历史文本编辑流程衔接的转写后处理与校勘辅助工具链

**工程启发**

> 为阿拉伯语历史科学手稿的数字化与全文转写提供了标注规范和基准数据，可用于训练和评估古籍OCR/HTR系统；其跨风格、跨文本迁移实验为实际馆藏数字化项目中的模型泛化评估提供了参考框架。

**为什么值得关注**

> 该文直接面向手写文本识别（HTR）与古文献数字化，涉及标注规范、数据集构建和视觉语言模型迁移评估，属于OCR/文档解析在历史手稿场景的核心问题，对多文字、变音符号和书法多样性的处理具有直接借鉴意义。

**原始摘要**

Despite recent progress in handwritten text recognition, medieval Arabic scientific manuscripts
remain an open challenge for current vision-language models (VLMs) due to cursive ligatures,
variable diacritization, and more importantly the lack of training data. This paper aims to address
this gap, by proposing the first annotation guidelines dedicated to the transcription of scientific
Arabic manuscripts inspired by textual criticism, a well-established approach to historical text
editing. We then propose, ATHAAR, a new dataset manually annotated following this guideline. Unlike
previous resources in the field, ATHAAR varies both witnesses of the same text, calligraphic styles,
and content to deal with texts but also numerals. Relying on state-of-the-art VLMs, we finally
design a set of experiments to study models transfer across scripts, chapters, and treatises. Our
findings highlight the limitations of current systems when faced with the specificities of ancient
scientific texts.

---
