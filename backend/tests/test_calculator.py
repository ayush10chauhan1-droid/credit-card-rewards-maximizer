# =====================================================================
# 🧪 UNIT TESTS — CALCULATION & CAPPING ENGINE
# =====================================================================

import pytest
from engine.calculator import (
    get_reward_rate,
    calculate_reward,
    compare_cards,
    calculate_card_annual_net,
    apply_monthly_cap
)


def test_reward_rate_priority():
    # Swiggy partner rate should be 10.0% on Swiggy HDFC
    rate, source = get_reward_rate("Swiggy HDFC", "Dining", "Swiggy")
    assert rate == 10.0
    assert "Swiggy" in source

    # Category rate fallback when vendor not listed
    rate, source = get_reward_rate("Swiggy HDFC", "Dining", None)
    assert rate == 10.0
    assert "Dining" in source


def test_monthly_capping():
    # SBI Cashback Card caps 5% cashback at ₹5,000/month
    raw_reward = 10000.0  # e.g. 5% on ₹2,00,000 spend
    capped, note = apply_monthly_cap("SBI Cashback Card", "Online Shopping", None, raw_reward)
    assert capped == 5000.0
    assert note is not None
    assert "Capped at ₹5,000" in note

    # Swiggy HDFC caps Swiggy at ₹1,500/month
    capped_swiggy, note = apply_monthly_cap("Swiggy HDFC", "Dining", "Swiggy", 2500.0)
    assert capped_swiggy == 1500.0
    assert "₹1,500" in note


def test_single_purchase_comparison():
    cards = ["SBI Cashback Card", "ICICI Amazon Pay", "HDFC Millennia"]
    comp = compare_cards(cards, "Online Shopping", 10000.0, vendor="Amazon")

    assert comp["best_card"] is not None
    assert len(comp["results"]) == 3
    # Rates on Amazon: SBI Cashback (5%), ICICI Amazon Pay (5%), HDFC Millennia (5%)
    assert comp["best_reward"] == 500.0


def test_annual_net_and_fee_waiver():
    # Spend ₹3,00,000 annually on HDFC Millennia (Waiver threshold is ₹1,00,000)
    monthly_spend = {"Online Shopping": 25000.0}
    net_data = calculate_card_annual_net("HDFC Millennia", monthly_spend)

    # Annual fee should be waived
    assert net_data["fee_waived"] is True
    assert net_data["effective_fee"] == 0
    assert net_data["net_yearly_return"] > 0
