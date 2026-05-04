from fastapi import FastAPI
from app.model import load_model, predict
from monitoring.prometheus_metrics import record_metrics
from explainability.shap_explainer import run_shap
from explainability.lime_explainer import run_lime

app = FastAPI()
model = load_model()

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/predict")
def run_model(prompt: str):
    result = predict(model, prompt)
    record_metrics(len(result))
    return {"response": result}

@app.get("/explain/shap")
def shap_explain():
    result = run_shap()
    return {"status": result}

@app.get("/explain/lime")
def lime_explain():
    result = run_lime()
    return {"status": result}