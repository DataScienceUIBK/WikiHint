Here’s your **updated GitHub README** with a **separate section for HintRank**:

---

# WikiHint: A Human-Annotated Dataset for Hint Ranking and Generation

<a href="https://doi.org/10.1145/3626772.3657855"><img src="https://img.shields.io/static/v1?label=Paper&message=ACM SIGIR&color=green&logo=arxiv"></a>
[![License](https://img.shields.io/badge/License-CC%20BY%204.0-blue)](https://creativecommons.org/licenses/by/4.0/)

<img src="https://github.com/DataScienceUIBK/WikiHint/blob/main/Images/Pipeline.png">

WikiHint is a **human-annotated dataset** designed for **automatic hint generation and ranking** for factoid questions. This dataset, based on Wikipedia, contains **5,000 hints for 1,000 questions** and supports research in **hint evaluation, ranking, and generation**.

---

## 📂 Repository Structure

```
📂 WikiHint/                                                # 🗂 Dataset files
│   ├── 📄 Training.json                                    # 📊 Training dataset (900 questions, 4500 hints)
│   ├── 📄 Test.json                                        # 📊 Test dataset (100 questions, 500 hints)
│
├── 📂 Experiments/                                         # 🧪 Model-generated hints
│   ├── 📜 GPT-4-Vanilla-answer-agnostic.json
│   ├── 📜 GPT-4-Vanilla-answer-aware.json
│   ├── 📜 LLaMA-3.1-405b-Vanilla-answer-agnostic.json
│   ├── 📜 LLaMA-3.1-405b-Vanilla-answer-aware.json
│   ├── 📜 LLaMA-3.1-70b-FTwA-answer-aware.json
│   ├── 📜 LLaMA-3.1-70b-FTwoA-answer-agnostic.json
│   ├── 📜 LLaMA-3.1-70b-Vanilla-answer-agnostic.json
│   ├── 📜 LLaMA-3.1-70b-Vanilla-answer-aware.json
│   ├── 📜 LLaMA-3.1-8b-FTwA-answer-aware.json
│   ├── 📜 LLaMA-3.1-8b-FTwoA-answer-agnostic.json
│   ├── 📜 LLaMA-3.1-8b-Vanilla-answer-agnostic.json
│   ├── 📜 LLaMA-3.1-8b-Vanilla-answer-aware.json
│
├── 📂 HumanEvaluation/                                     # 👨‍🔬 Human evaluation data
│   ├── 📂 Person_1/ (Person_2, ..., Person_5)
│   │   ├── 📑 Part_1.xlsx
│   │   ├── 📑 Part_2.xlsx
│   │   ├── ...
│   │   ├── 📑 Part_10.xlsx
│
└── 📘 README.md                                            # 📖 This file
```

---

## 🗂 Dataset Overview

- **1,000 questions** with **5,000 manually created hints**.
- Hints ranked by **human annotators** based on helpfulness.
- Includes **answer-aware and answer-agnostic** hints.
- Evaluated using **LLMs (LLaMA, GPT-4)** and **human performance studies**.
- Supports **hint ranking** and **automatic hint evaluation**.

---

## 🔬 Research Contributions

✅ **First human-annotated dataset** for hint generation and ranking.  
✅ **HintRank:** A lightweight method for automatic hint ranking.  
✅ **Human study** evaluating hint effectiveness in helping users answer questions.  
✅ **Fine-tuning open-source LLMs** (LLaMA-3.1, GPT-4) for hint generation.  

---

## 📊 Results and Insights

- **Answer-aware hints** improve hint effectiveness.  
- **Finetuned LLaMA models** generate better hints than vanilla models.  
- **Shorter hints** tend to be **more effective** than longer ones.  
- **Human-generated hints** outperform LLM-generated hints in clarity and ranking.

---

## 🏆 HintRank: A Lightweight Hint Ranking Method

HintRank is an **automatic evaluation and ranking method** for factoid hints using **BERT-based models**. It operates on **pairwise comparisons**, determining the **relative helpfulness of hints**.

### ✨ Features:
✔ **Lightweight**: Runs locally without requiring massive computational resources.  
✔ **LLM-free evaluation**: Works without relying on **large-scale generative models**.  
✔ **Human-aligned ranking**: Strong correlation with **human-assigned hint rankings**.  

### 🔍 How It Works:
1. **Concatenates question & two hints** → Converts them into BERT-compatible format.  
2. **Computes hint quality** → Determines which hint is **more useful**.  
3. **Generates hint rankings** → Assigns ranks based on pairwise comparisons.  

### 🚀 Using HintRank:
```python
from hint_rank import HintRank

question = "Which city is Australia's second-largest industrial centre?"
hint_1 = "This city is the capital of the Australian State of Victoria."
hint_2 = "This is the second most populous city in Australia after Sydney."

ranker = HintRank()
better_hint = ranker.compare(question, hint_1, hint_2)
print(f"Better Hint: {better_hint}")
```

📌 **HintRank achieves** higher accuracy compared to **Convergence and LLM-based hint ranking methods**, making it an efficient and reliable tool.

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```sh
git clone https://github.com/your-repo/wikiHint.git
cd wikiHint
```

### 2️⃣ Load the Dataset

```python
import json

with open("WikiHint/Training.json", "r") as f:
    training_data = json.load(f)

with open("WikiHint/Test.json", "r") as f:
    test_data = json.load(f)

print(f"Training set: {len(training_data)} questions")
print(f"Test set: {len(test_data)} questions")
```

#### Example of Answer-Aware vs. Answer-Agnostic Hints

| Type             | Example Hint |
|-----------------|-------------|
| Answer-Aware    | *This is the capital of the Australian state of Victoria.* |
| Answer-Agnostic | *This city is home to landmarks like the National Gallery of Victoria.* |

---

## 📜 License

This project is licensed under the **Creative Commons Attribution 4.0 International License (CC BY 4.0)**. You are free to use, share, and adapt the dataset with proper attribution.

---

## 📑 Citation

If you find this work useful, please cite [📜our paper](https://doi.org/10.48550/arXiv.2412.01626):

Mozafari, J., Gerhold, F., & Jatowt, A. (2024). WikiHint: A Human-Annotated Dataset for Hint Ranking and Generation. arXiv preprint arXiv:2412.01626.

### 📄 BibTeX:
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

---

This README is now **structured, visually appealing, and includes a dedicated HintRank section** for users interested in automatic hint ranking! 🚀 Let me know if you'd like any further improvements! 😊
