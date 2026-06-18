import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

# -----------------------------
# CONFIG
# -----------------------------

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

# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="Support Ticket Auto-Tagger",
    page_icon="🎫",
    layout="centered"
)

# -----------------------------
# SIDEBAR
# -----------------------------

with st.sidebar:
    st.title("🎫 Auto-Tagging System")

    st.markdown("### AI Model")
    st.write("LLaMA 3.1 8B (Groq)")

    st.markdown("### Techniques")
    st.write("• Zero-Shot Prompting")
    st.write("• Few-Shot Prompting")
    st.write("• Prompt Engineering")

    st.divider()

    st.markdown("### Internship")
    st.caption("DevelopersHub Corporation")
    st.caption("AI/ML Engineering Internship")
    st.caption("Task 5")

# -----------------------------
# HEADER
# -----------------------------

st.title("🎫 Support Ticket Auto-Tagger")

st.markdown(
    "Automatically classify support tickets into the **Top 3 most relevant categories** using LLM prompting techniques."
)

st.divider()

# -----------------------------
# PROMPT MODE
# -----------------------------

mode = st.radio(
    "Select Classification Mode",
    ["Zero-Shot", "Few-Shot"],
    horizontal=True
)

# -----------------------------
# INPUT
# -----------------------------

ticket = st.text_area(
    "Support Ticket",
    height=180,
    placeholder="Enter support ticket text here..."
)

# -----------------------------
# BUTTON
# -----------------------------

if st.button("Predict Categories", use_container_width=True):

    if not ticket.strip():
        st.warning("Please enter a support ticket.")
        st.stop()

    with st.spinner("Analyzing ticket..."):

        if mode == "Zero-Shot":

            prompt = f"""
You are a support ticket classification system.

Available categories:

{CATEGORIES}

Analyze the support ticket.

Return EXACTLY 3 category names.

Rules:
- No explanation
- No numbering
- One category per line

Ticket:
{ticket}
"""

        else:

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

No explanation.
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

        prediction = response.choices[0].message.content

    st.success("Classification Complete")

    st.subheader("Predicted Categories")

    st.code(prediction)