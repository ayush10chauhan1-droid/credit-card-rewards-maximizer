from src.reward_calculator import find_best_card

def test_best_card():
    cards = {
        "Card A": {"dining":0.05,"other":0.01},
        "Card B": {"dining":0.02,"other":0.01}
    }

    best_card, _ = find_best_card(cards, "dining", 1000)

    assert best_card == "Card A"
