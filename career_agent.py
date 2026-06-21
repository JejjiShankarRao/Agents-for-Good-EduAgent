import google.generativeai as genai

genai.configure(api_key="GEMINI_API_KEY")

model = genai.GenerativeModel("gemini-2.5-flash")

def career(query):

    response = model.generate_content(
        f"Provide career guidance on: {query}"
    )

    return response.text