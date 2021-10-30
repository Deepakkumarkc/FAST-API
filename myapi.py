from typing import Optional
from fastapi import FastAPI
from fastapi.param_functions import Path
from pydantic import BaseModel

app = FastAPI()

students ={
    1:{
        "name": "Deepak", "age": "23", "class": "MCA"
    }
}

class Student(BaseModel):
    name: str
    age: int
    year: str

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None

@app.get("/") ## app is variable is given to FastAPI object and get is method
def index():
    return{"name:" "Deepak" }

# Path Parameter Example - GET STUDENT DETAILS USIING ID
@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(None, description = "Enter the Id of the studuent you want to view.", gt = 0, lt = 3)): 
    ## Path parameters --> Descriptions display in Docs and other attributes are availabe gt -> greaterthan, lt -> lessthan, ge -> greaterthan equal, le -> lessthan equal
    if student_id not in students:
        return {"Error": "Student Not Found"}
    return students[student_id]

# This condition not working properly
# Query Parameter Example & Path and Query parameters
@app.get("/get-by-name/{student_id}")
def get_student( student_id: int ,name : Optional[str] = None): #, test : int 
    # Optional is you can give name or not its is optional / * -> run both condition optional and require(test) condition. Test is required filed you cannot empty that field
    if student_id not in students:
        return {"Error": "Student Not Found"}
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]  
    return {"Data": "Not Found"}

    

#POST method - CREATE USER
@app.post("/create-student/{student_id}")
def create_student(student_id : int, student : Student):
    if student_id in students:
        return {"Error": "Student already exists"}
    students[student_id] = student
    return students[student_id]

#PUT method -UPDATE USER
@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in  students:
        return {"Error":"Student Not Found"}
    
    if student.name != None:
        students[student_id].name = student.name
    
    if student.age != None:
        students[student_id].age = student.age
    
    if student.year != None:
        students[student_id].year = student.year

    return students[student_id]


#DELETE method - DELETE USER
@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error": "Student Not Found"}
    
    del students[student_id]
    return {"Successfully Deleted"}
