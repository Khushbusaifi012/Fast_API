from fastapi import FastAPI ,Path,HTTPException,Query
from fastapi.responses import JSONResponse
import json    #json file import
from pydantic import BaseModel,Field,computed_field
from typing import Annotated,Literal,Optional

app=FastAPI()

class Patient(BaseModel):   # first pydantic model
     id:Annotated[str,Field(...,description="Id of the Patient",examples=['p001'])]
     name:Annotated[str,Field(...,description="Name of the patient")]
     city:Annotated[str,Field(...,description='City where the patient is living')]
     age:Annotated[int,Field(...,gt=0,lt=120,description='Age of the patient')]
     gender:Annotated[Literal['male','female','others'],Field(...,description='Gender of the patient')]
     height:Annotated[float,Field(...,gt=0,description='Height of the patient in mtrs')]
     weight:Annotated[float,Field(...,gt=0,description='Weight of the patient in kgs')]

     @computed_field    #to calculate a bmi through weight and height:
     @property
     def bmi(self)->float:
          bmi=round(self.weight/(self.height**2),2)
          return bmi
     
@computed_field    # condtions with bmi circumstances
@property
def verdict(self) -> str:
     if self.bmi < 18.5:
          return "underweight"
     elif self.bmi < 25:
          return "normal"
     elif self.bmi < 30:
          return "normal"
     else:
          return "Obese"
     
#second pydantic model:
class PatientUpdate(BaseModel):
    name:Annotated[Optional[str],Field(default=None)]
    city:Annotated[Optional[str],Field(default=None)]
    age:Annotated[Optional[int],Field(default=None,gt=0)]
    gender:Annotated[Optional[Literal['male','female']],Field(default=None)]
    height:Annotated[Optional[float],Field(default=None,gt=0)]
    weight:Annotated[Optional[float],Field(default=None,gt=0)]

def load_data():  #method to get
    with open(r'C:\Users\FARUKH KHAN\OneDrive\khushbu personal\rest_api\myvenv\patients.json','r') as f:
        data=json.load(f)
    return data

def save_data(data): #method to post
     with open(r'C:\Users\FARUKH KHAN\OneDrive\khushbu personal\rest_api\myvenv\patients.json','w') as f:
          json.dump(data,f)


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

@app.get('/patient')   #relate to patient view
def patient():
    return {'message':'Patient Management System API'}

@app.get('/patients')  #relate to patient view
def patients():
    return {'message':'A fully Functional API to manage your patient records ! '}

@app.get('/view')
def view():   #fourth api
    data=load_data()
    return data

@app.get('/details/{details_id}')   #to show the data according to their id..
def view_details(details_id: str=Path(...,description='ID of the patient in the DB',example='p001')):
    #load all the patients
    data=load_data()

    if details_id in data:
        return data[details_id]
    raise HTTPException(status_code=404,detail='Patient not found')  #error raised number 

@app.get('/sort')   #sorting data according to our requirements
def sort_patients(sort_by:str=Query(...,description='Sort on the basis of height,weight on bmi'),order:str=Query('asc',description='Sort in asc or desc order')):
                valid_fields=['height','weight','bmi']
                if sort_by not in valid_fields:
                     raise HTTPException(status_code=400,detail=f'Invalid field select from {valid_fields}')
                
                if order not in['asc','desc']:
                     raise HTTPException(status_code=400,detail='Invalid order select between asc and desc')
                
                data=load_data()
                sort_order=True if order=='desc' else False
                sorted_data=sorted(data.values(),key=lambda x:x.get(sort_by,0),reverse=sort_order)
                return sorted_data

@app.post('/create')    #to post
def create_patient(patient:Patient):
     
     #load existing data
     data=load_data()

     #check if the patient already exists
     if patient.id in data:
          raise HTTPException(status_code=400,detail='Patient already exists')

     #new patient add to the database
     data[patient.id]=patient.model_dump(exclude=['id'])

     #save into the json file
     save_data(data)

     return JSONResponse(status_code=201,content={'message':'Patient created successfully'})

@app.put('/edit/{patient_id}')   #to put
def update_patient(patient_id:str,patient_update:PatientUpdate):
    data=load_data()

    if patient_id not in data:
         raise HTTPException(status_code=404,detail='patient not found')
    
    existing_patient_info=data[patient_id]

    updated_patient_info=patient_update.model_dump(exclude_unset=True)
    
    for key,value in updated_patient_info.items():
         existing_patient_info[key]=value

    #existing_patient_info->pydantic object->updated bmi+verdict
    existing_patient_info['id']=patient_id
    patient_pydantic_object=Patient(**existing_patient_info)

    #->pydantic object->dict
    existing_patient_info=patient_pydantic_object.model_dump(exclude='id')

     #add this dict to data
    data[patient_id]=existing_patient_info

    #save data
    save_data(data)

    return JSONResponse(status_code=200,content={'message':'patient updated'})

@app.delete('/delete/{patient_id}')   #to delete
def delete_patient(patient_id:str):
     
     #load data
     data=load_data()

     if patient_id not in data:
          raise HTTPException(status_code=404,detail='Patient not found')
     
     del data[patient_id]

     save_data(data)

     return JSONResponse(status_code=200,content={'message':'Patient deleted'})