import os
from dotenv import load_dotenv
import google.generativeai as genai
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def planner(query):

    response = model.generate_content(
        f"Create a study plan for: {query}"
    )

    return "Planner Agent:\n\n" + response.text