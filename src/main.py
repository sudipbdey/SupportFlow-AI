import os
from dotenv import load_dotenv
# Use this import if main.py and agent.py are in the same folder
try:
    from agent import app 
except ImportError:
    from .agent import app

# Load API keys from .env
load_dotenv()

scenarios = [
    "How do I reset my password?",
    "The export feature crashes when I select PDF format.",
    "I was charged twice for my subscription!",
    "Can you add dark mode to the mobile app?",
    "Our API integration fails intermittently with 504 errors."
]

def run_demo():
    # Check for API Key before running
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ ERROR: OPENAI_API_KEY not found. Please check your .env file.")
        return

    print("="*50)
    print("🚀 SupportFlow-AI: Autonomous Agent Demo")
    print("="*50)
    
    for email in scenarios:
        print(f"\n📩 Processing Email: \"{email}\"")
        
        # Invoke the LangGraph workflow
        result = app.invoke({"email_body": email})
        
        print(f"📂 Topic:    {result.get('category', 'N/A')}")
        print(f"🚨 Urgency:  {result.get('urgency', 'N/A')}")
        print(f"🤖 Decision: {result.get('action', 'N/A')}")
        print(f"📝 Draft:    {result.get('draft', 'N/A')}")
        print("-" * 30)

if __name__ == "__main__":
    run_demo()
