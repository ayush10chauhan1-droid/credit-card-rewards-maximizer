# =====================================================================
# 👛 SWIPESMART WALLET OPTIMIZATION ENGINE
# Solves the Multi-Card Routing Problem: "Which card in my wallet
# should I swipe for each category to maximize aggregate returns?"
# =====================================================================

from typing import Dict, List, Any
from data.cards_db import CARDS_DATABASE
from engine.calculator import get_reward_rate, get_point_multiplier, apply_monthly_cap


def find_optimal_wallet_strategy(
    wallet_cards: List[str],
    monthly_spend: Dict[str, float],
    valuation_mode: str = "default"
) -> Dict[str, Any]:
    """
    Given a user's wallet of credit cards and their monthly category spending,
    determine the mathematically optimal card assignment for every category.
    """
    if not wallet_cards:
        return {"error": "Please select at least one card in your wallet."}

    valid_cards = [c for c in wallet_cards if c in CARDS_DATABASE]
    if not valid_cards:
        return {"error": "No valid cards selected."}

    total_monthly_spend = sum(monthly_spend.values())
    total_annual_spend = total_monthly_spend * 12.0

    category_assignments = {}
    total_optimized_monthly_reward = 0.0
    card_usage_distribution = {c: {"spend": 0.0, "reward": 0.0, "categories": []} for c in valid_cards}

    # For each category, evaluate all cards in wallet and pick the one with highest net reward in ₹
    for category, spend in monthly_spend.items():
        if spend <= 0:
            continue

        best_card_for_cat = None
        highest_cat_reward = -1.0
        best_cat_rate = 0.0
        best_source = ""
        best_cap_note = None

        card_options = []

        for card_name in valid_cards:
            card_info = CARDS_DATABASE[card_name]
            multiplier = get_point_multiplier(card_info, valuation_mode)
            rate, source = get_reward_rate(card_name, category)
            raw_reward = (spend * (rate / 100.0)) * multiplier
            capped_reward, cap_note = apply_monthly_cap(card_name, category, None, raw_reward)

            card_options.append({
                "card": card_name,
                "rate": rate,
                "reward": round(capped_reward, 2),
                "source": source
            })

            if capped_reward > highest_cat_reward:
                highest_cat_reward = capped_reward
                best_card_for_cat = card_name
                best_cat_rate = rate
                best_source = source
                best_cap_note = cap_note

        # Record assignment
        category_assignments[category] = {
            "spend": spend,
            "assigned_card": best_card_for_cat,
            "effective_rate": best_cat_rate,
            "monthly_reward": round(highest_cat_reward, 2),
            "yearly_reward": round(highest_cat_reward * 12, 2),
            "source": best_source,
            "cap_note": best_cap_note,
            "all_options": sorted(card_options, key=lambda x: -x["reward"])
        }

        total_optimized_monthly_reward += highest_cat_reward
        card_usage_distribution[best_card_for_cat]["spend"] += spend
        card_usage_distribution[best_card_for_cat]["reward"] += highest_cat_reward
        card_usage_distribution[best_card_for_cat]["categories"].append(category)

    total_optimized_yearly_reward = round(total_optimized_monthly_reward * 12.0, 2)

    # Calculate total wallet annual fees & waivers
    total_annual_fees = 0
    total_effective_fees = 0
    card_fee_details = []

    for card_name in valid_cards:
        info = CARDS_DATABASE[card_name]
        fee = info.get("annual_fee", 0)
        waiver_spend = info.get("fee_waiver_spend", 0)

        # In a multi-card wallet, spend routed to this card counts toward waiver
        routed_annual_spend = card_usage_distribution[card_name]["spend"] * 12.0
        waived = (waiver_spend > 0 and routed_annual_spend >= waiver_spend)
        effective_fee = 0 if waived else fee

        total_annual_fees += fee
        total_effective_fees += effective_fee

        card_fee_details.append({
            "card": card_name,
            "fee": fee,
            "waiver_spend": waiver_spend,
            "routed_annual_spend": routed_annual_spend,
            "waived": waived,
            "effective_fee": effective_fee
        })

    net_optimized_yearly_return = round(total_optimized_yearly_reward - total_effective_fees, 2)
    optimized_roi_pct = round((net_optimized_yearly_return / total_annual_spend * 100.0), 2) if total_annual_spend > 0 else 0.0

    # Benchmark 1: What if user swiped ONLY their single best card everywhere?
    single_card_benchmarks = []
    for card_name in valid_cards:
        single_card_monthly_reward = 0.0
        for cat, spend in monthly_spend.items():
            if spend <= 0:
                continue
            card_info = CARDS_DATABASE[card_name]
            multiplier = get_point_multiplier(card_info, valuation_mode)
            rate, _ = get_reward_rate(card_name, cat)
            raw = (spend * (rate / 100.0)) * multiplier
            capped, _ = apply_monthly_cap(card_name, cat, None, raw)
            single_card_monthly_reward += capped

        single_card_yearly_gross = single_card_monthly_reward * 12.0
        fee = CARDS_DATABASE[card_name].get("annual_fee", 0)
        waiver = CARDS_DATABASE[card_name].get("fee_waiver_spend", 0)
        waived = (waiver > 0 and total_annual_spend >= waiver)
        eff_fee = 0 if waived else fee
        single_net = single_card_yearly_gross - eff_fee

        single_card_benchmarks.append({
            "card": card_name,
            "net_yearly": round(single_net, 2)
        })

    single_card_benchmarks.sort(key=lambda x: -x["net_yearly"])
    best_single_card = single_card_benchmarks[0] if single_card_benchmarks else {"card": "None", "net_yearly": 0}

    # Benchmark 2: Baseline 1% flat card
    baseline_1pct_yearly = round((total_annual_spend * 0.01), 2)

    # Synergy Bonus
    synergy_vs_single = round(net_optimized_yearly_return - best_single_card["net_yearly"], 2)
    synergy_vs_baseline = round(net_optimized_yearly_return - baseline_1pct_yearly, 2)

    return {
        "wallet_cards": valid_cards,
        "total_monthly_spend": total_monthly_spend,
        "total_annual_spend": total_annual_spend,
        "category_assignments": category_assignments,
        "total_optimized_monthly_reward": round(total_optimized_monthly_reward, 2),
        "total_optimized_yearly_reward": total_optimized_yearly_reward,
        "total_annual_fees": total_annual_fees,
        "total_effective_fees": total_effective_fees,
        "card_fee_details": card_fee_details,
        "net_optimized_yearly_return": net_optimized_yearly_return,
        "optimized_roi_pct": optimized_roi_pct,
        "card_usage_distribution": card_usage_distribution,
        "best_single_card": best_single_card,
        "baseline_1pct_yearly": baseline_1pct_yearly,
        "synergy_vs_single": max(0.0, synergy_vs_single),
        "synergy_vs_baseline": max(0.0, synergy_vs_baseline)
    }
