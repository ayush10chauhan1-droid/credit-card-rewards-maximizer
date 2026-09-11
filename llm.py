# Backward-compatible proxy for engine/llm_advisor.py
from engine.llm_advisor import (
    explain_single_purchase,
    explain_wallet_strategy,
    explain_matchmaker_recommendation,
    chat_with_copilot
)


def explain_recommendation(best_card, comparison_text, vendor=None, amount=5000, category="Online Shopping"):
    return explain_single_purchase(best_card, comparison_text, amount, category, vendor)


def explain_monthly(best_card, monthly_summary):
    return explain_wallet_strategy(monthly_summary)


def chat_with_ai(user_message, card_database_summary, chat_history=""):
    return chat_with_copilot(user_message, card_database_summary, chat_history)