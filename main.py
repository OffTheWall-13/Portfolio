from fastapi import FastAPI, Form
from fastapi.responses import FileResponse, HTMLResponse
from sqlalchemy.orm import Session, sessionmaker
from models import MessageBase, Base, create_db_and_tables
import uvicorn
from notifications.notifier import notify
import os


app = FastAPI()
DB_URL = os.getenv("DATABASE_URL", "sqlite:///db.sqlite3")
engine = create_engine(DB_URL, echo=False)

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
        
if __name__ == "__main__":
    uvicorn.run(app)
