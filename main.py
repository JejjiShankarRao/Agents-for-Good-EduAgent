from fastapi import FastAPI
from app import coordinator
from utils.security import is_safe

app = FastAPI()

@app.get("/")
def home():
    return {"message": "EduAgent API is running!"}

@app.get("/ask")
def ask(question: str):

    if not question.strip():

        return {
            "error": "Question cannot be empty"
        }

    if len(question) > 500:

        return {
            "error": "Question too long"
        }
    if not is_safe(question):
        return {
            "error": "Unsafe prompt detected"
        }

    try:

        answer = coordinator(question)

        return {

            "question": question,

            "answer": answer

        }

    except Exception as e:

        return {

            "error": str(e)

        }