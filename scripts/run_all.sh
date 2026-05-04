#!/bin/bash

echo "Generating data..."
python scripts/generate_data.py

echo "Running drift detection..."
python monitoring/evidently_monitor.py

echo "Starting API..."
uvicorn app.main:app --host 0.0.0.0 --port 8000

echo "Running explainability..."
python -c "from explainability.shap_explainer import run_shap; run_shap()"
python -c "from explainability.lime_explainer import run_lime; run_lime()"