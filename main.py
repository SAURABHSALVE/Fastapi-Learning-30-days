from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
app =  FastAPI()
 
def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data 

@app.get("/")
def hello():
    return {"message": "Patients data api"}

@app.get('/about')
def about():
    return {"message": "About Patients data api"}
 
@app.get('/view')
def view():
    data = load_data()
    
    return data