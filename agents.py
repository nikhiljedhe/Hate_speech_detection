

from crewai import Agent
import os
from langchain_google_genai import ChatGoogleGenerativeAI

# Get the Gemini API key from environment variable
gemini_api_key = os.environ.get("GOOGLE_API_KEY")

if not gemini_api_key:
    raise ValueError("GOOGLE_API_KEY environment variable not set. Please set it before running.")

# Use ChatGoogleGenerativeAI instance directly
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=gemini_api_key)

hate_speech_detector= Agent(
    role="Hate Speech Detector",
    goal="Accurately detect and identify instances of hate speech, discriminatory language, or harmful content in text.",
    llm=llm,
    backstory=("""you are a hate speech detector for twitter who understands details very well
    and a expet negotiator who can identify hate speech/ offensive language in given tweet"""),
    verbose=True
)
