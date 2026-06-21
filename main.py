from fastapi import FastAPI
from app import coordinator

app = FastAPI()

@app.get("/")
def home():
    return {"message": "EduAgent API is running!"}

@app.get("/ask")
def ask(question: str):

    answer = coordinator(question)
    return {
        "question":question,
        "answer": answer
    }