


from crewai import Task
from agents import hate_speech_detector


hate_speech_detection_task= Task(description=(
   "Analyze the following text to determine if it contains any hate speech or offensive language."
    "Follow these steps:\n"
    "1. Read the text carefully.\n"
    "2. Identify any language that targets a group or individual based on attributes such as race, gender, ethnicity, religion, sexual orientation, disability, or any other protected characteristic.\n"
    "3. Look for threats, dehumanizing language, insults, or promotion of violence or hatred.\n"
    "4. Evaluate the context to ensure words are not taken out of context. Consider intent and potential impact.\n"
    "5. Make an objective decision based on the content. Provide a clear 'Hate Speech' or 'No hate speech' classification.\n"
    "6. If classified as 'Hate Speech', explain *why* it is considered hate speech, referencing specific parts of the text and the criteria violated. If classified as 'No hate speech', briefly explain *why* it is not.\n"
    "Text:\n{text}"
    ),
expected_output="Provide a classification (Hate Speech / No hate speech) followed by a detailed explanation and reasoning for your decision.",
agent=hate_speech_detector,
)
    
