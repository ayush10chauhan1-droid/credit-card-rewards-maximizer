# =====================================================================
# 🎯 SWIPESMART AI CARD MATCHMAKER & GAP FINDER
# Identifies spending leaks in current wallet and recommends the
# most profitable new card to add with mathematically proven net ROI.
# =====================================================================

from typing import Dict, List, Any, Optional
from data.cards_db import CARDS_DATABASE
from engine.wallet_optimizer import find_optimal_wallet_strategy


def analyze_spend_gaps(
    wallet_cards: List[str],
    monthly_spend: Dict[str, float]
) -> List[Dict[str, Any]]:
    """
    Detects categories where user spends significant money but receives low reward rates (< 2.5%).
    """
    if not wallet_cards:
        return []

    strategy = find_optimal_wallet_strategy(wallet_cards, monthly_spend)
    if "error" in strategy:
        return []

    gaps = []
    assignments = strategy.get("category_assignments", {})

    for cat, data in assignments.items():
        spend = data["spend"]
        rate = data["effective_rate"]

        # High spend with low rate (< 2.5%) is a leakage gap
        if spend >= 3000 and rate < 2.5:
            annual_leak = round(spend * 12.0 * (0.05 - (rate / 100.0)), 2)
            gaps.append({
                "category": cat,
                "monthly_spend": spend,
                "current_rate": rate,
                "current_card": data["assigned_card"],
                "potential_rate": 5.0,  # Benchmark partner rate
                "annual_leak_estimate": max(0.0, annual_leak),
                "urgency": "High" if spend >= 10000 else "Medium"
            })

    gaps.sort(key=lambda x: -x["annual_leak_estimate"])
    return gaps


def recommend_next_cards(
    current_wallet: List[str],
    monthly_spend: Dict[str, float],
    lifestyle_filter: str = "All",
    max_fee: Optional[float] = None
) -> List[Dict[str, Any]]:
    """
    Evaluates every unowned card in the database by simulating its addition to the current wallet.
    Ranks candidates strictly by Net Incremental Annual Profit.
    """
    current_strategy = find_optimal_wallet_strategy(current_wallet, monthly_spend) if current_wallet else None
    current_net_yearly = current_strategy.get("net_optimized_yearly_return", 0.0) if current_strategy else 0.0

    candidates = []

    for card_name, card_info in CARDS_DATABASE.items():
        if card_name in current_wallet:
            continue

        fee = card_info.get("annual_fee", 0)
        if max_fee is not None and fee > max_fee:
            continue

        # Filter by lifestyle
        tier = card_info.get("tier", "")
        ctype = card_info.get("type", "")

        if lifestyle_filter == "Lifetime Free" and fee > 0:
            continue
        elif lifestyle_filter == "Pure Cashback" and ctype != "cashback":
            continue
        elif lifestyle_filter == "Travel & Lounges" and "Travel" not in tier and "Super Premium" not in tier and card_info.get("domestic_lounges") == "None":
            continue
        elif lifestyle_filter == "Super Premium" and "Super Premium" not in tier:
            continue

        # Simulate adding this card to current wallet
        simulated_wallet = list(current_wallet) + [card_name]
        simulated_strategy = find_optimal_wallet_strategy(simulated_wallet, monthly_spend)

        if "error" in simulated_strategy:
            continue

        new_net_yearly = simulated_strategy.get("net_optimized_yearly_return", 0.0)
        incremental_profit = round(new_net_yearly - current_net_yearly, 2)

        # Identify which categories this card would take over
        conquered_categories = []
        for cat, assign in simulated_strategy.get("category_assignments", {}).items():
            if assign["assigned_card"] == card_name:
                conquered_categories.append({
                    "category": cat,
                    "new_rate": assign["effective_rate"],
                    "monthly_gain": assign["monthly_reward"]
                })

        candidates.append({
            "card": card_name,
            "bank": card_info.get("bank", "Bank"),
            "tier": tier,
            "type": ctype,
            "annual_fee": fee,
            "fee_waiver_spend": card_info.get("fee_waiver_spend", 0),
            "forex_markup": card_info.get("forex_markup", 3.5),
            "domestic_lounges": card_info.get("domestic_lounges", "None"),
            "intl_lounges": card_info.get("intl_lounges", "None"),
            "incremental_annual_profit": incremental_profit,
            "simulated_total_net": new_net_yearly,
            "conquered_categories": conquered_categories,
            "welcome_gift": card_info.get("welcome_gift", ""),
            "summary": card_info.get("summary", ""),
            "apply_url": card_info.get("apply_url", "")
        })

    # Sort by incremental annual profit descending, then lowest fee
    candidates.sort(key=lambda x: (-x["incremental_annual_profit"], x["annual_fee"]))
    return candidates
