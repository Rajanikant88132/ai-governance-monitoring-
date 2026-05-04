import mlflow

def log_explanation(name, path):
    mlflow.log_artifact(path, artifact_path=name)