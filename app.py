from tutor_agent import tutor
from quiz_agent import quiz
from planner_agent import planner
from career_agent import career

def coordinator(query):

    query = query.lower()

    if "quiz" in query:
        return quiz(query)

    elif (
        "plan" in query or
        "learn" in query or
        "study" in query or
        "schedule" in query
    ):
        return planner(query)

    elif (
        "career" in query or
        "become" in query or
        "resume" in query or
        "job" in query or
        "linkedin" in query
    ):
        return career(query)

    else:
        return tutor(query)

