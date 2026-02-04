import os
import uuid
from fastapi import Depends, FastAPI, Query, Request, Response
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi_sso.sso.microsoft import MicrosoftSSO
from pydantic import BaseModel
from requests import Session
from ai_engine import Tutor
from database import User, get_db
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

sso = MicrosoftSSO(
    client_id=os.getenv("MS_CLIENT_ID"),
    client_secret = os.getenv("MS_CLIENT_SECRET"),
    tenant="common",
    redirect_uri="http://localhost:8000/auth/callback"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allows all origins for local testing
    allow_methods=["*"],
    allow_headers=["*"],
)
tutor = Tutor()

class UserQuestion(BaseModel):
    user_text: str

@app.get('/', response_class=HTMLResponse)
async def root():
    with open("login.html", "r") as f:
        return f.read()
    
@app.get("auth/guest")
async def guest_login(response:Response):
    guest_id = f"guest_{uuid.uuid4().hex[:8]}"
    res = RedirectResponse(url="/chat")
    res.set_cookie(key="user_id", value = guest_id)
    return res

@app.get("/auth/login")
async def login():
    with sso:
        return await sso.get_login_redirect()

@app.get("/auth/callback")
async def login_callback(request: Request, db: Session = Depends(get_db)):
    with sso:
        user_data = await sso.verify_and_process(request)
    
    user = Query(User).filter(User.id == user_data.id).first()
    if not user:
        user = User(id=user_data.id, email=user_data.email, display_name=user_data.display_name)
        db.add(user)
        db.commit()

@app.post("/sendmsg")
def sendMsg(user_question : UserQuestion):
    response = tutor.get_coaching(user_question.user_text)
    return{"reply" : response.text}