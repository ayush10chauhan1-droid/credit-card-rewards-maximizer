# =====================================================================
# 📚 SWIPESMART CARD KNOWLEDGE BASE & ISSUER RULES (RAG CORPUS)
# Curated terms, conditions, capping limits, exclusions, and lounge rules
# =====================================================================

CARD_RULES_CORPUS = [
    {
        "card": "HDFC Infinia Metal",
        "topic": "SmartBuy & Capping Rules",
        "text": """HDFC Infinia Metal offers 5x Reward Points on flight bookings and 10x on hotel bookings via HDFC SmartBuy portal.
The maximum accelerated reward points on SmartBuy are capped at 10,000 points per calendar month and 7,500 points per day.
Base reward rate is 5 points per ₹150 spent (3.33% reward rate) on standard retail spends.
Point value: 1 Reward Point = ₹1.00 when redeemed for flights/hotels via SmartBuy or 1:1 air miles transfer to partner airline programs.
Exclusions: Fuel spends, wallet load transactions, rent payments, government tax payments, and education fees do not earn reward points.
Fee Waiver: Annual fee of ₹12,500 + GST is completely waived if annual spends exceed ₹10,00,000 in the preceding card year."""
    },
    {
        "card": "HDFC Diners Black",
        "topic": "Lounge Access & Milestone Benefits",
        "text": """HDFC Diners Club Black Metal Edition provides unlimited complimentary airport lounge access worldwide for both primary and add-on cardholders.
Accelerated rewards on SmartBuy allow up to 10x reward points on hotels and 5x on flights, capped at 10,000 accelerated points per calendar month and 2,500 points per day.
Point redemption value is ₹1.00 per point for flights and hotels on SmartBuy.
Milestone perks: Spend ₹4,00,000 in a calendar year to receive complimentary annual memberships including Club Marriott, Swiggy One, and Amazon Prime.
Annual fee of ₹10,000 is waived upon spending ₹8,00,000 in the anniversary year.
Forex markup fee is reduced to 2.0% + GST."""
    },
    {
        "card": "SBI Cashback Card",
        "topic": "5% Online Cashback & Exclusions",
        "text": """SBI Cashback Card provides 5% cashback on all eligible online transactions across all merchant websites and apps in India.
Cashback is capped at ₹5,000 per monthly billing cycle (translates to 5% on ₹1,00,000 online monthly spend).
Spends beyond ₹5,000 cashback or offline POS swipes earn 1% cashback uncapped.
Cashback is automatically credited to the card account statement within 2 days of next statement generation.
Exclusions: Rent payments, wallet reloads, merchant EMI purchases, fuel, jewellery, school fees, utilities, and railway bookings do not earn 5% cashback.
Annual renewal fee of ₹999 + GST is waived if total annual spend exceeds ₹2,00,000."""
    },
    {
        "card": "ICICI Amazon Pay",
        "topic": "Unlimited Cashback & Prime Benefits",
        "text": """ICICI Amazon Pay is a Lifetime Free (₹0 joining, ₹0 annual fee) credit card.
Prime members earn flat 5% unlimited cashback on Amazon India shopping purchases. Non-prime members earn 3%.
Earn 2% cashback on payments through Amazon Pay for flight bookings, recharges, bill payments, and partner merchants (Swiggy, Zomato, Uber, BookMyShow).
All other retail spends earn flat 1% unlimited cashback.
Cashback has no minimum threshold and no monthly cap; it is automatically added as Amazon Pay balance every billing cycle.
Exclusions: Fuel spends do not earn cashback but receive a 1% fuel surcharge waiver on transactions between ₹400 and ₹4,000."""
    },
    {
        "card": "Axis Atlas",
        "topic": "EDGE Miles & Tier Upgrades",
        "text": """Axis Atlas credit card rewards cardholders in EDGE Miles.
Base earn rate: 2 EDGE Miles per ₹100 spent on all general retail spends (~4% value).
Travel earn rate: 5 EDGE Miles per ₹100 spent directly on airline websites and hotel reservations (~10% value), capped at ₹2,00,000 monthly travel spend.
Transfer ratio: 1 EDGE Mile = 2 Partner Points / Miles (e.g. 1 EDGE Mile = 2 Accor Live Limitless ALL points, worth approximately ₹3.60).
Milestones & Tiers:
- Silver Tier (Base): 8 domestic + 4 intl lounge visits.
- Gold Tier (on ₹7.5L spend): 5,000 bonus miles + 12 domestic + 6 intl lounge visits.
- Platinum Tier (on ₹15L spend): 10,000 bonus miles + 18 domestic + 12 intl lounge visits.
Annual fee: ₹5,000 + GST. Welcome bonus: 5,000 EDGE Miles upon 1st transaction."""
    },
    {
        "card": "Swiggy HDFC",
        "topic": "10% Food Delivery Cashback & Partner Slabs",
        "text": """Swiggy HDFC credit card earns 10% direct cashback on Swiggy application spends (Food Orders, Instamart grocery, and Dineout bills).
Swiggy 10% cashback is capped at ₹1,500 per calendar month (₹15,000 monthly spend).
Earn 5% cashback on top online merchants including Amazon, Flipkart, Myntra, Nykaa, Blinkit, Zepto, Uber, BookMyShow, and Netflix.
5% online partner cashback is capped at ₹1,500 per month.
All other retail spends earn 1% cashback capped at ₹500 per month.
Cashback is credited as Swiggy Money or statement cashback.
Annual fee: ₹500 + GST, waived upon spending ₹2,00,000 in a year."""
    },
    {
        "card": "Axis Ace",
        "topic": "Google Pay Utilities & Offline 1.5%",
        "text": """Axis Ace offers 5% cashback on electricity, water, gas, broadband, and mobile recharge bills paid via Google Pay app on Android.
Utility 5% cashback is capped at ₹500 per statement cycle (₹10,000 spend).
Earn 4% cashback on Swiggy, Zomato, and Ola rides, capped at ₹500 per statement cycle.
Earn flat 1.5% uncapped cashback on all other online and offline retail transactions.
Airport lounge: 4 complimentary domestic lounge visits per year, subject to ₹50,000 spend in preceding 3 months.
Annual fee: ₹499 + GST, waived upon annual spend of ₹2,00,000."""
    },
    {
        "card": "Airtel Axis",
        "topic": "25% Recharges & 10% Utilities",
        "text": """Airtel Axis credit card provides 25% cashback on Airtel Mobile, Broadband, DTH, and Wi-Fi bill payments via Airtel Thanks app (capped at ₹250/month).
Earn 10% cashback on utility bills (electricity, water, gas) paid via Airtel Thanks app (capped at ₹250/month).
Earn 10% cashback on Swiggy, Zomato, and BigBasket purchases (combined cap of ₹500/month).
All other spends earn 1% uncapped cashback.
Annual fee: ₹500 + GST, waived on ₹2,00,000 annual spend.
Airport lounge: 4 complimentary domestic visits per year upon spend criteria."""
    },
    {
        "card": "Scapia Federal Card",
        "topic": "Zero Forex Markup & Lounge Criteria",
        "text": """Scapia Federal Bank credit card charges 0% Forex Markup on international transactions worldwide (compared to 3.5% on standard cards).
Lifetime Free card with zero joining fee and zero annual fee.
Earn 10% Scapia Coins on general spends (2% reward rate, where 5 Scapia coins = ₹1).
Earn 20% Scapia Coins on flights and hotels booked via the Scapia travel app (4% reward rate).
Domestic airport lounge access: Unlimited complimentary visits across participating Indian airport lounges, conditioned on spending at least ₹5,000 in the previous billing cycle."""
    },
    {
        "card": "Amex Platinum Travel",
        "topic": "Milestone Taj Vouchers & MR Points",
        "text": """American Express Platinum Travel Credit Card is optimized exclusively for ₹4,00,000 annual expenditure.
Milestone Step 1: Spend ₹1,90,000 in a card membership year to receive 15,000 Membership Rewards points (worth ~₹7,500).
Milestone Step 2: Spend ₹4,00,000 in a card membership year to receive an additional 25,000 MR points plus a complimentary ₹10,000 Taj Experiences Gift Stay Voucher.
Total rewards on ₹4L spend: 48,000 MR points + ₹10,000 Taj Voucher = estimated ₹32,000+ total value (approx 8% net return).
Domestic lounge: 8 complimentary domestic airport lounge visits per year (2 per quarter).
Annual fee: ₹5,000 + GST. Welcome bonus: 10,000 MR points upon spending ₹15,000 within first 90 days."""
    },
    {
        "card": "Tata Neu Infinity HDFC",
        "topic": "10% Tata Neu & RuPay UPI",
        "text": """Tata Neu Infinity HDFC Bank card earns 10% NeuCoins on Tata Neu app purchases across Tata brands (BigBasket, Croma, Air India, Tata 1mg, Taj Hotels, Titan, Westside, Tata CLiQ).
Earn 1.5% NeuCoins on RuPay UPI merchant QR payments, capped at 500 NeuCoins per calendar month.
1 NeuCoin = ₹1.00 when redeemed across any Tata brand ecosystem website or app.
Domestic lounge: 8 complimentary visits per year (2 per quarter). International lounge: 4 visits per year via Priority Pass.
Annual fee: ₹1,499 + GST, waived on ₹3,00,000 annual spend."""
    },
    {
        "card": "General Exclusions & Surcharges",
        "topic": "Universal Indian Credit Card Exclusions",
        "text": """Across Indian credit cards, the following categories typically DO NOT earn standard or accelerated reward points:
1. Fuel Transactions: Usually exempt from points; instead receive 1% fuel surcharge waiver on transactions between ₹400 and ₹4,000.
2. Wallet Loads: Loading Paytm, Mobikwik, or Amazon Pay wallet with credit cards attracts a 1% to 2.5% surcharge from issuers.
3. Rent Payments: CRED, Magicbricks, NoBroker rent payments incur a 1% convenience fee + GST and zero reward points on most cards.
4. Government Transactions & Taxes: Advance tax and income tax payments are excluded from reward programs on HDFC, SBI, Axis, and ICICI.
5. School & Education Fees: Many banks now cap or exclude reward points on school fee payments."""
    }
]
