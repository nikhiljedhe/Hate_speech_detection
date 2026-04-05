

import os
from crewai import Crew

from agents import hate_speech_detector
from tasks import hate_speech_detection_task

crew= Crew(
    agents=[hate_speech_detector],
    tasks=[hate_speech_detection_task]
    )


while True:
    Text = input("Enter the text to analyze (type 'quit' or 'exit' to stop): ")
    if Text.lower() == 'quit' or Text.lower() == 'exit':
        print("Exiting analysis.")
        break

    result = crew.kickoff(inputs={"text": Text})

    print("Response: ", result)

    # Write results to a Markdown file
    with open("results.md", "a") as f:
        f.write(f"## Analysis of: \"{Text}\"\n")
        f.write(f"### Result:\n{result}\n\n")
        f.write("---\n\n") # Separator for readability
