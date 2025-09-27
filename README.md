# Named Entity Recognition (NER) App

This is a simple **Streamlit web app** for performing **Named Entity Recognition (NER)** using **spaCy**.
It allows you to input text, analyze entities, and visualize them interactively.

## Features

* 📝 Input custom text.
* 🧠 Uses **spaCy (`en_core_web_sm`)** model for NER.
* 🎨 Highlights recognized entities with `displacy`.
* 📊 Displays extracted entities in a structured dataframe.

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/ner-app.git
cd ner-app
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Download the spaCy model:

```bash
python -m spacy download en_core_web_sm
```

## Usage

Run the Streamlit app:

```bash
streamlit run NER.py
```

## Example

Input:

```
Apple is looking at buying U.K. startup for $1 billion.
```

Output:

* Entities highlighted in text
* Table of entities

| Text       | Label |
| ---------- | ----- |
| Apple      | ORG   |
| U.K.       | GPE   |
| $1 billion | MONEY |




