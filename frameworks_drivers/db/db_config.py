import os
from dotenv import load_dotenv
from sqlalchemy import URL, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

load_dotenv()
Base = declarative_base()

def setup_database():
    database_url = URL.create(
        drivername="postgresql+psycopg2",
        username=os.getenv("DB_USERNAME"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", 5432),
        database=os.getenv("DB_NAME")
    )

    engine = create_engine(database_url, echo=os.getenv("DB_ECHO", "FALSE").lower() == "true")
    session_factory = sessionmaker(bind=engine)
    Session = scoped_session(session_factory)
    Base.metadata.create_all(engine)
    return Session