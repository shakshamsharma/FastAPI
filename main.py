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

# ============================================================
# STUDENT MANAGEMENT API
# ============================================================


# ------------------------------------------------------------
# 1. IMPORTS
# ------------------------------------------------------------

from fastapi import FastAPI
# FastAPI → a Python class/framework used to create APIs.
# We import FastAPI so we can create our API application.


from pydantic import BaseModel
# BaseModel → a class provided by Pydantic.
# We use it to create models that validate request data.
# Example:
# age: int means age must be an integer.


# ------------------------------------------------------------
# 2. TEMPORARY DATABASE
# ------------------------------------------------------------

students = []
# students → VARIABLE
# Data type → LIST
# [] → empty list
#
# We use this list as our temporary database.
# Students will be stored inside this list.
#
# Example after adding students:
#
# students = [
#     Student(name="Saksham", age=22, course="CSE"),
#     Student(name="Rahul", age=21, course="ECE")
# ]
#
# IMPORTANT:
# This is NOT a real database.
# If the server restarts, the data will disappear.


# ------------------------------------------------------------
# 3. CREATE FASTAPI APPLICATION
# ------------------------------------------------------------

app = FastAPI()
# app → VARIABLE
# FastAPI() → creates an OBJECT of the FastAPI class.
#
# app is the main object we use to create our API routes.
#
# Example:
# @app.get(...)
# @app.post(...)
# @app.put(...)
# @app.patch(...)
# @app.delete(...)


# ------------------------------------------------------------
# 4. STUDENT MODEL
# ------------------------------------------------------------

class Student(BaseModel):
    # Student → CLASS
    # BaseModel → PARENT CLASS
    #
    # This class defines what a complete Student should look like.
    # We use it to validate incoming data.

    name: str
    # name → VARIABLE / FIELD
    # str → DATA TYPE = string
    #
    # Example:
    # "Saksham"

    age: int
    # age → VARIABLE / FIELD
    # int → DATA TYPE = integer
    #
    # Example:
    # 22

    course: str
    # course → VARIABLE / FIELD
    # str → DATA TYPE = string
    #
    # Example:
    # "CSE"


# ------------------------------------------------------------
# 5. STUDENT UPDATE MODEL
# ------------------------------------------------------------

class StudentUpdate(BaseModel):
    # StudentUpdate → CLASS
    # Used specifically for PATCH requests.
    #
    # PATCH allows us to update only SOME fields.
    #
    # Example:
    #
    # {
    #     "age": 23
    # }
    #
    # We don't need to send name and course.

    name: str | None = None
    # name → FIELD
    # str → can contain a string
    # None → can also contain no value
    # = None → default value is None
    #
    # Therefore name is OPTIONAL.

    age: int | None = None
    # age → FIELD
    # int → integer
    # None → no value
    # = None → default is None
    #
    # Therefore age is OPTIONAL.

    course: str | None = None
    # course → FIELD
    # str → string
    # None → no value
    # = None → default is None
    #
    # Therefore course is OPTIONAL.


# ============================================================
# CREATE
# ============================================================

@app.post("/students")
# @app.post() → DECORATOR
#
# It tells FastAPI:
# "When a POST request comes to /students,
#  run the function below."
#
# /students → URL PATH
#
# POST → HTTP METHOD


def add_student(student: Student):
    # add_student → FUNCTION
    #
    # student → PARAMETER / VARIABLE
    #
    # Student → TYPE ANNOTATION
    #
    # student: Student means:
    # "student should be a Student object."
    #
    # FastAPI receives JSON from the request body
    # and Pydantic converts/validates it as a Student object.

    students.append(student)
    # students → our LIST
    # append() → LIST METHOD
    #
    # Add the new student to the end of the list.
    #
    # Example:
    #
    # students = []
    #
    # After:
    # students.append(student)
    #
    # students = [
    #     Student(...)
    # ]

    return student
    # return → sends a response back to the client.
    #
    # Here we return the student that was just added.


# ============================================================
# READ ALL
# ============================================================

@app.get("/students")
# @app.get() → DECORATOR
#
# GET → HTTP METHOD
#
# /students → URL PATH
#
# When someone sends:
#
# GET /students
#
# FastAPI runs get_students().


def get_students():
    # get_students → FUNCTION
    #
    # No parameter is required because we want ALL students.

    return students
    # Return the entire students LIST.


# ============================================================
# READ ONE
# ============================================================

@app.get("/students/{student_id}")
# {student_id} → PATH PARAMETER
#
# Example:
#
# /students/0
# /students/1
# /students/2
#
# The number in the URL becomes student_id.


def get_student(student_id: int):
    # student_id → PARAMETER / VARIABLE
    # int → DATA TYPE
    #
    # Example:
    #
    # GET /students/1
    #
    # student_id = 1


    if 0 <= student_id < len(students):
        # if → CONDITION
        #
        # 0 <= student_id
        # means ID cannot be negative.
        #
        # student_id < len(students)
        # checks that the ID is inside the list.
        #
        # Example:
        #
        # If we have 3 students:
        # len(students) = 3
        #
        # Valid indexes:
        # 0, 1, 2
        #
        # 3 is NOT valid.

        return students[student_id]
        # students[student_id]
        # means get the student at that index.
        #
        # Example:
        #
        # student_id = 1
        #
        # students[1]
        # → Rahul


    return {"Error": "Student Not Found"}
    # If the ID doesn't exist,
    # return an error message.
    #
    # {"Error": "..."} → DICTIONARY


# ============================================================
# UPDATE - PUT
# ============================================================

@app.put("/students/{student_id}")
# PUT → HTTP METHOD
#
# PUT is generally used to replace/update the complete object.
#
# {student_id} → PATH PARAMETER.


def update_student(student_id: int, student: Student):
    # student_id → INTEGER
    # Used to identify WHICH student to update.
    #
    # student → Student OBJECT
    # Contains the NEW student information.
    #
    # Example:
    #
    # URL:
    # /students/1
    #
    # Body:
    # {
    #     "name": "Rahul",
    #     "age": 22,
    #     "course": "CSE"
    # }


    if 0 <= student_id < len(students):
        # Check whether the student exists.

        students[student_id] = student
        # LIST INDEX ASSIGNMENT
        #
        # Replace the old student with the new student.
        #
        # Example:
        #
        # Before:
        # students[1] = Rahul, age 21
        #
        # After:
        # students[1] = Rahul, age 22


        return {
            "message": "Student Updated",
            "Student": student
        }
        # Return a DICTIONARY containing:
        #
        # message → confirmation
        # Student → updated student object


    return {"Error": "Student Not Found"}
    # Student ID doesn't exist.


# ============================================================
# UPDATE - PATCH
# ============================================================

@app.patch("/students/{student_id}")
# PATCH → HTTP METHOD
#
# PATCH is used for PARTIAL updates.
#
# Example:
#
# Existing student:
#
# {
#     "name": "Saksham",
#     "age": 22,
#     "course": "CSE"
# }
#
# We can send only:
#
# {
#     "age": 23
# }
#
# Only age will be changed.


def patch_student(student_id: int, student: StudentUpdate):
    # student_id → INTEGER
    # Identifies WHICH student to update.
    #
    # student → StudentUpdate OBJECT
    # Contains only the fields the user wants to change.


    if 0 <= student_id < len(students):
        # Check whether the student exists.


        update_data = student.model_dump(exclude_unset=True)
        # student → StudentUpdate object
        #
        # model_dump()
        # converts the Pydantic object into a Python DICTIONARY.
        #
        # exclude_unset=True
        # means:
        # "Only include fields that the user actually sent."
        #
        # Example request:
        #
        # {
        #     "age": 23
        # }
        #
        # update_data becomes:
        #
        # {
        #     "age": 23
        # }


        for field, value in update_data.items():
            # for → LOOP
            #
            # .items()
            # gets KEY + VALUE from a dictionary.
            #
            # Example:
            #
            # update_data = {
            #     "age": 23
            # }
            #
            # field = "age"
            # value = 23
            #
            # If there are multiple fields:
            #
            # {
            #     "name": "Saksham",
            #     "age": 23
            # }
            #
            # The loop runs twice.


            setattr(students[student_id], field, value)
            # setattr() → PYTHON BUILT-IN FUNCTION
            #
            # It changes an ATTRIBUTE of an OBJECT.
            #
            # Example:
            #
            # field = "age"
            # value = 23
            #
            # This:
            #
            # setattr(student, "age", 23)
            #
            # is basically the same as:
            #
            # student.age = 23
            #
            # So we dynamically change whatever field
            # the user sent.


        return {
            "message": "Student Updated",
            "Student": students[student_id]
        }
        # Return the updated student.


    return {"Error": "Student Not Found"}
    # Student ID doesn't exist.


# ============================================================
# DELETE
# ============================================================

@app.delete("/students/{student_id}")
# DELETE → HTTP METHOD
#
# Used to delete one student.
#
# {student_id} → PATH PARAMETER


def delete_student(student_id: int):
    # student_id → PARAMETER
    # int → DATA TYPE
    #
    # Example:
    #
    # DELETE /students/1
    #
    # student_id = 1


    if 0 <= student_id < len(students):
        # Check whether the student exists.


        deleted_student = students.pop(student_id)
        # students → LIST
        # pop() → LIST METHOD
        #
        # Removes the student from the list.
        #
        # Example:
        #
        # Before:
        # [Saksham, Rahul, Priya]
        #
        # pop(1)
        #
        # After:
        # [Saksham, Priya]
        #
        # IMPORTANT:
        # pop() also RETURNS the item it removed.
        #
        # Therefore:
        #
        # deleted_student
        # contains Rahul.


        return {
            "message": "Student Deleted",
            "Student": deleted_student
        }
        # Return confirmation + deleted student.


    return {"Error": "Student Not Found"}
    # Student ID doesn't exist.