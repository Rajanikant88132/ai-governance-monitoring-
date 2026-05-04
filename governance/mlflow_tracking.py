import mlflow
from explainability.utils import log_explanation

def log_run():
    mlflow.start_run()
    mlflow.log_param("model", "GPT-J")
    mlflow.log_metric("accuracy", 0.9)
    mlflow.end_run()
    
def log_explainability():
    log_explanation("shap", "dashboards/shap_summary.png")
    log_explanation("lime", "dashboards/lime_explanation.html")