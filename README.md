# AI Governance & Monitoring (Open Source)

## Overview
This project demonstrates monitoring and governance of:
- AI models
- AI agents
- AI pipelines

## Stack
- Model: GPT-J (HuggingFace)
- Monitoring: Evidently, Prometheus, Grafana
- Governance: MLflow, OpenLineage, OPA
- Agent: LangChain-style agent

## Features
- Drift detection
- Metrics monitoring
- Policy enforcement
- Model versioning
- Audit logging

## Aligns with EU AI Act:

Logging ✔
Monitoring ✔
Risk control ✔
Human oversight ✔

## Term	                        Meaning
| Term                      | Meaning                                                   |
| ------------------------- | --------------------------------------------------------- |
| **AI Model Monitoring**   | Tracking model performance, drift, data quality, fairness |
| **AI Governance**         | Policies, compliance, risk & audit logging                |
| **AI Solution/AI Agents** | Full systems combining multiple AI components             |
| **Open-Source Tools**     | Tools with source code you can run & modify freely        |


## Data Flow

1. Data Source →
2. Model Inference (LLM / AI Agent) →
3. Metrics & Logs
   - Prometheus
   - OpenTelemetry
   - Custom logs
4. Governance & Audit
 - MLflow / OpenLineage
  -OPA policies
5.Dashboarding & Alerts
   - Grafana / Evidently dashboards
   - Alert via Slack/Email



## 🧩 2. Recommended Open-Source Stack
## 🖥️ Application Layer
FastAPI (backend)
React or Streamlit (UI)
WebSocket for streaming AI responses
## 🧠 AI Processing Layer
LangChain → AI agents + orchestration
LlamaIndex → RAG pipeline
OpenAI / Ollama → local LLMs
Tools: calculator, search, database tools for agents
## 📊 Monitoring Layer
Langfuse → LLM tracing (VERY IMPORTANT for your thesis)
Prometheus → metrics
Grafana → dashboards
OpenTelemetry → distributed tracing
## ⚖️ Governance Layer
MLflow → model registry + experiment tracking
Evidently AI → drift + data quality monitoring
Open Policy Agent → policy enforcement
DVC → dataset versioning
## 🔍 Explainability Layer
SHAP (feature importance)
LIME (local explanations)
Langfuse trace viewer (LLM reasoning path)
RAG citations (source-based explainability)
### ⚙️ 3. Demo Workflow (What You Will Show)
   ## Step 1: User Query

    User asks:

    “Should I approve this loan?”

   ## Step 2: AI Processing Layer
      LangChain agent calls:
      credit scoring model
      policy rules engine
      document retrieval (RAG)
   ## Step 3: Monitoring Layer Captures Everything
      Prompt
      Model response
      Latency
      Token usage
      Tool calls

   ## Visible in:
      👉 Langfuse dashboard + Grafana

   ## Step 4: Governance Layer Checks:
      MLflow logs model version
      Evidently checks drift (income distribution shift)
      OPA checks policy:
      “Loan > 50k requires manual approval”
   ## Step 5: Explainability Layer Output:

# System shows:

Why decision was made
SHAP chart (feature importance)
Retrieved documents (RAG evidence)
Full reasoning trace


## Run

```bash
docker-compose up --build
## 🏗️ 1. High-Level Architecture
┌──────────────────────────────────────────────┐
│ 1. Application Layer (UI + API)             │
│  - Chat UI / Dashboard                      │
│  - REST / FastAPI backend                   │
└──────────────────────────────────────────────┘
                 ↓
┌──────────────────────────────────────────────┐
│ 2. AI Processing Layer                      │
│  - LLM (OpenAI / Llama / Mistral)          │
│  - AI Agents (LangChain / CrewAI)          │
│  - RAG pipeline (optional)                 │
└──────────────────────────────────────────────┘
                 ↓
┌──────────────────────────────────────────────┐
│ 3. Monitoring & Observability Layer         │
│  - Langfuse / LangSmith (traces)           │
│  - Prometheus (metrics)                    │
│  - Grafana (dashboards)                    │
│  - OpenTelemetry (tracing)                 │
└──────────────────────────────────────────────┘
                 ↓
┌──────────────────────────────────────────────┐
│ 4. Governance & Compliance Layer            │
│  - MLflow (model registry)                 │
│  - Evidently AI (drift, bias)             │
│  - OpenPolicyAgent (OPA)                  │
│  - Data/version control (DVC)             │
└──────────────────────────────────────────────┘
                 ↓
┌──────────────────────────────────────────────┐
│ 5. Explainability Layer                     │
│  - SHAP / LIME (tabular models)           │
│  - LLM explanation prompts                │
│  - Langfuse trace replay                  │
│  - RAG source attribution                 │
└──────────────────────────────────────────────┘


## 📊 Model Monitoring Architecture


                +-----------------+
                |  AI Model / LLM |
                +-----------------+
                           |
        -----------------------------------
        |                |                |
   Metrics (Prom)   Drift (Evidently)   Lineage (OpenLineage)
        |                |                |
   +----------+     +-----------+       +-----------+
   |Prometheus|     |Drift HTML |       | Metadata  |
   +----------+     +-----------+       +-----------+
        |                 |
   +------------------------------+
   |         Grafana             |
   +------------------------------+

##🧩 2. Recommended Open-Source Stack
🖥️ Application Layer
FastAPI (backend)
React or Streamlit (UI)
WebSocket for streaming AI responses
🧠 AI Processing Layer
LangChain → AI agents + orchestration
LlamaIndex → RAG pipeline
OpenAI / Ollama → local LLMs
Tools: calculator, search, database tools for agents
📊 Monitoring Layer
Langfuse → LLM tracing (VERY IMPORTANT for your thesis)
Prometheus → metrics
Grafana → dashboards
OpenTelemetry → distributed tracing
⚖️ Governance Layer
MLflow → model registry + experiment tracking
Evidently AI → drift + data quality monitoring
Open Policy Agent → policy enforcement
DVC → dataset versioning
🔍 Explainability Layer
SHAP (feature importance)
LIME (local explanations)
Langfuse trace viewer (LLM reasoning path)
RAG citations (source-based explainability)
##
⚙️ 3. Demo Workflow (What You Will Show)
Step 1: User Query

User asks:

“Should I approve this loan?”

Step 2: AI Processing Layer
LangChain agent calls:
credit scoring model
policy rules engine
document retrieval (RAG)
Step 3: Monitoring Layer Captures Everything
Prompt
Model response
Latency
Token usage
Tool calls

Visible in:
👉 Langfuse dashboard + Grafana

Step 4: Governance Layer Checks:
MLflow logs model version
Evidently checks drift (income distribution shift)
OPA checks policy:
“Loan > 50k requires manual approval”
Step 5: Explainability Layer Output:

System shows:

Why decision was made
SHAP chart (feature importance)
Retrieved documents (RAG evidence)
Full reasoning trace
