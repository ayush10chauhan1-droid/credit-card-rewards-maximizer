# =====================================================================
# 🧪 UNIT TESTS — MULTI-CARD WALLET OPTIMIZER & MATCHMAKER
# =====================================================================

import pytest
from engine.wallet_optimizer import find_optimal_wallet_strategy
from engine.matchmaker import analyze_spend_gaps, recommend_next_cards


def test_multi_card_routing():
    # User holds SBI Cashback and Axis Ace
    # SBI Cashback should win on Online Shopping (5% vs 1.5%)
    # Axis Ace should win on Utilities (5% vs 1%)
    wallet = ["SBI Cashback Card", "Axis Ace"]
    spend = {
        "Online Shopping": 15000.0,
        "Utilities": 5000.0
    }

    strategy = find_optimal_wallet_strategy(wallet, spend)
    assert "error" not in strategy
    assignments = strategy["category_assignments"]

    assert assignments["Online Shopping"]["assigned_card"] == "SBI Cashback Card"
    assert assignments["Utilities"]["assigned_card"] == "Axis Ace"
    assert strategy["synergy_vs_single"] >= 0.0


def test_gap_analysis_and_matchmaker():
    # User only holds a low reward card
    wallet = ["ICICI Coral"]
    spend = {
        "Dining": 12000.0,
        "Online Shopping": 20000.0
    }

    gaps = analyze_spend_gaps(wallet, spend)
    assert len(gaps) > 0

    recs = recommend_next_cards(wallet, spend)
    assert len(recs) > 0
    # Top recommendation should have high positive incremental profit
    top = recs[0]
    assert top["incremental_annual_profit"] > 0
    assert len(top["conquered_categories"]) > 0
