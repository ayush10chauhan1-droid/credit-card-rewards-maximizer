# =====================================================================
# 🇮🇳 COMPLETE INDIAN CREDIT CARD DATABASE — WITH VENDOR REWARDS
# =====================================================================

CARD_DATA = {

    # ================= HDFC =================

    "HDFC Millennia": {
        "type": "cashback",
        "annual_fee": 1000,
        "network": "Visa",
        "rewards": {
            "Online Shopping": 5,
            "Dining": 1,
            "Grocery": 1,
            "Fuel": 1,
            "Other": 1
        },
        "vendor_rewards": {
            "Amazon": 5, "Flipkart": 5, "Myntra": 5,
            "Swiggy": 5, "Zomato": 5,
            "BookMyShow": 5, "Netflix": 5, "Hotstar": 5,
        }
    },

    "HDFC Regalia": {
        "type": "points",
        "annual_fee": 2500,
        "network": "Visa",
        "rewards": {
            "Dining": 4,
            "Travel": 4,
            "International": 4,
            "Other": 1
        },
        "vendor_rewards": {
            "MakeMyTrip": 5, "Goibibo": 5, "Cleartrip": 5,
            "Zomato": 4, "Swiggy": 4,
        }
    },

    "HDFC Diners Black": {
        "type": "points",
        "annual_fee": 10000,
        "network": "Diners Club",
        "rewards": {
            "Dining": 10,
            "Travel": 10,
            "International": 10,
            "Other": 3.3
        },
        "vendor_rewards": {
            "Swiggy": 10, "Zomato": 10,
            "MakeMyTrip": 10, "Goibibo": 10,
            "BookMyShow": 10, "Cleartrip": 10, "Yatra": 10,
        }
    },

    # ================= SBI =================

    "SBI Cashback Card": {
        "type": "cashback",
        "annual_fee": 999,
        "network": "Visa",
        "rewards": {
            "Online Shopping": 5,
            "Other": 1
        },
        "vendor_rewards": {
            "Amazon": 5, "Flipkart": 5, "Myntra": 5,
            "BigBasket": 5, "Blinkit": 5,
        }
    },

    "SBI SimplyCLICK": {
        "type": "points",
        "annual_fee": 499,
        "network": "Visa",
        "rewards": {
            "Online Shopping": 5,
            "Dining": 1,
            "Other": 1
        },
        "vendor_rewards": {
            "Amazon": 5, "Flipkart": 5,
            "Cleartrip": 10, "Netmeds": 5,
        }
    },

    "SBI Prime": {
        "type": "points",
        "annual_fee": 2999,
        "network": "Visa",
        "rewards": {
            "Dining": 10,
            "Grocery": 10,
            "Movies/Entertainment": 10,
            "Other": 2
        },
        "vendor_rewards": {
            "Swiggy": 10, "Zomato": 10,
            "BigBasket": 10, "Blinkit": 10,
            "BookMyShow": 10,
        }
    },

    # ================= ICICI =================

    "ICICI Amazon Pay": {
        "type": "cashback",
        "annual_fee": 0,
        "network": "Visa",
        "rewards": {
            "Amazon": 5,
            "Online Shopping": 2,
            "Dining": 1,
            "Other": 1
        },
        "vendor_rewards": {
            "Amazon": 5,
            "Swiggy": 2, "Zomato": 2,
            "Flipkart": 2, "BookMyShow": 2,
        }
    },

    "ICICI Coral": {
        "type": "points",
        "annual_fee": 500,
        "network": "Visa",
        "rewards": {
            "Dining": 2,
            "Travel": 2,
            "Other": 1
        },
        "vendor_rewards": {
            "Swiggy": 2, "Zomato": 2,
            "MakeMyTrip": 2, "BookMyShow": 2,
        }
    },

    "ICICI Sapphiro": {
        "type": "points",
        "annual_fee": 6500,
        "network": "Visa",
        "rewards": {
            "Dining": 4,
            "Travel": 4,
            "Movies/Entertainment": 4,
            "Other": 2
        },
        "vendor_rewards": {
            "BookMyShow": 4, "Swiggy": 4, "Zomato": 4,
            "MakeMyTrip": 4, "Cleartrip": 4,
        }
    },

    # ================= Axis =================

    "Axis Ace": {
        "type": "cashback",
        "annual_fee": 499,
        "network": "Visa",
        "rewards": {
            "Utilities": 5,
            "Dining": 2,
            "Grocery": 2,
            "Other": 1
        },
        "vendor_rewards": {
            "Swiggy": 5, "Zomato": 5,
            "Uber": 5, "Ola": 5,
            "BigBasket": 2, "Zepto": 2,
        }
    },

    "Axis Flipkart": {
        "type": "cashback",
        "annual_fee": 500,
        "network": "Visa",
        "rewards": {
            "Online Shopping": 5,
            "Dining": 4,
            "Other": 1
        },
        "vendor_rewards": {
            "Flipkart": 5, "Myntra": 5, "Ajio": 4,
            "Swiggy": 4, "Zomato": 4,
            "Uber": 4, "Ola": 4,
        }
    },

    "Axis Magnus": {
        "type": "points",
        "annual_fee": 12500,
        "network": "Visa",
        "rewards": {
            "Travel": 12,
            "International": 12,
            "Dining": 12,
            "Other": 4
        },
        "vendor_rewards": {
            "MakeMyTrip": 12, "Goibibo": 12, "Cleartrip": 12,
            "Swiggy": 12, "Zomato": 12, "BookMyShow": 12,
        }
    },

    # ================= Kotak =================

    "Kotak League Platinum": {
        "type": "points",
        "annual_fee": 499,
        "network": "Visa",
        "rewards": {
            "Dining": 4,
            "Shopping": 4,
            "Other": 1
        },
        "vendor_rewards": {
            "Swiggy": 4, "Zomato": 4,
            "Amazon": 4, "Flipkart": 4,
        }
    },

    "Kotak Zen Signature": {
        "type": "cashback",
        "annual_fee": 1500,
        "network": "Visa",
        "rewards": {
            "Dining": 5,
            "Movies/Entertainment": 5,
            "Other": 1
        },
        "vendor_rewards": {
            "Swiggy": 5, "Zomato": 5,
            "BookMyShow": 5, "Netflix": 5,
            "Hotstar": 5, "Spotify": 5,
        }
    },

    # ================= IndusInd =================

    "IndusInd Legend": {
        "type": "cashback",
        "annual_fee": 0,
        "network": "Visa",
        "rewards": {
            "Dining": 2,
            "Fuel": 1,
            "Other": 1
        },
        "vendor_rewards": {
            "Swiggy": 2, "Zomato": 2,
            "HP Fuel": 1, "Indian Oil": 1, "BPCL": 1,
        }
    },

    "IndusInd Pinnacle": {
        "type": "points",
        "annual_fee": 15000,
        "network": "Diners Club",
        "rewards": {
            "Travel": 15,
            "International": 15,
            "Dining": 10,
            "Other": 2.5
        },
        "vendor_rewards": {
            "MakeMyTrip": 15, "Goibibo": 15, "Cleartrip": 15,
            "Swiggy": 10, "Zomato": 10,
        }
    },

    # ================= Yes Bank =================

    "YES Prosperity Cashback": {
        "type": "cashback",
        "annual_fee": 999,
        "network": "Visa",
        "rewards": {
            "Online Shopping": 3,
            "Dining": 3,
            "Other": 1
        },
        "vendor_rewards": {
            "Amazon": 3, "Flipkart": 3,
            "Swiggy": 3, "Zomato": 3,
        }
    },

    "YES Marquee": {
        "type": "points",
        "annual_fee": 9999,
        "network": "Visa",
        "rewards": {
            "Travel": 12,
            "International": 12,
            "Dining": 6,
            "Other": 3
        },
        "vendor_rewards": {
            "MakeMyTrip": 12, "Goibibo": 12,
            "Swiggy": 6, "Zomato": 6, "BookMyShow": 6,
        }
    },

    # ================= RBL =================

    "RBL World Safari": {
        "type": "points",
        "annual_fee": 3000,
        "network": "MasterCard",
        "rewards": {
            "International": 10,
            "Travel": 10,
            "Other": 2
        },
        "vendor_rewards": {
            "MakeMyTrip": 10, "Cleartrip": 10, "Yatra": 10,
        }
    },

    "RBL Shoprite": {
        "type": "cashback",
        "annual_fee": 500,
        "network": "MasterCard",
        "rewards": {
            "Grocery": 5,
            "Other": 1
        },
        "vendor_rewards": {
            "BigBasket": 5, "Blinkit": 5, "Zepto": 5,
            "DMart": 5, "JioMart": 5,
        }
    },

    # ================= IDFC =================

    "IDFC First Wealth": {
        "type": "cashback",
        "annual_fee": 0,
        "network": "Visa",
        "rewards": {
            "Dining": 3,
            "Online Shopping": 3,
            "Other": 1.5
        },
        "vendor_rewards": {
            "Swiggy": 3, "Zomato": 3,
            "Amazon": 3, "Flipkart": 3,
        }
    },

    "IDFC First Select": {
        "type": "cashback",
        "annual_fee": 0,
        "network": "Visa",
        "rewards": {
            "Dining": 2,
            "Online Shopping": 2,
            "Other": 1
        },
        "vendor_rewards": {
            "Swiggy": 2, "Zomato": 2,
            "Amazon": 2, "Flipkart": 2,
        }
    },
}


# =========================================
# VENDORS (Category → Merchant mapping)
# =========================================

VENDORS = {
    "Online Shopping": [
        "Amazon", "Flipkart", "Myntra", "Ajio",
        "Nykaa", "Croma", "Reliance Digital",
    ],
    "Dining": [
        "Swiggy", "Zomato", "EatSure", "Dominos",
    ],
    "Grocery": [
        "BigBasket", "Blinkit", "Zepto", "JioMart", "DMart",
    ],
    "Travel": [
        "MakeMyTrip", "Goibibo", "IRCTC", "Cleartrip",
        "Yatra", "Uber", "Ola",
    ],
    "Movies/Entertainment": [
        "BookMyShow", "Netflix", "Hotstar", "Spotify",
    ],
    "Fuel": [
        "HP Fuel", "Indian Oil", "BPCL",
    ],
    "Utilities": [
        "Electricity", "Water", "Gas",
        "Broadband", "Mobile Recharge",
    ],
}


# =========================================
# UI LISTS
# =========================================

POPULAR_CARDS = list(CARD_DATA.keys())

CATEGORIES = [
    "Dining",
    "Travel",
    "Grocery",
    "Fuel",
    "Online Shopping",
    "Amazon",
    "Utilities",
    "International",
    "Shopping",
    "Movies/Entertainment",
    "Other",
]