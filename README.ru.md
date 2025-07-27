[English](README.md) | [中文](README.zh.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Русский](README.ru.md)

# WikiHint: Аннотированный человеком набор данных для ранжирования и генерации подсказок
<a href="https://huggingface.co/datasets/JamshidJDMY/WikiHint"><img alt="Huggingface" src="https://img.shields.io/static/v1?label=Dataset&message=WikiHint&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAAIGNIUk0AAHomAACAhAAA+gAAAIDoAAB1MAAA6mAAADqYAAAXcJy6UTwAAAIoUExURQAAAP/////57v/67xUVFf/clv+KAP/uzf/sxv8AAP9TAP/ltP///v/ouP/////////////////////////////8+v/pvP/biP/Vbf/Vbv/cif/qv//9+//////////03v/Yev/Zfv/14//25v/Uav/Vbv/46//////dkf/gmP/////04P/25//pvP/sxf/////lr//ouP/qwP/tyf/msv/ntf/+/P/36f/LUf/36P/w0v/w0//w0//w0//78//gm//QZv/RZv/gm//78v/////14v/nt//gnP/hn//w0f/////w0f/hn//gnP/nt//14v/////////////////LLv/MGv/PGf/LL//LG//THP/THv/SHv/UHv/LGv/LH/7SHuK8JOzDIuW+I+jAI//LHv/PTP/NF/PBG3BkOpyGMvrOH4R0NoV0NvzJGv/MF//QT//MLv/LGPu/FNayJu7FIdq2Jf7DFP/JF//ML//LJurCIsCiKujCIubAI7+hK/DHIf/LJ//HK//NGf/SHeS9IlxSP25QQmtOQmVZPu3DIf/RHf/HLP++Kf/AD/++EP3EFNCfLNhpQthrQdinKv/FFP/AEP+/K/++Dv/BEv+/Ef/CE//MIf/NIP/MGf++D//KTP/FOP/DE//PG//PHP/JGP/EFP/EM//BDf/TH//GFP/CEP/DEP/EEv/BDv/MS//IJ//JHf/JHP/JP//IQf/IHP/IJv/LSf///7SHOh0AAABUdFJOUwAAAAAAAAAAAAAAAAAABiZCQykIAUGn3/Hy4q5KAwRy7vJ/Yfb7cR/X4ipkdpepAqi5mavM2z5v/pGTtZS2QtP4999bIGyry8yUR4fJzbJ2BRIRE9ZoIHEAAAABYktHRAH/Ai3eAAAAB3RJTUUH6AIGEyohVAr+rAAAARZJREFUGNNjYGBgZGTi4xcQFBJmZmRkYQDxRUTFxCUkpaRlZBkZQXw5eYWQ0LCw0HBFJWGgCCOrskpEZFR0dExkrKoaG1BAXSMuPiExOjopOSpFU4uRgV07NS09IzMqKzsnNy9fh4OBU7egsKi4JCo6ubSsvEJPlkHfoDIqqqq6prauPiqqwVCYgcuosam5pbWtvaOzq6nbWJZBy6Snt69/wsRJk6f0TZ1masZgbjF9xsxZhbPnzJ01c8a8+ZYMVgt6F5aHLly0eGHokqVTl1kz2CxYXhi1YuWq1WuiouauXWbLYGe/bv2GjZscHDdv2bh1m5MzA7eLq5u7h6eXoLePr5+/ENDpjBwBgYH6PIyMQcF8vIyMAKnZUpQQgaV4AAAAJXRFWHRkYXRlOmNyZWF0ZQAyMDI0LTAyLTA2VDE5OjQyOjI1KzAwOjAwybP6HAAAACV0RVh0ZGF0ZTptb2RpZnkAMjAyNC0wMi0wNlQxOTo0MjoyNSswMDowMLjuQqAAAAAodEVYdGRhdGU6dGltZXN0YW1wADIwMjQtMDItMDZUMTk6NDI6MzMrMDA6MDBAgVbbAAAAAElFTkSuQmCC&color=20BEFF"/></a>
<a href="https://doi.org/10.1145/3726302.3730284"><img src="https://img.shields.io/static/v1?label=Paper&message=ACM%20SIGIR&color=green&logo=arxiv"></a>
<a href="https://colab.research.google.com/github/DataScienceUIBK/WikiHint/blob/main/HintRank/Demo.ipynb"><img src="https://img.shields.io/static/v1?label=Colab&message=Demo&logo=Google%20Colab&color=f9ab00"></a>
[![License](https://img.shields.io/badge/License-CC%20BY%204.0-blue)](https://creativecommons.org/licenses/by/4.0/)
<img src="https://github.com/DataScienceUIBK/WikiHint/blob/main/WikiHint/Pipeline.png">

WikiHint — это **аннотированный человеком набор данных**, предназначенный для **автоматической генерации и ранжирования подсказок** для фактологических вопросов. Этот набор данных, основанный на Википедии, содержит **5000 подсказок для 1000 вопросов** и поддерживает исследования в области **оценки, ранжирования и генерации подсказок**.

## <img src="https://github.com/DataScienceUIBK/TriviaHG/blob/main/Framework/gif-dan.gif" width="32" height="32"/> Внимание <img src="https://github.com/DataScienceUIBK/TriviaHG/blob/main/Framework/gif-dan.gif" width="32" height="32"/>

С **февраля 2025 года** мы рекомендуем использовать **HintEval** — фреймворк для **генерации и оценки подсказок**. HintEval включает в себя **датасет WikiHint**, а также метрики оценки, представленные в статье о WikiHint, что делает работу с подсказками проще, чем когда-либо.

Ознакомьтесь с HintEval здесь:  
- 📖 **[Документация HintEval](http://hinteval.readthedocs.io/)**  
- 📦 **[Установка HintEval через PyPI](https://pypi.org/project/hinteval/)**  
- 💻 **[Репозиторий HintEval на GitHub](https://github.com/DataScienceUIBK/HintEval)**  
- 📜 **[Научная статья о HintEval (arXiv)](https://doi.org/10.48550/arXiv.2502.00857)**  

Для **бесшовной интеграции** генерации и оценки подсказок мы настоятельно рекомендуем **перейти** на **HintEval**!


## 🗂 Обзор

- **1000 вопросов** с **5000 вручную созданными подсказками**.
- Подсказки ранжированы **аннотаторами** на основе полезности.
- Оценка с помощью **LLM-моделей (LLaMA, GPT-4)** и **человеческих исследований**.
- Поддержка **ранжирования подсказок** и **автоматической оценки их качества**.

## 🔬 Вклад в исследования

✅ **Первый аннотированный человеком набор данных** для генерации и ранжирования подсказок.  
✅ **HintRank:** Легковесный метод автоматического ранжирования подсказок.  
✅ **Исследование с участием людей**, оценивающее эффективность подсказок.  
✅ **Дообучение открытых LLM-моделей** (LLaMA-3.1, GPT-4) для генерации подсказок.  

## 📈 Ключевые выводы

- **Подсказки, учитывающие ответ**, более эффективны.  
- **Дообученные модели LLaMA** генерируют подсказки лучше, чем базовые модели.  
- **Короткие подсказки** оказываются **более полезными**, чем длинные.  
- **Подсказки, созданные людьми**, превосходят подсказки LLM по ясности и ранжированию.

## 🚀 Начало работы

### 1️⃣ Клонирование репозитория

```sh
git clone https://github.com/DataScienceUIBK/WikiHint.git
cd WikiHint
```

### 2️⃣ Загрузка набора данных

```python
import json

with open("./WikiHint/training.json", "r") as f:
    training_data = json.load(f)

with open("./WikiHint/test.json", "r") as f:
    test_data = json.load(f)

print(f"Обучающий набор: {len(training_data)} вопросов")
print(f"Тестовый набор: {len(test_data)} вопросов")
```

## 🏆 HintRank: Легковесный метод ранжирования подсказок

HintRank — это **автоматический метод ранжирования подсказок** с использованием **BERT-моделей**. Он работает на основе **парных сравнений**, определяя **относительную полезность подсказок**.

<p align="center">
    <img src="https://raw.githubusercontent.com/DataScienceUIBK/WikiHint/main/HintRank/EvaluationMethod.png" width="35%">
</p>

### ✨ Возможности:
✔ **Легковесность**: Запускается локально без необходимости в мощных вычислительных ресурсах.  
✔ **Оценка без LLM**: Работает без **крупных генеративных моделей**.  
✔ **Ранжирование, соответствующее оценкам человека**: Сильная корреляция с **человеческими оценками подсказок**.  

### 🔍 Как это работает:
1. **Объединяет вопрос и две подсказки** → Преобразует их в формат, совместимый с BERT.  
2. **Оценивает качество подсказок** → Определяет, какая подсказка **полезнее**.  
3. **Формирует ранжирование подсказок** → Присваивает ранги на основе парных сравнений.  

## 📌 Использование `HintRank` для ранжирования подсказок

Модуль `HintRank` предназначен для **автоматического ранжирования подсказок** на основе их полезности с использованием **BERT-моделей**.

### 🚀 Запуск демонстрации HintRank в Google Colab

Вы можете протестировать **HintRank** прямо в браузере через **Google Colab** без необходимости установки на локальный компьютер. Просто **[откройте ноутбук Colab](https://colab.research.google.com/github/DataScienceUIBK/WikiHint/blob/main/HintRank/Demo.ipynb)** и попробуйте HintRank в интерактивном режиме.


### 1️⃣ Установка зависимостей

Если вы запускаете локально, установите необходимые зависимости:

```sh
pip install transformers torch numpy scipy
```

### 2️⃣ Импорт и инициализация HintRank

Перейдите в каталог `HintRank` и импортируйте модуль `hint_rank`:

```python
from HintRank.hint_rank import HintRank

# Инициализация модели HintRank
ranker = HintRank()
```

### 3️⃣ Ранжирование подсказок для заданного вопроса

```python
question = "Какова столица Австрии?"
answer = "Вена"
hints = [
    "Здесь когда-то жили Моцарт и Бетховен.",
    "Это крупный город в Европе.",
    "Крупнейший город Австрии."
]

# Пример парного сравнения
better_hint_answer_aware = ranker.pairwise_compare(question, hints[1], hints[2], answer)
better_hint_answer_agnostic = ranker.pairwise_compare(question, hints[0], hints[1])

print(f"С учетом ответа: Подсказка {2 if better_hint_answer_aware == 1 else 3} лучше, чем подсказка {3 if better_hint_answer_aware == 0 else 2}.")
print(f"Без учета ответа: Подсказка {1 if better_hint_answer_agnostic == 1 else 2} лучше, чем подсказка {2 if better_hint_answer_agnostic == 0 else 1}.")
```

### 4️⃣ Ранжирование списка подсказок

Можно также ранжировать несколько подсказок сразу:

```python
print("\nРанжированные подсказки (с учетом ответа):")
ranked_hints_answer_aware = ranker.listwise_compare(question, hints, answer)
for i, (hint, _) in enumerate(ranked_hints_answer_aware):
    print(f"Ранг {i + 1}: {hint}")

print("\nРанжированные подсказки (без учета ответа):")
ranked_hints_answer_agnostic = ranker.listwise_compare(question, hints)
for i, (hint, _) in enumerate(ranked_hints_answer_agnostic):
    print(f"Ранг {i + 1}: {hint}")
```

### 📌 Ожидаемый вывод

```
Сравнение пар подсказок
	С учетом ответа: Подсказка 3 лучше, чем подсказка 2.
	Без учета ответа: Подсказка 2 лучше, чем подсказка 1.

Ранжирование списка подсказок
	Ранжированные подсказки (с учетом ответа):
		Ранг 1: Крупнейший город Австрии.
		Ранг 2: Здесь когда-то жили Моцарт и Бетховен.
		Ранг 3: Это крупный город в Европе.

	Ранжированные подсказки (без учета ответа):
		Ранг 1: Это крупный город в Европе.
		Ранг 2: Крупнейший город Австрии.
		Ранг 3: Здесь когда-то жили Моцарт и Бетховен.
```

---

## 📊 🆚 Сравнение WikiHint и TriviaHG

В таблице ниже приведено сравнение **WikiHint** с **TriviaHG**, крупнейшим ранее существовавшим набором данных для генерации подсказок. **WikiHint** демонстрирует **лучшее сходимость**, **более короткие** и **более качественные подсказки** по ряду метрик.

| **Набор данных** | **Подмножество** | **Релевантность** | **Читаемость** | **Сходимость** | **Знакомство** | **Длина** | **Утечка ответа (ср.)** | **Утечка ответа (макс.)** |
|------------------|----------------|----------------|----------------|----------------|----------------|----------|----------------|----------------|
| TriviaHG        | Полный         | 0.95           | 0.71           | 0.57           | 0.77           | 20.82    | 0.23           | 0.44           |
| WikiHint        | Полный         | 0.98           | 0.72           | 0.73           | 0.75           | 17.82    | 0.24           | 0.49           |
| TriviaHG        | Обучение       | 0.95           | 0.73           | 0.57           | 0.75           | 21.19    | 0.22           | 0.44           |
| WikiHint        | Обучение       | 0.98           | 0.71           | 0.74           | 0.76           | 17.77    | 0.24           | 0.49           |
| TriviaHG        | Тест           | 0.95           | 0.73           | 0.60           | 0.77           | 20.97    | 0.23           | 0.44           |
| WikiHint        | Тест           | 0.98           | 0.83           | 0.72           | 0.73           | 18.32    | 0.24           | 0.47           |

📌 **Основные выводы**:
- **WikiHint превосходит TriviaHG** по **сходимости**, что означает, что его подсказки **лучше помогают пользователям находить правильные ответы**.
- **Подсказки в WikiHint короче**, что делает их **более лаконичными и эффективными**.

## 📊🤖 Оценка сгенерированных подсказок

Таблица ниже представляет **оценку сгенерированных подсказок** различными **LLM-моделями (LLaMA-3.1, GPT-4)** по параметрам **релевантности, читаемости, сходимости, знакомства, длины подсказки и утечки ответа**. Она показывает, как **дообучение (FT)** и **учет ответа (wA)** влияют на качество подсказок.

| **Модель** | **Конфигурация** | **Использует ответ?** | **Rel** | **Read** | **Conv (LLaMA-8B)** | **Conv (LLaMA-70B)** | **Fam** | **Len** | **AnsLkg (ср.)** | **AnsLkg (макс.)** |
|------------|---------------|----------------|----------|---------|----------------|----------------|--------|------|----------------|----------------|
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

📌 **Основные выводы**:
- **Релевантность**: **Крупные модели (405b, 70b) генерируют лучшие подсказки**, чем меньшие (8b).
- **Читаемость**: **GPT-4 производит самые читаемые подсказки**.
- **Сходимость**: **Учет ответа (wA) помогает LLM-моделям генерировать более полезные подсказки**.
- **Длина подсказки**: **Дообученные модели (FTwA, FTwoA) генерируют более короткие и качественные подсказки**.

## 📂 Структура репозитория

```
📂 WikiHint/                                                # 🗂 Файлы набора данных
│   ├── 📄 Pipeline.png                                     # 📊 Визуализация обработки данных
│   ├── 📄 training.json                                    # 📊 Обучающий набор (900 вопросов, 4500 подсказок)
│   ├── 📄 test.json                                        # 📊 Тестовый набор (100 вопросов, 500 подсказок)
│
├── 📂 Experiments/                                         # 🧪 Подсказки, сгенерированные моделями
│   ├── 📄 GPT-4-Vanilla-answer-aware.json
│   ├── 📄 LLaMA-3.1-405b-Vanilla-answer-agnostic.json
│   ├── 📄 LLaMA-3.1-70b-FTwA-answer-aware.json
│
├── 📂 HintRank/                                            # 🏆 Метод ранжирования подсказок
│   ├── 📄 EvaluationMethod.png                             # 📊 Визуализация метода оценки HintRank
│   ├── 📄 hint_rank.py                                     # 📜 Реализация HintRank
│
├── 📂 HumanEvaluation/                                     # 👨‍🔬 Данные оценки человеком
│   ├── 📂 Person_1/                                       
│   │   ├── 📑 Part_1.xlsx
│   │   ├── 📑 Part_2.xlsx
│
└── 📘 README.md                                            # 📖 Этот файл
```

## 📜 Лицензия

Этот проект лицензирован под **Creative Commons Attribution 4.0 International (CC BY 4.0)**. Вы можете использовать, делиться и адаптировать набор данных с указанием авторства.

## 📑 Цитирование

Если эта работа оказалась вам полезной, пожалуйста, укажите ссылку на [📜 нашу статью](https://doi.org/10.1145/3726302.3730284):

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

## 🙏 Благодарности

Благодарим всех участников и Университет Инсбрука за поддержку этого проекта. 🚀
