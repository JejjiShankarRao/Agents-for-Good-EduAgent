import google.generativeai as genai

genai.configure(api_key="GEMINI_API_KEY")

model = genai.GenerativeModel("gemini-2.5-flash")

def quiz(query):

    response = model.generate_content(
        f"Create a quiz on: {query}"
    )

    return response.text