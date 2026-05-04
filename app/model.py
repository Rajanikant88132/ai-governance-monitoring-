from transformers import pipeline

def load_model():
    return pipeline("text-generation", model="EleutherAI/gpt-j-6B")

def predict(model, prompt):
    return model(prompt, max_length=100)[0]["generated_text"]