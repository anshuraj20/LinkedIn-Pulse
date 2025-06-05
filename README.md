# LinkedInPulse: AI-Powered LinkedIn Post Generator

An AI-powered tool that helps LinkedIn users generate personalized, topic-specific, and engaging posts. Built with Generative AI (LLMs), this project learns from the user's previous writing style and generates content consistent with their tone and voice.

---

## 📌 Project Overview

- [Introduction](#introduction)
- [Problem Statement](#problem-statement)
- [Objectives](#objectives)
- [Key Features](#key-features)
- [Architecture & Workflow](#architecture--workflow)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Deliverables](#deliverables)
- [Conclusion](#conclusion)

---

## 🔍 Introduction

LinkedInPulse is a personalized LinkedIn post generator that uses LLMs to create professional, relevant, and consistent posts based on a user’s previous content. It improves content quality and reduces the time required to maintain an active LinkedIn presence.

---

## ❗ Problem Statement

- Maintaining a consistent voice and posting frequency is difficult for busy professionals.
- Manual content creation takes time and effort.
- Existing AI tools generate generic content that lacks personalization.

---

## 🎯 Objectives

- Generate LinkedIn posts tailored to a user’s writing style using LLMs.
- Allow customization based on topic, language, and length.
- Provide an easy-to-use interface for content generation.

---

## ✨ Key Features

- Personalized post generation using user’s past content.
- Topic-based post creation with tone and length control.
- Streamlit UI for real-time interaction.
- Uses few-shot examples to guide the LLM.

---

## 🧱 Architecture & Workflow

```
[raw_posts.json] 
   ↓ (Preprocessing)
[processed_posts.json] 
   ↓ (Filtered Examples)
[few_shot.py] 
   ↓ (Prompt Construction)
[post_generator.py] 
   ↓ (LLM via GROQ API)
[main.py → Streamlit UI]
```

---

## 🛠 Technologies Used

- Python 3.x
- Streamlit
- LangChain
- GROQ API (LLaMA 3.2)
- Pandas
- JSON

---

## 💾 Installation

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/linkedinpulse.git
cd linkedinpulse
```

2. (Optional) Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory and add your GROQ API key:

```env
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Usage

1. Preprocess the raw posts:

```bash
python preprocess.py
```

2. Run the Streamlit application:

```bash
streamlit run main.py
```

3. In the browser:
   - Select topic, length, and language.
   - Click "Generate" to see a new personalized LinkedIn post.

---

## 📂 Project Structure

| File/Folder         | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| `main.py`           | Streamlit app for user interaction                                          |
| `preprocess.py`     | Converts raw posts into structured format                                   |
| `few_shot.py`       | Filters example posts based on user input                                   |
| `post_generator.py` | Builds prompt and generates post using the LLM                              |
| `llm_helper.py`     | Initializes and configures the GROQ LLaMA 3 model                           |
| `raw_posts.json`    | Input file with user's previous LinkedIn posts                              |
| `processed_posts.json` | Output of preprocessing step, used for few-shot prompting              |
| `requirements.txt`  | Python dependencies                                                         |

---

## 📦 Deliverables

- AI-powered LinkedIn post generator
- Streamlit-based UI
- Dynamic few-shot prompt generation
- GROQ API integration for high-speed LLM inference

---

## ✅ Conclusion

LinkedInPulse offers a fast and reliable way to create personalized LinkedIn content using LLMs. By analyzing past posts, it ensures consistency in tone, topic, and engagement. Its open architecture and customization options make it scalable for future enhancements like multilingual support and sentiment-based generation.
