import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT_ID")
LOCATION = "global" 
if not PROJECT_ID:
    print("ERROR: GOOGLE_CLOUD_PROJECT_ID not found in .env")
    sys.exit(1)

client = genai.Client(
    vertexai=True,
    project=PROJECT_ID,
    location=LOCATION
)

with open("resources/context/tutor_instructions.txt", "r") as f:
        tutor_instructions = f.read()

textbook_uri = "gs://wgucalc1tutorgunnarisenberg/Calculus_Volume_1_-_WEB_l4sAIKd.pdf"
textbook = types.Part.from_uri(
    file_uri=textbook_uri,
    mime_type="application/pdf"
)

config = types.GenerateContentConfig(
       system_instruction=tutor_instructions,
       temperature=.9  # Use Gemini 3 default
   )

def getResponse(prompt : str) -> str:
    response = client.models.generate_content(
         model="gemini-3-flash-preview",
         #I understand that this increases infrence cost -> but the model returns a 400 error with the config parameter (even when direcly copied from gemini docs D: )
         contents=[textbook, tutor_instructions, prompt]#,
         #config=config
    )
    return response

prompt = "How do I start finding the derivative of f(x) = sin(x^2)?"
print(getResponse(prompt))
