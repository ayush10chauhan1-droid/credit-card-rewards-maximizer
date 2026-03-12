def find_best_card(cards, category, amount):

    best_card = None
    max_reward = 0
    reward_details = {}

    for card, rewards in cards.items():
        rate = rewards.get(category, rewards["other"])
        reward = amount * rate
        reward_details[card] = reward

        if reward > max_reward:
            max_reward = reward
            best_card = card

    return best_card, reward_details
