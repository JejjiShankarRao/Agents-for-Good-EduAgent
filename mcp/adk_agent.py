from google.adk.agents import Agent

edu_agent = Agent(
    name="EduAgent",
    model="gemini-2.5-flash",
    instruction="""
    You are an educational AI assistant.
    Help students learn concepts simply.
    """
)