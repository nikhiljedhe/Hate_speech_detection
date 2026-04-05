# 🛡️ Hate Speech Detection using CrewAI + Google Gemini

A lightweight, agentic hate speech detector built with **CrewAI** and **LangChain Google GenAI (Gemini 2.5 Flash)**. The system takes free-form text input from the user and returns a clear verdict — **Hate Speech** or **No Hate Speech** — powered by an AI agent with a structured analysis pipeline.

Designed to run seamlessly on **Google Colab**.

---

## 🚀 Tech Stack

| Tool | Role |
|---|---|
| [CrewAI](https://github.com/joaomdmoura/crewAI) | Multi-agent orchestration framework |
| [LangChain Google GenAI](https://python.langchain.com/docs/integrations/chat/google_generative_ai/) | LLM interface for Gemini |
| Google Gemini 2.5 Flash | Core LLM for content analysis |
| Google Colab | Execution environment |

---

## 📁 Project Structure
hate-speech-detection/
│

├── agents.py                          # Defines the CrewAI Hate Speech Detector agent

├── tasks.py                           # Defines the structured detection task

├── main.py                            # Entry point — user input loop & crew execution

├── requirements.txt                   # Project dependencies

├── Hate_Speech_Detection.ipynb        # Google Colab notebook (run everything here)

---

## ⚙️ How It Works

1. **Agent** (`agents.py`) — A `Hate Speech Detector` CrewAI agent backed by Gemini 2.5 Flash, acting as an expert content moderator for social media (Twitter-style) text.

2. **Task** (`tasks.py`) — A structured 5-step analysis task:
   - Read the input text carefully
   - Identify language targeting groups by race, gender, ethnicity, or religion
   - Look for threats, dehumanizing language, or promotion of violence
   - Evaluate context to avoid false positives
   - Return a clear verdict: `Hate Speech` / `No Hate Speech`

3. **Main Loop** (`main.py`) — Accepts continuous user input, kicks off the crew for each input, and prints the result. Type `quit` or `exit` to stop.

---

## 🔧 Setup & Usage (Google Colab)

### Step 1 — Install Dependencies
```python
!pip install crewai==0.35.0 langchain-google-genai
Step 2 — Add Your Google API Key
In Colab, go to Secrets (🔑 icon on the left panel) and add:
Name: GOOGLE_API_KEY
Value: your_gemini_api_key_here
Step 3 — Run the Notebook
Execute all cells in order. The final cell will start an interactive loop:
Enter the text to analyze (type 'quit' or 'exit' to stop):
Step 4 — Get Your Result
Response: No Hate Speech
or
Response: Hate Speech
📦 Requirements
crewai==0.35.0
langchain-google-genai
🔑 Getting a Google Gemini API Key
Go to Google AI Studio
Sign in with your Google account
Click Create API Key
Copy and paste it into your Colab Secrets
💡 Example Inputs
Input Text
Output
"I love everyone regardless of where they're from"
✅ No Hate Speech
"People from [group] should not be allowed here"
🚨 Hate Speech
"Great game today by the team!"
✅ No Hate Speech
📌 Notes
This project uses CrewAI v0.35.0 — newer versions may have API changes.
The agent is prompted as a Twitter content moderator for context-aware detection.
OpenAI API key is explicitly removed from the environment to avoid conflicts with CrewAI's defaults.
🙋 Author
Nikhil Jedhe
Data Science Enthusiast | CrewAI & LLM Projects
https://www.linkedin.com/in/nikhil-jedhe-a14aa02aa • https://github.com/nikhiljedhe
📄 License
This project is open-source and available under the MIT License.
