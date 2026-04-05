

from crewai import Task 
from agents import hate_speech_detector


hate_speech_detection_task= Task(description=(
   "Analyze the following text to determine if it contains any hate speech or offensive language"
    "Follow these steps:.\n"
    "1 .Read the text carefully.\n"
    "2. Identify any language that targets a group or individual based on attributes such as race, gender, ethnicity, religion.\n"
    "3. Look for theats , dehumanizing language, insults, or promotion of viloence or hatred.\n"
    "4. Evaluate the context to ensure words are not taken out of context.\n"
    "5. Make an objective decision based on the content.\n"
    "Text:\n{text}"
    ), 
expected_output="Respond with 'Hate Speech / No hate speech' ", 
agent=hate_speech_detector,
)
    
