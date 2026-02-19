#uvicorn main:app --reload
from fastapi import FastAPI, HTTPException
from typing import List, Optional
from models import Student, Feedback
from database import students
from nlp_utils import analyze_sentiment, smart_search

# IMPORTANT: This line must exist
app = FastAPI(
    title="AI-Powered Student RESTful API",
    version="1.0.0"
)

# Home API
@app.get("/")
def home():
    return {"message": "API is running successfully 🚀"}


# CREATE Student
@app.post("/students", response_model=Student)
def create_student(student: Student):
    students.append(student)
    return student


# GET All Students
@app.get("/students", response_model=List[Student])
def get_students():
    return students


# GET Student by ID
@app.get("/students/{student_id}", response_model=Student)
def get_student(student_id: int):
    if student_id < 0 or student_id >= len(students):
        raise HTTPException(status_code=404, detail="Student not found")
    return students[student_id]


# UPDATE Student
@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):
    if student_id < 0 or student_id >= len(students):
        raise HTTPException(status_code=404, detail="Student not found")

    students[student_id] = updated_student
    return {"message": "Student updated successfully", "data": updated_student}


# DELETE Student
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if student_id < 0 or student_id >= len(students):
        raise HTTPException(status_code=404, detail="Student not found")

    deleted = students.pop(student_id)
    return {"message": "Student deleted successfully", "data": deleted}


# NLP Sentiment Analysis
@app.post("/analyze-feedback")
def analyze_feedback(feedback: Feedback):
    result = analyze_sentiment(feedback.text)
    return {
        "text": feedback.text, #user input through request
        "analysis": result #return output
    } 


# Smart Search
@app.get("/search") #API endpoint
def search_students(query: str): #query input-should be string
    results = smart_search(students, query) #students are impoerted from database.py but is global, query is local
    #results is a list
    if not results: #check for empty list
        raise HTTPException(status_code=404, detail="No matching students found")

    return {"count": len(results), "students": results}
 