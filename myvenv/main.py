from fastapi import FastAPI ,Path,HTTPException,Query
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

@app.get('/details/{details_id}')   #to show the data according to their id
def view_details(details_id: str=Path(...,description='ID of the patient in the DB',example='p001')):
    #load all the patients
    data=load_data()

    if details_id in data:
        return data[details_id]
    raise HTTPException(status_code=404,detail='Patient not found')  #error raised number

@app.get('/sort')
def sort_patients(sort_by:str=Query(...,description='Sort on the basis of height,weight on bmi'),order:str=Query('asc',description='Sort in asc or desc order')):
                valid_fields=['height','weight','bmi']
                if sort_by not in valid_fields:
                     raise HTTPException(status_code=400,detail=f'Invalid field select from {valid_fields}')
                
                if order not in['asc','desc']:
                     raise HTTPException(status_code=400,detail='Invalid ordere select betwwn asc and desc')
                
                data=load_data()
                sort_order=True if order=='desc' else False
                sorted_data=sorted(data.values(),key=lambda x:x.get(sort_by,0),reverse=sort_order)
                return sorted_data
