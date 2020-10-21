from fastapi import FastAPI, Depends, HTTPException
from typing import Optional, List
from sqlalchemy.orm import Session
import psycopg2
import json

from app.database import SessionLocal, engine
from app import crud, models, schemas


models.Base.metadata.create_all(engine)


app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/')
async def root():
    return {"message": "Welcome to Gruvi App Api."}


@app.post('/user/sign_up')
async def create_user(user: schemas.UserBase):
    try:
        # make connection to the postgres database using psycopg2
        # conn = psycopg2.connect(
        #     user = "dlsvxkxqmbftya",
        #     password = "c589c1ce2c1a843abfbecb3b232f378b7c1c960ad50ff826038ae4395f9ea58b",
        #     host = "ec2-3-218-112-22.compute-1.amazonaws.com",
        #     port = "5432",
        #     database = "daf67btr09q6qt"
        # )
        conn = psycopg2.connect(
            user = "postgres",
            password = "iampistis",
            host = "localhost",
            port = "5432",
            database = "pistis"
        )
        
        cursor = conn.cursor()
        # save user info to the database
        query = """
            INSERT INTO gruvi_user VALUES(%s, %s, %s, %s);
        """
        
        insert_values = (user.full_name, user.username, user.email, user.password)
        cursor.execute(query, insert_values)
        conn.commit()
        
        count = cursor.rowcount
        return json.dumps({"status": 200, "message": "Inserted successfully"})
    except(Exception, psycopg2.Error) as error:
        print("Error connecting to PostgreSQL database", error)
        conn = None
        return json.dumps({"status": 404, "message": "An error occured"})
    finally:
        if(conn != None):
            cursor.close()
            conn.close()
            print("PostgreSQL connection is now closed")
        
        return {"message": "thats all"}
            
            
@app.post('/user/signup', response_model=schemas.UserBase)
def save_user(user: schemas.UserBase, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)
