# =========================================
# 🇮🇳 REALISTIC VENDOR DATABASE (2026)
# =========================================
# Data sourced from actual vendor websites and offers

VENDOR_DATA = {
    
    # ================= FOOD DELIVERY =================
    
    "Swiggy": {
        "category": "Food Delivery",
        "base_cashback": 10,  # 10% on Swiggy HDFC card
        "max_cashback": 1500,  # Monthly cap
        "icon": "🍔",
        "description": "10% cashback on Swiggy platforms (Food, Instamart, Dine Out)",
        "min_order": 100,
        "popular_payment": "HDFC Credit Card"
    },
    
    "Zomato": {
        "category": "Food Delivery",
        "base_cashback": 5,  # Average 5% on dining with cards
        "max_cashback": 1000,
        "icon": "🍕",
        "description": "5% cashback on food delivery and dining",
        "min_order": 100,
        "popular_payment": "ICICI Card"
    },
    
    "Uber Eats": {
        "category": "Food Delivery",
        "base_cashback": 4,  # 4% base on select dining
        "max_cashback": 800,
        "icon": "🚗",
        "description": "4% cashback on food delivery (Uber One membership adds 10% off)",
        "min_order": 200,
        "popular_payment": "Credit Card"
    },
    
    # ================= ONLINE SHOPPING =================
    
    "Amazon": {
        "category": "Shopping",
        "base_cashback": 5,  # 5% for Prime members
        "max_cashback": 2000,
        "icon": "📦",
        "description": "5% cashback for Amazon Prime members with cards",
        "min_order": 500,
        "popular_payment": "Amazon Pay ICICI"
    },
    
    "Flipkart": {
        "category": "Shopping",
        "base_cashback": 5,  # 5% on Flipkart Axis card
        "max_cashback": 4000,  # Quarterly cap
        "icon": "🛍️",
        "description": "5% cashback + 7.5% on Myntra",
        "min_order": 500,
        "popular_payment": "Flipkart Axis Card"
    },
    
    "Myntra": {
        "category": "Shopping",
        "base_cashback": 7.5,  # 7.5% with Flipkart Axis
        "max_cashback": 3000,
        "icon": "👗",
        "description": "7.5% cashback on fashion with premium cards",
        "min_order": 1000,
        "popular_payment": "Flipkart Axis Card"
    },
    
    # ================= TRAVEL & BOOKINGS =================
    
    "MakeMyTrip": {
        "category": "Travel",
        "base_cashback": 8,  # 8% on travel with premium cards
        "max_cashback": 5000,
        "icon": "✈️",
        "description": "8% cashback on flights, hotels, and packages",
        "min_order": 5000,
        "popular_payment": "HDFC Diners / Axis Magnus"
    },
    
    "Cleartrip": {
        "category": "Travel",
        "base_cashback": 5,  # 5% with Flipkart Axis
        "max_cashback": 2000,
        "icon": "🏨",
        "description": "5% cashback on hotel and flight bookings",
        "min_order": 3000,
        "popular_payment": "Flipkart Axis Card"
    },
    
    # ================= GROCERIES & ESSENTIALS =================
    
    "Blinkit": {
        "category": "Grocery",
        "base_cashback": 3,  # 3% average
        "max_cashback": 500,
        "icon": "🥕",
        "description": "Quick 10-minute grocery delivery with minor cashback",
        "min_order": 200,
        "popular_payment": "Digital Wallets"
    },
    
    "BigBasket": {
        "category": "Grocery",
        "base_cashback": 5,  # 5% with select cards
        "max_cashback": 1000,
        "icon": "🛒",
        "description": "5% cashback on grocery orders",
        "min_order": 500,
        "popular_payment": "Credit Cards"
    },
    
    # ================= ENTERTAINMENT =================
    
    "BookMyShow": {
        "category": "Entertainment",
        "base_cashback": 10,  # Up to 10% on select cards
        "max_cashback": 1500,
        "icon": "🎬",
        "description": "10% instant discount on movie tickets with premium cards",
        "min_order": 400,
        "popular_payment": "HDFC/ICICI Cards"
    },
    
    "Netflix": {
        "category": "Entertainment",
        "base_cashback": 2,  # 2% on subscriptions
        "max_cashback": 100,
        "icon": "📺",
        "description": "Minimal cashback - primarily for subscription bundling",
        "min_order": 199,
        "popular_payment": "Any Card"
    },
    
    # ================= RIDE SHARING =================
    
    "Uber": {
        "category": "Travel/Rides",
        "base_cashback": 4,  # 4% on select cards
        "max_cashback": 500,
        "icon": "🚗",
        "description": "4% cashback on rides (more with Uber One)",
        "min_order": 100,
        "popular_payment": "Credit Cards"
    },
    
    "Ola": {
        "category": "Travel/Rides",
        "base_cashback": 5,  # 5% average
        "max_cashback": 600,
        "icon": "🚕",
        "description": "5% cashback on rides and OLA Money",
        "min_order": 100,
        "popular_payment": "Credit Cards"
    },
    
}

# =========================================
# VENDOR RANKINGS BY CATEGORY
# =========================================

VENDOR_CATEGORIES = {
    "Food Delivery": ["Swiggy", "Zomato", "Uber Eats"],
    "Shopping": ["Amazon", "Flipkart", "Myntra"],
    "Travel": ["MakeMyTrip", "Cleartrip"],
    "Grocery": ["BigBasket", "Blinkit"],
    "Entertainment": ["BookMyShow", "Netflix"],
    "Rides": ["Uber", "Ola"]
}