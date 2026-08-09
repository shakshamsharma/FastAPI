"""
#http://127.0.0.1:8000/users/saksham
#uvicorn main:app --reload

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"Name":"Saksham"}


#Path Parameter
@app.get("/country/{country}")
def country(country):
    return {"Country": country}


#Type Hints
@app.get("/square/{number}")
def square(number: int):
    return {"square": number * number}

#Query Parameters

@app.get("/search")
def search(q):
    return {"Search": q}


@app.get("/square")
def square(number: int):
    return {"Square": number*number}

#Mini Practice
@app.get("/movie")
def movie(name):
    return {"Movie": name}


#Question 2
@app.get("/calculate")
def calculate(num: int):
    return {"double": num * 2}


#Default Parameter
@app.get("/Research")
def Research(q="Python"):
    return {"Search": q}

@app.get("/catagory")
def catagory(product="Laptop"):
    return {"Catagory": product}



#Multiple Query Parameters
@app.get("/products")
def products(catagory, model: int, price: int):
    return {"Catagory": catagory,
            "Model": model,
            "Price": price
            }

#Optional Query Parameter

@app.get("/catagories")
def catagories(smartphone, ram=None):
    return {"SmartPhone": smartphone,
            "Ram": ram
        }

#Post Request

from fastapi import FastAPI
from pydantic import BaseModel

class Student(BaseModel):
    name: str
    age: int

@app.post("/student")
def create_student(student: Student):
    return student

"""

#Student Management API
#Post Method - To Add Students
from fastapi import FastAPI
from pydantic import BaseModel

# Temporary database
students = []

app = FastAPI()


class Student(BaseModel):
    name: str
    age: int
    course: str


# CREATE
@app.post("/students")
def add_student(student: Student):
    students.append(student)
    return student


# READ ALL
@app.get("/students")
def get_students():
    return students


# READ ONE
@app.get("/students/{student_id}")
def get_student(student_id: int):
    if 0 <= student_id < len(students):
        return students[student_id]

    return {"Error": "Student Not Found"}


# UPDATE
@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    if 0 <= student_id < len(students):
        students[student_id] = student
        return {
            "message": "Student Updated",
            "Student": student
        }

    return {"Error": "Student Not Found"}


# DELETE
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if 0 <= student_id < len(students):
        deleted_student = students.pop(student_id)
        return {
            "message": "Student Deleted",
            "Student": deleted_student
        }

    return {"Error": "Student Not Found"}


    

    



    

        

