from fastapi import FastAPI
from pydantic import BaseModel
from ai_engine import Tutor
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allows all origins for local testing
    allow_methods=["*"],
    allow_headers=["*"],
)
tutor = Tutor()

class UserQuestion(BaseModel):
    user_text: str

@app.post("/sendmsg")
def sendMsg(user_question : UserQuestion):
    response = tutor.get_coaching(user_question.user_text)
    return{"reply" : response.text}