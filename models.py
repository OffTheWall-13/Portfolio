from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Base(DeclarativeBase):    # main model
    __abstract__ = True


class MessageBase(Base):
    __tablename__ = "messages"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(254))
    subject: Mapped[str] = mapped_column(String(300))
    main_message: Mapped[str] = mapped_column(String(1000))


DB_URL = 'sqlite:///db.sqlite3'
engine = create_engine(DB_URL, echo=True)


def create_db_and_tables() -> None:
    Base.metadata.create_all(engine)
    

if __name__ == "__main__":
    create_db_and_tables()

    