from sqlalchemy import String, create_engine, Column, Integer, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./tutor_app.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread":False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__="users"
    id = Column(String, primary_key=True, index=True)
    email = Column(String)
    display_name = Column(String)

class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True,index=True)
    user_id = Column(String, ForeignKey("users.id"))
    role = Column(String)
    content = Column(Text)

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()