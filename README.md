# Dubai Real Estate Voice AI Assistant

## Overview

This project implements a **voice-enabled conversational AI assistant** designed to simulate a **Dubai real estate sales agent**.
The assistant can understand user queries about property investment in Dubai, respond intelligently, and provide answers through both **text and natural speech**.

The solution demonstrates **prompt engineering for sales conversion** and a **voice AI pipeline** integrating speech recognition, large language models, and text-to-speech.

---

## Features

* Conversational **AI real estate sales assistant**
* **Prompt engineering** for sales conversations
* **Objection handling** and **lead qualification**
* **Voice input** using speech-to-text
* **Streaming AI responses** for real-time interaction
* **Text-to-speech** voice responses
* **Multi-model LLM selection**
* **Property recommendation examples**
* **Conversation memory**

---

## Architecture

The assistant follows a voice AI pipeline:

User Input (Text or Voice)
→ Speech-to-Text (Whisper)
→ Conversational Agent
→ LLM Response (Groq LLaMA Models)
→ Streaming Output
→ Text-to-Speech Response

---

## Project Structure

```
akoni_voice_ai/

app.py
agent.py
llm.py
stt.py
tts.py
recommender.py
property_data.py

prompts/
    system_prompt.txt

requirements.txt
.env.example
README.md
```

---

## Installation

1. Clone or download the project.

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Create an environment file:

```
.env
```

Add your Groq API key:

```
GROQ_API_KEY=your_api_key_here
```

---

## Run the Application

Start the Streamlit application:

```
streamlit run app.py
```

The assistant will launch in your browser.

---

## Example Interaction

User:

> I’m not sure if I want to buy property in India now.

Assistant:

> That’s completely understandable. Many buyers initially feel the same way.
> However, Dubai’s property market has shown strong appreciation in recent years, especially in areas like Dubai Marina and Downtown.
> Would you like me to show you some properties that are currently offering strong rental yields?

---

## Technologies Used

* **Python**
* **Streamlit**
* **Groq LLaMA models**
* **OpenAI Whisper (Speech-to-Text)**
* **gTTS (Text-to-Speech)**
* **Prompt Engineering**

---

## Assignment Objectives

This implementation addresses the following requirements:

### Task 1 – Prompt Engineering

* Sales-style conversational responses
* Objection handling
* Lead qualification prompts
* Conversation examples

### Task 2 – Voice AI Assistant

* Speech input processing
* Intelligent response generation
* Natural speech output

---

## Author

Nitin G Ghumare

Email: [nghumare570@gmail.com](mailto:nghumare570@gmail.com)
GitHub: https://github.com/NitinGhumare

---
