# Embedded AI Practice Project

This repository contains a practice project built using **Embeddable Watson AI libraries**. The goal of the project is to create an AI‑powered Python application that performs natural language processing and speech-related tasks using locally embeddable Watson libraries.


## About Embeddable Watson AI Libraries

Embeddable Watson AI libraries provide offline‑capable AI functionality that can be packaged directly within an application. These libraries are already pre-installed in the **Skills Network Labs Cloud IDE**, and the project must be run in that environment rather than a local IDE.


### Included Libraries

#### NLP Library
Provides functions for:

- Sentiment analysis  
- Emotion detection  
- Text classification  
- Language detection  
- Other text‑processing capabilities  

#### Speech-to-Text Library (STT)
Converts spoken audio into written text using transcription models.

#### Text-to-Speech Library (TTS)
Generates natural‑sounding audio output from written text.


## Running the Project

This project is intended to run inside the **Skills Network Theia Lab** environment.

To execute the main application:
---
python app.py

To run unit tests:
---
python -m unittest


## Example Usage

Sentiment analysis example:

```python
from sentimentanalysis.sentiment_analysis import sentiment_analyzer

result = sentiment_analyzer("I love working with Python")
print(result)
