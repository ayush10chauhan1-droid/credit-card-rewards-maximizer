# =====================================================================
# 🤖 SwipeSmart AI — LLM Layer (Google Gemini via LangChain)
# =====================================================================

import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)


def explain_recommendation(best_card, comparison_text, vendor=None):
    """Generate explanation for single purchase recommendation."""

    vendor_context = ""
    if vendor:
        vendor_context = f"""
VENDOR CONTEXT:
The user is purchasing at: {vendor}
Some cards have vendor-specific rates. Highlight this.
"""

    prompt = f"""
You are SwipeSmart AI — a professional Indian credit card rewards advisor.

STRICT RULES:
- ONLY use the data below. Do NOT invent numbers.
- 4-5 sentences max. Mention runner-up.
- If vendor rates apply, explain that advantage.
- Use ₹ symbol. Be friendly but professional.

DATA:
{comparison_text}

{vendor_context}

Provide your recommendation:
"""

    try:
        response = llm.invoke(prompt)
        return response.content
    except Exception as e:
        return f"⚠️ Explanation unavailable: {str(e)}"


def explain_monthly(best_card, monthly_summary):
    """Generate explanation for monthly spending analysis."""

    prompt = f"""
You are SwipeSmart AI — a professional Indian credit card rewards advisor.

STRICT RULES:
- ONLY use the data below. Do NOT invent numbers.
- 4-5 sentences max. Focus on net yearly rewards.
- Mention top 2 cards. Give one actionable tip.
- Use ₹ symbol.

DATA:
{monthly_summary}

BEST CARD: {best_card}

Provide your monthly recommendation:
"""

    try:
        response = llm.invoke(prompt)
        return response.content
    except Exception as e:
        return f"⚠️ Explanation unavailable: {str(e)}"


def chat_with_ai(user_message, card_database_summary, chat_history=""):
    """AI chatbot that answers credit card questions using card database context."""

    prompt = f"""
You are SwipeSmart AI — India's smartest credit card assistant chatbot.

YOUR PERSONALITY:
- Friendly, helpful, and concise
- Expert on Indian credit cards and reward optimization
- You speak in a casual yet professional tone
- Use emojis occasionally to be engaging 💳✨
- Always use ₹ for Indian Rupees

STRICT RULES:
- ONLY answer credit card related questions
- If asked something unrelated, politely redirect to credit cards
- Use the card database below for factual answers
- If you don't know something, say so honestly
- Keep answers under 6 sentences unless the user asks for detail
- Never invent reward rates — only use what's in the database

CARD DATABASE:
{card_database_summary}

CONVERSATION HISTORY:
{chat_history}

USER MESSAGE: {user_message}

YOUR RESPONSE:
"""

    try:
        response = llm.invoke(prompt)
        return response.content
    except Exception as e:
        return f"⚠️ Sorry, I couldn't process that: {str(e)}"