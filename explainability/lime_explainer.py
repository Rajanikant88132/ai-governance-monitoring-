import pandas as pd
from lime.lime_tabular import LimeTabularExplainer
from sklearn.ensemble import RandomForestClassifier

def run_lime():
    df = pd.read_csv("explainability/sample_data.csv")
    X = df.drop("target", axis=1)
    y = df["target"]

    model = RandomForestClassifier()
    model.fit(X, y)

    explainer = LimeTabularExplainer(
        training_data=X.values,
        feature_names=X.columns,
        class_names=["0", "1"],
        mode="classification"
    )

    exp = explainer.explain_instance(
        X.iloc[0].values,
        model.predict_proba
    )

    exp.save_to_file("dashboards/lime_explanation.html")

    return "LIME explanation generated"