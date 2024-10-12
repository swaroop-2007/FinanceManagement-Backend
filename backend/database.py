from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_database = 'sqlite:///./finance.db'

engine = create_engine(URL_database, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)

Base = declarative_base()