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






