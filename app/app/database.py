from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'postgresql://dlsvxkxqmbftya:c589c1ce2c1a843abfbecb3b232f378b7c1c960ad50ff826038ae4395f9ea58b@ec2-3-218-112-22.compute-1.amazonaws.com/daf67btr09q6qt'

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()