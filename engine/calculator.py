# =====================================================================
# 🧮 SWIPESMART ENTERPRISE CALCULATION ENGINE
# Handles realistic reward capping, point valuation, milestone perks,
# spend-based fee waivers, and true net annual ROI.
# =====================================================================

from typing import Dict, List, Optional, Tuple, Any
from data.cards_db import CARDS_DATABASE, CATEGORIES


def get_reward_rate(card_name: str, category: str, vendor: Optional[str] = None) -> Tuple[float, str]:
    """
    Find reward rate for a given card, category, and optional vendor.
    Priority: vendor_rewards → category rewards → "Other" → 0.0%
    """
    card = CARDS_DATABASE.get(card_name)
    if not card:
        return 0.0, "Unknown Card"

    # 1. Vendor specific rate
    if vendor:
        vendor_rates = card.get("vendor_rewards", {})
        if vendor in vendor_rates:
            return float(vendor_rates[vendor]), f"🏪 {vendor} Partner Rate"

    # 2. Category rate
    cat_rates = card.get("rewards", {})
    if category in cat_rates:
        return float(cat_rates[category]), f"📂 {category}"

    # 3. Fallback to "Other"
    other_rate = cat_rates.get("Other", 1.0)
    return float(other_rate), "📂 Standard Spend Rate"


def get_point_multiplier(card_info: Dict[str, Any], valuation_mode: str = "default") -> float:
    """
    Get conversion rate of 1 reward point into ₹.
    For pure cashback cards, multiplier is always 1.00.
    """
    if card_info.get("type") == "cashback":
        return 1.00

    valuations = card_info.get("point_valuation", {})
    if valuation_mode in valuations:
        return float(valuations[valuation_mode])
    return float(valuations.get("default", 1.00))


def calculate_reward(amount: float, rate: float) -> float:
    """Calculate raw reward value in ₹ before card-specific capping."""
    return round(amount * (rate / 100.0), 2)


def apply_monthly_cap(card_name: str, category: str, vendor: Optional[str], raw_reward: float) -> Tuple[float, Optional[str]]:
    """
    Apply card-specific monthly capping rules to ensure realistic numbers.
    Returns (capped_reward, cap_notice_str).
    """
    card = CARDS_DATABASE.get(card_name, {})
    caps = card.get("caps", {})

    # SBI Cashback Card: Online cap ₹5,000 / month
    if card_name == "SBI Cashback Card":
        online_cap = caps.get("online_monthly_cashback", 5000)
        if raw_reward > online_cap:
            return online_cap, f"Capped at ₹{online_cap:,}/mo on 5% online spends"

    # Swiggy HDFC: ₹1,500 Swiggy cap, ₹1,500 online partner cap
    elif card_name == "Swiggy HDFC":
        if vendor == "Swiggy" or category == "Dining":
            swiggy_cap = caps.get("swiggy_monthly_cashback", 1500)
            if raw_reward > swiggy_cap:
                return swiggy_cap, f"Capped at ₹{swiggy_cap:,}/mo on Swiggy"
        elif category in ["Online Shopping", "Grocery"]:
            online_cap = caps.get("online_monthly_cashback", 1500)
            if raw_reward > online_cap:
                return online_cap, f"Capped at ₹{online_cap:,}/mo on 5% merchants"

    # HDFC Millennia: ₹1,000 partner cap
    elif card_name == "HDFC Millennia":
        partner_cap = caps.get("partner_monthly_cashback", 1000)
        if raw_reward > partner_cap:
            return partner_cap, f"Capped at ₹{partner_cap:,}/mo on 5% partner spends"

    # Axis Ace: ₹500 utility cap, ₹500 dining cap
    elif card_name == "Axis Ace":
        if category == "Utilities":
            u_cap = caps.get("utility_monthly_cashback", 500)
            if raw_reward > u_cap:
                return u_cap, f"Capped at ₹{u_cap:,}/mo on Google Pay utilities"
        elif category == "Dining":
            d_cap = caps.get("dining_monthly_cashback", 500)
            if raw_reward > d_cap:
                return d_cap, f"Capped at ₹{d_cap:,}/mo on Swiggy/Zomato"

    # Airtel Axis: ₹250 Airtel, ₹250 Utility, ₹500 Food/Grocery
    elif card_name == "Airtel Axis":
        if vendor == "Airtel Mobile/Broadband":
            a_cap = caps.get("airtel_monthly_cashback", 250)
            if raw_reward > a_cap:
                return a_cap, f"Capped at ₹{a_cap:,}/mo on Airtel bills"
        elif category == "Utilities":
            u_cap = caps.get("utility_monthly_cashback", 250)
            if raw_reward > u_cap:
                return u_cap, f"Capped at ₹{u_cap:,}/mo on utility bills"
        elif category in ["Dining", "Grocery"]:
            f_cap = caps.get("food_grocery_monthly_cashback", 500)
            if raw_reward > f_cap:
                return f_cap, f"Capped at ₹{f_cap:,}/mo on Swiggy/Zomato/BigBasket"

    # SBI BPCL Octane: ₹2,500 fuel points cap
    elif card_name == "SBI BPCL Octane" and category == "Fuel":
        fuel_cap = caps.get("fuel_monthly_points", 2500) * 0.25
        if raw_reward > fuel_cap:
            return fuel_cap, f"Capped at ₹{fuel_cap:,.0f}/mo on BPCL fuel"

    return raw_reward, None


def compare_cards(
    card_names: List[str],
    category: str,
    amount: float,
    vendor: Optional[str] = None,
    valuation_mode: str = "default"
) -> Dict[str, Any]:
    """
    Compare multiple credit cards for a single transaction.
    Returns sorted cards from highest reward to lowest, with tiebreaker on fee.
    """
    results = []

    for name in card_names:
        card_info = CARDS_DATABASE.get(name)
        if not card_info:
            continue

        rate, source = get_reward_rate(name, category, vendor)
        raw_reward = calculate_reward(amount, rate)

        # Apply point valuation
        multiplier = get_point_multiplier(card_info, valuation_mode)
        reward_inr = round(raw_reward * multiplier, 2)

        # Check for single purchase capping indicator
        capped_reward, cap_note = apply_monthly_cap(name, category, vendor, reward_inr)

        annual_fee = card_info.get("annual_fee", 0)
        fee_waiver = card_info.get("fee_waiver_spend", 0)

        # Break even spend calculation
        break_even_spend = 0
        if annual_fee > 0 and rate > 0:
            break_even_spend = round(annual_fee / ((rate * multiplier) / 100.0))

        results.append({
            "card": name,
            "bank": card_info.get("bank", "Bank"),
            "rate": rate,
            "reward": capped_reward,
            "source": source,
            "cap_note": cap_note,
            "type": card_info.get("type", "cashback"),
            "tier": card_info.get("tier", "Standard"),
            "network": card_info.get("network", "Visa"),
            "annual_fee": annual_fee,
            "fee_waiver_spend": fee_waiver,
            "break_even_spend": break_even_spend,
            "forex_markup": card_info.get("forex_markup", 3.5),
            "domestic_lounges": card_info.get("domestic_lounges", "None"),
            "summary": card_info.get("summary", ""),
            "apply_url": card_info.get("apply_url", "")
        })

    # Sort: highest reward first, then lowest annual fee
    results.sort(key=lambda x: (-x["reward"], x["annual_fee"]))
    best = results[0] if results else None

    return {
        "results": results,
        "best_card": best["card"] if best else None,
        "best_reward": best["reward"] if best else 0,
        "runner_up": results[1]["card"] if len(results) > 1 else None
    }


def calculate_card_annual_net(
    card_name: str,
    monthly_spend: Dict[str, float],
    valuation_mode: str = "default"
) -> Dict[str, Any]:
    """
    Calculate annual net return for a single card across monthly spending habits.
    Includes:
    - Category-by-category reward with capping
    - Milestone perk evaluation
    - Spend-based fee waiver qualification
    - Net Annual Value = (Gross Yearly Rewards + Milestone Perks) - (Annual Fee if not waived)
    - Effective Annual ROI %
    """
    card_info = CARDS_DATABASE.get(card_name, {})
    multiplier = get_point_multiplier(card_info, valuation_mode)

    total_monthly_spend = sum(monthly_spend.values())
    total_annual_spend = total_monthly_spend * 12.0

    monthly_reward = 0.0
    breakdown = {}

    for cat, amt in monthly_spend.items():
        if amt <= 0:
            continue

        rate, source = get_reward_rate(card_name, cat)
        raw_cat_reward = (amt * (rate / 100.0)) * multiplier
        capped_cat_reward, cap_note = apply_monthly_cap(card_name, cat, None, raw_cat_reward)

        monthly_reward += capped_cat_reward
        breakdown[cat] = {
            "amount": amt,
            "rate": rate,
            "monthly_reward": round(capped_cat_reward, 2),
            "yearly_reward": round(capped_cat_reward * 12, 2),
            "cap_note": cap_note
        }

    yearly_gross_reward = round(monthly_reward * 12.0, 2)

    # Fee waiver check
    annual_fee = card_info.get("annual_fee", 0)
    fee_waiver_spend = card_info.get("fee_waiver_spend", 0)
    fee_waived = (fee_waiver_spend > 0 and total_annual_spend >= fee_waiver_spend)
    effective_fee = 0 if fee_waived else annual_fee

    # Milestone benefits
    milestone_value = 0
    milestones_achieved = []
    for ms in card_info.get("milestones", []):
        if total_annual_spend >= ms.get("spend", 99999999):
            # Don't double count fee waiver in milestone value
            if "Fee waiver" not in ms.get("description", ""):
                milestone_value += ms.get("benefit_value", 0)
            milestones_achieved.append(ms.get("description"))

    net_yearly_return = round(yearly_gross_reward + milestone_value - effective_fee, 2)
    roi_pct = round((net_yearly_return / total_annual_spend * 100.0), 2) if total_annual_spend > 0 else 0.0

    return {
        "card": card_name,
        "bank": card_info.get("bank", "Bank"),
        "tier": card_info.get("tier", "Standard"),
        "type": card_info.get("type", "cashback"),
        "annual_fee": annual_fee,
        "fee_waived": fee_waived,
        "effective_fee": effective_fee,
        "fee_waiver_spend": fee_waiver_spend,
        "monthly_reward": round(monthly_reward, 2),
        "yearly_gross_reward": yearly_gross_reward,
        "milestone_value": milestone_value,
        "milestones_achieved": milestones_achieved,
        "net_yearly_return": net_yearly_return,
        "roi_pct": roi_pct,
        "breakdown": breakdown,
        "domestic_lounges": card_info.get("domestic_lounges", "None"),
        "intl_lounges": card_info.get("intl_lounges", "None"),
        "forex_markup": card_info.get("forex_markup", 3.5),
        "summary": card_info.get("summary", "")
    }


def compare_monthly(
    card_names: List[str],
    monthly_spend: Dict[str, float],
    valuation_mode: str = "default"
) -> Dict[str, Any]:
    """
    Compare multiple cards for an entire monthly spending profile.
    Sorts by Net Yearly Return descending.
    """
    results = [calculate_card_annual_net(c, monthly_spend, valuation_mode) for c in card_names if c in CARDS_DATABASE]
    results.sort(key=lambda x: (-x["net_yearly_return"], x["effective_fee"]))

    best = results[0] if results else None
    return {
        "results": results,
        "best_card": best["card"] if best else None,
        "best_net_yearly": best["net_yearly_return"] if best else 0.0
    }


def generate_smart_tips(
    results: List[Dict[str, Any]],
    best_card: str,
    amount: float,
    category: str,
    vendor: Optional[str] = None
) -> List[Dict[str, str]]:
    """Generate rule-based financial advice and actionable insights."""
    tips = []
    best_data = next((r for r in results if r["card"] == best_card), None)
    if not best_data:
        return tips

    worst_data = results[-1] if len(results) > 1 else None

    # Tip 1: Opportunity cost vs worst card
    if worst_data and worst_data["card"] != best_card:
        diff = best_data["reward"] - worst_data["reward"]
        if diff > 0:
            tips.append({
                "icon": "💰",
                "title": "Instant Swipe Alpha",
                "text": f"Swiping **{best_card}** instead of **{worst_data['card']}** yields an extra **₹{diff:.2f}** in your pocket on this single swipe."
            })

    # Tip 2: Fee break-even warning
    if best_data["annual_fee"] > 0 and best_data["break_even_spend"] > 0:
        tips.append({
            "icon": "⚖️",
            "title": "Annual Fee Break-Even",
            "text": f"**{best_card}** carries a ₹{best_data['annual_fee']:,}/yr annual fee. You need to spend at least **₹{best_data['break_even_spend']:,}/year** in this category to offset the card fee."
        })

    # Tip 3: Zero-fee alternative
    free_cards = [r for r in results if r["annual_fee"] == 0 and r["reward"] > 0 and r["card"] != best_card]
    if free_cards and best_data["annual_fee"] > 0:
        best_free = free_cards[0]
        tips.append({
            "icon": "🆓",
            "title": "Lifetime Free Alternative",
            "text": f"Prefer zero annual commitment? **{best_free['card']}** earns **₹{best_free['reward']:.2f}** with ₹0 annual maintenance fee."
        })

    # Tip 4: Annual projection
    yearly_val = best_data["reward"] * 12
    tips.append({
        "icon": "📈",
        "title": "Compounded Annual Projection",
        "text": f"Consistently spending ₹{amount:,.0f}/month at this rate on **{best_card}** yields **₹{yearly_val:,.2f}** in annual rewards."
    })

    # Tip 5: Specific vendor nudge
    if not vendor:
        tips.append({
            "icon": "🏪",
            "title": "Merchant Multiplier Tip",
            "text": "Selecting a specific merchant (e.g. Swiggy, Amazon, SmartBuy) frequently unlocks 2x to 5x higher accelerated rewards on partner cards."
        })

    return tips
