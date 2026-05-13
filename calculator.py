# =====================================================================
# 🧮 REWARD CALCULATION ENGINE
# =====================================================================

from cards_data import CARD_DATA


def get_reward_rate(card_name: str, category: str, vendor: str = None) -> tuple:
    """
    Returns (rate, source_label).
    Priority: vendor_rewards → category rewards → "Other" → 0
    """
    card = CARD_DATA.get(card_name)
    if not card:
        return 0.0, "unknown"

    # 1) Vendor-specific rate
    if vendor:
        vendor_rate = card.get("vendor_rewards", {}).get(vendor)
        if vendor_rate is not None:
            return vendor_rate, f"🏪 {vendor}"

    # 2) Category rate
    cat_rate = card.get("rewards", {}).get(category)
    if cat_rate is not None:
        return cat_rate, f"📂 {category}"

    # 3) Fallback to "Other"
    return card.get("rewards", {}).get("Other", 0), "📂 Other"


def calculate_reward(amount: float, rate: float) -> float:
    """Calculate reward value in ₹."""
    return round(amount * (rate / 100), 2)


def compare_cards(card_names: list, category: str, amount: float, vendor: str = None) -> dict:
    """
    Compare multiple cards. Returns sorted results + best card.
    Tie-break: higher reward → lower annual fee.
    """
    results = []

    for card_name in card_names:
        card_info = CARD_DATA.get(card_name, {})
        rate, source = get_reward_rate(card_name, category, vendor)
        reward = calculate_reward(amount, rate)

        results.append({
            "card": card_name,
            "rate": rate,
            "reward": reward,
            "source": source,
            "type": card_info.get("type", "cashback"),
            "annual_fee": card_info.get("annual_fee", 0),
            "network": card_info.get("network", "N/A"),
        })

    # Sort: highest reward first, then lowest fee
    results.sort(key=lambda x: (-x["reward"], x["annual_fee"]))

    best = results[0] if results else None

    return {
        "results": results,
        "best_card": best["card"] if best else None,
        "best_reward": best["reward"] if best else 0,
    }


def compare_monthly(card_names: list, monthly_spend: dict) -> dict:
    """
    Compare cards across entire monthly spending profile.
    monthly_spend = {"Dining": 5000, "Grocery": 8000, ...}
    Returns sorted results with category-wise breakdown.
    """
    results = []

    for card_name in card_names:
        card_info = CARD_DATA.get(card_name, {})
        total_reward = 0
        breakdown = {}

        for cat, amt in monthly_spend.items():
            if amt > 0:
                rate, source = get_reward_rate(card_name, cat)
                reward = calculate_reward(amt, rate)
                total_reward += reward
                breakdown[cat] = {
                    "amount": amt,
                    "rate": rate,
                    "reward": reward,
                }

        results.append({
            "card": card_name,
            "total_reward": round(total_reward, 2),
            "yearly_reward": round(total_reward * 12, 2),
            "annual_fee": card_info.get("annual_fee", 0),
            "net_yearly": round((total_reward * 12) - card_info.get("annual_fee", 0), 2),
            "type": card_info.get("type", "cashback"),
            "breakdown": breakdown,
        })

    results.sort(key=lambda x: (-x["net_yearly"], x["annual_fee"]))

    best = results[0] if results else None

    return {
        "results": results,
        "best_card": best["card"] if best else None,
        "best_net_yearly": best["net_yearly"] if best else 0,
    }


def generate_smart_tips(results: list, best_card: str, amount: float,
                        category: str, vendor: str = None) -> list:
    """Generate intelligent tips from comparison data — no LLM needed."""
    tips = []

    best_data = next((r for r in results if r["card"] == best_card), None)
    if not best_data:
        return tips

    worst_data = results[-1] if len(results) > 1 else None

    # Tip 1: Savings vs worst card
    if worst_data and worst_data["card"] != best_card:
        savings = best_data["reward"] - worst_data["reward"]
        if savings > 0:
            tips.append({
                "icon": "💰",
                "title": "You're Saving Money",
                "text": (
                    f"Using **{best_card}** instead of **{worst_data['card']}** "
                    f"saves you **₹{savings:.2f}** on this single purchase!"
                )
            })

    # Tip 2: Annual fee break-even
    if best_data["annual_fee"] > 0 and best_data["rate"] > 0:
        break_even = best_data["annual_fee"] / (best_data["rate"] / 100)
        tips.append({
            "icon": "⚠️",
            "title": "Fee Break-Even",
            "text": (
                f"**{best_card}** has ₹{best_data['annual_fee']}/yr fee. "
                f"Spend **₹{break_even:,.0f}/yr** in this category to break even."
            )
        })

    # Tip 3: Zero-fee alternative
    free_cards = [r for r in results if r["annual_fee"] == 0 and r["reward"] > 0]
    if free_cards and best_data["annual_fee"] > 0:
        best_free = free_cards[0]
        tips.append({
            "icon": "🆓",
            "title": "Zero-Fee Option",
            "text": (
                f"Want no annual fee? **{best_free['card']}** earns "
                f"₹{best_free['reward']:.2f} with ₹0 fee."
            )
        })

    # Tip 4: Yearly projection
    yearly = best_data["reward"] * 12
    tips.append({
        "icon": "📈",
        "title": "Yearly Projection",
        "text": (
            f"Spending ₹{amount:,}/month here with **{best_card}** earns "
            f"**₹{yearly:,.2f}/year** in rewards!"
        )
    })

    # Tip 5: Vendor nudge
    if not vendor:
        tips.append({
            "icon": "🏪",
            "title": "Pro Tip",
            "text": (
                "Select a **specific vendor** above — some cards offer "
                "significantly higher rates at partner merchants!"
            )
        })

    return tips