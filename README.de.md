[English](README.md) | [中文](README.zh.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Русский](README.ru.md)

# WikiHint: Ein von Menschen annotierter Datensatz für Hinweisbewertung und -generierung
<a href="https://huggingface.co/datasets/JamshidJDMY/WikiHint"><img alt="Huggingface" src="https://img.shields.io/static/v1?label=Dataset&message=WikiHint&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAAIGNIUk0AAHomAACAhAAA+gAAAIDoAAB1MAAA6mAAADqYAAAXcJy6UTwAAAIoUExURQAAAP/////57v/67xUVFf/clv+KAP/uzf/sxv8AAP9TAP/ltP///v/ouP/////////////////////////////8+v/pvP/biP/Vbf/Vbv/cif/qv//9+//////////03v/Yev/Zfv/14//25v/Uav/Vbv/46//////dkf/gmP/////04P/25//pvP/sxf/////lr//ouP/qwP/tyf/msv/ntf/+/P/36f/LUf/36P/w0v/w0//w0//w0//78//gm//QZv/RZv/gm//78v/////14v/nt//gnP/hn//w0f/////w0f/hn//gnP/nt//14v/////////////////LLv/MGv/PGf/LL//LG//THP/THv/SHv/UHv/LGv/LH/7SHuK8JOzDIuW+I+jAI//LHv/PTP/NF/PBG3BkOpyGMvrOH4R0NoV0NvzJGv/MF//QT//MLv/LGPu/FNayJu7FIdq2Jf7DFP/JF//ML//LJurCIsCiKujCIubAI7+hK/DHIf/LJ//HK//NGf/SHeS9IlxSP25QQmtOQmVZPu3DIf/RHf/HLP++Kf/AD/++EP3EFNCfLNhpQthrQdinKv/FFP/AEP+/K/++Dv/BEv+/Ef/CE//MIf/NIP/MGf++D//KTP/FOP/DE//PG//PHP/JGP/EFP/EM//BDf/TH//GFP/CEP/DEP/EEv/BDv/MS//IJ//JHf/JHP/JP//IQf/IHP/IJv/LSf///7SHOh0AAABUdFJOUwAAAAAAAAAAAAAAAAAABiZCQykIAUGn3/Hy4q5KAwRy7vJ/Yfb7cR/X4ipkdpepAqi5mavM2z5v/pGTtZS2QtP4999bIGyry8yUR4fJzbJ2BRIRE9ZoIHEAAAABYktHRAH/Ai3eAAAAB3RJTUUH6AIGEyohVAr+rAAAARZJREFUGNNjYGBgZGTi4xcQFBJmZmRkYQDxRUTFxCUkpaRlZBkZQXw5eYWQ0LCw0HBFJWGgCCOrskpEZFR0dExkrKoaG1BAXSMuPiExOjopOSpFU4uRgV07NS09IzMqKzsnNy9fh4OBU7egsKi4JCo6ubSsvEJPlkHfoDIqqqq6prauPiqqwVCYgcuosam5pbWtvaOzq6nbWJZBy6Snt69/wsRJk6f0TZ1masZgbjF9xsxZhbPnzJ01c8a8+ZYMVgt6F5aHLly0eGHokqVTl1kz2CxYXhi1YuWq1WuiouauXWbLYGe/bv2GjZscHDdv2bh1m5MzA7eLq5u7h6eXoLePr5+/ENDpjBwBgYH6PIyMQcF8vIyMAKnZUpQQgaV4AAAAJXRFWHRkYXRlOmNyZWF0ZQAyMDI0LTAyLTA2VDE5OjQyOjI1KzAwOjAwybP6HAAAACV0RVh0ZGF0ZTptb2RpZnkAMjAyNC0wMi0wNlQxOTo0MjoyNSswMDowMLjuQqAAAAAodEVYdGRhdGU6dGltZXN0YW1wADIwMjQtMDItMDZUMTk6NDI6MzMrMDA6MDBAgVbbAAAAAElFTkSuQmCC&color=20BEFF"/></a>
<a href="https://doi.org/10.1145/3726302.3730284"><img src="https://img.shields.io/static/v1?label=Paper&message=ACM%20SIGIR&color=green&logo=arxiv"></a>
<a href="https://colab.research.google.com/github/DataScienceUIBK/WikiHint/blob/main/HintRank/Demo.ipynb"><img src="https://img.shields.io/static/v1?label=Colab&message=Demo&logo=Google%20Colab&color=f9ab00"></a>
[![License](https://img.shields.io/badge/License-CC%20BY%204.0-blue)](https://creativecommons.org/licenses/by/4.0/)
<img src="https://github.com/DataScienceUIBK/WikiHint/blob/main/WikiHint/Pipeline.png">

WikiHint ist ein **von Menschen annotierter Datensatz**, der für die **automatische Generierung und Bewertung von Hinweisen** bei Faktfragen entwickelt wurde. Der Datensatz basiert auf Wikipedia und enthält **5.000 Hinweise zu 1.000 Fragen**. Er unterstützt die Forschung in den Bereichen **Hinweisbewertung, -ranking und -generierung**.

## <img src="https://github.com/DataScienceUIBK/TriviaHG/blob/main/Framework/gif-dan.gif" width="32" height="32"/> Achtung <img src="https://github.com/DataScienceUIBK/TriviaHG/blob/main/Framework/gif-dan.gif" width="32" height="32"/>

Ab **Februar 2025** empfehlen wir die Nutzung von **HintEval**, dem Framework für **Hinweiserzeugung und -bewertung**. HintEval enthält den **WikiHint-Datensatz** sowie die Evaluationsmetriken aus der WikiHint-Publikation und macht die Arbeit mit Hinweisen so einfach wie nie zuvor.

Hier geht’s zu HintEval:  
- 📖 **[HintEval-Dokumentation](http://hinteval.readthedocs.io/)**  
- 📦 **[HintEval PyPI-Installation](https://pypi.org/project/hinteval/)**  
- 💻 **[HintEval GitHub-Repository](https://github.com/DataScienceUIBK/HintEval)**  
- 📜 **[HintEval-Paper (arXiv)](https://doi.org/10.48550/arXiv.2502.00857)**  

Für eine **nahtlose Integration** von Hinweiserzeugung und -bewertung empfehlen wir dringend den **Umstieg** auf **HintEval**!

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
