// =====================================================================
// 💳 SWIPESMART AI — 26 INDIAN PREMIER CREDIT CARDS DATASET
// Complete specifications, capping rules, multipliers & design visual tokens
// =====================================================================

export interface CardSkinConfig {
  gradient: string;
  accentColor: string;
  textColor: string;
  subtextColor: string;
  chipColor: string;
  pattern: 'metal' | 'cyber' | 'waves' | 'grid' | 'aurora' | 'minimal';
  badge: string;
  tagline: string;
}

export interface CreditCardData {
  name: string;
  bank: string;
  network: string;
  tier: string;
  type: 'cashback' | 'points' | 'miles';
  annual_fee: number;
  fee_waiver_spend: number;
  forex_markup: number;
  domestic_lounges: string;
  intl_lounges: string;
  fuel_surcharge_waiver: number;
  point_valuation: Record<string, number>;
  rewards: Record<string, number>;
  vendor_rewards?: Record<string, number>;
  caps?: Record<string, number>;
  milestones?: Array<{ spend: number; benefit_value: number; description: string }>;
  welcome_gift: string;
  summary: string;
  apply_url: string;
  skin: CardSkinConfig;
}

export const CATEGORIES = [
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
];

export const CATEGORY_ICONS: Record<string, string> = {
  "Online Shopping": "🛍️",
  "Dining": "🍽️",
  "Grocery": "🛒",
  "Travel": "✈️",
  "Utilities": "💡",
  "Movies/Entertainment": "🎬",
  "Fuel": "⛽",
  "International": "🌍",
  "UPI": "📲",
  "Other": "📌"
};

export const VENDORS_METADATA: Record<string, { category: string; icon: string; best_cards: string[]; max_potential_rate: number; description: string }> = {
  "Swiggy": {
    category: "Dining",
    icon: "🍔",
    best_cards: ["Swiggy HDFC", "Airtel Axis", "HDFC Infinia Metal", "Axis Ace"],
    max_potential_rate: 10.0,
    description: "10% cashback on Swiggy HDFC (up to ₹1,500/mo) and Airtel Axis (up to ₹500/mo)"
  },
  "Zomato": {
    category: "Dining",
    icon: "🍕",
    best_cards: ["Airtel Axis", "HDFC Infinia Metal", "Axis Ace", "SBI Cashback Card"],
    max_potential_rate: 10.0,
    description: "10% cashback on Airtel Axis, 9.9% on Infinia via SmartBuy, 5% on SBI Cashback"
  },
  "Amazon": {
    category: "Online Shopping",
    icon: "📦",
    best_cards: ["ICICI Amazon Pay", "SBI Cashback Card", "HDFC Millennia", "HDFC Infinia Metal"],
    max_potential_rate: 9.9,
    description: "5% uncapped on Amazon Pay ICICI, 5% on SBI Cashback (capped ₹5k), 9.9% via Infinia SmartBuy vouchers"
  },
  "Flipkart": {
    category: "Online Shopping",
    icon: "🛍️",
    best_cards: ["Axis Flipkart", "SBI Cashback Card", "HDFC Millennia", "HDFC Infinia Metal"],
    max_potential_rate: 9.9,
    description: "5% unlimited on Flipkart Axis, 5% on SBI Cashback, 5% on HDFC Millennia"
  },
  "Myntra": {
    category: "Online Shopping",
    icon: "👗",
    best_cards: ["HDFC Regalia Gold", "Axis Flipkart", "SBI Cashback Card", "HDFC Millennia"],
    max_potential_rate: 6.6,
    description: "6.6% via Regalia Gold 5x, 5% on Flipkart Axis, 5% on HDFC Millennia"
  },
  "Blinkit": {
    category: "Grocery",
    icon: "⚡",
    best_cards: ["SBI Cashback Card", "Swiggy HDFC", "Tata Neu Infinity HDFC"],
    max_potential_rate: 5.0,
    description: "5% on SBI Cashback Card and Swiggy HDFC"
  },
  "BigBasket": {
    category: "Grocery",
    icon: "🛒",
    best_cards: ["Tata Neu Infinity HDFC", "Airtel Axis", "SBI Cashback Card"],
    max_potential_rate: 10.0,
    description: "10% NeuCoins on Tata Neu Infinity, 10% on Airtel Axis"
  },
  "MakeMyTrip": {
    category: "Travel",
    icon: "✈️",
    best_cards: ["HDFC Infinia Metal", "Axis Atlas", "HDFC Diners Black", "SBI Cashback Card"],
    max_potential_rate: 16.5,
    description: "16.5% on Infinia/Diners Black, 10% in EDGE Miles on Axis Atlas"
  },
  "SmartBuy Flights": {
    category: "Travel",
    icon: "🛫",
    best_cards: ["HDFC Infinia Metal", "HDFC Diners Black", "HDFC Regalia Gold"],
    max_potential_rate: 16.5,
    description: "16.5% on Infinia & Diners Black via HDFC SmartBuy portal"
  },
  "SmartBuy Hotels": {
    category: "Travel",
    icon: "🏨",
    best_cards: ["HDFC Infinia Metal", "HDFC Diners Black"],
    max_potential_rate: 33.0,
    description: "Up to 33% value back on hotel bookings via HDFC SmartBuy"
  },
  "BookMyShow": {
    category: "Movies/Entertainment",
    icon: "🎬",
    best_cards: ["ICICI Sapphiro", "Axis Magnus", "IDFC First Wealth", "IndusInd Legend"],
    max_potential_rate: 50.0,
    description: "BOGO offers: Buy 1 Get 1 ticket free up to ₹500 off"
  },
  "Google Pay Utilities": {
    category: "Utilities",
    icon: "💡",
    best_cards: ["Axis Ace", "Airtel Axis", "SBI Prime"],
    max_potential_rate: 5.0,
    description: "5% cashback on bill payments & DTH via Google Pay on Axis Ace"
  },
  "BPCL Fuel": {
    category: "Fuel",
    icon: "⛽",
    best_cards: ["SBI BPCL Octane"],
    max_potential_rate: 7.25,
    description: "7.25% value back on BPCL fuel pumps across India"
  },
  "Uber": {
    category: "Travel",
    icon: "🚗",
    best_cards: ["HDFC Infinia Metal", "Axis Ace", "SBI Cashback Card"],
    max_potential_rate: 9.9,
    description: "9.9% on Infinia SmartBuy vouchers, 5% on SBI Cashback, 2% on Axis Ace"
  },
  "Zepto": {
    category: "Grocery",
    icon: "🚀",
    best_cards: ["SBI Cashback Card", "Swiggy HDFC", "Axis Ace"],
    max_potential_rate: 5.0,
    description: "5% cashback on SBI Cashback and Swiggy HDFC"
  }
};

export const POPULAR_MERCHANTS = Object.keys(VENDORS_METADATA);

// Detailed 26 Cards Database
export const CARDS_DATABASE: Record<string, CreditCardData> = {
  "HDFC Infinia Metal": {
    name: "HDFC Infinia Metal",
    bank: "HDFC Bank",
    network: "Visa Infinite",
    tier: "Super Premium",
    type: "points",
    annual_fee: 12500,
    fee_waiver_spend: 1000000,
    forex_markup: 2.0,
    domestic_lounges: "Unlimited (Primary + Add-on)",
    intl_lounges: "Unlimited (Priority Pass)",
    fuel_surcharge_waiver: 1.0,
    point_valuation: { flight_hotel: 1.00, air_miles: 1.00, vouchers: 0.50, cash: 0.30, default: 1.00 },
    rewards: { "Travel": 16.5, "Online Shopping": 3.3, "Dining": 3.3, "Grocery": 3.3, "International": 3.3, "Utilities": 3.3, "Movies/Entertainment": 3.3, "Other": 3.3 },
    vendor_rewards: { "SmartBuy Flights": 16.5, "SmartBuy Hotels": 33.0, "Apple (SmartBuy)": 16.5, "Amazon": 9.9, "Flipkart": 9.9, "Swiggy": 9.9, "Zomato": 9.9, "MakeMyTrip": 16.5, "Myntra": 9.9, "Uber": 9.9 },
    caps: { accelerated_monthly_points: 10000, accelerated_daily_points: 7500 },
    milestones: [{ spend: 1000000, benefit_value: 12500, description: "Annual Fee Waiver on ₹10L annual spend" }],
    welcome_gift: "12,500 Reward Points upon fee payment",
    summary: "India's undisputed king of reward cards. 3.3% base reward, up to 33% via SmartBuy with 1:1 point value.",
    apply_url: "https://www.hdfcbank.com/personal/pay/cards/credit-cards/infinia-credit-card",
    skin: {
      gradient: "linear-gradient(135deg, #18191E 0%, #0D0E11 50%, #20222B 100%)",
      accentColor: "#F59E0B",
      textColor: "#F8FAFC",
      subtextColor: "#94A3B8",
      chipColor: "#F59E0B",
      pattern: "metal",
      badge: "METAL • 33% MAX",
      tagline: "The Sovereign Metal Standard"
    }
  },

  "SBI Cashback Card": {
    name: "SBI Cashback Card",
    bank: "SBI Card",
    network: "Visa Signature",
    tier: "Cashback",
    type: "cashback",
    annual_fee: 999,
    fee_waiver_spend: 200000,
    forex_markup: 3.5,
    domestic_lounges: "None",
    intl_lounges: "None",
    fuel_surcharge_waiver: 1.0,
    point_valuation: { default: 1.00, cash: 1.00 },
    rewards: { "Online Shopping": 5.0, "Dining": 5.0, "Grocery": 5.0, "Travel": 5.0, "Movies/Entertainment": 5.0, "Utilities": 1.0, "Other": 1.0 },
    vendor_rewards: { "Amazon": 5.0, "Flipkart": 5.0, "Myntra": 5.0, "Swiggy": 5.0, "Zomato": 5.0, "Blinkit": 5.0, "Zepto": 5.0 },
    caps: { online_monthly_cashback: 5000 },
    milestones: [{ spend: 200000, benefit_value: 999, description: "Annual Fee Waiver on ₹2 Lakh annual spend" }],
    welcome_gift: "None",
    summary: "Flat 5% direct cashback on all online spends with ₹5,000 monthly cap. Auto-credited to statement.",
    apply_url: "https://www.sbicard.com/en/personal/credit-cards/rewards/cashback-sbi-card.page",
    skin: {
      gradient: "linear-gradient(135deg, #0A1E3F 0%, #030C1E 60%, #002B66 100%)",
      accentColor: "#00E5FF",
      textColor: "#FFFFFF",
      subtextColor: "#93C5FD",
      chipColor: "#38BDF8",
      pattern: "cyber",
      badge: "5% UNRESTRICTED ONLINE",
      tagline: "Flat Cashback Machine"
    }
  },

  "HDFC Millennia": {
    name: "HDFC Millennia",
    bank: "HDFC Bank",
    network: "Mastercard World",
    tier: "Mid-tier Premium",
    type: "cashback",
    annual_fee: 1000,
    fee_waiver_spend: 100000,
    forex_markup: 3.5,
    domestic_lounges: "4 visits/year (1 per quarter on ₹50k spend)",
    intl_lounges: "None",
    fuel_surcharge_waiver: 1.0,
    point_valuation: { cash: 1.00, default: 1.00 },
    rewards: { "Online Shopping": 5.0, "Dining": 5.0, "Grocery": 1.0, "Travel": 5.0, "Other": 1.0 },
    vendor_rewards: { "Amazon": 5.0, "Flipkart": 5.0, "Myntra": 5.0, "Swiggy": 5.0, "Zomato": 5.0, "Uber": 5.0, "BookMyShow": 5.0 },
    caps: { partner_monthly_cashback: 1000 },
    milestones: [{ spend: 100000, benefit_value: 1000, description: "Quarterly ₹1,000 gift voucher on ₹1L spend" }],
    welcome_gift: "1,000 CashPoints on membership fee payment",
    summary: "5% cashback on 10+ merchant partners (Amazon, Flipkart, Swiggy, Zomato, Uber) with ₹1,000 monthly partner cap.",
    apply_url: "https://www.hdfcbank.com/personal/pay/cards/credit-cards/millennia-credit-card",
    skin: {
      gradient: "linear-gradient(135deg, #0F172A 0%, #1E3A8A 50%, #0F2350 100%)",
      accentColor: "#60A5FA",
      textColor: "#F8FAFC",
      subtextColor: "#93C5FD",
      chipColor: "#E2E8F0",
      pattern: "waves",
      badge: "5% 10+ PARTNERS",
      tagline: "The Everyday Lifestyle Staple"
    }
  },

  "Axis Ace": {
    name: "Axis Ace",
    bank: "Axis Bank",
    network: "Visa Platinum",
    tier: "Cashback",
    type: "cashback",
    annual_fee: 499,
    fee_waiver_spend: 200000,
    forex_markup: 3.5,
    domestic_lounges: "4 visits/year (1 per quarter)",
    intl_lounges: "None",
    fuel_surcharge_waiver: 1.0,
    point_valuation: { cash: 1.00, default: 1.00 },
    rewards: { "Utilities": 5.0, "Dining": 4.0, "Online Shopping": 1.5, "Grocery": 1.5, "Travel": 1.5, "Other": 1.5 },
    vendor_rewards: { "Google Pay Utilities": 5.0, "Swiggy": 4.0, "Zomato": 4.0, "Ola": 4.0 },
    caps: { utility_monthly_cashback: 500, dining_monthly_cashback: 500 },
    milestones: [{ spend: 200000, benefit_value: 499, description: "Fee waiver on ₹2,00,000 annual spend" }],
    welcome_gift: "None",
    summary: "5% cashback on Utility bill payments via Google Pay, 4% on Swiggy/Zomato/Ola, 1.5% unlimited offline.",
    apply_url: "https://www.axisbank.com/retail/cards/credit-card/ace-credit-card",
    skin: {
      gradient: "linear-gradient(135deg, #1C1917 0%, #292524 50%, #14532D 100%)",
      accentColor: "#22C55E",
      textColor: "#F8FAFC",
      subtextColor: "#86EFAC",
      chipColor: "#E2E8F0",
      pattern: "grid",
      badge: "5% G-PAY UTILITIES",
      tagline: "The Bill Payment Champion"
    }
  },

  "Axis Atlas": {
    name: "Axis Atlas",
    bank: "Axis Bank",
    network: "Visa Signature",
    tier: "Miles / Travel",
    type: "miles",
    annual_fee: 5000,
    fee_waiver_spend: 0,
    forex_markup: 3.5,
    domestic_lounges: "Up to 12 visits/year (Tier-based)",
    intl_lounges: "Up to 6 visits/year (Tier-based)",
    fuel_surcharge_waiver: 1.0,
    point_valuation: { air_miles: 2.00, flight_hotel: 2.00, cash: 1.00, default: 2.00 },
    rewards: { "Travel": 10.0, "Online Shopping": 4.0, "Dining": 4.0, "Grocery": 4.0, "International": 4.0, "Other": 4.0 },
    vendor_rewards: { "MakeMyTrip": 10.0, "Airline Direct": 10.0, "Hotel Direct": 10.0 },
    caps: {},
    milestones: [
      { spend: 300000, benefit_value: 5000, description: "Silver Tier: 2,500 bonus EDGE Miles worth ₹5,000" },
      { spend: 750000, benefit_value: 10000, description: "Gold Tier: 5,000 bonus EDGE Miles worth ₹10,000" },
      { spend: 1500000, benefit_value: 20000, description: "Platinum Tier: 10,000 bonus EDGE Miles worth ₹20,000" }
    ],
    welcome_gift: "5,000 EDGE Miles (worth ₹10,000 in miles) upon 1st transaction within 30 days",
    summary: "India's premier travel card. 5 EDGE Miles (10%) on direct airlines/hotels, 2 EDGE Miles (4%) on all other spends.",
    apply_url: "https://www.axisbank.com/retail/cards/credit-card/atlas-credit-card",
    skin: {
      gradient: "linear-gradient(135deg, #1E1B4B 0%, #312E81 50%, #4338CA 100%)",
      accentColor: "#A5B4FC",
      textColor: "#F8FAFC",
      subtextColor: "#C7D2FE",
      chipColor: "#F59E0B",
      pattern: "aurora",
      badge: "10% DIRECT TRAVEL",
      tagline: "The Wanderlust Aviator"
    }
  },

  "ICICI Amazon Pay": {
    name: "ICICI Amazon Pay",
    bank: "ICICI Bank",
    network: "Visa Platinum",
    tier: "Lifetime Free",
    type: "cashback",
    annual_fee: 0,
    fee_waiver_spend: 0,
    forex_markup: 3.5,
    domestic_lounges: "None",
    intl_lounges: "None",
    fuel_surcharge_waiver: 1.0,
    point_valuation: { cash: 1.00, default: 1.00 },
    rewards: { "Online Shopping": 5.0, "Dining": 2.0, "Grocery": 2.0, "Utilities": 2.0, "Travel": 2.0, "Other": 1.0 },
    vendor_rewards: { "Amazon": 5.0, "Amazon Pay Recharges": 2.0, "Swiggy": 2.0, "Zomato": 2.0 },
    caps: {},
    milestones: [],
    welcome_gift: "Up to ₹2,000 in Amazon Pay Balance upon joining",
    summary: "Uncapped 5% cashback on Amazon for Prime members (3% for non-Prime), 2% on 100+ Amazon Pay partner merchants, 1% elsewhere.",
    apply_url: "https://www.icicibank.com/personal-banking/cards/credit-cards/amazon-pay-credit-card",
    skin: {
      gradient: "linear-gradient(135deg, #1A1A1A 0%, #282828 50%, #2C2016 100%)",
      accentColor: "#FF9900",
      textColor: "#FFFFFF",
      subtextColor: "#E2E8F0",
      chipColor: "#FF9900",
      pattern: "minimal",
      badge: "LIFETIME FREE • UNCAPPED",
      tagline: "The Zero-Fee Amazon Engine"
    }
  },

  "Swiggy HDFC": {
    name: "Swiggy HDFC",
    bank: "HDFC Bank",
    network: "Mastercard",
    tier: "Cashback",
    type: "cashback",
    annual_fee: 500,
    fee_waiver_spend: 200000,
    forex_markup: 3.5,
    domestic_lounges: "None",
    intl_lounges: "None",
    fuel_surcharge_waiver: 0.0,
    point_valuation: { cash: 1.00, default: 1.00 },
    rewards: { "Dining": 10.0, "Online Shopping": 5.0, "Grocery": 5.0, "Other": 1.0 },
    vendor_rewards: { "Swiggy": 10.0, "Instamart": 10.0, "Dineout": 10.0, "Amazon": 5.0, "Flipkart": 5.0, "Myntra": 5.0, "Nykaa": 5.0, "Blinkit": 5.0 },
    caps: { swiggy_monthly_cashback: 1500, online_monthly_cashback: 1500 },
    milestones: [{ spend: 200000, benefit_value: 500, description: "Fee waiver on ₹2L annual spend" }],
    welcome_gift: "3-Month Complimentary Swiggy One membership",
    summary: "10% cashback on Swiggy (Food, Instamart, Dineout, Genie) up to ₹1,500/mo. 5% cashback on top online merchants up to ₹1,500/mo.",
    apply_url: "https://www.hdfcbank.com/personal/pay/cards/credit-cards/swiggy-hdfc-bank-credit-card",
    skin: {
      gradient: "linear-gradient(135deg, #3B1B0A 0%, #1A0D07 50%, #EA580C 100%)",
      accentColor: "#FC8019",
      textColor: "#FFFFFF",
      subtextColor: "#FDBA74",
      chipColor: "#E2E8F0",
      pattern: "cyber",
      badge: "10% SWIGGY ECOSYSTEM",
      tagline: "Foodie & Quick-Commerce Giant"
    }
  },

  "Tata Neu Infinity HDFC": {
    name: "Tata Neu Infinity HDFC",
    bank: "HDFC Bank",
    network: "RuPay Select",
    tier: "Mid-tier Premium",
    type: "points",
    annual_fee: 1499,
    fee_waiver_spend: 300000,
    forex_markup: 2.0,
    domestic_lounges: "8 visits/year (2 per quarter)",
    intl_lounges: "4 visits/year (Priority Pass)",
    fuel_surcharge_waiver: 1.0,
    point_valuation: { default: 1.00, vouchers: 1.00 },
    rewards: { "Grocery": 10.0, "Online Shopping": 10.0, "Travel": 10.0, "UPI": 1.5, "Other": 1.5 },
    vendor_rewards: { "BigBasket": 10.0, "Croma": 10.0, "Tata 1mg": 10.0, "Tata CLiQ": 10.0, "Air India": 10.0, "Taj Hotels": 10.0 },
    caps: { upi_monthly_points: 500 },
    milestones: [{ spend: 300000, benefit_value: 1499, description: "Annual fee waiver on ₹3 Lakh annual spend" }],
    welcome_gift: "1,499 NeuCoins upon 1st spend within 30 days",
    summary: "10% NeuCoins back on Tata brands via Tata Neu App (BigBasket, Croma, Tata 1mg, Taj Hotels). 1.5% back on RuPay UPI payments.",
    apply_url: "https://www.hdfcbank.com/personal/pay/cards/credit-cards/tata-neu-infinity-credit-card",
    skin: {
      gradient: "linear-gradient(135deg, #2A0845 0%, #150020 50%, #640D5F 100%)",
      accentColor: "#D946EF",
      textColor: "#FFFFFF",
      subtextColor: "#F5D0FE",
      chipColor: "#FBBF24",
      pattern: "waves",
      badge: "10% TATA + RUPAY UPI",
      tagline: "The Unified Conglomerate Powerhouse"
    }
  },

  "Airtel Axis": {
    name: "Airtel Axis",
    bank: "Axis Bank",
    network: "Mastercard",
    tier: "Cashback",
    type: "cashback",
    annual_fee: 500,
    fee_waiver_spend: 0,
    forex_markup: 3.5,
    domestic_lounges: "4 visits/year (1 per quarter on ₹50k spend)",
    intl_lounges: "None",
    fuel_surcharge_waiver: 1.0,
    point_valuation: { cash: 1.00, default: 1.00 },
    rewards: { "Utilities": 10.0, "Dining": 10.0, "Grocery": 10.0, "Online Shopping": 1.0, "Other": 1.0 },
    vendor_rewards: { "Airtel Mobile/Broadband": 25.0, "Google Pay Utilities": 10.0, "Swiggy": 10.0, "Zomato": 10.0, "BigBasket": 10.0 },
    caps: { airtel_monthly_cashback: 250, utility_monthly_cashback: 250, food_grocery_monthly_cashback: 500 },
    milestones: [],
    welcome_gift: "₹500 Amazon gift card upon card activation within 30 days",
    summary: "25% cashback on Airtel Mobile, Broadband & DTH via Airtel Thanks App. 10% on Utility bills and 10% on Swiggy, Zomato, BigBasket.",
    apply_url: "https://www.axisbank.com/retail/cards/credit-card/airtel-axis-bank-credit-card",
    skin: {
      gradient: "linear-gradient(135deg, #1C0A0A 0%, #360E0E 50%, #EF4444 100%)",
      accentColor: "#EF4444",
      textColor: "#FFFFFF",
      subtextColor: "#FCA5A5",
      chipColor: "#E2E8F0",
      pattern: "grid",
      badge: "25% AIRTEL • 10% BILLS",
      tagline: "The Household Utility Powerhouse"
    }
  },

  "HDFC Diners Black": {
    name: "HDFC Diners Black",
    bank: "HDFC Bank",
    network: "Diners Club",
    tier: "Super Premium",
    type: "points",
    annual_fee: 10000,
    fee_waiver_spend: 800000,
    forex_markup: 2.0,
    domestic_lounges: "Unlimited (Primary + Add-on)",
    intl_lounges: "Unlimited",
    fuel_surcharge_waiver: 1.0,
    point_valuation: { flight_hotel: 1.00, air_miles: 1.00, vouchers: 0.50, cash: 0.30, default: 1.00 },
    rewards: { "Travel": 16.5, "Online Shopping": 3.3, "Dining": 6.6, "Grocery": 3.3, "International": 3.3, "Other": 3.3 },
    vendor_rewards: { "SmartBuy Flights": 16.5, "SmartBuy Hotels": 33.0, "Amazon": 9.9, "Flipkart": 9.9, "Swiggy": 9.9, "Zomato": 9.9 },
    caps: { accelerated_monthly_points: 7500 },
    milestones: [{ spend: 800000, benefit_value: 10000, description: "Annual fee waiver on ₹8L spend" }],
    welcome_gift: "10,000 Reward Points on fee payment",
    summary: "Elite competitor to Infinia. 3.3% base reward, up to 33% on SmartBuy, 2x on Weekend Dining, unlimited lounges worldwide.",
    apply_url: "https://www.hdfcbank.com/personal/pay/cards/credit-cards/diners-black",
    skin: {
      gradient: "linear-gradient(135deg, #111827 0%, #1F2937 50%, #0369A1 100%)",
      accentColor: "#38BDF8",
      textColor: "#FFFFFF",
      subtextColor: "#7DD3FC",
      chipColor: "#F59E0B",
      pattern: "metal",
      badge: "GLOBAL DINERS CLUB",
      tagline: "Super Premium Global Traveler"
    }
  },

  "Amex Platinum Travel": {
    name: "Amex Platinum Travel",
    bank: "American Express",
    network: "American Express",
    tier: "Miles / Travel",
    type: "points",
    annual_fee: 5000,
    fee_waiver_spend: 0,
    forex_markup: 3.5,
    domestic_lounges: "8 visits/year (2 per quarter)",
    intl_lounges: "None",
    fuel_surcharge_waiver: 0.0,
    point_valuation: { air_miles: 0.50, vouchers: 0.50, default: 0.50 },
    rewards: { "Online Shopping": 1.5, "Dining": 1.5, "Grocery": 1.5, "Travel": 1.5, "Other": 1.5 },
    vendor_rewards: {},
    caps: {},
    milestones: [
      { spend: 190000, benefit_value: 7500, description: "15,000 bonus Membership Rewards points on ₹1.9L spend" },
      { spend: 400000, benefit_value: 20000, description: "25,000 bonus MR points + ₹10,000 Taj Stay Voucher on ₹4L spend" }
    ],
    welcome_gift: "10,000 Membership Rewards points upon card activation",
    summary: "The undisputed milestone champion. Spend exactly ₹4,00,000 in a year to unlock 48,000 MR points + ₹10,000 Taj voucher (~9% net return).",
    apply_url: "https://www.americanexpress.com/in/credit-cards/platinum-travel-credit-card/",
    skin: {
      gradient: "linear-gradient(135deg, #1E293B 0%, #334155 50%, #475569 100%)",
      accentColor: "#94A3B8",
      textColor: "#F8FAFC",
      subtextColor: "#CBD5E1",
      chipColor: "#E2E8F0",
      pattern: "metal",
      badge: "MILESTONE MASTER • TAJ",
      tagline: "The 4-Lakh Milestone Benchmark"
    }
  },

  "SBI BPCL Octane": {
    name: "SBI BPCL Octane",
    bank: "SBI Card",
    network: "Visa",
    tier: "Cashback",
    type: "points",
    annual_fee: 1499,
    fee_waiver_spend: 200000,
    forex_markup: 3.5,
    domestic_lounges: "4 visits/year (1 per quarter)",
    intl_lounges: "None",
    fuel_surcharge_waiver: 1.0,
    point_valuation: { cash: 0.25, default: 0.25 },
    rewards: { "Fuel": 7.25, "Dining": 2.5, "Grocery": 2.5, "Movies/Entertainment": 2.5, "Other": 0.25 },
    vendor_rewards: { "BPCL Fuel": 7.25, "Bharatgas": 7.25 },
    caps: { fuel_monthly_points: 2500 },
    milestones: [{ spend: 200000, benefit_value: 1499, description: "Fee waiver on ₹2L spend" }],
    welcome_gift: "6,000 bonus reward points (worth ₹1,500) upon fee payment",
    summary: "7.25% value back on BPCL fuel (25 reward points per ₹100 spend + 1% surcharge waiver) capped at 2,500 points/billing cycle.",
    apply_url: "https://www.sbicard.com/en/personal/credit-cards/rewards/bpcl-sbi-card-octane.page",
    skin: {
      gradient: "linear-gradient(135deg, #064E3B 0%, #022C22 50%, #047857 100%)",
      accentColor: "#10B981",
      textColor: "#FFFFFF",
      subtextColor: "#6EE7B7",
      chipColor: "#F59E0B",
      pattern: "grid",
      badge: "7.25% BPCL FUEL",
      tagline: "The High-Octane Commuter"
    }
  },

  "Scapia Federal": {
    name: "Scapia Federal",
    bank: "Federal Bank",
    network: "Visa Signature",
    tier: "Lifetime Free",
    type: "miles",
    annual_fee: 0,
    fee_waiver_spend: 0,
    forex_markup: 0.0,
    domestic_lounges: "Unlimited domestic lounge access on spending ₹5,000/month",
    intl_lounges: "None",
    fuel_surcharge_waiver: 1.0,
    point_valuation: { flight_hotel: 0.20, default: 0.20 },
    rewards: { "Travel": 4.0, "Online Shopping": 2.0, "Dining": 2.0, "Grocery": 2.0, "International": 2.0, "Other": 2.0 },
    vendor_rewards: { "Scapia App Travel": 4.0 },
    caps: {},
    milestones: [],
    welcome_gift: "Zero forex markup for life + Instant virtual card in app",
    summary: "Lifetime Free card with TRUE 0% forex markup on all overseas transactions. Unlimited domestic lounge visits with just ₹5k/mo spend.",
    apply_url: "https://www.scapia.cards/",
    skin: {
      gradient: "linear-gradient(135deg, #0F766E 0%, #115E59 50%, #134E4A 100%)",
      accentColor: "#2DD4BF",
      textColor: "#FFFFFF",
      subtextColor: "#99F6E4",
      chipColor: "#E2E8F0",
      pattern: "aurora",
      badge: "0% ZERO FOREX • LTF",
      tagline: "The Modern Globe-Trotter"
    }
  },

  "Axis Magnus": {
    name: "Axis Magnus",
    bank: "Axis Bank",
    network: "Mastercard World Elite",
    tier: "Super Premium",
    type: "points",
    annual_fee: 12500,
    fee_waiver_spend: 2500000,
    forex_markup: 2.0,
    domestic_lounges: "Unlimited (Primary + Add-on)",
    intl_lounges: "Unlimited (Priority Pass with 8 guest visits)",
    fuel_surcharge_waiver: 1.0,
    point_valuation: { flight_hotel: 0.40, air_miles: 0.40, default: 0.40 },
    rewards: { "Travel": 12.0, "Online Shopping": 2.4, "Dining": 2.4, "Grocery": 2.4, "International": 2.4, "Other": 2.4 },
    vendor_rewards: { "Travel EDGE Flights": 12.0, "Travel EDGE Hotels": 12.0, "BookMyShow": 50.0 },
    caps: {},
    milestones: [{ spend: 2500000, benefit_value: 12500, description: "Fee waiver on ₹25 Lakh annual spend" }],
    welcome_gift: "Luxury domestic flight voucher or Postcard Hotels voucher worth fee",
    summary: "Ultra-premium card with unlimited airport VIP concierge meet & greet services, unlimited lounges with guests, 5:2 transfer ratio.",
    apply_url: "https://www.axisbank.com/retail/cards/credit-card/magnus-credit-card",
    skin: {
      gradient: "linear-gradient(135deg, #4A0E17 0%, #1A0508 50%, #7F1D1D 100%)",
      accentColor: "#FBBF24",
      textColor: "#FFFFFF",
      subtextColor: "#FCA5A5",
      chipColor: "#F59E0B",
      pattern: "metal",
      badge: "VIP CONCIERGE & MEET",
      tagline: "Burgundy Elite Indulgence"
    }
  }
};

export const POPULAR_CARDS = Object.keys(CARDS_DATABASE);
