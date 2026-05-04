from evidently.report import Report
from evidently.metric_preset import DataDriftPreset
import pandas as pd

def run_drift():
    ref = pd.read_csv("data/reference.csv")
    curr = pd.read_csv("data/current.csv")

    report = Report(metrics=[DataDriftPreset()])
    report.run(reference_data=ref, current_data=curr)
    report.save_html("dashboards/drift_report.html")