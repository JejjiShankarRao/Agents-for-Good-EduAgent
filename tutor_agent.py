import google.generativeai as genai

genai.configure(api_key="GEMINI_API_KEY")

model = genai.GenerativeModel("gemini-2.5-flash")

def tutor(query):

    response = model.generate_content(
        f"Explain simply: {query}"
    )

    print(response)

    return response.text