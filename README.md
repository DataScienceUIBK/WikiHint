# WikiHint: A Human-Annotated Dataset for Hint Ranking and Generation

<a href="https://doi.org/10.48550/arXiv.2412.01626"><img src="https://img.shields.io/static/v1?label=Paper&message=ACM SIGIR&color=green&logo=arxiv"></a>
[![License](https://img.shields.io/badge/License-CC%20BY%204.0-blue)](https://creativecommons.org/licenses/by/4.0/)

<img src="https://github.com/DataScienceUIBK/WikiHint/blob/main/WikiHint/Pipeline.png">

WikiHint is a **human-annotated dataset** designed for **automatic hint generation and ranking** for factoid questions. This dataset, based on Wikipedia, contains **5,000 hints for 1,000 questions** and supports research in **hint evaluation, ranking, and generation**.

## 📂 Repository Structure

```
📂 WikiHint/                                                # 🗂 Dataset files
│   ├── 📄 Training.json                                    # 📊 Training dataset (900 questions, 4500 hints)
│   ├── 📄 Test.json                                        # 📊 Test dataset (100 questions, 500 hints)
│
├── 📂 Experiments/                                         # 🧪 Model-generated hints
│   ├── 📄 GPT-4-Vanilla-answer-agnostic.json
│   ├── 📄 GPT-4-Vanilla-answer-aware.json
│   ├── 📄 LLaMA-3.1-405b-Vanilla-answer-agnostic.json
│   ├── 📄 LLaMA-3.1-405b-Vanilla-answer-aware.json
│   ├── 📄 LLaMA-3.1-70b-FTwA-answer-aware.json
│   ├── 📄 LLaMA-3.1-70b-FTwoA-answer-agnostic.json
│   ├── 📄 LLaMA-3.1-70b-Vanilla-answer-agnostic.json
│   ├── 📄 LLaMA-3.1-70b-Vanilla-answer-aware.json
│   ├── 📄 LLaMA-3.1-8b-FTwA-answer-aware.json
│   ├── 📄 LLaMA-3.1-8b-FTwoA-answer-agnostic.json
│   ├── 📄 LLaMA-3.1-8b-Vanilla-answer-agnostic.json
│   ├── 📄 LLaMA-3.1-8b-Vanilla-answer-aware.json
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

## 🗂 Overview

- **1,000 questions** with **5,000 manually created hints**.
- Hints ranked by **human annotators** based on helpfulness.
- Includes **answer-aware and answer-agnostic** hints.
- Evaluated using **LLMs (LLaMA, GPT-4)** and **human performance studies**.
- Supports **hint ranking** and **automatic hint evaluation**.

## 🔬 Research Contributions

✅ **First human-annotated dataset** for hint generation and ranking.  
✅ **HintRank:** A lightweight method for automatic hint ranking.  
✅ **Human study** evaluating hint effectiveness in helping users answer questions.  
✅ **Fine-tuning open-source LLMs** (LLaMA-3.1, GPT-4) for hint generation.  

## 📈 Key Insights

- **Answer-aware hints** improve hint effectiveness.  
- **Finetuned LLaMA models** generate better hints than vanilla models.  
- **Shorter hints** tend to be **more effective** than longer ones.  
- **Human-generated hints** outperform LLM-generated hints in clarity and ranking.

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


## 🏆 HintRank: A Lightweight Hint Ranking Method

HintRank is an **automatic ranking method** for hints using **BERT-based models**. It operates on **pairwise comparisons**, determining the **relative helpfulness of hints**.

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

# Initialize the HintRank model
ranker = HintRank()

# Define question, answer, and hints
question = "What is the capital of Austria?"
answer = "Vienna"
hints = [
    "Mozart and Beethoven once lived here.",
    "It is a big city in Europe.",
    "Austria’s largest city and capital."
]

# Pairwise Comparison Example
print("Pairwise Hint Comparison\n")
better_hint_answer_aware = ranker.pairwise_compare(question, hints[1], hints[2], answer)
better_hint_answer_agnostic = ranker.pairwise_compare(question, hints[0], hints[1])

print(f"Answer-Aware: Hint {2 if better_hint_answer_aware == 1 else 3} is better than Hint {3 if better_hint_answer_aware == 0 else 2}.")
print(f"Answer-Agnostic: Hint {1 if better_hint_answer_agnostic == 1 else 2} is better than Hint {2 if better_hint_answer_agnostic == 0 else 1}.")

print("\nListwise Hint Ranking")

# Answer-Aware Ranking
print("\nAnswer-Aware Ranked Hints:")
ranked_hints_answer_aware = ranker.listwise_compare(question, hints, answer)
for i, (hint, _) in enumerate(ranked_hints_answer_aware):
    print(f"Rank {i + 1}: {hint}")

# Answer-Agnostic Ranking
print("\nAnswer-Agnostic Ranked Hints:")
ranked_hints_answer_agnostic = ranker.listwise_compare(question, hints)
for i, (hint, _) in enumerate(ranked_hints_answer_agnostic):
    print(f"Rank {i + 1}: {hint}")
```

### 📌 Example Output

```
Pairwise Hint Comparison
	Answer-Aware: Hint 3 is better than Hint 2.
	Answer-Agnostic: Hint 2 is better than Hint 1.

Listwise Hint Ranking
	Answer-Aware Ranked Hints:
		Rank 1: Austria’s largest city and capital.
		Rank 2: Mozart and Beethoven once lived here.
		Rank 3: It is a big city in Europe.

	Answer-Agnostic Ranked Hints:
		Rank 1: It is a big city in Europe.
		Rank 2: Austria’s largest city and capital.
		Rank 3: Mozart and Beethoven once lived here.
```

📌 **HintRank achieves** higher accuracy compared to **Convergence and LLM-based hint ranking methods**, making it an efficient and reliable tool.

## 📊 🆚 WikiHint vs. TriviaHG Dataset Comparison

The table below compares **WikiHint** with **TriviaHG**, the largest previous dataset for hint generation. WikiHint has **better convergence**, **shorter hints**, and **higher-quality** hints based on multiple evaluation metrics.

| **Dataset** | **Subset** | **Relevance** | **Readability** | **Convergence** | **Familiarity** | **Length** | **Answer Leakage (Avg.)** | **Answer Leakage (Max.)** |
|------------|-----------|--------------|----------------|--------------|--------------|---------|----------------|----------------|
| TriviaHG   | Entire    | 0.95         | 0.71           | 0.57         | 0.77         | 20.82   | 0.23           | 0.44           |
| WikiHint   | Entire    | 0.98         | 0.72           | 0.73         | 0.75         | 17.82   | 0.24           | 0.49           |
| TriviaHG   | Train     | 0.95         | 0.73           | 0.57         | 0.75         | 21.19   | 0.22           | 0.44           |
| WikiHint   | Train     | 0.98         | 0.71           | 0.74         | 0.76         | 17.77   | 0.24           | 0.49           |
| TriviaHG   | Test      | 0.95         | 0.73           | 0.60         | 0.77         | 20.97   | 0.23           | 0.44           |
| WikiHint   | Test      | 0.98         | 0.83           | 0.72         | 0.73         | 18.32   | 0.24           | 0.47           |

📌 **Key Findings**:
- **WikiHint outperforms TriviaHG** in **convergence**, meaning its hints help users **arrive at answers more effectively**.
- **WikiHint’s hints are shorter**, leading to **more concise and effective guidance**.

## 📊🤖 Evaluation of Generated Hints

This table presents an **evaluation of generated hints** across different **LLMs (LLaMA-3.1, GPT-4)** based on **Relevance, Readability, Convergence, Familiarity, Hint Length, and Answer Leakage**. It provides insights into how **finetuning (FT)** and **answer-awareness (wA)** affect hint quality.

| **Model** | **Config** | **Use Answer?** | **Rel** | **Read** | **Conv (LLaMA-8B)** | **Conv (LLaMA-70B)** | **Fam** | **Len** | **AnsLkg (Avg.)** | **AnsLkg (Max.)** |
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

📌 **Key Takeaways**:
- **Relevance**: **Larger models (405b, 70b) provide better hints** compared to smaller (8b) models.
- **Readability**: **GPT-4 produces the most readable hints**.
- **Convergence**: **Answer-aware hints (wA) help LLMs generate better hints**.
- **Familiarity**: Larger models generate **more familiar hints** based on common knowledge.
- **Hint Length**: **Finetuned models (FTwA, FTwoA) generate shorter and better hints**.


## 📜 License

This project is licensed under the **Creative Commons Attribution 4.0 International License (CC BY 4.0)**. You are free to use, share, and adapt the dataset with proper attribution.


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

## 🙏Acknowledgments

Thanks to our contributors and the University of Innsbruck for supporting this project.
