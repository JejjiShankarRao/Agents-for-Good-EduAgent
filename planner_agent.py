import google.generativeai as genai

genai.configure(api_key="GEMINI-API_KEY")

model = genai.GenerativeModel("gemini-2.5-flash")

def planner(query):

    response = model.generate_content(
        f"Create a study plan for: {query}"
    )

    return response.text