# =====================================================================
# 🇮🇳 SWIPESMART ENTERPRISE — COMPREHENSIVE CREDIT CARD DATABASE (2026)
# Covers 26 Premier Indian Credit Cards across all major issuers
# =====================================================================

CARDS_DATABASE = {
    # ─────────────────────────────────────────────────────────────────
    # HDFC BANK
    # ─────────────────────────────────────────────────────────────────
    "HDFC Infinia Metal": {
        "bank": "HDFC Bank",
        "network": "Visa Infinite",
        "tier": "Super Premium",
        "type": "points",
        "annual_fee": 12500,
        "fee_waiver_spend": 1000000,
        "forex_markup": 2.0,
        "domestic_lounges": "Unlimited (Primary + Add-on)",
        "intl_lounges": "Unlimited (Priority Pass)",
        "fuel_surcharge_waiver": 1.0,
        "point_valuation": {
            "flight_hotel": 1.00,
            "air_miles": 1.00,
            "vouchers": 0.50,
            "cash": 0.30,
            "default": 1.00
        },
        "rewards": {
            "Travel": 16.5,
            "Online Shopping": 3.3,
            "Dining": 3.3,
            "Grocery": 3.3,
            "International": 3.3,
            "Utilities": 3.3,
            "Movies/Entertainment": 3.3,
            "Other": 3.3
        },
        "vendor_rewards": {
            "SmartBuy Flights": 16.5,
            "SmartBuy Hotels": 33.0,
            "Apple (SmartBuy)": 16.5,
            "Amazon": 9.9,
            "Flipkart": 9.9,
            "Swiggy": 9.9,
            "Zomato": 9.9,
            "MakeMyTrip": 16.5,
            "Myntra": 9.9,
            "Uber": 9.9
        },
        "caps": {
            "accelerated_monthly_points": 10000,
            "accelerated_daily_points": 7500
        },
        "milestones": [
            {"spend": 1000000, "benefit_value": 12500, "description": "Annual Fee Waiver on ₹10L annual spend"}
        ],
        "welcome_gift": "12,500 Reward Points upon fee payment",
        "summary": "India's undisputed king of reward cards. 3.3% base reward, up to 33% via SmartBuy for flights and hotels, with 1:1 point value.",
        "apply_url": "https://www.hdfcbank.com/personal/pay/cards/credit-cards/infinia-credit-card"
    },

    "HDFC Diners Black": {
        "bank": "HDFC Bank",
        "network": "Diners Club",
        "tier": "Super Premium",
        "type": "points",
        "annual_fee": 10000,
        "fee_waiver_spend": 800000,
        "forex_markup": 2.0,
        "domestic_lounges": "Unlimited (Primary + Add-on)",
        "intl_lounges": "Unlimited",
        "fuel_surcharge_waiver": 1.0,
        "point_valuation": {
            "flight_hotel": 1.00,
            "air_miles": 1.00,
            "vouchers": 0.50,
            "cash": 0.30,
            "default": 1.00
        },
        "rewards": {
            "Travel": 16.5,
            "Dining": 3.3,
            "Online Shopping": 3.3,
            "International": 3.3,
            "Grocery": 3.3,
            "Movies/Entertainment": 3.3,
            "Utilities": 3.3,
            "Other": 3.3
        },
        "vendor_rewards": {
            "SmartBuy Flights": 16.5,
            "SmartBuy Hotels": 33.0,
            "Swiggy": 9.9,
            "Zomato": 9.9,
            "MakeMyTrip": 16.5,
            "Amazon": 9.9,
            "Flipkart": 9.9,
            "BookMyShow": 9.9
        },
        "caps": {
            "accelerated_monthly_points": 10000,
            "accelerated_daily_points": 2500
        },
        "milestones": [
            {"spend": 800000, "benefit_value": 10000, "description": "Annual Fee waiver at ₹8L annual spend"},
            {"spend": 400000, "benefit_value": 5000, "description": "Club Marriott / Swiggy One membership vouchers"}
        ],
        "welcome_gift": "10,000 Reward Points + Complimentary Annual Memberships (Club Marriott, Forbes, Amazon Prime)",
        "summary": "Elite Diners Club metal card offering unlimited global lounge access, 3.3% base reward, and up to 33% on SmartBuy.",
        "apply_url": "https://www.hdfcbank.com/personal/pay/cards/credit-cards/diners-club-black"
    },

    "HDFC Regalia Gold": {
        "bank": "HDFC Bank",
        "network": "Visa Signature",
        "tier": "Mid-tier Premium",
        "type": "points",
        "annual_fee": 2500,
        "fee_waiver_spend": 400000,
        "forex_markup": 2.0,
        "domestic_lounges": "12 visits/year (Visa)",
        "intl_lounges": "6 visits/year (Priority Pass)",
        "fuel_surcharge_waiver": 1.0,
        "point_valuation": {
            "flight_hotel": 0.50,
            "air_miles": 0.50,
            "vouchers": 0.35,
            "cash": 0.20,
            "default": 0.50
        },
        "rewards": {
            "Online Shopping": 6.6,
            "Travel": 6.6,
            "Dining": 2.6,
            "International": 2.6,
            "Grocery": 1.33,
            "Other": 1.33
        },
        "vendor_rewards": {
            "Myntra": 6.6,
            "Nykaa": 6.6,
            "Marks & Spencer": 6.6,
            "Reliance Digital": 6.6,
            "MakeMyTrip": 6.6,
            "SmartBuy": 6.6,
            "Swiggy": 2.6,
            "Zomato": 2.6
        },
        "caps": {
            "accelerated_monthly_points": 5000
        },
        "milestones": [
            {"spend": 400000, "benefit_value": 2500, "description": "Fee waiver on ₹4L spend"},
            {"spend": 500000, "benefit_value": 5000, "description": "₹5,000 flight voucher on ₹5L annual spend"}
        ],
        "welcome_gift": "₹2,500 gift voucher (Marks & Spencer / Myntra / Reliance) on fee payment",
        "summary": "Versatile mid-tier luxury travel card with 12 domestic + 6 intl lounges and 5x rewards on curated retail brands.",
        "apply_url": "https://www.hdfcbank.com/personal/pay/cards/credit-cards/regalia-gold"
    },

    "HDFC Millennia": {
        "bank": "HDFC Bank",
        "network": "Visa / MasterCard",
        "tier": "Cashback",
        "type": "cashback",
        "annual_fee": 1000,
        "fee_waiver_spend": 100000,
        "forex_markup": 3.5,
        "domestic_lounges": "4 visits/year (1 per quarter upon ₹1L spend)",
        "intl_lounges": "None",
        "fuel_surcharge_waiver": 1.0,
        "point_valuation": {
            "cash": 1.00,
            "flight_hotel": 1.00,
            "vouchers": 1.00,
            "default": 1.00
        },
        "rewards": {
            "Online Shopping": 5.0,
            "Dining": 5.0,
            "Travel": 5.0,
            "Grocery": 1.0,
            "Utilities": 1.0,
            "Other": 1.0
        },
        "vendor_rewards": {
            "Amazon": 5.0,
            "Flipkart": 5.0,
            "Myntra": 5.0,
            "Swiggy": 5.0,
            "Zomato": 5.0,
            "BookMyShow": 5.0,
            "Uber": 5.0,
            "Tata CLiQ": 5.0,
            "Cult.fit": 5.0,
            "Sony LIV": 5.0
        },
        "caps": {
            "partner_monthly_cashback": 1000,
            "other_monthly_cashback": 1000
        },
        "milestones": [
            {"spend": 100000, "benefit_value": 1000, "description": "Fee waiver on ₹1L spend"},
            {"spend": 100000, "benefit_value": 1000, "description": "₹1,000 gift voucher each calendar quarter on ₹1L spend"}
        ],
        "welcome_gift": "1,000 CashPoints on fee payment",
        "summary": "India's favorite millennial card: flat 5% cashback on 10 top digital merchants (Amazon, Flipkart, Swiggy, Zomato, Uber).",
        "apply_url": "https://www.hdfcbank.com/personal/pay/cards/credit-cards/millennia-credit-card"
    },

    "Swiggy HDFC": {
        "bank": "HDFC Bank",
        "network": "MasterCard",
        "tier": "Cashback",
        "type": "cashback",
        "annual_fee": 500,
        "fee_waiver_spend": 200000,
        "forex_markup": 3.5,
        "domestic_lounges": "None",
        "intl_lounges": "None",
        "fuel_surcharge_waiver": 1.0,
        "point_valuation": {
            "cash": 1.00,
            "default": 1.00
        },
        "rewards": {
            "Dining": 10.0,
            "Grocery": 10.0,
            "Online Shopping": 5.0,
            "Movies/Entertainment": 5.0,
            "Travel": 5.0,
            "Other": 1.0
        },
        "vendor_rewards": {
            "Swiggy": 10.0,
            "Blinkit": 5.0,
            "BigBasket": 5.0,
            "Zepto": 5.0,
            "Amazon": 5.0,
            "Flipkart": 5.0,
            "Myntra": 5.0,
            "Nykaa": 5.0,
            "Uber": 5.0,
            "BookMyShow": 5.0,
            "Netflix": 5.0
        },
        "caps": {
            "swiggy_monthly_cashback": 1500,
            "online_monthly_cashback": 1500,
            "other_monthly_cashback": 500
        },
        "milestones": [
            {"spend": 200000, "benefit_value": 500, "description": "Fee waiver on ₹2L annual spend"}
        ],
        "welcome_gift": "3-month Swiggy One membership complimentary",
        "summary": "Unbeatable for foodies and quick commerce: 10% direct cashback on Swiggy (Food, Instamart, Dineout) + 5% on top apps.",
        "apply_url": "https://www.hdfcbank.com/personal/pay/cards/credit-cards/swiggy-credit-card"
    },

    "Tata Neu Infinity HDFC": {
        "bank": "HDFC Bank",
        "network": "RuPay / Visa",
        "tier": "Mid-tier Premium",
        "type": "points",
        "annual_fee": 1499,
        "fee_waiver_spend": 300000,
        "forex_markup": 2.0,
        "domestic_lounges": "8 visits/year (2 per quarter)",
        "intl_lounges": "4 visits/year (1 per quarter via Priority Pass)",
        "fuel_surcharge_waiver": 1.0,
        "point_valuation": {
            "tata_brands": 1.00,
            "cash": 0.50,
            "default": 1.00
        },
        "rewards": {
            "Online Shopping": 10.0,
            "Grocery": 10.0,
            "Travel": 10.0,
            "UPI": 1.5,
            "Utilities": 5.0,
            "Other": 1.5
        },
        "vendor_rewards": {
            "Tata Neu": 10.0,
            "BigBasket": 10.0,
            "Croma": 10.0,
            "Air India": 10.0,
            "Tata 1mg": 10.0,
            "Taj Hotels": 10.0,
            "Titan": 10.0,
            "Tata CLiQ": 10.0,
            "Westside": 10.0
        },
        "caps": {
            "upi_monthly_coins": 500
        },
        "milestones": [
            {"spend": 300000, "benefit_value": 1499, "description": "Fee waiver on ₹3L spend"}
        ],
        "welcome_gift": "1,499 NeuCoins upon card activation",
        "summary": "Top-tier Tata ecosystem powerhouse. 10% NeuCoins on Tata brands, 1.5% rewards on RuPay UPI QR scans, plus lounge access.",
        "apply_url": "https://www.hdfcbank.com/personal/pay/cards/credit-cards/tata-neu-infinity-credit-card"
    },

    # ─────────────────────────────────────────────────────────────────
    # STATE BANK OF INDIA (SBI CARD)
    # ─────────────────────────────────────────────────────────────────
    "SBI Cashback Card": {
        "bank": "SBI Card",
        "network": "Visa",
        "tier": "Cashback",
        "type": "cashback",
        "annual_fee": 999,
        "fee_waiver_spend": 200000,
        "forex_markup": 3.5,
        "domestic_lounges": "None",
        "intl_lounges": "None",
        "fuel_surcharge_waiver": 1.0,
        "point_valuation": {
            "cash": 1.00,
            "default": 1.00
        },
        "rewards": {
            "Online Shopping": 5.0,
            "Dining": 5.0,
            "Grocery": 5.0,
            "Travel": 5.0,
            "Movies/Entertainment": 5.0,
            "Utilities": 1.0,
            "Fuel": 0.0,
            "Other": 1.0
        },
        "vendor_rewards": {
            "Amazon": 5.0,
            "Flipkart": 5.0,
            "Myntra": 5.0,
            "Swiggy": 5.0,
            "Zomato": 5.0,
            "Blinkit": 5.0,
            "BigBasket": 5.0,
            "MakeMyTrip": 5.0,
            "BookMyShow": 5.0,
            "Uber": 5.0,
            "Cleartrip": 5.0
        },
        "caps": {
            "online_monthly_cashback": 5000
        },
        "milestones": [
            {"spend": 200000, "benefit_value": 999, "description": "Annual Fee waiver on ₹2L spend"}
        ],
        "welcome_gift": "Direct statement credit model; no initial voucher",
        "summary": "India's highest uncapped-utility cashback card: flat 5% cashback on almost ALL online transactions up to ₹5,000/month.",
        "apply_url": "https://www.sbicard.com/en/personal/credit-cards/rewards/cashback-sbi-card.page"
    },

    "SBI SimplyCLICK": {
        "bank": "SBI Card",
        "network": "Visa",
        "tier": "Entry Rewards",
        "type": "points",
        "annual_fee": 499,
        "fee_waiver_spend": 100000,
        "forex_markup": 3.5,
        "domestic_lounges": "None",
        "intl_lounges": "None",
        "fuel_surcharge_waiver": 1.0,
        "point_valuation": {
            "vouchers": 0.25,
            "cash": 0.25,
            "default": 0.25
        },
        "rewards": {
            "Online Shopping": 2.5,
            "Dining": 1.25,
            "Travel": 2.5,
            "Other": 0.25
        },
        "vendor_rewards": {
            "Cleartrip": 5.0,
            "BookMyShow": 5.0,
            "Yatra": 5.0,
            "Netmeds": 5.0,
            "Amazon": 2.5,
            "Flipkart": 2.5,
            "Swiggy": 2.5
        },
        "caps": {},
        "milestones": [
            {"spend": 100000, "benefit_value": 2000, "description": "₹2,000 Cleartrip e-voucher on ₹1L online spend"},
            {"spend": 200000, "benefit_value": 2000, "description": "Additional ₹2,000 Cleartrip e-voucher on ₹2L online spend"}
        ],
        "welcome_gift": "Amazon.in gift voucher worth ₹500",
        "summary": "A staple first credit card. 10x points on partners (Cleartrip, BookMyShow), 5x on all online spends, and low threshold fee waiver.",
        "apply_url": "https://www.sbicard.com/en/personal/credit-cards/rewards/simplyclick-sbi-card.page"
    },

    "SBI Prime": {
        "bank": "SBI Card",
        "network": "Visa Signature",
        "tier": "Mid-tier Premium",
        "type": "points",
        "annual_fee": 2999,
        "fee_waiver_spend": 300000,
        "forex_markup": 3.5,
        "domestic_lounges": "8 visits/year (2 per quarter)",
        "intl_lounges": "4 visits/year (Priority Pass)",
        "fuel_surcharge_waiver": 1.0,
        "point_valuation": {
            "vouchers": 0.25,
            "cash": 0.25,
            "default": 0.25
        },
        "rewards": {
            "Dining": 2.5,
            "Grocery": 2.5,
            "Movies/Entertainment": 2.5,
            "Utilities": 5.0,
            "Other": 0.5
        },
        "vendor_rewards": {
            "Swiggy": 2.5,
            "Zomato": 2.5,
            "BigBasket": 2.5,
            "Blinkit": 2.5,
            "BookMyShow": 2.5,
            "Electricity": 5.0,
            "Mobile Recharge": 5.0
        },
        "caps": {
            "utility_monthly_points": 3000
        },
        "milestones": [
            {"spend": 300000, "benefit_value": 2999, "description": "Fee waiver on ₹3L spend"},
            {"spend": 500000, "benefit_value": 7000, "description": "₹7,000 Yatra/Pantaloons vouchers on ₹5L annual spend"}
        ],
        "welcome_gift": "₹3,000 e-gift voucher from Bata, Marks & Spencer, Pantaloons, Shoppers Stop, or Yatra",
        "summary": "Balanced lifestyle card with 20 points per ₹100 on utility bill payments, 10 points on dining/groceries, and Club Vistara membership.",
        "apply_url": "https://www.sbicard.com/en/personal/credit-cards/rewards/sbi-card-prime.page"
    },

    "SBI BPCL Octane": {
        "bank": "SBI Card",
        "network": "Visa",
        "tier": "Cashback",
        "type": "points",
        "annual_fee": 1499,
        "fee_waiver_spend": 200000,
        "forex_markup": 3.5,
        "domestic_lounges": "4 visits/year (1 per quarter)",
        "intl_lounges": "None",
        "fuel_surcharge_waiver": 1.0,
        "point_valuation": {
            "fuel": 0.25,
            "default": 0.25
        },
        "rewards": {
            "Fuel": 7.25,
            "Grocery": 2.5,
            "Dining": 2.5,
            "Movies/Entertainment": 2.5,
            "Other": 0.25
        },
        "vendor_rewards": {
            "BPCL Fuel": 7.25,
            "Bharatgas": 6.25,
            "BigBasket": 2.5,
            "Swiggy": 2.5,
            "Zomato": 2.5
        },
        "caps": {
            "fuel_monthly_points": 2500
        },
        "milestones": [
            {"spend": 200000, "benefit_value": 1499, "description": "Fee waiver on ₹2L spend"}
        ],
        "welcome_gift": "6,000 Bonus Reward Points (₹1,500 value) upon fee payment",
        "summary": "India's #1 fuel savings credit card. 7.25% value back on BPCL fuel purchases + 6.25% on Bharatgas LPG cylinders.",
        "apply_url": "https://www.sbicard.com/en/personal/credit-cards/travel/bpcl-sbi-card-octane.page"
    },

    # ─────────────────────────────────────────────────────────────────
    # ICICI BANK
    # ─────────────────────────────────────────────────────────────────
    "ICICI Amazon Pay": {
        "bank": "ICICI Bank",
        "network": "Visa Platinum",
        "tier": "Lifetime Free",
        "type": "cashback",
        "annual_fee": 0,
        "fee_waiver_spend": 0,
        "forex_markup": 3.5,
        "domestic_lounges": "None",
        "intl_lounges": "None",
        "fuel_surcharge_waiver": 1.0,
        "point_valuation": {
            "cash": 1.00,
            "default": 1.00
        },
        "rewards": {
            "Online Shopping": 5.0,
            "Utilities": 2.0,
            "Dining": 1.0,
            "Grocery": 2.0,
            "Travel": 2.0,
            "Other": 1.0
        },
        "vendor_rewards": {
            "Amazon": 5.0,
            "Amazon Pay Recharges": 2.0,
            "Amazon Pay Bill Payments": 2.0,
            "Swiggy": 2.0,
            "Zomato": 2.0,
            "Uber": 2.0,
            "BookMyShow": 2.0,
            "Flipkart": 1.0
        },
        "caps": {},
        "milestones": [],
        "welcome_gift": "Up to ₹2,500 Amazon Pay balance + coupons on approval",
        "summary": "The gold standard Lifetime Free card. Flat 5% uncapped cashback on Amazon for Prime members, 2% on bills, auto-credited to Amazon Pay.",
        "apply_url": "https://www.amazon.in/cbcc/market"
    },

    "ICICI Coral": {
        "bank": "ICICI Bank",
        "network": "Visa / RuPay",
        "tier": "Entry Rewards",
        "type": "points",
        "annual_fee": 500,
        "fee_waiver_spend": 150000,
        "forex_markup": 3.5,
        "domestic_lounges": "4 visits/year (1 per quarter upon ₹75k spend)",
        "intl_lounges": "None",
        "fuel_surcharge_waiver": 1.0,
        "point_valuation": {
            "vouchers": 0.25,
            "cash": 0.25,
            "default": 0.25
        },
        "rewards": {
            "Dining": 1.0,
            "Utilities": 0.5,
            "Other": 0.5
        },
        "vendor_rewards": {
            "BookMyShow": 25.0,
            "Swiggy": 1.0,
            "Zomato": 1.0,
            "Inox": 25.0
        },
        "caps": {},
        "milestones": [
            {"spend": 150000, "benefit_value": 500, "description": "Fee waiver on ₹1.5L annual spend"}
        ],
        "welcome_gift": "Reward points upon activation",
        "summary": "Affordable credit card with 25% discount on BookMyShow movie tickets and RuPay UPI compatibility.",
        "apply_url": "https://www.icicibank.com/personal-banking/cards/credit-cards/coral-credit-card"
    },

    "ICICI Sapphiro": {
        "bank": "ICICI Bank",
        "network": "Visa Signature + Mastercard World",
        "tier": "Mid-tier Premium",
        "type": "points",
        "annual_fee": 6500,
        "fee_waiver_spend": 600000,
        "forex_markup": 3.5,
        "domestic_lounges": "16 visits/year (4 per quarter)",
        "intl_lounges": "2 visits/year (Dreamfolks DragonPass)",
        "fuel_surcharge_waiver": 1.0,
        "point_valuation": {
            "vouchers": 0.25,
            "cash": 0.25,
            "default": 0.25
        },
        "rewards": {
            "Dining": 1.0,
            "Travel": 1.0,
            "International": 2.0,
            "Grocery": 1.0,
            "Other": 0.5
        },
        "vendor_rewards": {
            "BookMyShow": 50.0,
            "Swiggy": 1.0,
            "Zomato": 1.0,
            "MakeMyTrip": 1.0
        },
        "caps": {},
        "milestones": [
            {"spend": 600000, "benefit_value": 6500, "description": "Annual fee waiver on ₹6L spend"}
        ],
        "welcome_gift": "Vouchers worth ₹9,000+ (Tata CLiQ, EaseMyTrip, Croma, Urban Ladder)",
        "summary": "Dual-card package with Buy 1 Get 1 free movie tickets on BookMyShow (up to ₹500 off twice a month), golf games, and spa visits.",
        "apply_url": "https://www.icicibank.com/personal-banking/cards/credit-cards/sapphiro-credit-card"
    },

    "ICICI Emeralde Private Metal": {
        "bank": "ICICI Bank",
        "network": "Visa Infinite",
        "tier": "Super Premium",
        "type": "points",
        "annual_fee": 12500,
        "fee_waiver_spend": 1000000,
        "forex_markup": 1.5,
        "domestic_lounges": "Unlimited (Primary + Add-on)",
        "intl_lounges": "Unlimited (Priority Pass)",
        "fuel_surcharge_waiver": 1.0,
        "point_valuation": {
            "flight_hotel": 1.00,
            "cash": 1.00,
            "default": 1.00
        },
        "rewards": {
            "Online Shopping": 3.0,
            "Dining": 3.0,
            "Travel": 3.0,
            "International": 3.0,
            "Grocery": 3.0,
            "Utilities": 3.0,
            "Other": 3.0
        },
        "vendor_rewards": {
            "BookMyShow": 50.0,
            "Amazon": 3.0,
            "Flipkart": 3.0,
            "Swiggy": 3.0,
            "MakeMyTrip": 3.0
        },
        "caps": {},
        "milestones": [
            {"spend": 1000000, "benefit_value": 12500, "description": "Fee waiver on ₹10L spend"}
        ],
        "welcome_gift": "12,500 Bonus Reward Points + Taj Epicure Membership",
        "summary": "ICICI's apex metal card. Flat 3% reward rate on ALL spends with no merchant capping, 1.5% forex fee, and unlimited lounge visits.",
        "apply_url": "https://www.icicibank.com/personal-banking/cards/credit-cards/emeralde-private-metal-credit-card"
    },

    # ─────────────────────────────────────────────────────────────────
    # AXIS BANK
    # ─────────────────────────────────────────────────────────────────
    "Axis Atlas": {
        "bank": "Axis Bank",
        "network": "Visa Signature / Infinite",
        "tier": "Miles / Travel",
        "type": "miles",
        "annual_fee": 5000,
        "fee_waiver_spend": 1500000,
        "forex_markup": 3.5,
        "domestic_lounges": "8 to 18 visits/year (Tier based)",
        "intl_lounges": "4 to 12 visits/year (Tier based)",
        "fuel_surcharge_waiver": 1.0,
        "point_valuation": {
            "accor_points": 1.80,
            "air_miles": 1.00,
            "flight_hotel": 1.00,
            "default": 1.80
        },
        "rewards": {
            "Travel": 10.0,
            "Dining": 4.0,
            "Online Shopping": 4.0,
            "International": 4.0,
            "Other": 4.0
        },
        "vendor_rewards": {
            "Air India": 10.0,
            "IndiGo": 10.0,
            "Singapore Airlines": 10.0,
            "Emirates": 10.0,
            "Marriott": 10.0,
            "Taj": 10.0,
            "Accor": 10.0,
            "MakeMyTrip": 10.0,
            "Swiggy": 4.0,
            "Amazon": 4.0
        },
        "caps": {
            "accelerated_monthly_spends": 200000
        },
        "milestones": [
            {"spend": 300000, "benefit_value": 4500, "description": "2,500 bonus EDGE Miles on ₹3L spend"},
            {"spend": 750000, "benefit_value": 9000, "description": "5,000 bonus EDGE Miles on ₹7.5L spend (Upgrade to Gold Tier)"},
            {"spend": 1500000, "benefit_value": 18000, "description": "10,000 bonus EDGE Miles on ₹15L spend (Upgrade to Platinum Tier)"}
        ],
        "welcome_gift": "5,000 EDGE Miles (worth up to ₹10,000 in hotel stays) upon 1st transaction",
        "summary": "The premier air miles credit card in India. 5 EDGE Miles per ₹100 on airlines/hotels (1:2 transfer ratio to Accor, ITC, Singapore Airlines).",
        "apply_url": "https://www.axisbank.com/retail/cards/credit-card/axis-bank-atlas-credit-card"
    },

    "Axis Ace": {
        "bank": "Axis Bank",
        "network": "Visa Signature",
        "tier": "Cashback",
        "type": "cashback",
        "annual_fee": 499,
        "fee_waiver_spend": 200000,
        "forex_markup": 3.5,
        "domestic_lounges": "4 visits/year (upon ₹50k spend in previous 3 months)",
        "intl_lounges": "None",
        "fuel_surcharge_waiver": 1.0,
        "point_valuation": {
            "cash": 1.00,
            "default": 1.00
        },
        "rewards": {
            "Utilities": 5.0,
            "Dining": 4.0,
            "Travel": 4.0,
            "Grocery": 1.5,
            "Online Shopping": 1.5,
            "Other": 1.5
        },
        "vendor_rewards": {
            "Google Pay Utilities": 5.0,
            "Electricity": 5.0,
            "Water": 5.0,
            "Gas": 5.0,
            "Broadband": 5.0,
            "Mobile Recharge": 5.0,
            "Swiggy": 4.0,
            "Zomato": 4.0,
            "Ola": 4.0,
            "BigBasket": 1.5,
            "Amazon": 1.5
        },
        "caps": {
            "utility_monthly_cashback": 500,
            "dining_monthly_cashback": 500
        },
        "milestones": [
            {"spend": 200000, "benefit_value": 499, "description": "Annual fee waiver on ₹2L spend"}
        ],
        "welcome_gift": "100% cashback on first utility bill payment up to ₹250",
        "summary": "Utility & offline champion: 5% cashback on bill payments & DTH via Google Pay, 4% on Swiggy/Zomato/Ola, and flat 1.5% uncapped everywhere else.",
        "apply_url": "https://www.axisbank.com/retail/cards/credit-card/ace-credit-card"
    },

    "Airtel Axis": {
        "bank": "Axis Bank",
        "network": "Visa",
        "tier": "Cashback",
        "type": "cashback",
        "annual_fee": 500,
        "fee_waiver_spend": 200000,
        "forex_markup": 3.5,
        "domestic_lounges": "4 visits/year (upon ₹50k spend in previous 3 months)",
        "intl_lounges": "None",
        "fuel_surcharge_waiver": 1.0,
        "point_valuation": {
            "cash": 1.00,
            "default": 1.00
        },
        "rewards": {
            "Utilities": 10.0,
            "Dining": 10.0,
            "Grocery": 10.0,
            "Other": 1.0
        },
        "vendor_rewards": {
            "Airtel Mobile/Broadband": 25.0,
            "Electricity": 10.0,
            "Water": 10.0,
            "Gas": 10.0,
            "Swiggy": 10.0,
            "Zomato": 10.0,
            "BigBasket": 10.0
        },
        "caps": {
            "airtel_monthly_cashback": 250,
            "utility_monthly_cashback": 250,
            "food_grocery_monthly_cashback": 500
        },
        "milestones": [
            {"spend": 200000, "benefit_value": 500, "description": "Fee waiver on ₹2L spend"}
        ],
        "welcome_gift": "Amazon voucher worth ₹500 on 1st transaction within 30 days",
        "summary": "Essential household card: 25% on Airtel recharges/Wi-Fi, 10% on utility bills via Airtel Thanks, 10% on Swiggy/Zomato/BigBasket.",
        "apply_url": "https://www.axisbank.com/retail/cards/credit-card/airtel-axis-bank-credit-card"
    },

    "Axis Flipkart": {
        "bank": "Axis Bank",
        "network": "Visa",
        "tier": "Cashback",
        "type": "cashback",
        "annual_fee": 500,
        "fee_waiver_spend": 350000,
        "forex_markup": 3.5,
        "domestic_lounges": "4 visits/year (upon ₹50k spend in previous 3 months)",
        "intl_lounges": "None",
        "fuel_surcharge_waiver": 1.0,
        "point_valuation": {
            "cash": 1.00,
            "default": 1.00
        },
        "rewards": {
            "Online Shopping": 5.0,
            "Dining": 4.0,
            "Travel": 4.0,
            "Other": 1.0
        },
        "vendor_rewards": {
            "Flipkart": 5.0,
            "Myntra": 5.0,
            "Cleartrip": 4.0,
            "Swiggy": 4.0,
            "Uber": 4.0,
            "Cult.fit": 4.0,
            "PVR": 4.0
        },
        "caps": {},
        "milestones": [
            {"spend": 350000, "benefit_value": 500, "description": "Fee waiver on ₹3.5L spend"}
        ],
        "welcome_gift": "₹600 welcome benefits on Flipkart and partner merchants",
        "summary": "Flipkart's official card offering unlimited 5% cashback on Flipkart & Myntra, 4% on Cleartrip/Swiggy/Uber, credited directly to statement.",
        "apply_url": "https://www.axisbank.com/retail/cards/credit-card/flipkart-axis-bank-credit-card"
    },

    "Axis Magnus": {
        "bank": "Axis Bank",
        "network": "Visa Infinite",
        "tier": "Super Premium",
        "type": "points",
        "annual_fee": 12500,
        "fee_waiver_spend": 2500000,
        "forex_markup": 2.0,
        "domestic_lounges": "Unlimited (Primary + 8 Guest visits)",
        "intl_lounges": "Unlimited (Priority Pass with 8 Guest visits)",
        "fuel_surcharge_waiver": 1.0,
        "point_valuation": {
            "travel_edge": 0.40,
            "air_miles": 0.40,
            "cash": 0.20,
            "default": 0.40
        },
        "rewards": {
            "Travel": 7.0,
            "International": 2.4,
            "Dining": 1.2,
            "Other": 1.2
        },
        "vendor_rewards": {
            "Travel EDGE": 7.0,
            "MakeMyTrip": 7.0,
            "Swiggy": 1.2,
            "Zomato": 1.2,
            "BookMyShow": 50.0
        },
        "caps": {},
        "milestones": [
            {"spend": 2500000, "benefit_value": 12500, "description": "Fee waiver on ₹25L annual spend"}
        ],
        "welcome_gift": "Complimentary domestic flight ticket or luxury hotel stay voucher worth up to ₹10,000",
        "summary": "Luxury card with unlimited domestic and global lounge access including 8 complimentary guest visits and BookMyShow BOGO up to 5 times/month.",
        "apply_url": "https://www.axisbank.com/retail/cards/credit-card/magnus-credit-card"
    },

    # ─────────────────────────────────────────────────────────────────
    # AMERICAN EXPRESS (AMEX)
    # ─────────────────────────────────────────────────────────────────
    "Amex Platinum Travel": {
        "bank": "American Express",
        "network": "Amex",
        "tier": "Miles / Travel",
        "type": "points",
        "annual_fee": 5000,
        "fee_waiver_spend": 0,
        "forex_markup": 3.5,
        "domestic_lounges": "8 visits/year (2 per quarter)",
        "intl_lounges": "None",
        "fuel_surcharge_waiver": 0.0,
        "point_valuation": {
            "taj_vouchers": 0.50,
            "marriott_bonvoy": 0.50,
            "statement_cash": 0.25,
            "default": 0.50
        },
        "rewards": {
            "Online Shopping": 1.0,
            "Dining": 1.0,
            "Travel": 1.0,
            "Other": 1.0
        },
        "vendor_rewards": {
            "MakeMyTrip": 2.0,
            "Taj Hotels": 3.0,
            "Amazon": 1.0,
            "Flipkart": 1.0
        },
        "caps": {},
        "milestones": [
            {"spend": 190000, "benefit_value": 7500, "description": "15,000 MR points (worth ~₹7,500) on ₹1.9L spend"},
            {"spend": 400000, "benefit_value": 24500, "description": "Additional 25,000 MR points + ₹10,000 Taj Hotel voucher on ₹4L annual spend"}
        ],
        "welcome_gift": "10,000 Membership Rewards points on fee payment and ₹15k spend in 90 days",
        "summary": "India's greatest milestone credit card. Spend ₹4,00,000 a year to earn 48,000 Membership Reward points + ₹10,000 Taj Voucher (~8% net return).",
        "apply_url": "https://www.americanexpress.com/in/credit-cards/platinum-travel-credit-card/"
    },

    # ─────────────────────────────────────────────────────────────────
    # IDFC FIRST BANK
    # ─────────────────────────────────────────────────────────────────
    "IDFC First Wealth": {
        "bank": "IDFC FIRST Bank",
        "network": "Visa Infinite",
        "tier": "Lifetime Free",
        "type": "points",
        "annual_fee": 0,
        "fee_waiver_spend": 0,
        "forex_markup": 1.5,
        "domestic_lounges": "16 visits/year (4 per quarter upon ₹20k spend)",
        "intl_lounges": "16 visits/year (Dreamfolks DragonPass)",
        "fuel_surcharge_waiver": 1.0,
        "point_valuation": {
            "cash": 0.25,
            "vouchers": 0.25,
            "default": 0.25
        },
        "rewards": {
            "Online Shopping": 1.5,
            "Dining": 1.5,
            "Travel": 1.5,
            "International": 1.5,
            "Other": 0.75
        },
        "vendor_rewards": {
            "BookMyShow": 50.0,
            "Swiggy": 1.5,
            "Zomato": 1.5,
            "Amazon": 1.5
        },
        "caps": {},
        "milestones": [
            {"spend": 30000, "benefit_value": 1500, "description": "10x reward points (~2.5% return) on monthly spends above ₹30,000"}
        ],
        "welcome_gift": "Gift voucher worth ₹500 on spending ₹15,000 in first 90 days + 5% cashback on 1st EMI",
        "summary": "Premium Lifetime Free card: 1.5% low forex markup, 16 domestic + 16 international lounge visits, BOGO movie tickets, and points that never expire.",
        "apply_url": "https://www.idfcfirstbank.com/credit-card/wealth"
    },

    "IDFC First Select": {
        "bank": "IDFC FIRST Bank",
        "network": "Visa Signature",
        "tier": "Lifetime Free",
        "type": "points",
        "annual_fee": 0,
        "fee_waiver_spend": 0,
        "forex_markup": 1.99,
        "domestic_lounges": "16 visits/year (4 per quarter upon ₹20k spend)",
        "intl_lounges": "None",
        "fuel_surcharge_waiver": 1.0,
        "point_valuation": {
            "cash": 0.25,
            "vouchers": 0.25,
            "default": 0.25
        },
        "rewards": {
            "Online Shopping": 1.5,
            "Dining": 1.5,
            "Other": 0.75
        },
        "vendor_rewards": {
            "BookMyShow": 50.0,
            "Swiggy": 1.5,
            "Amazon": 1.5
        },
        "caps": {},
        "milestones": [
            {"spend": 25000, "benefit_value": 1250, "description": "10x points (~2.5% return) on monthly spends exceeding ₹25,000"}
        ],
        "welcome_gift": "Gift voucher worth ₹500 on ₹15k spend in 90 days",
        "summary": "Lifetime Free card with 4 domestic airport + railway lounge visits per quarter, BOGO movie tickets, and 10x reward points on spends above ₹25,000.",
        "apply_url": "https://www.idfcfirstbank.com/credit-card/select"
    },

    # ─────────────────────────────────────────────────────────────────
    # FEDERAL SCAPIA & RBL
    # ─────────────────────────────────────────────────────────────────
    "Scapia Federal Card": {
        "bank": "Federal Bank",
        "network": "Visa Signature",
        "tier": "Lifetime Free",
        "type": "points",
        "annual_fee": 0,
        "fee_waiver_spend": 0,
        "forex_markup": 0.0,
        "domestic_lounges": "Unlimited (Requires ₹5,000 spend in preceding billing cycle)",
        "intl_lounges": "None",
        "fuel_surcharge_waiver": 1.0,
        "point_valuation": {
            "flight_hotel": 0.20,
            "default": 0.20
        },
        "rewards": {
            "Travel": 4.0,
            "Online Shopping": 2.0,
            "Dining": 2.0,
            "International": 2.0,
            "Other": 2.0
        },
        "vendor_rewards": {
            "Scapia Flights & Hotels": 4.0,
            "MakeMyTrip": 2.0,
            "Swiggy": 2.0,
            "Zomato": 2.0,
            "Amazon": 2.0
        },
        "caps": {},
        "milestones": [],
        "welcome_gift": "Lifetime Free + zero joining fee",
        "summary": "The ultimate international travel companion: TRUE 0% Forex Markup, Lifetime Free, and unlimited domestic lounge access with just ₹5,000 monthly spend.",
        "apply_url": "https://www.scapia.cards/"
    },

    "RBL World Safari": {
        "bank": "RBL Bank",
        "network": "Mastercard World",
        "tier": "Miles / Travel",
        "type": "points",
        "annual_fee": 3000,
        "fee_waiver_spend": 300000,
        "forex_markup": 0.0,
        "domestic_lounges": "8 visits/year (2 per quarter)",
        "intl_lounges": "2 visits/year (Priority Pass)",
        "fuel_surcharge_waiver": 1.0,
        "point_valuation": {
            "travel": 0.25,
            "default": 0.25
        },
        "rewards": {
            "Travel": 2.5,
            "International": 2.0,
            "Other": 1.0
        },
        "vendor_rewards": {
            "MakeMyTrip": 2.5,
            "Cleartrip": 2.5,
            "Yatra": 2.5
        },
        "caps": {},
        "milestones": [
            {"spend": 300000, "benefit_value": 3000, "description": "Fee waiver on ₹3L spend"},
            {"spend": 500000, "benefit_value": 10000, "description": "₹10,000 Taj Gift Voucher on ₹5L annual spend"}
        ],
        "welcome_gift": "MakeMyTrip gift voucher worth ₹3,000",
        "summary": "Pioneer 0% Forex markup credit card with 2 international + 8 domestic lounge visits and ₹10,000 Taj voucher milestone.",
        "apply_url": "https://www.rblbank.com/product/credit-cards/world-safari-credit-card"
    },

    # ─────────────────────────────────────────────────────────────────
    # KOTAK MAHINDRA BANK
    # ─────────────────────────────────────────────────────────────────
    "Kotak League Platinum": {
        "bank": "Kotak Mahindra Bank",
        "network": "Visa Platinum",
        "tier": "Entry Rewards",
        "type": "points",
        "annual_fee": 499,
        "fee_waiver_spend": 50000,
        "forex_markup": 3.5,
        "domestic_lounges": "None",
        "intl_lounges": "None",
        "fuel_surcharge_waiver": 1.0,
        "point_valuation": {
            "vouchers": 0.25,
            "cash": 0.25,
            "default": 0.25
        },
        "rewards": {
            "Dining": 2.0,
            "Online Shopping": 2.0,
            "Other": 0.66
        },
        "vendor_rewards": {
            "Swiggy": 2.0,
            "Zomato": 2.0,
            "Amazon": 2.0,
            "Flipkart": 2.0
        },
        "caps": {},
        "milestones": [
            {"spend": 50000, "benefit_value": 499, "description": "Fee waiver on ₹50k annual spend"},
            {"spend": 125000, "benefit_value": 1000, "description": "4 free PVR tickets or 10,000 reward points on ₹1.25L spend"}
        ],
        "welcome_gift": "Welcome reward points or movie vouchers",
        "summary": "Entry-level card with 8x reward points on select categories and very easy annual fee waiver at ₹50,000.",
        "apply_url": "https://www.kotak.com/en/personal-banking/cards/credit-cards/league-platinum-card.html"
    },

    "Kotak Zen Signature": {
        "bank": "Kotak Mahindra Bank",
        "network": "Visa Signature",
        "tier": "Mid-tier Premium",
        "type": "points",
        "annual_fee": 1500,
        "fee_waiver_spend": 150000,
        "forex_markup": 3.5,
        "domestic_lounges": "8 visits/year (2 per quarter)",
        "intl_lounges": "None",
        "fuel_surcharge_waiver": 1.0,
        "point_valuation": {
            "vouchers": 0.25,
            "cash": 0.25,
            "default": 0.25
        },
        "rewards": {
            "Dining": 3.3,
            "Movies/Entertainment": 3.3,
            "Online Shopping": 3.3,
            "Other": 1.0
        },
        "vendor_rewards": {
            "BookMyShow": 3.3,
            "Swiggy": 3.3,
            "Zomato": 3.3,
            "Myntra": 3.3
        },
        "caps": {},
        "milestones": [
            {"spend": 150000, "benefit_value": 1500, "description": "Fee waiver on ₹1.5L spend"},
            {"spend": 300000, "benefit_value": 3750, "description": "15,000 bonus Zen points on ₹3L spend"}
        ],
        "welcome_gift": "1,500 Zen points upon fee payment",
        "summary": "10 Zen points per ₹150 on apparel and lifestyle purchases, 8 domestic airport lounges per year.",
        "apply_url": "https://www.kotak.com/en/personal-banking/cards/credit-cards/zen-signature-card.html"
    },

    # ─────────────────────────────────────────────────────────────────
    # INDUSIND BANK
    # ─────────────────────────────────────────────────────────────────
    "IndusInd Legend": {
        "bank": "IndusInd Bank",
        "network": "Visa Signature",
        "tier": "Lifetime Free",
        "type": "points",
        "annual_fee": 0,
        "fee_waiver_spend": 0,
        "forex_markup": 3.5,
        "domestic_lounges": "4 visits/year (1 per quarter)",
        "intl_lounges": "None",
        "fuel_surcharge_waiver": 1.0,
        "point_valuation": {
            "cash": 0.75,
            "vouchers": 0.75,
            "default": 0.75
        },
        "rewards": {
            "Dining": 1.5,
            "Online Shopping": 1.5,
            "Other": 0.75
        },
        "vendor_rewards": {
            "BookMyShow": 50.0,
            "Swiggy": 1.5,
            "Zomato": 1.5
        },
        "caps": {},
        "milestones": [
            {"spend": 600000, "benefit_value": 4000, "description": "4,000 bonus reward points on ₹6L annual spend"}
        ],
        "welcome_gift": "Oberoi Hotel / Yatra gift voucher options",
        "summary": "Lifetime Free premium card offering 2 reward points per ₹100 on weekend spends, 1 complimentary lounge visit per quarter, and BOGO movie tickets.",
        "apply_url": "https://www.indusind.com/in/en/personal/cards/credit-cards/legend-credit-card.html"
    },

    "IndusInd Pinnacle": {
        "bank": "IndusInd Bank",
        "network": "Mastercard World",
        "tier": "Super Premium",
        "type": "points",
        "annual_fee": 15000,
        "fee_waiver_spend": 0,
        "forex_markup": 2.5,
        "domestic_lounges": "Unlimited (Primary cardholder)",
        "intl_lounges": "8 visits/year (Priority Pass)",
        "fuel_surcharge_waiver": 1.0,
        "point_valuation": {
            "cash": 1.00,
            "air_miles": 1.00,
            "default": 1.00
        },
        "rewards": {
            "Online Shopping": 2.5,
            "Travel": 2.5,
            "Dining": 2.5,
            "International": 2.5,
            "Other": 1.0
        },
        "vendor_rewards": {
            "BookMyShow": 50.0,
            "MakeMyTrip": 2.5,
            "Swiggy": 2.5,
            "Zomato": 2.5
        },
        "caps": {},
        "milestones": [],
        "welcome_gift": "Luxury hotel stay vouchers (Oberoi / Postcard Hotels) worth fee amount",
        "summary": "1 pt = ₹1 direct cashback value, complimentary golf coaching & games, unlimited domestic lounges, and 2.5% reward rate on ecommerce.",
        "apply_url": "https://www.indusind.com/in/en/personal/cards/credit-cards/pinnacle-credit-card.html"
    }
}

# ─────────────────────────────────────────────────────────────────
# BACKWARD COMPATIBILITY ALIASES
# ─────────────────────────────────────────────────────────────────
CARD_DATA = CARDS_DATABASE
POPULAR_CARDS = list(CARDS_DATABASE.keys())

CATEGORIES = [
    "Online Shopping",
    "Dining",
    "Grocery",
    "Travel",
    "Utilities",
    "Movies/Entertainment",
    "Fuel",
    "International",
    "UPI",
    "Other"
]

CARD_TIERS = ["All Tiers", "Cashback", "Super Premium", "Mid-tier Premium", "Miles / Travel", "Lifetime Free"]
CARD_ISSUERS = ["All Banks", "HDFC Bank", "SBI Card", "ICICI Bank", "Axis Bank", "American Express", "IDFC FIRST Bank", "Federal Bank", "Kotak Mahindra Bank", "IndusInd Bank", "RBL Bank"]
