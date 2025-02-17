[English](README.md) | [中文](README.zh.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Русский](README.ru.md)

# WikiHint : Un Jeu de Données Annoté par des Humains pour le Classement et la Génération d'Indices

<a href="https://doi.org/10.48550/arXiv.2412.01626"><img src="https://img.shields.io/static/v1?label=Article&message=arXiv&color=green&logo=arxiv"></a>
<a href="https://colab.research.google.com/github/DataScienceUIBK/WikiHint/blob/main/HintRank/Demo.ipynb"><img src="https://img.shields.io/static/v1?label=Colab&message=Demo&logo=Google%20Colab&color=f9ab00"></a>
[![License](https://img.shields.io/badge/License-CC%20BY%204.0-blue)](https://creativecommons.org/licenses/by/4.0/)
<img src="https://github.com/DataScienceUIBK/WikiHint/blob/main/WikiHint/Pipeline.png">

WikiHint est un **jeu de données annoté par des humains** conçu pour la **génération et le classement automatiques d'indices** pour les questions factuelles. Ce jeu de données, basé sur Wikipedia, contient **5 000 indices pour 1 000 questions** et soutient la recherche sur **l’évaluation, le classement et la génération d’indices**.

## 🗂 Vue d’ensemble

- **1 000 questions** avec **5 000 indices créés manuellement**.
- Indices classés par des **annotateurs humains** selon leur utilité.
- Évalué à l'aide de **LLMs (LLaMA, GPT-4)** et d’**études sur la performance humaine**.
- Supporte le **classement des indices** et **l’évaluation automatique des indices**.

## 🔬 Contributions à la recherche

✅ **Premier jeu de données annoté par des humains** pour la génération et le classement d'indices.  
✅ **HintRank** : Une méthode légère pour le classement automatique des indices.  
✅ **Étude humaine** évaluant l’efficacité des indices pour aider les utilisateurs à répondre aux questions.  
✅ **Ajustement fin des LLM open-source** (LLaMA-3.1, GPT-4) pour la génération d’indices.  

## 📈 Principaux enseignements

- **Les indices tenant compte de la réponse** améliorent leur efficacité.  
- **Les modèles LLaMA ajustés finement** génèrent de meilleurs indices que les modèles bruts.  
- **Les indices plus courts** ont tendance à être **plus efficaces** que les plus longs.  
- **Les indices générés par des humains** surpassent ceux des LLM en termes de clarté et de classement.

## 🚀 Prise en main

### 1️⃣ Cloner le dépôt

```sh
git clone https://github.com/DataScienceUIBK/WikiHint.git
cd WikiHint
```

### 2️⃣ Charger le jeu de données

```python
import json

with open("./WikiHint/training.json", "r") as f:
    training_data = json.load(f)

with open("./WikiHint/test.json", "r") as f:
    test_data = json.load(f)

print(f"Ensemble d’entraînement : {len(training_data)} questions")
print(f"Ensemble de test : {len(test_data)} questions")
```

## 🏆 HintRank : Une Méthode Légère de Classement des Indices

HintRank est une **méthode de classement automatique** des indices utilisant des **modèles basés sur BERT**. Il fonctionne sur le principe des **comparaisons par paires**, déterminant la **pertinence relative des indices**.

<p align="center">
    <img src="https://raw.githubusercontent.com/DataScienceUIBK/WikiHint/main/HintRank/EvaluationMethod.png" width="35%">
</p>

### ✨ Fonctionnalités :
✔ **Léger** : Fonctionne localement sans nécessiter de ressources informatiques massives.  
✔ **Évaluation sans LLM** : Fonctionne sans dépendre de **grands modèles génératifs**.  
✔ **Classement aligné sur les humains** : Forte corrélation avec le **classement des indices établi par des humains**.  

### 🔍 Comment ça marche ?
1. **Concatène la question & deux indices** → Les convertit au format compatible BERT.  
2. **Calcule la qualité des indices** → Détermine quel indice est **le plus utile**.  
3. **Génère un classement des indices** → Attribue un rang basé sur des comparaisons par paires.  

## 📌 Utilisation de `HintRank` pour le Classement des Indices

Le module `HintRank` est conçu pour **classer automatiquement les indices** selon leur pertinence à l’aide de **modèles basés sur BERT**.

### 🚀 Exécuter la Démo HintRank sur Google Colab

Vous pouvez facilement essayer **HintRank** dans votre navigateur via **Google Colab**, sans installation locale requise. Lancez simplement le **[notebook Colab](https://colab.research.google.com/github/DataScienceUIBK/WikiHint/blob/main/HintRank/Demo.ipynb)** pour explorer **HintRank** de manière interactive.

### 1️⃣ Installer les dépendances

Si vous exécutez HintRank localement, assurez-vous d’avoir installé les dépendances requises :

```sh
pip install transformers torch numpy scipy
```

### 2️⃣ Importer et initialiser HintRank

Accédez au répertoire `HintRank` et importez le module `hint_rank` :

```python
from HintRank.hint_rank import HintRank

# Initialiser le modèle HintRank
ranker = HintRank()
```

### 3️⃣ Classer les indices pour une question donnée

```python
question = "Quelle est la capitale de l'Autriche ?"
answer = "Vienne"
hints = [
    "Mozart et Beethoven y ont vécu.",
    "C'est une grande ville en Europe.",
    "La plus grande ville d'Autriche."
]

# Exemple de comparaison par paires
better_hint_answer_aware = ranker.pairwise_compare(question, hints[1], hints[2], answer)
better_hint_answer_agnostic = ranker.pairwise_compare(question, hints[0], hints[1])

print(f"Réponse-Consciente : L'indice {2 if better_hint_answer_aware == 1 else 3} est meilleur que l'indice {3 if better_hint_answer_aware == 0 else 2}.")
print(f"Réponse-Agnostique : L'indice {1 if better_hint_answer_agnostic == 1 else 2} est meilleur que l'indice {2 if better_hint_answer_agnostic == 0 else 1}.")
```

### 4️⃣ Classement des indices en liste

Vous pouvez également classer plusieurs indices en une seule fois :

```python
print("\nIndices classés (Réponse-Consciente) :")
ranked_hints_answer_aware = ranker.listwise_compare(question, hints, answer)
for i, (hint, _) in enumerate(ranked_hints_answer_aware):
    print(f"Rang {i + 1} : {hint}")

print("\nIndices classés (Réponse-Agnostique) :")
ranked_hints_answer_agnostic = ranker.listwise_compare(question, hints)
for i, (hint, _) in enumerate(ranked_hints_answer_agnostic):
    print(f"Rang {i + 1} : {hint}")
```

---

### 📌 Résultat Attendu

```
Comparaison par Paires des Indices
	Réponse-Consciente : L'indice 3 est meilleur que l'indice 2.
	Réponse-Agnostique : L'indice 2 est meilleur que l'indice 1.

Classement des Indices en Liste
	Indices Classés (Réponse-Consciente) :
		Rang 1 : La plus grande ville d'Autriche.
		Rang 2 : Mozart et Beethoven y ont vécu.
		Rang 3 : C'est une grande ville en Europe.

	Indices Classés (Réponse-Agnostique) :
		Rang 1 : C'est une grande ville en Europe.
		Rang 2 : La plus grande ville d'Autriche.
		Rang 3 : Mozart et Beethoven y ont vécu.
```

---

## 📊 🆚 Comparaison du Jeu de Données WikiHint vs. TriviaHG

Le tableau ci-dessous compare **WikiHint** avec **TriviaHG**, le plus grand jeu de données précédent pour la génération d'indices. WikiHint offre **une meilleure convergence**, des **indices plus courts** et des **indices de meilleure qualité** selon plusieurs métriques d'évaluation.

| **Jeu de Données** | **Sous-ensemble** | **Pertinence** | **Lisibilité** | **Convergence** | **Familiarité** | **Longueur** | **Fuite de Réponse (Moyenne)** | **Fuite de Réponse (Max.)** |
|--------------------|------------------|---------------|---------------|---------------|---------------|----------|------------------|------------------|
| TriviaHG          | Complet          | 0.95          | 0.71          | 0.57          | 0.77          | 20.82    | 0.23             | 0.44             |
| WikiHint          | Complet          | 0.98          | 0.72          | 0.73          | 0.75          | 17.82    | 0.24             | 0.49             |
| TriviaHG          | Entraînement      | 0.95          | 0.73          | 0.57          | 0.75          | 21.19    | 0.22             | 0.44             |
| WikiHint          | Entraînement      | 0.98          | 0.71          | 0.74          | 0.76          | 17.77    | 0.24             | 0.49             |
| TriviaHG          | Test              | 0.95          | 0.73          | 0.60          | 0.77          | 20.97    | 0.23             | 0.44             |
| WikiHint          | Test              | 0.98          | 0.83          | 0.72          | 0.73          | 18.32    | 0.24             | 0.47             |

📌 **Principaux Résultats** :
- **WikiHint surpasse TriviaHG** en **convergence**, ce qui signifie que ses indices aident les utilisateurs **à trouver les réponses plus efficacement**.
- **Les indices de WikiHint sont plus courts**, ce qui permet une **guidance plus concise et efficace**.

---

## 📊🤖 Évaluation des Indices Générés

Ce tableau présente une **évaluation des indices générés** par différents **LLMs (LLaMA-3.1, GPT-4)** en fonction de **la pertinence, la lisibilité, la convergence, la familiarité, la longueur des indices et la fuite de réponse**. Il met en évidence l'impact du **finetuning (FT)** et de la **prise en compte de la réponse (wA)** sur la qualité des indices.

| **Modèle** | **Config** | **Utilise la Réponse ?** | **Pert.** | **Lisib.** | **Conv. (LLaMA-8B)** | **Conv. (LLaMA-70B)** | **Fam.** | **Long.** | **Fuite (Moyenne)** | **Fuite (Max.)** |
|------------|-----------|----------------|-----------|-----------|------------------|------------------|-----------|---------|----------------|----------------|
| **GPT-4**  | Vanilla   | ✅              | 0.91      | 1.00      | 0.14             | 0.48             | 0.84      | 26.36   | 0.23           | 0.51           |
| **GPT-4**  | Vanilla   | ❌              | 0.92      | 1.10      | 0.12             | 0.47             | 0.81      | 26.93   | 0.24           | 0.52           |
| **LLaMA-3.1-405b** | Vanilla | ✅     | 0.94      | 1.49      | 0.11             | 0.47             | 0.76      | 41.81   | 0.23           | 0.50           |
| **LLaMA-3.1-405b** | Vanilla | ❌     | 0.92      | 1.53      | 0.10             | 0.45             | 0.78      | 50.91   | 0.23           | 0.50           |

📌 **Principaux Enseignements** :
- **Pertinence** : **Les modèles plus grands (405b, 70b) produisent de meilleurs indices** que les modèles plus petits (8b).
- **Lisibilité** : **GPT-4 génère les indices les plus lisibles**.
- **Convergence** : **Les indices prenant en compte la réponse (wA) aident les LLMs à générer de meilleurs indices**.
- **Familiarité** : Les modèles plus grands génèrent **des indices plus familiers**, basés sur des connaissances générales.
- **Longueur des indices** : **Les modèles ajustés finement (FTwA, FTwoA) génèrent des indices plus courts et plus efficaces**.

---

## 📂 Structure du Dépôt

```
📂 WikiHint/                                                # 🗂 Fichiers du jeu de données
│   ├── 📄 Pipeline.png                                     # 📊 Visualisation du pipeline du jeu de données
│   ├── 📄 training.json                                    # 📊 Ensemble d'entraînement (900 questions, 4500 indices)
│   ├── 📄 test.json                                        # 📊 Ensemble de test (100 questions, 500 indices)
│
├── 📂 Experiments/                                         # 🧪 Indices générés par les modèles
│   ├── 📄 GPT-4-Vanilla-answer-agnostic.json
│   ├── 📄 GPT-4-Vanilla-answer-aware.json
│
├── 📂 HintRank/                                            # 🏆 Méthode de classement des indices
│   ├── 📄 EvaluationMethod.png                             # 📊 Visualisation de l’évaluation de HintRank
│   ├── 📄 hint_rank.py                                     # 📜 Implémentation de HintRank
│
├── 📂 HumanEvaluation/                                     # 👨‍🔬 Données d’évaluation humaine
│   ├── 📂 Person_1/  
│   │   ├── 📑 Part_1.xlsx
│   │   ├── 📑 Part_2.xlsx
│   │   ├── 📑 Part_3.xlsx
│   │
│   ├── 📂 Person_2/ (Même structure que Person_1)
│   ├── 📂 Person_3/ (Même structure que Person_1)
│
└── 📘 README.md                                            # 📖 Ce fichier
```

---

## 📜 Licence

Ce projet est sous licence **Creative Commons Attribution 4.0 International (CC BY 4.0)**. Vous êtes libre d'utiliser, partager et adapter le jeu de données avec attribution.

## 📑 Citation

Si ce travail vous est utile, merci de citer [📜notre article](https://doi.org/10.48550/arXiv.2412.01626) :

### 📄 BibTeX :
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

## 🙏 Remerciements

Merci à nos contributeurs et à l'Université d'Innsbruck pour leur soutien à ce projet.
