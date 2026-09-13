# Backward-compatible proxy for data/cards_db.py
from data.cards_db import (
    CARDS_DATABASE,
    CARD_DATA,
    POPULAR_CARDS,
    CATEGORIES,
    CARD_TIERS,
    CARD_ISSUERS
)

# Merchant to Category mapping
VENDORS = {
    "Online Shopping": [
        "Amazon", "Flipkart", "Myntra", "Ajio", "Nykaa", "Croma",
        "Reliance Digital", "Tata CLiQ"
    ],
    "Dining": [
        "Swiggy", "Zomato", "EatSure", "Dominos", "McDonalds"
    ],
    "Grocery": [
        "Blinkit", "BigBasket", "Zepto", "JioMart", "DMart"
    ],
    "Travel": [
        "SmartBuy Flights", "SmartBuy Hotels", "MakeMyTrip", "Cleartrip",
        "Goibibo", "Yatra", "Air India", "IndiGo", "Uber", "Ola"
    ],
    "Movies/Entertainment": [
        "BookMyShow", "PVR", "Inox", "Netflix", "Hotstar", "Sony LIV", "Spotify"
    ],
    "Utilities": [
        "Google Pay Utilities", "Electricity", "Water", "Gas", "Broadband",
        "Mobile Recharge", "Airtel Mobile/Broadband"
    ],
    "Fuel": [
        "BPCL Fuel", "HP Fuel", "Indian Oil", "Bharatgas"
    ],
    "International": [
        "International Travel", "Overseas Retail", "Foreign Online Spends"
    ],
    "UPI": [
        "RuPay UPI Merchants", "Offline QR Spends"
    ],
    "Other": [
        "General Offline", "Hospitality", "Departmental Stores"
    ]
}