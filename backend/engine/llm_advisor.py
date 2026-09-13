# =====================================================================
# 🤖 SWIPESMART AI — ENTERPRISE LLM ADVISOR
# Powered by Google Gemini with multi-turn chat memory and RAG context
# =====================================================================

import os
from typing import Optional, List, Dict, Any
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from engine.rag_service import build_rag_context

load_dotenv()

# Cache initialized LLM
_llm_instance = None
_cached_key = None

def get_llm():
    """Dynamically get or initialize the Gemini LLM instance."""
    global _llm_instance, _cached_key
    load_dotenv(override=True)
    api_key = os.getenv("GOOGLE_API_KEY", "").strip()

    if not api_key or api_key == "your_gemini_api_key_here":
        return None

    if _llm_instance is not None and _cached_key == api_key:
        return _llm_instance

    try:
        _llm_instance = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=0.1,
            google_api_key=api_key,
            max_retries=2
        )
        _cached_key = api_key
        return _llm_instance
    except Exception:
        return None


def explain_single_purchase(
    best_card: str,
    comparison_text: str,
    amount: float,
    category: str,
    vendor: Optional[str] = None
) -> str:
    """Generate concise, actionable AI rationale for single purchase recommendation."""
    llm = get_llm()
    if not llm:
        return f"🏆 **{best_card}** is mathematically optimal for ₹{amount:,.0f} in {category} based on your selected cards."

    vendor_text = f"at {vendor}" if vendor else f"in {category}"
    prompt = f"""You are SwipeSmart AI — India's premier credit card rewards advisor.

TASK:
Analyze the card comparison below for a purchase of ₹{amount:,.0f} {vendor_text}.
Explain why {best_card} is the winning choice.

STRICT GUIDELINES:
- Maximum 4 concise sentences.
- Mention the runner-up card and the exact savings difference in ₹.
- Mention if any partner rate, capping, or fee break-even applies.
- Always use the ₹ symbol. Maintain an authoritative, polished fintech tone.

DATA:
{comparison_text}

WINNER: {best_card}
"""
    try:
        response = llm.invoke(prompt)
        return response.content.strip()
    except Exception as e:
        return f"💡 **{best_card}** provides the highest net reward on this transaction according to card terms. (AI note: {str(e)})"


def explain_wallet_strategy(strategy_summary: str) -> str:
    """Generate executive summary of multi-card monthly routing strategy."""
    llm = get_llm()
    if not llm:
        return "Your wallet cards have been routed category-by-category to maximize net annual return."

    prompt = f"""You are SwipeSmart AI — Chief Financial Advisor for Credit Card Portfolios.

TASK:
Analyze the following multi-card wallet optimization strategy across monthly spending categories.

STRICT GUIDELINES:
- Provide an executive 4-bullet point summary:
  1. Primary card driving highest volume
  2. Category routing highlights
  3. Net annual return & synergy bonus vs swiping a single card
  4. One high-impact portfolio tip (e.g. fee waiver or milestone reminder)
- Use ₹ symbol and bullet points. Be crisp and high-value.

STRATEGY DATA:
{strategy_summary}
"""
    try:
        response = llm.invoke(prompt)
        return response.content.strip()
    except Exception as e:
        return f"📊 Multi-card strategy optimized across categories. (AI note: {str(e)})"


def explain_matchmaker_recommendation(
    recommended_card: str,
    incremental_profit: float,
    conquered_categories: List[Dict[str, Any]],
    user_spends_summary: str
) -> str:
    """Generate clear rationale for why a user should apply for a new card."""
    llm = get_llm()
    if not llm:
        return f"Adding **{recommended_card}** generates an estimated +₹{incremental_profit:,.2f}/year in net profit after accounting for card fees."

    cats_str = ", ".join([f"{c['category']} ({c['new_rate']}%)" for c in conquered_categories])
    prompt = f"""You are SwipeSmart AI Matchmaker.

TASK:
Explain why the user should apply for {recommended_card} as their next credit card.
It will generate +₹{incremental_profit:,.2f} in net incremental profit per year.
It takes over: {cats_str}

MONTHLY SPENDING PROFILE:
{user_spends_summary}

STRICT GUIDELINES:
- 3 to 4 sentences max.
- Highlight the exact spending leak this card plugs.
- Mention annual fee and welcome perks if relevant.
- Be persuasive, factual, and use ₹ symbol.
"""
    try:
        response = llm.invoke(prompt)
        return response.content.strip()
    except Exception as e:
        return f"💡 Adding **{recommended_card}** plugs key category leaks to produce +₹{incremental_profit:,.2f}/yr net gain."


def fallback_copilot_response(user_message: str) -> str:
    """Provide structured, helpful answer from the local RAG knowledge base when Gemini API key is not set."""
    from engine.rag_service import search_knowledge_base
    cleaned = user_message.strip().lower()

    if cleaned in ["hi", "hii", "hello", "hey", "hola", "namaste", "good morning", "good evening"]:
        return (
            "👋 **Hello! I'm your SwipeSmart Copilot.**\n\n"
            "I'm currently powered by the verified **Card Rules & RAG Knowledge Hub** across 26 Indian credit cards.\n\n"
            "Feel free to ask me questions like:\n"
            "• *\"How does SBI Cashback capping work?\"*\n"
            "• *\"Which card offers complimentary lounge access?\"*\n"
            "• *\"What is the forex fee on Scapia?\"*\n"
            "• *\"Compare Infinia vs Axis Atlas\"*\n\n"
            "*(💡 To enable Google Gemini 2.5 generative reasoning, configure your `GOOGLE_API_KEY` in the `.env` file.)*"
        )

    docs = search_knowledge_base(user_message, top_k=2)
    scored_docs = [d for d in docs if d.get("score", 0) > 0]

    if scored_docs:
        reply_parts = ["📚 **Verified Card Knowledge Hub Answer:**\n"]
        for d in scored_docs:
            reply_parts.append(f"💳 **{d['card']}** — *{d['topic']}*:\n{d['text']}\n")
        reply_parts.append("\n*(💡 To enable Gemini 2.5 Flash multi-turn AI reasoning, set `GOOGLE_API_KEY` in your `.env` file.)*")
        return "\n".join(reply_parts)

    return (
        f"🔍 I searched the knowledge base for **\"{user_message}\"**.\n\n"
        "Try asking about specific cards (*Infinia, SBI Cashback, Axis Atlas, Scapia*) or topics (*lounges, forex markup, monthly capping*).\n\n"
        "*(💡 To unlock full Gemini 2.5 generative AI reasoning, configure your `GOOGLE_API_KEY` in `.env`.)*"
    )


def chat_with_copilot(
    user_message: str,
    card_database_summary: str,
    chat_history: str = ""
) -> str:
    """Intelligent credit card copilot chatbot with RAG context and Gemini 2.5."""
    llm = get_llm()
    if not llm:
        return fallback_copilot_response(user_message)

    # Retrieve relevant RAG terms and rules
    rag_context = build_rag_context(user_message)

    prompt = f"""You are SwipeSmart Copilot — an elite, highly knowledgeable Indian credit card & rewards strategist.

CORE ATTRIBUTES:
- World-class expert on Indian credit cards (HDFC, SBI, ICICI, Axis, Amex, IDFC, Federal Scapia, Kotak, IndusInd).
- Authoritative, friendly, mathematically rigorous, and objective.
- Always use the Indian Rupee symbol (₹).
- When discussing cards, cite actual features: capping limits, lounge access, point valuations, milestone tiers, and exclusions.
- If asked something completely outside personal finance / credit cards, politely pivot back to credit cards.

RELEVANT KNOWLEDGE BASE CONTEXT (RAG):
{rag_context}

CARD DATABASE REFERENCE:
{card_database_summary[:3000]}

CONVERSATION HISTORY:
{chat_history}

USER INQUIRY:
{user_message}

YOUR ANSWER:
"""
    try:
        response = llm.invoke(prompt)
        return response.content.strip()
    except Exception as e:
        return f"⚠️ I encountered an error answering your inquiry: {str(e)}"

