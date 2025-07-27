[English](README.md) | [中文](README.zh.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Русский](README.ru.md)

# WikiHint : Un Jeu de Données Annoté par des Humains pour le Classement et la Génération d'Indices
<a href="https://huggingface.co/datasets/JamshidJDMY/WikiHint"><img alt="Huggingface" src="https://img.shields.io/static/v1?label=Dataset&message=WikiHint&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAAIGNIUk0AAHomAACAhAAA+gAAAIDoAAB1MAAA6mAAADqYAAAXcJy6UTwAAAIoUExURQAAAP/////57v/67xUVFf/clv+KAP/uzf/sxv8AAP9TAP/ltP///v/ouP/////////////////////////////8+v/pvP/biP/Vbf/Vbv/cif/qv//9+//////////03v/Yev/Zfv/14//25v/Uav/Vbv/46//////dkf/gmP/////04P/25//pvP/sxf/////lr//ouP/qwP/tyf/msv/ntf/+/P/36f/LUf/36P/w0v/w0//w0//w0//78//gm//QZv/RZv/gm//78v/////14v/nt//gnP/hn//w0f/////w0f/hn//gnP/nt//14v/////////////////LLv/MGv/PGf/LL//LG//THP/THv/SHv/UHv/LGv/LH/7SHuK8JOzDIuW+I+jAI//LHv/PTP/NF/PBG3BkOpyGMvrOH4R0NoV0NvzJGv/MF//QT//MLv/LGPu/FNayJu7FIdq2Jf7DFP/JF//ML//LJurCIsCiKujCIubAI7+hK/DHIf/LJ//HK//NGf/SHeS9IlxSP25QQmtOQmVZPu3DIf/RHf/HLP++Kf/AD/++EP3EFNCfLNhpQthrQdinKv/FFP/AEP+/K/++Dv/BEv+/Ef/CE//MIf/NIP/MGf++D//KTP/FOP/DE//PG//PHP/JGP/EFP/EM//BDf/TH//GFP/CEP/DEP/EEv/BDv/MS//IJ//JHf/JHP/JP//IQf/IHP/IJv/LSf///7SHOh0AAABUdFJOUwAAAAAAAAAAAAAAAAAABiZCQykIAUGn3/Hy4q5KAwRy7vJ/Yfb7cR/X4ipkdpepAqi5mavM2z5v/pGTtZS2QtP4999bIGyry8yUR4fJzbJ2BRIRE9ZoIHEAAAABYktHRAH/Ai3eAAAAB3RJTUUH6AIGEyohVAr+rAAAARZJREFUGNNjYGBgZGTi4xcQFBJmZmRkYQDxRUTFxCUkpaRlZBkZQXw5eYWQ0LCw0HBFJWGgCCOrskpEZFR0dExkrKoaG1BAXSMuPiExOjopOSpFU4uRgV07NS09IzMqKzsnNy9fh4OBU7egsKi4JCo6ubSsvEJPlkHfoDIqqqq6prauPiqqwVCYgcuosam5pbWtvaOzq6nbWJZBy6Snt69/wsRJk6f0TZ1masZgbjF9xsxZhbPnzJ01c8a8+ZYMVgt6F5aHLly0eGHokqVTl1kz2CxYXhi1YuWq1WuiouauXWbLYGe/bv2GjZscHDdv2bh1m5MzA7eLq5u7h6eXoLePr5+/ENDpjBwBgYH6PIyMQcF8vIyMAKnZUpQQgaV4AAAAJXRFWHRkYXRlOmNyZWF0ZQAyMDI0LTAyLTA2VDE5OjQyOjI1KzAwOjAwybP6HAAAACV0RVh0ZGF0ZTptb2RpZnkAMjAyNC0wMi0wNlQxOTo0MjoyNSswMDowMLjuQqAAAAAodEVYdGRhdGU6dGltZXN0YW1wADIwMjQtMDItMDZUMTk6NDI6MzMrMDA6MDBAgVbbAAAAAElFTkSuQmCC&color=20BEFF"/></a>
<a href="https://doi.org/10.1145/3726302.3730284"><img src="https://img.shields.io/static/v1?label=Paper&message=ACM%20SIGIR&color=green&logo=arxiv"></a>
<a href="https://colab.research.google.com/github/DataScienceUIBK/WikiHint/blob/main/HintRank/Demo.ipynb"><img src="https://img.shields.io/static/v1?label=Colab&message=Demo&logo=Google%20Colab&color=f9ab00"></a>
[![License](https://img.shields.io/badge/License-CC%20BY%204.0-blue)](https://creativecommons.org/licenses/by/4.0/)
<img src="https://github.com/DataScienceUIBK/WikiHint/blob/main/WikiHint/Pipeline.png">

WikiHint est un **jeu de données annoté par des humains** conçu pour la **génération et le classement automatiques d'indices** pour les questions factuelles. Ce jeu de données, basé sur Wikipedia, contient **5 000 indices pour 1 000 questions** et soutient la recherche sur **l’évaluation, le classement et la génération d’indices**.

## <img src="https://github.com/DataScienceUIBK/TriviaHG/blob/main/Framework/gif-dan.gif" width="32" height="32"/> Attention <img src="https://github.com/DataScienceUIBK/TriviaHG/blob/main/Framework/gif-dan.gif" width="32" height="32"/>

À partir de **février 2025**, nous recommandons d’utiliser **HintEval**, le framework pour la **génération et l’évaluation d’indices**. HintEval inclut le **jeu de données WikiHint** ainsi que les métriques d’évaluation présentées dans l’article WikiHint, rendant le travail avec les indices plus simple que jamais.

Découvrez HintEval ici :  
- 📖 **[Documentation HintEval](http://hinteval.readthedocs.io/)**  
- 📦 **[Installation HintEval via PyPI](https://pypi.org/project/hinteval/)**  
- 💻 **[Dépôt GitHub HintEval](https://github.com/DataScienceUIBK/HintEval)**  
- 📜 **[Article HintEval (arXiv)](https://doi.org/10.48550/arXiv.2502.00857)**  

Pour une **intégration fluide** de la génération et de l’évaluation d’indices, nous vous recommandons vivement de **migrer** vers **HintEval** !

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

Si ce travail vous est utile, merci de citer [📜notre article](https://doi.org/10.1145/3726302.3730284) :

Jamshid Mozafari, Florian Gerhold, and Adam Jatowt. 2025. WikiHint: A Human-Annotated Dataset for Hint Ranking and Generation. In Proceedings of the 48th International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR '25). Association for Computing Machinery, New York, NY, USA, 3821–3831. https://doi.org/10.1145/3726302.3730284

### 📄 BibTeX:
```bibtex
@inproceedings{10.1145/3726302.3730284,
	author = {Mozafari, Jamshid and Gerhold, Florian and Jatowt, Adam},
	title = {WikiHint: A Human-Annotated Dataset for Hint Ranking and Generation},
	year = {2025},
	isbn = {9798400715921},
	publisher = {Association for Computing Machinery},
	address = {New York, NY, USA},
	url = {https://doi.org/10.1145/3726302.3730284},
	doi = {10.1145/3726302.3730284},
	booktitle = {Proceedings of the 48th International ACM SIGIR Conference on Research and Development in Information Retrieval},
	pages = {3821–3831},
	numpages = {11},
	keywords = {hint dataset, hint evaluation, hint generation, hint ranking},
	location = {Padua, Italy},
	series = {SIGIR '25}
}
```

---

## 🙏 Remerciements

Merci à nos contributeurs et à l'Université d'Innsbruck pour leur soutien à ce projet.
