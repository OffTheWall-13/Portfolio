from fastapi.responses import FileResponse, HTMLResponse
from sqlalchemy.orm import Session, sessionmaker
from notifications.notifier import notify
from models import MessageBase, Base
from sqlalchemy import create_engine
from fastapi import FastAPI, Form
from dotenv import load_dotenv
import uvicorn
import os

load_dotenv()

app = FastAPI()
DB_URL = os.getenv("DATABASE_URL")
engine = create_engine(DB_URL, echo=False, future=True)
Session = sessionmaker(engine)

@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(engine)

@app.get("/", response_class=HTMLResponse)
def main_page():
    return FileResponse("templates/index.html")


@app.post('/')
def handle_form_submission(name: str = Form(...),
                           email: str = Form(...),
                           subject: str = Form(...),
                           message: str = Form(...)):
    new_message = MessageBase(name=name,
                              email=email,
                              subject=subject,
                              main_message=message)
    with Session() as session:  
        try:
            session.add(new_message)
            session.commit()
        except Exception:
            session.rollback()
            raise
    notify(name, email, subject, message)
        