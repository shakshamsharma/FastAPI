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


