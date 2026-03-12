from src.card_manager import load_cards
from src.reward_calculator import find_best_card

category = input("Enter purchase category (dining/grocery/travel/other): ").lower()
amount = float(input("Enter purchase amount: "))

cards = load_cards("cards.json")

best_card, reward_details = find_best_card(cards, category, amount)

print("\nReward Calculation:\n")

for card, reward in reward_details.items():
    print(f"{card} → ₹{reward}")

print("\nBest card to use:", best_card)
