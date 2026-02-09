import os
from typing import TypedDict, Literal
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, END

load_dotenv()

# 1. Define the state
class AgentState(TypedDict):
    email_body: str
    category: str
    urgency: str
    action: str  # "respond", "escalate", or "follow_up"
    draft: str

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# 2. Node: Classification
def classify_node(state: AgentState):
    prompt = f"""Classify the following email for:
    1. Topic: (Account, Billing, Bug, Feature Request, Technical Issue)
    2. Urgency: (Low, Medium, High)
    
    Email: {state['email_body']}
    Return only: Topic | Urgency"""
    
    response = llm.invoke(prompt).content
    topic, urgency = response.split(" | ")
    return {"category": topic, "urgency": urgency}

# 3. Node: Router (The Decision Logic)
def router_node(state: AgentState):
    # Rule-based escalation for high risk topics
    if state['urgency'] == "High" or state['category'] == "Billing":
        return "escalate"
    return "respond"

# 4. Node: Action Handlers
def escalate_action(state: AgentState):
    return {
        "action": "Human Escalation", 
        "draft": f"Critical {state['category']} issue detected. Handing over to a human specialist."
    }

def respond_action(state: AgentState):
    return {
        "action": "AI Auto-Reply", 
        "draft": f"Thank you for reaching out about {state['category']}. Here is the information from our docs..."
    }

# 5. Build the Graph
workflow = StateGraph(AgentState)

workflow.add_node("classify", classify_node)
workflow.add_node("escalate", escalate_action)
workflow.add_node("respond", respond_action)

workflow.set_entry_point("classify")

# Conditional logic: Decide which path to take after classification
workflow.add_conditional_edges(
    "classify",
    router_node,
    {
        "escalate": "escalate",
        "respond": "respond"
    }
)

workflow.add_edge("escalate", END)
workflow.add_edge("respond", END)

app = workflow.compile()
