import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

CATEGORIES = [
    "Feature Request",
    "Subscription Cancellation",
    "Performance Issue",
    "Security Concern",
    "Login Issue",
    "Payment Problem",
    "Bug Report",
    "Refund Request",
    "Data Sync Issue",
    "Account Suspension"
]

ticket = input("Enter support ticket: ")

prompt = f"""
You are a support ticket classification system.

Available categories:

{CATEGORIES}

Examples:

Ticket:
The payment was deducted from my bank account but the transaction failed.

Categories:
Payment Problem
Refund Request
Bug Report

---

Ticket:
I cannot log into my account after changing my password.

Categories:
Login Issue
Security Concern
Account Suspension

---

Ticket:
The application crashes whenever I upload a file.

Categories:
Bug Report
Performance Issue
Data Sync Issue

---

Analyze the following ticket.

Return EXACTLY 3 category names.

No explanations.
No numbering.

Ticket:
{ticket}
"""

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0
)

print("\nPredicted Categories:\n")
print(response.choices[0].message.content)