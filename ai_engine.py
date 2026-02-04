import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

class Tutor:
    def __init__(self):
        load_dotenv()
        self.project_id = os.getenv("GOOGLE_CLOUD_PROJECT_ID")
        self.location = "us-central1"

        self.client = genai.Client(
            vertexai=True,
            project=self.project_id,
            location = self.location
        )

        with open("resources/context/tutor_instructions.txt", "r") as f:
            self.instructions = f.read()

        self.textbook_uri = "gs://wgucalc1tutorgunnarisenberg/Calculus_Volume_1_-_WEB_l4sAIKd.pdf"
        self.textbook_part = types.Part.from_uri(
            file_uri=self.textbook_uri,
            mime_type="application/pdf"
        )

    def get_coaching(self, user_prompt : str) -> str:
        config = types.GenerateContentConfig(
            system_instruction=self.instructions,
            temperature=.9
        )

        response = self.client.models.generate_content(
            model = "gemini-3-flash-preview",
            contents = [self.textbook_part, user_prompt]#,
            #config = config
        )
        
        return response.text