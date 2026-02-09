# SupportFlow-AI
Autonomous Customer Support Orchestrator
# SupportFlow-AI: Autonomous Support Agent

An AI-driven system built with **LangChain** and **LangGraph** to process customer emails from ingestion to resolution.

## 🚀 Overview
This agent automates the support workflow by:
1. **Classifying** intent and urgency.
2. **Searching** local documentation (RAG).
3. **Drafting** responses or **Escalating** to humans.



## 🛠️ Escalation Logic
To ensure accuracy and safety, the agent triggers a human handoff in these cases:
- **Billing Issues:** All financial discrepancies (e.g., double charges) require manual review.
- **Technical Failures:** Infrastructure errors like **504 Gateway Timeouts** are escalated to DevOps.
- **High Urgency:** Any request flagged as "High" priority bypasses automated drafts.

## 📁 Project Structure
- `src/agent.py`: LangGraph workflow logic.
- `src/main.py`: Test runner for the 5 required scenarios.
- `data/knowledge_base.json`: Mock company policy documentation.
- `requirements.txt`: Python dependencies.

## ⚡ Quick Start
1. Install dependencies: `pip install -r requirements.txt`
2. Add your API key to a `.env` file.
3. Run the demo: `python src/main.py`
