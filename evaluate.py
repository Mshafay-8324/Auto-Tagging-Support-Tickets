import os
import pandas as pd
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

# Load dataset
df = pd.read_csv("ticket.csv")

# Take a small sample
sample_df = df.sample(n=20, random_state=42)

correct = 0
total = len(sample_df)

for idx, row in sample_df.iterrows():

    ticket = row["issue_description"]
    actual_category = row["category"]

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

Return ONLY the SINGLE most relevant category.

No explanation.
No numbering.

Ticket:
{ticket}
"""

    try:
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

        prediction = response.choices[0].message.content.strip()

        print("\n----------------------------------")
        print("Ticket:", ticket[:80])
        print("Actual:", actual_category)
        print("Predicted:", prediction)

        if prediction.lower() == actual_category.lower():
            correct += 1

    except Exception as e:
        print("Error:", e)

accuracy = (correct / total) * 100

print("\n==================================")
print(f"Correct Predictions: {correct}/{total}")
print(f"Accuracy: {accuracy:.2f}%")
print("==================================")