[English](README.md) | [中文](README.zh.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Русский](README.ru.md)

# WikiHint：用于提示排序与生成的人工标注数据集
<a href="https://huggingface.co/datasets/JamshidJDMY/WikiHint"><img alt="Huggingface" src="https://img.shields.io/static/v1?label=Dataset&message=WikiHint&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAAIGNIUk0AAHomAACAhAAA+gAAAIDoAAB1MAAA6mAAADqYAAAXcJy6UTwAAAIoUExURQAAAP/////57v/67xUVFf/clv+KAP/uzf/sxv8AAP9TAP/ltP///v/ouP/////////////////////////////8+v/pvP/biP/Vbf/Vbv/cif/qv//9+//////////03v/Yev/Zfv/14//25v/Uav/Vbv/46//////dkf/gmP/////04P/25//pvP/sxf/////lr//ouP/qwP/tyf/msv/ntf/+/P/36f/LUf/36P/w0v/w0//w0//w0//78//gm//QZv/RZv/gm//78v/////14v/nt//gnP/hn//w0f/////w0f/hn//gnP/nt//14v/////////////////LLv/MGv/PGf/LL//LG//THP/THv/SHv/UHv/LGv/LH/7SHuK8JOzDIuW+I+jAI//LHv/PTP/NF/PBG3BkOpyGMvrOH4R0NoV0NvzJGv/MF//QT//MLv/LGPu/FNayJu7FIdq2Jf7DFP/JF//ML//LJurCIsCiKujCIubAI7+hK/DHIf/LJ//HK//NGf/SHeS9IlxSP25QQmtOQmVZPu3DIf/RHf/HLP++Kf/AD/++EP3EFNCfLNhpQthrQdinKv/FFP/AEP+/K/++Dv/BEv+/Ef/CE//MIf/NIP/MGf++D//KTP/FOP/DE//PG//PHP/JGP/EFP/EM//BDf/TH//GFP/CEP/DEP/EEv/BDv/MS//IJ//JHf/JHP/JP//IQf/IHP/IJv/LSf///7SHOh0AAABUdFJOUwAAAAAAAAAAAAAAAAAABiZCQykIAUGn3/Hy4q5KAwRy7vJ/Yfb7cR/X4ipkdpepAqi5mavM2z5v/pGTtZS2QtP4999bIGyry8yUR4fJzbJ2BRIRE9ZoIHEAAAABYktHRAH/Ai3eAAAAB3RJTUUH6AIGEyohVAr+rAAAARZJREFUGNNjYGBgZGTi4xcQFBJmZmRkYQDxRUTFxCUkpaRlZBkZQXw5eYWQ0LCw0HBFJWGgCCOrskpEZFR0dExkrKoaG1BAXSMuPiExOjopOSpFU4uRgV07NS09IzMqKzsnNy9fh4OBU7egsKi4JCo6ubSsvEJPlkHfoDIqqqq6prauPiqqwVCYgcuosam5pbWtvaOzq6nbWJZBy6Snt69/wsRJk6f0TZ1masZgbjF9xsxZhbPnzJ01c8a8+ZYMVgt6F5aHLly0eGHokqVTl1kz2CxYXhi1YuWq1WuiouauXWbLYGe/bv2GjZscHDdv2bh1m5MzA7eLq5u7h6eXoLePr5+/ENDpjBwBgYH6PIyMQcF8vIyMAKnZUpQQgaV4AAAAJXRFWHRkYXRlOmNyZWF0ZQAyMDI0LTAyLTA2VDE5OjQyOjI1KzAwOjAwybP6HAAAACV0RVh0ZGF0ZTptb2RpZnkAMjAyNC0wMi0wNlQxOTo0MjoyNSswMDowMLjuQqAAAAAodEVYdGRhdGU6dGltZXN0YW1wADIwMjQtMDItMDZUMTk6NDI6MzMrMDA6MDBAgVbbAAAAAElFTkSuQmCC&color=20BEFF"/></a>
<a href="https://doi.org/10.48550/arXiv.2412.01626"><img src="https://img.shields.io/static/v1?label=Paper&message=arXiv&color=green&logo=arxiv"></a>
<a href="https://colab.research.google.com/github/DataScienceUIBK/WikiHint/blob/main/HintRank/Demo.ipynb"><img src="https://img.shields.io/static/v1?label=Colab&message=Colab&logo=Google%20Colab&color=f9ab00"></a>
[![License](https://img.shields.io/badge/License-CC%20BY%204.0-blue)](https://creativecommons.org/licenses/by/4.0/)

<img src="https://github.com/DataScienceUIBK/WikiHint/blob/main/WikiHint/Pipeline.png">

WikiHint 是一个**人工标注数据集**，专为**自动提示生成与排序**设计。该数据集基于维基百科，包含 **1,000 道问题及 5,000 条提示**，支持**提示评估、排序和生成**相关研究。

## <img src="https://github.com/DataScienceUIBK/TriviaHG/blob/main/Framework/gif-dan.gif" width="32" height="32"/> 注意 <img src="https://github.com/DataScienceUIBK/TriviaHG/blob/main/Framework/gif-dan.gif" width="32" height="32"/>

从 **2025 年 2 月** 起，我们推荐使用 **HintEval** —— 一个用于**提示生成与评估**的框架。HintEval 集成了 **WikiHint 数据集** 以及 WikiHint 论文中提出的评估指标，让提示处理变得前所未有的简单。

点击下方链接了解 HintEval：  
- 📖 **[HintEval 文档](http://hinteval.readthedocs.io/)**  
- 📦 **[HintEval PyPI 安装](https://pypi.org/project/hinteval/)**  
- 💻 **[HintEval GitHub 仓库](https://github.com/DataScienceUIBK/HintEval)**  
- 📜 **[HintEval 论文 (arXiv)](https://doi.org/10.48550/arXiv.2502.00857)**  

为了**无缝集成**提示生成与评估，我们强烈推荐迁移至 **HintEval**！

## 🗂 数据集概览

- **1,000 道问题**，配有 **5,000 条人工创建的提示**。
- 由**人工标注人员**根据提示的有效性进行排序。
- 使用 **LLM（LLaMA、GPT-4）** 和 **人工实验** 进行评估。
- 适用于 **提示排序** 和 **自动提示评估**。

## 🔬 研究贡献

✅ **首个人工标注的提示生成与排序数据集**。  
✅ **HintRank**：一种轻量级的自动提示排序方法。  
✅ **人工实验** 评估提示在帮助用户回答问题方面的有效性。  
✅ **微调开源 LLM（LLaMA-3.1、GPT-4）** 以优化提示生成能力。  

## 📈 关键发现

- **基于答案的提示** 可提高提示的有效性。  
- **微调后的 LLaMA 模型** 生成的提示比基础模型更优。  
- **较短的提示** 通常比**较长的提示**更有效。  
- **人工生成的提示** 在清晰度和排序上优于 LLM 生成的提示。

## 🚀 快速开始

### 1️⃣ 克隆代码仓库

```sh
git clone https://github.com/DataScienceUIBK/WikiHint.git
cd WikiHint
```

### 2️⃣ 加载数据集

```python
import json

with open("./WikiHint/training.json", "r") as f:
    training_data = json.load(f)

with open("./WikiHint/test.json", "r") as f:
    test_data = json.load(f)

print(f"训练集：{len(training_data)} 道问题")
print(f"测试集：{len(test_data)} 道问题")
```

## 🏆 HintRank：轻量级提示排序方法

HintRank 是一种基于 **BERT 模型** 的**自动提示排序方法**，采用**成对比较**的方式，确定提示的**相对有效性**。

<p align="center">
    <img src="https://raw.githubusercontent.com/DataScienceUIBK/WikiHint/main/HintRank/EvaluationMethod.png" width="35%">
</p>

### ✨ 主要特点：
✔ **轻量级**：可在本地运行，无需大量计算资源。  
✔ **无需 LLM**：不依赖**大规模生成式模型**进行评估。  
✔ **符合人工排序**：排序结果与**人工标注的提示排序高度一致**。  

### 🔍 工作原理：
1. **将问题与两个提示连接** → 转换为 BERT 可处理的格式。  
2. **计算提示质量** → 判断哪个提示**更有用**。  
3. **生成提示排序** → 通过成对比较确定提示的排名。  

## 📌 使用 `HintRank` 进行提示排序

`HintRank` 模块可基于 **BERT 模型** **自动对提示进行排序**。

### 🚀 在 Google Colab 运行 HintRank 演示

无需本地安装，您可以直接在浏览器中使用 **Google Colab** 运行 **HintRank**。点击 **[启动 Colab Notebook](https://colab.research.google.com/github/DataScienceUIBK/WikiHint/blob/main/HintRank/Demo.ipynb)** 进行交互式体验。

### 1️⃣ 安装依赖

如果在本地运行，请确保已安装以下依赖项：

```sh
pip install transformers torch numpy scipy
```

### 2️⃣ 导入并初始化 HintRank

进入 `HintRank` 目录并导入 `hint_rank` 模块：

```python
from HintRank.hint_rank import HintRank

# 初始化 HintRank 模型
ranker = HintRank()
```

### 3️⃣ 对特定问题的提示进行排序

```python
question = "奥地利的首都是哪里？"
answer = "维也纳"
hints = [
    "莫扎特和贝多芬曾在这里居住。",
    "它是欧洲的一座大城市。",
    "奥地利最大的城市。"
]

# 进行成对比较
better_hint_answer_aware = ranker.pairwise_compare(question, hints[1], hints[2], answer)
better_hint_answer_agnostic = ranker.pairwise_compare(question, hints[0], hints[1])

print(f"基于答案的排序：提示 {2 if better_hint_answer_aware == 1 else 3} 优于 提示 {3 if better_hint_answer_aware == 0 else 2}。")
print(f"不考虑答案的排序：提示 {1 if better_hint_answer_agnostic == 1 else 2} 优于 提示 {2 if better_hint_answer_agnostic == 0 else 1}。")
```

### 4️⃣ 进行多提示排序

您也可以一次性对多个提示进行排序：

```python
print("\n基于答案的提示排序：")
ranked_hints_answer_aware = ranker.listwise_compare(question, hints, answer)
for i, (hint, _) in enumerate(ranked_hints_answer_aware):
    print(f"排名 {i + 1}：{hint}")

print("\n不考虑答案的提示排序：")
ranked_hints_answer_agnostic = ranker.listwise_compare(question, hints)
for i, (hint, _) in enumerate(ranked_hints_answer_agnostic):
    print(f"排名 {i + 1}：{hint}")
```

### 📌 预期输出

```
成对提示比较：
	基于答案：提示 3 优于 提示 2。
	不考虑答案：提示 2 优于 提示 1。

多提示排序：
	基于答案的排序：
		排名 1：奥地利最大的城市。
		排名 2：莫扎特和贝多芬曾在这里居住。
		排名 3：它是欧洲的一座大城市。

	不考虑答案的排序：
		排名 1：它是欧洲的一座大城市。
		排名 2：奥地利最大的城市。
		排名 3：莫扎特和贝多芬曾在这里居住。
```

---

## 📊 🆚 WikiHint vs. TriviaHG 数据集对比

下表比较了 **WikiHint** 和 **TriviaHG**（此前最大的提示生成数据集）。WikiHint 在多个评估指标上表现更优，包括 **更高的收敛性**、**更短的提示** 和 **更高质量的提示**。

| **数据集** | **子集** | **相关性** | **可读性** | **收敛性** | **熟悉度** | **提示长度** | **答案泄露（均值）** | **答案泄露（最大值）** |
|------------|-----------|--------------|----------------|--------------|--------------|---------|----------------|----------------|
| TriviaHG   | 全部      | 0.95         | 0.71           | 0.57         | 0.77         | 20.82   | 0.23           | 0.44           |
| WikiHint   | 全部      | 0.98         | 0.72           | 0.73         | 0.75         | 17.82   | 0.24           | 0.49           |
| TriviaHG   | 训练集    | 0.95         | 0.73           | 0.57         | 0.75         | 21.19   | 0.22           | 0.44           |
| WikiHint   | 训练集    | 0.98         | 0.71           | 0.74         | 0.76         | 17.77   | 0.24           | 0.49           |
| TriviaHG   | 测试集    | 0.95         | 0.73           | 0.60         | 0.77         | 20.97   | 0.23           | 0.44           |
| WikiHint   | 测试集    | 0.98         | 0.83           | 0.72         | 0.73         | 18.32   | 0.24           | 0.47           |

📌 **主要发现**：
- **WikiHint 在收敛性上优于 TriviaHG**，这意味着它的提示更有助于用户**更快地找到正确答案**。
- **WikiHint 的提示更短**，提供**更简洁和有效的指导**。

## 📊🤖 生成提示的评估

下表展示了不同 **LLM（LLaMA-3.1、GPT-4）** 生成的提示在 **相关性、可读性、收敛性、熟悉度、提示长度和答案泄露** 方面的评估。这可以帮助理解 **微调（FT）** 和 **基于答案（wA）** 对提示质量的影响。

| **模型** | **配置** | **使用答案？** | **相关性** | **可读性** | **收敛性（LLaMA-8B）** | **收敛性（LLaMA-70B）** | **熟悉度** | **提示长度** | **答案泄露（均值）** | **答案泄露（最大值）** |
|-----------|----------|---------------|--------------|----------------|------------------|------------------|--------------|---------|----------------|----------------|
| **GPT-4**    | Vanilla  | ✅      | 0.91         | 1.00           | 0.14             | 0.48             | 0.84         | 26.36   | 0.23           | 0.51           |
| **GPT-4**    | Vanilla  | ❌      | 0.92         | 1.10           | 0.12             | 0.47             | 0.81         | 26.93   | 0.24           | 0.52           |
| **LLaMA-3.1-405b** | Vanilla  | ✅ | 0.94         | 1.49           | 0.11             | 0.47             | 0.76         | 41.81   | 0.23           | 0.50           |
| **LLaMA-3.1-405b** | Vanilla  | ❌| 0.92         | 1.53           | 0.10             | 0.45             | 0.78         | 50.91   | 0.23           | 0.50           |
| **LLaMA-3.1-70b**  | FTwA    | ✅ | 0.88         | 1.50           | 0.09             | 0.42             | 0.84         | 43.69   | 0.22           | 0.48           |
| **LLaMA-3.1-70b**  | Vanilla  | ✅ | 0.86         | 1.53           | 0.05             | 0.42             | 0.80         | 45.51   | 0.23           | 0.50           |
| **LLaMA-3.1-70b**  | FTwoA   | ❌ | 0.86         | 1.50           | 0.08             | 0.38             | 0.80         | 51.07   | 0.22           | 0.51           |
| **LLaMA-3.1-70b**  | Vanilla  | ❌ | 0.87         | 1.56           | 0.06             | 0.38             | 0.76         | 53.24   | 0.22           | 0.50           |
| **LLaMA-3.1-8b**   | FTwA    | ✅ | 0.78         | 1.63           | 0.05             | 0.37             | 0.79         | 50.33   | 0.22           | 0.52           |
| **LLaMA-3.1-8b**   | Vanilla  | ✅ | 0.81         | 1.72           | 0.05             | 0.32             | 0.80         | 54.38   | 0.22           | 0.50           |
| **LLaMA-3.1-8b**   | FTwoA   | ❌ | 0.76         | 1.70           | 0.03             | 0.32             | 0.80         | 55.02   | 0.22           | 0.51           |
| **LLaMA-3.1-8b**   | Vanilla  | ❌ | 0.78         | 1.76           | 0.04             | 0.30             | 0.83         | 52.99   | 0.22           | 0.50           |

📌 **关键结论**：
- **相关性**：**更大规模的模型（405b、70b）提供更优质的提示**，相比之下小型模型（8b）表现较弱。
- **可读性**：**GPT-4 生成的提示最容易理解**。
- **收敛性**：**基于答案的提示（wA）能帮助 LLM 生成更好的提示**。
- **熟悉度**：较大的模型能够**生成更符合常识的提示**。
- **提示长度**：**微调后的模型（FTwA、FTwoA）生成更短且更优质的提示**。

---

## 📂 代码仓库结构

```
📂 WikiHint/               # 🗂 数据集文件
│   ├── 📄 Pipeline.png    # 📊 数据集处理流程
│   ├── 📄 training.json   # 📊 训练数据集（900 道问题，4500 条提示）
│   ├── 📄 test.json       # 📊 测试数据集（100 道问题，500 条提示）
│
├── 📂 Experiments/        # 🧪 LLM 生成的提示
│   ├── 📄 GPT-4-Vanilla-answer-agnostic.json
│   ├── 📄 GPT-4-Vanilla-answer-aware.json
│   ├── 📄 LLaMA-3.1-70b-FTwA-answer-aware.json
│   ├── 📄 LLaMA-3.1-70b-FTwoA-answer-agnostic.json
│
├── 📂 HintRank/           # 🏆 提示排序方法
│   ├── 📄 EvaluationMethod.png  # 📊 HintRank 评估方法可视化
│   ├── 📄 hint_rank.py          # 📜 HintRank 实现
│
├── 📂 HumanEvaluation/    # 👨‍🔬 人工评估数据
│   ├── 📂 Person_1/  
│   │   ├── 📑 Part_1.xlsx
│   │   ├── 📑 Part_2.xlsx
│   │   ├── ...（其余同 Person_1）
│
└── 📘 README.md           # 📖 本文件
```

## 📜 许可协议

本项目采用 **Creative Commons Attribution 4.0 International License (CC BY 4.0)** 许可。您可以自由使用、共享和修改数据集，但需注明出处。

## 📑 论文引用

如果您觉得本项目对您的研究有所帮助，请引用 [📜我们的论文](https://doi.org/10.48550/arXiv.2412.01626)：

```bibtex
@article{mozafari2025wikihinthumanannotateddatasethint,
      title={WikiHint: A Human-Annotated Dataset for Hint Ranking and Generation}, 
      author={Jamshid Mozafari and Florian Gerhold and Adam Jatowt},
      year={2025},
      eprint={2412.01626},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      doi={10.48550/arXiv.2412.01626}, 
}
```

## 🙏 致谢

感谢所有贡献者以及因斯布鲁克大学（University of Innsbruck）对本项目的支持。
