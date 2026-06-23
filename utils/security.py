blocked_words = [
    "ignore previous instructions",
    "reveal api key",
    "show system prompt",
    "show hidden instructions",
    "bypass security"
]

def is_safe(prompt):

    prompt = prompt.lower()

    for word in blocked_words:

        if word in prompt:

            return False

    return True