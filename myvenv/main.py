from fastapi import FastAPI
import json

app=FastAPI()

def load_data():
    with open(r'C:\Users\FARUKH KHAN\OneDrive\khushbu personal\rest_api\myvenv\patients.json','r') as f:
        data=json.load(f)
    return data


@app.get("/")

def hello():    #first api
    return {'message':'Hello World !'}

@app.get('/about')

def about():   #second api
    return {'message':'Essentia.dev is a software development company !'}

@app.get('/myself')

def myself():    #third api
    return {
        'name':'Khushbu saifi',
        'profile':'Software developer',
        'office':'Essentia softserv'
    }

@app.get('/patient')
def patient():
    return {'message':'Patient Management System API'}

@app.get('/patients')
def patients():
    return {'message':'A fully Functional API to manage your patient records ! '}

@app.get('/view')
def view():   #fourth api
    data=load_data()
    return data