from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
app =  FastAPI()
 
import json
def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data

@app.get("/")
def hello():
    return {"message": "patients api"}

@app.get("/about")
def about():
    return {"message": "This is a simple API to manage patient data."}

@app.get("/views")
def views():
    data = load_data()

    return data 

