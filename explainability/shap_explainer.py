import shap
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

def train_sample_model():
    df = pd.read_csv("explainability/sample_data.csv")
    X = df.drop("target", axis=1)
    y = df["target"]

    model = RandomForestClassifier()
    model.fit(X, y)

    return model, X

def run_shap():
    model, X = train_sample_model()

    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X)

    # Global explanation
    shap.summary_plot(shap_values, X, show=False)
    import matplotlib.pyplot as plt
    plt.savefig("dashboards/shap_summary.png")

    return "SHAP explanation generated"