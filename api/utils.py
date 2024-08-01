import re

def preprocess_prompt(prompt):
    # Remove extra whitespace and normalize text
    prompt = re.sub(r'\s+', ' ', prompt).strip()
    return prompt

def validate_input(prompt):
    if len(prompt) < 5:
        return False, "Prompt is too short. Please provide a more detailed prompt."
    if len(prompt) > 500:
        return False, "Prompt is too long. Please limit your prompt to 500 characters."
    return True, ""