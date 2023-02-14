from datetime import datetime, timedelta
from fastapi import Depends, FastAPI, Form, Query, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from jose import jwt
from pydantic import EmailStr
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.db import models
from app.db.database import Base, SessionLocal, engine
from app.schemas.magic_link import MagicLinkTokenPayload

from app.schemas.settings import Settings
from app.services.magic_link_service import MagicLinkService
from app.services.smtp_client import SMTPClient

settings = Settings()
templates = Jinja2Templates(directory="app/views")
models.Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/sign_in", response_class=HTMLResponse)
async def sign_in(request: Request):
    return templates.TemplateResponse("sign_in.html", {"request": request})

@app.post("/sign_in", response_class=HTMLResponse)
async def request_magic_link(request: Request, email: EmailStr = Form(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == email).first()
    if user != None:
        smtp_client = SMTPClient(settings.smtp_server, settings.smtp_port, settings.smtp_user, settings.smtp_password)
        magic_link_service = MagicLinkService(smtp_client, settings.magic_link_base_url, settings.jwt_secret, settings.magic_link_from_email)
        magic_link = magic_link_service.generate_magic_link(
            MagicLinkTokenPayload(user_id = user.id, exp=datetime.utcnow() + timedelta(minutes=30))
        )
        magic_link_service.send_magic_link(email, magic_link)
    
    return templates.TemplateResponse("magic_link_sent.html", {"request": request, "email": email})

@app.get("/magic_sign_in", response_class=HTMLResponse)
async def sign_in(request: Request, token: str = Query()):
    return templates.TemplateResponse("confirm_sign_in.html", {"request": request, "token": token})

@app.post("/magic_sign_in", response_class=HTMLResponse)
async def sign_in(request: Request, token: str = Form(), db: Session = Depends(get_db)):
    jwt_payload = jwt.decode(token, settings.jwt_secret, algorithms=["HS256"])
    magic_link = MagicLinkTokenPayload.parse_obj(jwt_payload)
    user = db.get(models.User, magic_link.user_id)
    return templates.TemplateResponse("welcome.html", {"request": request, "user": user})
