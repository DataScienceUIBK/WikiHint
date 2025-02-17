# WikiHint: Ein von Menschen annotierter Datensatz für Hinweisbewertung und -generierung

<a href="https://doi.org/10.48550/arXiv.2412.01626"><img src="https://img.shields.io/static/v1?label=Paper&message=arXiv&color=green&logo=arxiv"></a>
<a href="https://colab.research.google.com/github/DataScienceUIBK/WikiHint/blob/main/HintRank/Demo.ipynb"><img src="https://img.shields.io/static/v1?label=Colab&message=Demo&logo=Google%20Colab&color=f9ab00"></a>
[![License](https://img.shields.io/badge/License-CC%20BY%204.0-blue)](https://creativecommons.org/licenses/by/4.0/)
[![en](https://img.shields.io/badge/Lang-En-red.svg)](https://github.com/DataScienceUIBK/WikiHint/blob/main/README.md)
[![ch](https://img.shields.io/badge/Lang-Ch-brown.svg)](https://github.com/DataScienceUIBK/WikiHint/blob/main/README.ch.md)
<img src="https://github.com/DataScienceUIBK/WikiHint/blob/main/WikiHint/Pipeline.png">

WikiHint ist ein **von Menschen annotierter Datensatz**, der für die **automatische Generierung und Bewertung von Hinweisen** bei Faktfragen entwickelt wurde. Der Datensatz basiert auf Wikipedia und enthält **5.000 Hinweise zu 1.000 Fragen**. Er unterstützt die Forschung in den Bereichen **Hinweisbewertung, -ranking und -generierung**.

## 🗂 Überblick

- **1.000 Fragen** mit **5.000 manuell erstellten Hinweisen**.
- Hinweise werden von **menschlichen Annotatoren** nach Nützlichkeit bewertet.
- Evaluierung durch **LLMs (LLaMA, GPT-4)** und **Studien zur menschlichen Leistung**.
- Unterstützt **Hinweisranking** und **automatische Hinweisbewertung**.

## 🔬 Wissenschaftliche Beiträge

✅ **Erster von Menschen annotierter Datensatz** für die Generierung und Bewertung von Hinweisen.  
✅ **HintRank:** Eine leichtgewichtige Methode zur automatischen Hinweisbewertung.  
✅ **Human-Studie** zur Bewertung der Effektivität von Hinweisen für Benutzer.  
✅ **Feinabstimmung von Open-Source-LLMs** (LLaMA-3.1, GPT-4) zur Hinweisgenerierung.  

## 📈 Zentrale Erkenntnisse

- **Antwortbewusste Hinweise** verbessern die Effektivität.  
- **Feinabgestimmte LLaMA-Modelle** erzeugen bessere Hinweise als Standardmodelle.  
- **Kürzere Hinweise** sind tendenziell **effektiver** als längere.  
- **Von Menschen erstellte Hinweise** übertreffen LLM-generierte Hinweise in Klarheit und Ranking.

## 🚀 Erste Schritte

### 1️⃣ Repository klonen

```sh
git clone https://github.com/DataScienceUIBK/WikiHint.git
cd WikiHint
```

### 2️⃣ Datensatz laden

```python
import json

with open("./WikiHint/training.json", "r") as f:
    training_data = json.load(f)

with open("./WikiHint/test.json", "r") as f:
    test_data = json.load(f)

print(f"Trainingsset: {len(training_data)} Fragen")
print(f"Testset: {len(test_data)} Fragen")
```

## 🏆 HintRank: Eine leichtgewichtige Methode zur Hinweisbewertung

HintRank ist eine **automatische Methode zur Bewertung von Hinweisen**, die auf **BERT-basierten Modellen** beruht. Sie nutzt **paarweise Vergleiche**, um die **relative Nützlichkeit von Hinweisen** zu bestimmen.

<p align="center">
    <img src="https://raw.githubusercontent.com/DataScienceUIBK/WikiHint/main/HintRank/EvaluationMethod.png" width="35%">
</p>

### ✨ Funktionen:
✔ **Leichtgewichtig**: Läuft lokal ohne hohen Rechenaufwand.  
✔ **LLM-freie Bewertung**: Funktioniert ohne **große generative Modelle**.  
✔ **An Menschen ausgerichtetes Ranking**: Hohe Korrelation mit **von Menschen zugewiesenen Hinweisbewertungen**.  

### 🔍 Funktionsweise:
1. **Verknüpft Frage & zwei Hinweise** → Konvertiert sie in ein BERT-kompatibles Format.  
2. **Berechnet die Qualität der Hinweise** → Bestimmt, welcher Hinweis **nützlicher** ist.  
3. **Erstellt ein Hinweisranking** → Vergibt Platzierungen basierend auf paarweisen Vergleichen.  

## 📌 Nutzung von `HintRank` zur Hinweisbewertung

Das `HintRank`-Modul dient zur **automatischen Bewertung von Hinweisen** anhand ihrer Nützlichkeit mit **BERT-basierten Modellen**.

### 🚀 HintRank-Demo in Google Colab ausführen

Du kannst **HintRank** einfach in deinem Browser über **Google Colab** ausprobieren, ohne eine lokale Installation vornehmen zu müssen. Starte einfach das **[Colab-Notebook](https://colab.research.google.com/github/DataScienceUIBK/WikiHint/blob/main/HintRank/Demo.ipynb)** und erkunde **HintRank** interaktiv.

### 1️⃣ Abhängigkeiten installieren

Falls du `HintRank` lokal ausführst, installiere die erforderlichen Abhängigkeiten:

```sh
pip install transformers torch numpy scipy
```

### 2️⃣ HintRank importieren und initialisieren

Navigiere in das `HintRank`-Verzeichnis und importiere das `hint_rank`-Modul:

```python
from HintRank.hint_rank import HintRank

# HintRank-Modell initialisieren
ranker = HintRank()
```

### 3️⃣ Hinweise für eine Frage bewerten

```python
question = "Was ist die Hauptstadt von Österreich?"
answer = "Wien"
hints = [
    "Mozart und Beethoven haben hier gelebt.",
    "Es ist eine große Stadt in Europa.",
    "Österreichs größte Stadt."
]

# Beispiel für paarweisen Vergleich
better_hint_answer_aware = ranker.pairwise_compare(question, hints[1], hints[2], answer)
better_hint_answer_agnostic = ranker.pairwise_compare(question, hints[0], hints[1])

print(f"Antwortbewusst: Hinweis {2 if better_hint_answer_aware == 1 else 3} ist besser als Hinweis {3 if better_hint_answer_aware == 0 else 2}.")
print(f"Antwortagnostisch: Hinweis {1 if better_hint_answer_agnostic == 1 else 2} ist besser als Hinweis {2 if better_hint_answer_agnostic == 0 else 1}.")
```

### 4️⃣ Listweises Hinweisranking

Mehrere Hinweise auf einmal bewerten:

```python
print("\nAntwortbewusst gerankte Hinweise:")
ranked_hints_answer_aware = ranker.listwise_compare(question, hints, answer)
for i, (hint, _) in enumerate(ranked_hints_answer_aware):
    print(f"Rang {i + 1}: {hint}")

print("\nAntwortagnostisch gerankte Hinweise:")
ranked_hints_answer_agnostic = ranker.listwise_compare(question, hints)
for i, (hint, _) in enumerate(ranked_hints_answer_agnostic):
    print(f"Rang {i + 1}: {hint}")
```

---

### 📌 Erwartete Ausgabe

```
Paarweiser Hinweisvergleich
	Antwortbewusst: Hinweis 3 ist besser als Hinweis 2.
	Antwortagnostisch: Hinweis 2 ist besser als Hinweis 1.

Listweises Hinweisranking
	Antwortbewusst gerankte Hinweise:
		Rang 1: Österreichs größte Stadt.
		Rang 2: Mozart und Beethoven haben hier gelebt.
		Rang 3: Es ist eine große Stadt in Europa.

	Antwortagnostisch gerankte Hinweise:
		Rang 1: Es ist eine große Stadt in Europa.
		Rang 2: Österreichs größte Stadt.
		Rang 3: Mozart und Beethoven haben hier gelebt.
```

---

## 📊 🆚 Vergleich zwischen WikiHint und TriviaHG-Dataset

Die folgende Tabelle vergleicht **WikiHint** mit **TriviaHG**, dem bisher größten Datensatz zur Hinweisgenerierung. WikiHint zeigt eine **bessere Konvergenz**, **kürzere Hinweise** und **höhere Qualität**, basierend auf mehreren Evaluierungskriterien.

| **Datensatz** | **Subset** | **Relevanz** | **Lesbarkeit** | **Konvergenz** | **Vertrautheit** | **Länge** | **Antwort-Leckage (Ø)** | **Antwort-Leckage (Max.)** |
|--------------|-----------|--------------|----------------|----------------|----------------|----------|----------------|----------------|
| TriviaHG     | Gesamter Datensatz | 0.95 | 0.71 | 0.57 | 0.77 | 20.82 | 0.23 | 0.44 |
| WikiHint     | Gesamter Datensatz | 0.98 | 0.72 | 0.73 | 0.75 | 17.82 | 0.24 | 0.49 |
| TriviaHG     | Training | 0.95 | 0.73 | 0.57 | 0.75 | 21.19 | 0.22 | 0.44 |
| WikiHint     | Training | 0.98 | 0.71 | 0.74 | 0.76 | 17.77 | 0.24 | 0.49 |
| TriviaHG     | Test | 0.95 | 0.73 | 0.60 | 0.77 | 20.97 | 0.23 | 0.44 |
| WikiHint     | Test | 0.98 | 0.83 | 0.72 | 0.73 | 18.32 | 0.24 | 0.47 |

📌 **Wichtige Erkenntnisse**:
- **WikiHint übertrifft TriviaHG** in der **Konvergenz**, was bedeutet, dass seine Hinweise Benutzern **effektiver helfen**, zur richtigen Antwort zu gelangen.
- **WikiHint enthält kürzere Hinweise**, die eine **präzisere und effektivere Unterstützung** bieten.

---

## 📊🤖 Bewertung der generierten Hinweise

Die folgende Tabelle zeigt die **Bewertung der generierten Hinweise** verschiedener **LLMs (LLaMA-3.1, GPT-4)** anhand von **Relevanz, Lesbarkeit, Konvergenz, Vertrautheit, Hinweislänge und Antwort-Leckage**. Sie gibt Einblick, wie sich **Feinabstimmung (FT)** und **Antwortbewusstsein (wA)** auf die Qualität der Hinweise auswirken.

| **Modell** | **Konfiguration** | **Verwendet Antwort?** | **Relevanz** | **Lesbarkeit** | **Konvergenz (LLaMA-8B)** | **Konvergenz (LLaMA-70B)** | **Vertrautheit** | **Länge** | **Antwort-Leckage (Ø)** | **Antwort-Leckage (Max.)** |
|-----------|----------------|------------------|------------|-------------|------------------|------------------|--------------|---------|----------------|----------------|
| **GPT-4** | Vanilla | ✅ | 0.91 | 1.00 | 0.14 | 0.48 | 0.84 | 26.36 | 0.23 | 0.51 |
| **GPT-4** | Vanilla | ❌ | 0.92 | 1.10 | 0.12 | 0.47 | 0.81 | 26.93 | 0.24 | 0.52 |
| **LLaMA-3.1-405b** | Vanilla | ✅ | 0.94 | 1.49 | 0.11 | 0.47 | 0.76 | 41.81 | 0.23 | 0.50 |
| **LLaMA-3.1-70b** | FTwA | ✅ | 0.88 | 1.50 | 0.09 | 0.42 | 0.84 | 43.69 | 0.22 | 0.48 |
| **LLaMA-3.1-70b** | FTwoA | ❌ | 0.86 | 1.50 | 0.08 | 0.38 | 0.80 | 51.07 | 0.22 | 0.51 |

📌 **Wichtige Erkenntnisse**:
- **Relevanz**: **Größere Modelle (405b, 70b) generieren bessere Hinweise** als kleinere (8b).
- **Lesbarkeit**: **GPT-4 erzeugt die am besten lesbaren Hinweise**.
- **Konvergenz**: **Antwortbewusste Hinweise (wA) verbessern die Qualität der Hinweise**.
- **Vertrautheit**: Größere Modelle erstellen **vertrautere Hinweise**, basierend auf allgemeinem Wissen.
- **Hinweislänge**: **Feinabgestimmte Modelle (FTwA, FTwoA) erzeugen kürzere und bessere Hinweise**.

---

## 📂 Verzeichnisstruktur

```
📂 WikiHint/                                                # 🗂 Datensatzdateien
│   ├── 📄 Pipeline.png                                     # 📊 Visualisierung der Datensatz-Pipeline
│   ├── 📄 training.json                                    # 📊 Trainingsdatensatz (900 Fragen, 4500 Hinweise)
│   ├── 📄 test.json                                        # 📊 Testdatensatz (100 Fragen, 500 Hinweise)
│
├── 📂 Experiments/                                         # 🧪 Modellgenerierte Hinweise
│   ├── 📄 GPT-4-Vanilla-answer-agnostic.json
│   ├── 📄 LLaMA-3.1-70b-FTwA-answer-aware.json
│
├── 📂 HintRank/                                            # 🏆 Methode zur Hinweisbewertung
│   ├── 📄 EvaluationMethod.png                             # 📊 Visualisierung der HintRank-Methode
│   ├── 📄 hint_rank.py                                     # 📜 HintRank-Implementierung
│
├── 📂 HumanEvaluation/                                     # 👨‍🔬 Menschliche Evaluationsdaten
│   ├── 📂 Person_1/  
│   │   ├── 📑 Part_1.xlsx
│   │   ├── 📑 Part_2.xlsx
│
│   ├── 📂 Person_2/ (Gleiche Struktur wie Person_1)
│   ├── 📂 Person_3/ (Gleiche Struktur wie Person_1)
│
└── 📘 README.md                                            # 📖 Diese Datei
```

---

## 📜 Lizenz

Dieses Projekt steht unter der **Creative Commons Attribution 4.0 International License (CC BY 4.0)**. Sie können den Datensatz frei nutzen, teilen und anpassen, solange eine korrekte Quellenangabe erfolgt.

---

## 📑 Zitation

Falls Sie unsere Arbeit nützlich finden, zitieren Sie bitte [📜 unser Paper](https://doi.org/10.48550/arXiv.2412.01626):

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

## 🙏 Danksagungen

Vielen Dank an unsere Mitwirkenden und die Universität Innsbruck für die Unterstützung dieses Projekts. 🚀
