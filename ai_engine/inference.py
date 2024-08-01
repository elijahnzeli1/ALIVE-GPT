from ai_engine.model import GenAIModel

gen_ai_model = GenAIModel()

def generate_content(prompt):
    return gen_ai_model.generate(prompt)