from fastapi import FastAPI, Form
from fastapi.responses import FileResponse, HTMLResponse
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine
from models import MessageBase, Base
import uvicorn
from notifications.notifier import notify


app = FastAPI()
DB_URL = 'sqlite:///db.sqlite3'
engine = create_engine(DB_URL, echo=True)

Base.metadata.create_all(bind=engine)

Session = sessionmaker(engine)


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
            notify(name, email, subject, message)
        except:
            session.rollback()
            raise
        
        
if __name__ == "__main__":
    uvicorn.run(app)






