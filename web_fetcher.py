import requests
from bs4 import BeautifulSoup

# Official card URLs
CARD_URLS = {
    "Chase Sapphire Preferred": "https://creditcards.chase.com/rewards-credit-cards/sapphire/preferred",
    "Chase Sapphire Reserve": "https://creditcards.chase.com/rewards-credit-cards/sapphire/reserve",
    "Chase Freedom Unlimited": "https://creditcards.chase.com/cash-back-credit-cards/freedom/unlimited",
    "Chase Freedom Flex": "https://creditcards.chase.com/cash-back-credit-cards/freedom/flex",
    "American Express Gold": "https://www.americanexpress.com/us/credit-cards/card/gold-card/",
    "Capital One Venture X": "https://www.capitalone.com/credit-cards/venture-x/"
}

def fetch_card_data(card_name):
    url = CARD_URLS.get(card_name)

    if not url:
        return f"No official URL found for {card_name}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code != 200:
            return f"Failed to fetch {card_name}"

        soup = BeautifulSoup(response.text, "html.parser")

        # Remove scripts and styles
        for tag in soup(["script", "style", "noscript"]):
            tag.decompose()

        text = soup.get_text(separator="\n")
        clean_text = "\n".join(
            line.strip() for line in text.splitlines() if line.strip()
        )

        return clean_text

    except Exception as e:
        return f"Error fetching {card_name}: {str(e)}"


def fetch_multiple_cards(card_list):
    combined = ""

    for card in card_list:
        combined += f"\n\n===== {card} =====\n"
        combined += fetch_card_data(card)

    return combined