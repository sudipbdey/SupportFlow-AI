from agent import app

scenarios = [
    "How do I reset my password?",
    "The export feature crashes when I select PDF format.",
    "I was charged twice for my subscription!",
    "Can you add dark mode to the mobile app?",
    "Our API integration fails intermittently with 504 errors."
]

def run_demo():
    print("--- SupportFlow-AI Execution ---")
    for email in scenarios:
        print(f"\nProcessing: {email}")
        result = app.invoke({"email_body": email})
        
        print(f"-> Topic: {result['category']}")
        print(f"-> Urgency: {result['urgency']}")
        print(f"-> Decision: {result['action']}")
        print(f"-> Final Output: {result['draft']}")
        print("-" * 30)

if __name__ == "__main__":
    run_demo()
