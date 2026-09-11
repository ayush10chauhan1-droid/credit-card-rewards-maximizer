# =====================================================================
# 🧠 SWIPESMART AI ENTERPRISE — INDIA'S PREMIER CREDIT CARD REWARD PLATFORM
# Production-Grade Multi-Card Wallet Optimizer, Matchmaker, & RAG Advisor
# =====================================================================

import json
from datetime import datetime
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from streamlit_float import float_init

# Core Engines & Databases
from data.cards_db import (
    CARDS_DATABASE,
    CARD_DATA,
    POPULAR_CARDS,
    CATEGORIES,
    CARD_TIERS,
    CARD_ISSUERS
)
from data.vendors_db import VENDORS_METADATA
from cards_data import VENDORS
from engine.calculator import (
    compare_cards,
    compare_monthly,
    calculate_card_annual_net,
    generate_smart_tips,
    get_reward_rate
)
from engine.wallet_optimizer import find_optimal_wallet_strategy
from engine.matchmaker import analyze_spend_gaps, recommend_next_cards
from engine.rag_service import search_knowledge_base, build_rag_context
from engine.llm_advisor import (
    explain_single_purchase,
    explain_wallet_strategy,
    explain_matchmaker_recommendation,
    chat_with_copilot
)

# ─────────────────────────────────────────────────────────────────────
# APP CONFIGURATION
# ─────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="SwipeSmart AI Enterprise — Credit Card Maximizer",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="expanded",
)

float_init(theme=False)

# Session State Initialization
if "chat_open" not in st.session_state:
    st.session_state.chat_open = False
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "chat_input_key" not in st.session_state:
    st.session_state.chat_input_key = 0
if "user_wallet" not in st.session_state:
    st.session_state.user_wallet = ["SBI Cashback Card", "HDFC Millennia", "Axis Ace"]
if "spending_profile" not in st.session_state:
    st.session_state.spending_profile = {
        "Online Shopping": 15000.0,
        "Dining": 8000.0,
        "Grocery": 10000.0,
        "Travel": 12000.0,
        "Utilities": 5000.0,
        "Movies/Entertainment": 2000.0,
        "Fuel": 4000.0,
        "International": 0.0,
        "UPI": 3000.0,
        "Other": 5000.0
    }

def toggle_chat():
    st.session_state.chat_open = not st.session_state.chat_open

def clear_chat():
    st.session_state.chat_history = []


# ─────────────────────────────────────────────────────────────────────
# HIGH-END FINTECH DESIGN SYSTEM (CSS)
# ─────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;700&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

    /* CSS Variables & Tokens */
    :root {
        --bg-main: #07070e;
        --bg-card: rgba(15, 16, 32, 0.65);
        --bg-card-hover: rgba(23, 25, 48, 0.85);
        --border-subtle: rgba(99, 102, 241, 0.16);
        --border-focus: rgba(99, 102, 241, 0.45);
        --primary: #6366f1;
        --accent: #14b8a6;
        --accent-glow: #5eead4;
        --purple: #a855f7;
        --text-bright: #f3f4f8;
        --text-sub: #9ca3af;
        --text-dim: #64748b;
    }

    /* Keyframes */
    @keyframes float { 0%,100%{transform:translateY(0)} 50%{transform:translateY(-6px)} }
    @keyframes shimmer { 0%{background-position:-200% center} 100%{background-position:200% center} }
    @keyframes glowPulse { 0%,100%{box-shadow:0 0 20px rgba(20,184,166,0.15)} 50%{box-shadow:0 0 35px rgba(20,184,166,0.35)} }
    @keyframes popIn { 0%{opacity:0;transform:scale(0.9) translateY(15px)} 100%{opacity:1;transform:scale(1) translateY(0)} }

    /* Base Styling */
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    /* Streamlit Chrome Removal */
    #MainMenu {visibility: hidden !important;}
    footer {visibility: hidden !important;}
    header {visibility: hidden !important;}
    .stDeployButton {display: none !important;}
    [data-testid="stToolbar"] {display: none !important;}
    [data-testid="stDecoration"] {display: none !important;}
    [data-testid="stStatusWidget"] {display: none !important;}
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 3rem !important;
        max-width: 1350px !important;
    }

    p, span, label, div, li {
        color: #cbd5e1;
    }
    b, strong {
        color: #f1f5f9 !important;
    }

    /* Scrollbars */
    ::-webkit-scrollbar { width: 6px; height: 6px; }
    ::-webkit-scrollbar-track { background: #07070e; }
    ::-webkit-scrollbar-thumb { background: linear-gradient(180deg, #6366f1, #14b8a6); border-radius: 3px; }

    /* Hero Banner */
    .hero-container {
        background: linear-gradient(135deg, rgba(16, 17, 36, 0.95) 0%, rgba(22, 24, 52, 0.9) 100%);
        border: 1px solid rgba(99, 102, 241, 0.25);
        border-radius: 20px;
        padding: 2.2rem 2.8rem;
        margin-bottom: 2rem;
        position: relative;
        overflow: hidden;
        box-shadow: 0 16px 45px rgba(0, 0, 0, 0.35);
    }
    .hero-container::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0; height: 2px;
        background: linear-gradient(90deg, transparent, #6366f1, #14b8a6, #a855f7, transparent);
        background-size: 200% auto;
        animation: shimmer 4s linear infinite;
    }
    .hero-title {
        font-size: 2.4rem;
        font-weight: 800;
        margin: 0;
        letter-spacing: -0.5px;
        background: linear-gradient(135deg, #ffffff 0%, #cbd5e1 50%, #94a3b8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .hero-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        padding: 4px 12px;
        background: rgba(20, 184, 166, 0.12);
        border: 1px solid rgba(20, 184, 166, 0.3);
        border-radius: 20px;
        font-size: 0.72rem;
        font-weight: 600;
        color: #5eead4 !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 0.8rem;
    }
    .hero-sub {
        font-size: 1.02rem;
        color: #94a3b8 !important;
        margin-top: 0.4rem;
        max-width: 820px;
        line-height: 1.5;
    }
    .hero-metrics {
        display: flex;
        gap: 2.2rem;
        margin-top: 1.4rem;
        flex-wrap: wrap;
    }
    .hero-metric-box {
        background: rgba(10, 11, 24, 0.6);
        border: 1px solid rgba(99, 102, 241, 0.15);
        border-radius: 12px;
        padding: 0.6rem 1.2rem;
    }
    .hero-metric-val {
        font-size: 1.3rem;
        font-weight: 700;
        color: #f8fafc !important;
        font-family: 'JetBrains Mono', monospace;
    }
    .hero-metric-lbl {
        font-size: 0.72rem;
        color: #64748b !important;
        text-transform: uppercase;
        letter-spacing: 0.8px;
    }

    /* Winner Banner */
    .winner-banner {
        background: linear-gradient(135deg, rgba(8, 28, 26, 0.95) 0%, rgba(13, 38, 36, 0.9) 100%);
        border: 1px solid rgba(20, 184, 166, 0.4);
        border-radius: 18px;
        padding: 1.8rem 2.2rem;
        text-align: center;
        margin: 1.5rem 0;
        position: relative;
        overflow: hidden;
        animation: glowPulse 3s ease-in-out infinite;
    }
    .winner-banner .trophy { font-size: 2.3rem; animation: float 3s ease-in-out infinite; display: inline-block; }
    .winner-banner h2 {
        font-size: 1.9rem;
        margin: 0.4rem 0 0.2rem;
        background: linear-gradient(135deg, #5eead4, #14b8a6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .winner-banner .highlight {
        color: #5eead4 !important;
        font-weight: 700;
        font-family: 'JetBrains Mono', monospace;
    }

    /* Cards & Tiles */
    .fintech-card {
        background: rgba(15, 16, 32, 0.6);
        backdrop-filter: blur(16px);
        border: 1px solid rgba(99, 102, 241, 0.14);
        border-radius: 16px;
        padding: 1.4rem;
        transition: all 0.25s ease;
        position: relative;
        overflow: hidden;
    }
    .fintech-card:hover {
        border-color: rgba(99, 102, 241, 0.35);
        transform: translateY(-3px);
        box-shadow: 0 12px 30px rgba(0, 0, 0, 0.25);
    }
    .fintech-card.winner-card {
        border-color: rgba(20, 184, 166, 0.4);
        background: rgba(10, 28, 26, 0.6);
    }
    .card-title {
        font-size: 1.05rem;
        font-weight: 700;
        color: #f8fafc !important;
        margin-bottom: 0.4rem;
    }
    .card-reward-amount {
        font-size: 1.8rem;
        font-weight: 800;
        font-family: 'JetBrains Mono', monospace;
        margin: 0.3rem 0;
        color: #5eead4 !important;
    }
    .card-reward-sub {
        font-size: 0.8rem;
        color: #94a3b8 !important;
    }

    /* Tags & Pills */
    .badge-pill {
        display: inline-block;
        padding: 3px 10px;
        border-radius: 20px;
        font-size: 0.7rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .pill-cashback { background: rgba(20,184,166,0.15); color:#5eead4 !important; border:1px solid rgba(20,184,166,0.3); }
    .pill-points { background: rgba(99,102,241,0.15); color:#a5b4fc !important; border:1px solid rgba(99,102,241,0.3); }
    .pill-miles { background: rgba(168,85,247,0.15); color:#d8b4fe !important; border:1px solid rgba(168,85,247,0.3); }

    /* Routing Table Card */
    .route-item {
        background: rgba(15, 16, 32, 0.7);
        border: 1px solid rgba(99, 102, 241, 0.12);
        border-radius: 14px;
        padding: 1rem 1.4rem;
        margin-bottom: 0.7rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 10px;
        transition: all 0.2s;
    }
    .route-item:hover {
        background: rgba(20, 22, 45, 0.8);
        border-color: rgba(99, 102, 241, 0.25);
    }
    .route-cat {
        font-weight: 600;
        font-size: 0.95rem;
        color: #f1f5f9 !important;
    }
    .route-card-name {
        color: #5eead4 !important;
        font-weight: 700;
        font-size: 0.95rem;
    }
    .route-metric {
        font-family: 'JetBrains Mono', monospace;
        font-weight: 700;
        color: #cbd5e1 !important;
    }

    /* AI Executive Box */
    .ai-executive-box {
        background: linear-gradient(135deg, rgba(19, 18, 42, 0.7) 0%, rgba(26, 22, 54, 0.6) 100%);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(168, 85, 247, 0.25);
        border-radius: 18px;
        padding: 1.6rem 2rem;
        margin-top: 1.2rem;
        line-height: 1.7;
        position: relative;
    }
    .ai-executive-box::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0; height: 2px;
        background: linear-gradient(90deg, transparent, #a855f7, #6366f1, transparent);
    }
    .ai-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: rgba(168, 85, 247, 0.15);
        border: 1px solid rgba(168, 85, 247, 0.35);
        color: #d8b4fe !important;
        font-size: 0.7rem;
        font-weight: 700;
        padding: 3px 10px;
        border-radius: 16px;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        margin-bottom: 0.8rem;
    }

    /* Section Headers */
    .sec-heading {
        font-size: 0.88rem;
        font-weight: 700;
        color: #94a3b8 !important;
        text-transform: uppercase;
        letter-spacing: 1.4px;
        margin: 2rem 0 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 1px solid rgba(99, 102, 241, 0.12);
    }

    /* Streamlit overrides */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: rgba(13, 14, 28, 0.8);
        padding: 6px;
        border-radius: 14px;
        border: 1px solid rgba(99, 102, 241, 0.15);
    }
    .stTabs [data-baseweb="tab"] {
        border-radius: 10px;
        padding: 8px 18px;
        color: #94a3b8;
        font-weight: 600;
        font-size: 0.9rem;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.25), rgba(20, 184, 166, 0.25)) !important;
        color: #f8fafc !important;
        border: 1px solid rgba(20, 184, 166, 0.35) !important;
    }
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────
# HERO BANNER
# ─────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="hero-container">
    <div class="hero-badge">⚡ SwipeSmart AI Enterprise v3.0</div>
    <div class="hero-title">Credit Card Reward Maximizer</div>
    <div class="hero-sub">
        India's most advanced AI-powered credit card decision engine. Optimize single swipes,
        route category spends across your wallet, plug spending leaks, and unlock maximum financial returns.
    </div>
    <div class="hero-metrics">
        <div class="hero-metric-box">
            <div class="hero-metric-val">{len(CARDS_DATABASE)}</div>
            <div class="hero-metric-lbl">Premier Indian Cards</div>
        </div>
        <div class="hero-metric-box">
            <div class="hero-metric-val">{len(CATEGORIES)}</div>
            <div class="hero-metric-lbl">Spend Categories</div>
        </div>
        <div class="hero-metric-box">
            <div class="hero-metric-val">{len(VENDORS_METADATA)}+</div>
            <div class="hero-metric-lbl">Partner Merchants</div>
        </div>
        <div class="hero-metric-box">
            <div class="hero-metric-val">Gemini 2.5</div>
            <div class="hero-metric-lbl">AI & RAG Engine</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────
# SIDEBAR CONTROLS
# ─────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 💳 Your Card Wallet")
    st.caption("Select the cards you currently own to tailor recommendations and wallet routing.")

    st.session_state.user_wallet = st.multiselect(
        "Cards in Wallet",
        options=POPULAR_CARDS,
        default=st.session_state.user_wallet,
        help="Select cards you carry in your physical or digital wallet."
    )

    st.markdown("---")
    st.markdown("### ⚙️ Valuation & Engine")
    val_mode = st.selectbox(
        "Point Redemption Preference",
        options=["default", "cash", "flight_hotel", "air_miles", "vouchers"],
        format_func=lambda x: {
            "default": "Optimal (Best Value Option)",
            "cash": "Statement Credit / Direct Cash",
            "flight_hotel": "Flights & Luxury Hotels (SmartBuy / Travel EDGE)",
            "air_miles": "Airline Miles (Accor / Air India / Singapore)",
            "vouchers": "Brand Shopping Vouchers"
        }.get(x, x),
        help="Determines how non-cashback reward points are converted to real ₹ value."
    )

    st.markdown("---")
    st.markdown("### 💬 SwipeSmart Copilot")
    if st.button("Open AI Assistant 🧠", use_container_width=True, type="secondary"):
        toggle_chat()
        st.rerun()

    st.markdown("---")
    st.caption("SwipeSmart Enterprise v3.0 — Built with Gemini & RAG")


# ─────────────────────────────────────────────────────────────────────
# MAIN NAVIGATION TABS
# ─────────────────────────────────────────────────────────────────────
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🛒 Instant Swipe Recommender",
    "👛 Multi-Card Wallet Router",
    "🎯 AI Card Matchmaker & Gaps",
    "⚖️ Head-to-Head Comparison Matrix",
    "📚 Card Rules & RAG Knowledge Hub"
])


# =====================================================================
# TAB 1: INSTANT SWIPE RECOMMENDER (SINGLE PURCHASE)
# =====================================================================
with tab1:
    st.markdown('<div class="sec-heading">🛒 SINGLE TRANSACTION OPTIMIZER</div>', unsafe_allow_html=True)
    st.markdown("Choose whether to compare only the cards in your wallet, or search the entire 26-card database.")

    c1, c2, c3, c4 = st.columns([2, 2, 2, 2])
    with c1:
        eval_scope = st.radio("Evaluation Scope", ["My Wallet Only", "All 26 Database Cards"], horizontal=True)
    with c2:
        category = st.selectbox("Spend Category", CATEGORIES, index=0, key="t1_cat")
    with c3:
        available_merchants = VENDORS.get(category, [])
        merchant_choice = st.selectbox("Partner Merchant (Optional)", ["— General / Any Merchant —"] + available_merchants, key="t1_vendor")
        vendor = None if merchant_choice == "— General / Any Merchant —" else merchant_choice
    with c4:
        amount = st.number_input("Purchase Amount (₹)", min_value=50, max_value=2000000, value=5000, step=500, key="t1_amt")

    target_cards = st.session_state.user_wallet if eval_scope == "My Wallet Only" else POPULAR_CARDS

    if not target_cards:
        st.warning("⚠️ No cards selected. Please choose cards in the sidebar or switch to 'All 26 Database Cards'.")
    else:
        comp = compare_cards(target_cards, category, amount, vendor, valuation_mode=val_mode)
        results = comp["results"]
        best_card = comp["best_card"]
        best_reward = comp["best_reward"]

        if results:
            vendor_display = f"at {vendor}" if vendor else f"in {category}"
            st.markdown(f"""
            <div class="winner-banner">
                <div class="trophy">🏆</div>
                <h2>{best_card}</h2>
                <div>
                    Earns <span class="highlight">₹{best_reward:.2f}</span> on ₹{amount:,} {vendor_display}
                </div>
            </div>
            """, unsafe_allow_html=True)

            # Card Grid
            st.markdown('<div class="sec-heading">📊 CARD REWARD RANKINGS</div>', unsafe_allow_html=True)
            cols = st.columns(min(len(results), 4))
            for idx, r in enumerate(results[:8]):
                with cols[idx % len(cols)]:
                    is_winner = r["card"] == best_card
                    cls = "fintech-card winner-card" if is_winner else "fintech-card"
                    crown = "👑 " if is_winner else ""
                    pill_class = f"pill-{r['type']}" if r['type'] in ["cashback", "points", "miles"] else "pill-cashback"

                    st.markdown(f"""
                    <div class="{cls}">
                        <div class="card-title">{crown}{r['card']}</div>
                        <div class="card-reward-amount">₹{r['reward']:.2f}</div>
                        <div class="card-reward-sub">{r['rate']}% · {r['source']}</div>
                        <div class="card-reward-sub" style="margin-top:4px;">Fee: ₹{r['annual_fee']:,}/yr · {r['network']}</div>
                        <div style="margin-top:8px;">
                            <span class="badge-pill {pill_class}">{r['type']}</span>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    st.write("")

            # Visual Comparison
            st.markdown('<div class="sec-heading">📈 VISUAL REWARD COMPARISON</div>', unsafe_allow_html=True)
            top_chart_cards = results[:8]
            fig = go.Figure()
            fig.add_trace(go.Bar(
                x=[r["card"] for r in top_chart_cards],
                y=[r["reward"] for r in top_chart_cards],
                text=[f"₹{r['reward']:.2f}" for r in top_chart_cards],
                textposition="outside",
                marker_color=["#14b8a6" if r["card"] == best_card else "#6366f1" for r in top_chart_cards],
                marker_line=dict(width=0),
            ))
            fig.update_layout(
                xaxis_title=None,
                yaxis_title="Estimated Net Reward (₹)",
                height=380,
                font=dict(family="Plus Jakarta Sans", size=12, color="#94a3b8"),
                plot_bgcolor="rgba(0,0,0,0)",
                paper_bgcolor="rgba(0,0,0,0)",
                xaxis=dict(tickangle=-25, gridcolor="rgba(0,0,0,0)"),
                yaxis=dict(gridcolor="rgba(99,102,241,0.1)"),
                margin=dict(t=25, b=70, l=10, r=10),
            )
            st.plotly_chart(fig, use_container_width=True)

            # Smart Tips
            tips = generate_smart_tips(results, best_card, amount, category, vendor)
            if tips:
                st.markdown('<div class="sec-heading">💡 ACTIONABLE FINTECH ADVICE</div>', unsafe_allow_html=True)
                t_cols = st.columns(min(len(tips), 3))
                for idx, t in enumerate(tips):
                    with t_cols[idx % len(t_cols)]:
                        st.markdown(f"""
                        <div class="fintech-card" style="padding:1rem;">
                            <div style="font-weight:700; color:#f1f5f9 !important;">{t['icon']} {t['title']}</div>
                            <div style="font-size:0.84rem; color:#94a3b8 !important; margin-top:0.4rem; line-height:1.5;">{t['text']}</div>
                        </div>
                        """, unsafe_allow_html=True)

            # AI Rationale
            st.markdown('<div class="sec-heading">🤖 SWIPESMART AI RATIONALE</div>', unsafe_allow_html=True)
            comp_text = "\n".join([f"{r['card']}: {r['rate']}% ({r['source']}) = ₹{r['reward']:.2f}" for r in results[:5]])
            ai_exp = explain_single_purchase(best_card, comp_text, amount, category, vendor)
            st.markdown(f"""
            <div class="ai-executive-box">
                <div class="ai-badge">🧠 SwipeSmart Neural Advisor</div>
                <div style="color:#e2e8f0 !important; font-size:0.95rem;">{ai_exp}</div>
            </div>
            """, unsafe_allow_html=True)

            # Export
            st.markdown('<div class="sec-heading">📤 EXPORT TRANSACTION REPORT</div>', unsafe_allow_html=True)
            export_payload = {
                "report": "SwipeSmart Single Transaction Optimizer",
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "category": category,
                "vendor": vendor,
                "amount": amount,
                "best_card": best_card,
                "best_reward": best_reward,
                "rankings": results
            }
            ec1, ec2, ec3 = st.columns(3)
            with ec1:
                st.download_button("📥 Export JSON", json.dumps(export_payload, indent=2), "swipesmart_single.json", "application/json", use_container_width=True)
            with ec2:
                csv_data = "Card,Rate,Reward_INR,Source,AnnualFee\n" + "\n".join([f"{r['card']},{r['rate']},{r['reward']},{r['source']},{r['annual_fee']}" for r in results])
                st.download_button("📥 Export CSV", csv_data, "swipesmart_single.csv", "text/csv", use_container_width=True)
            with ec3:
                txt_summary = f"SwipeSmart Advice: Use {best_card} for ₹{best_reward:.2f} reward on ₹{amount:,} in {category} ({vendor or 'General'}).\n\nRankings:\n{comp_text}"
                st.download_button("📥 Export Text Summary", txt_summary, "swipesmart_single.txt", "text/plain", use_container_width=True)


# =====================================================================
# TAB 2: MULTI-CARD WALLET ROUTER (MONTHLY BUDGET OPTIMIZER)
# =====================================================================
with tab2:
    st.markdown('<div class="sec-heading">👛 CATEGORY-BY-CATEGORY WALLET ROUTER</div>', unsafe_allow_html=True)
    st.markdown("Enter your typical monthly expenditure. The routing engine automatically solves the multi-card assignment problem to maximize your aggregate annual return.")

    # Preset Budget Profiles
    p1, p2, p3, p4 = st.columns(4)
    with p1:
        if st.button("💼 Urban Tech Pro (₹70k/mo)", use_container_width=True):
            st.session_state.spending_profile = {
                "Online Shopping": 20000.0, "Dining": 12000.0, "Grocery": 12000.0,
                "Travel": 10000.0, "Utilities": 6000.0, "Movies/Entertainment": 3000.0,
                "Fuel": 3000.0, "International": 0.0, "UPI": 4000.0, "Other": 5000.0
            }
            st.rerun()
    with p2:
        if st.button("✈️ High Flyer / Traveler (₹1.5L/mo)", use_container_width=True):
            st.session_state.spending_profile = {
                "Online Shopping": 25000.0, "Dining": 20000.0, "Grocery": 15000.0,
                "Travel": 50000.0, "Utilities": 8000.0, "Movies/Entertainment": 5000.0,
                "Fuel": 7000.0, "International": 15000.0, "UPI": 5000.0, "Other": 10000.0
            }
            st.rerun()
    with p3:
        if st.button("🏡 Family Household (₹85k/mo)", use_container_width=True):
            st.session_state.spending_profile = {
                "Online Shopping": 15000.0, "Dining": 8000.0, "Grocery": 25000.0,
                "Travel": 5000.0, "Utilities": 12000.0, "Movies/Entertainment": 4000.0,
                "Fuel": 6000.0, "International": 0.0, "UPI": 5000.0, "Other": 8000.0
            }
            st.rerun()
    with p4:
        if st.button("🌱 Minimalist (₹35k/mo)", use_container_width=True):
            st.session_state.spending_profile = {
                "Online Shopping": 8000.0, "Dining": 5000.0, "Grocery": 8000.0,
                "Travel": 2000.0, "Utilities": 4000.0, "Movies/Entertainment": 1500.0,
                "Fuel": 2500.0, "International": 0.0, "UPI": 2000.0, "Other": 2000.0
            }
            st.rerun()

    # Category inputs
    spend_cols = st.columns(5)
    cat_icons = {
        "Online Shopping": "🛍️", "Dining": "🍽️", "Grocery": "🛒", "Travel": "✈️",
        "Utilities": "💡", "Movies/Entertainment": "🎬", "Fuel": "⛽",
        "International": "🌍", "UPI": "📲", "Other": "📌"
    }

    for idx, cat in enumerate(CATEGORIES):
        with spend_cols[idx % 5]:
            icon = cat_icons.get(cat, "📌")
            curr_val = float(st.session_state.spending_profile.get(cat, 0.0))
            st.session_state.spending_profile[cat] = st.number_input(
                f"{icon} {cat}",
                min_value=0,
                max_value=2000000,
                value=int(curr_val),
                step=1000,
                key=f"m_spend_{cat}"
            )

    tot_monthly = sum(st.session_state.spending_profile.values())
    st.markdown(f"""
    <div style="background:rgba(15,16,32,0.7); border:1px solid rgba(99,102,241,0.2); border-radius:14px; padding:0.8rem 1.6rem; display:inline-flex; gap:2rem; align-items:center; margin:1rem 0;">
        <span style="color:#94a3b8 !important; text-transform:uppercase; font-size:0.75rem; letter-spacing:1px;">Monthly Budget</span>
        <span style="color:#5eead4 !important; font-size:1.3rem; font-weight:800; font-family:'JetBrains Mono',monospace;">₹{tot_monthly:,.0f}</span>
        <span style="color:#94a3b8 !important; text-transform:uppercase; font-size:0.75rem; letter-spacing:1px;">Annualized Spend</span>
        <span style="color:#a5b4fc !important; font-size:1.3rem; font-weight:800; font-family:'JetBrains Mono',monospace;">₹{tot_monthly*12:,.0f}</span>
    </div>
    """, unsafe_allow_html=True)

    if not st.session_state.user_wallet:
        st.warning("⚠️ Please select at least one card in the sidebar to run the wallet optimizer.")
    elif tot_monthly == 0:
        st.info("Enter spending values above to calculate optimal routing.")
    else:
        strategy = find_optimal_wallet_strategy(st.session_state.user_wallet, st.session_state.spending_profile, valuation_mode=val_mode)

        if "error" in strategy:
            st.error(strategy["error"])
        else:
            # High-level Metrics Row
            m1, m2, m3, m4 = st.columns(4)
            with m1:
                st.markdown(f"""
                <div class="fintech-card">
                    <div style="font-size:0.72rem; color:#94a3b8 !important; text-transform:uppercase;">Optimized Monthly Rewards</div>
                    <div style="font-size:1.7rem; font-weight:800; font-family:'JetBrains Mono',monospace; color:#5eead4 !important;">₹{strategy['total_optimized_monthly_reward']:,.2f}</div>
                </div>
                """, unsafe_allow_html=True)
            with m2:
                st.markdown(f"""
                <div class="fintech-card">
                    <div style="font-size:0.72rem; color:#94a3b8 !important; text-transform:uppercase;">Net Annual Return (After Fees)</div>
                    <div style="font-size:1.7rem; font-weight:800; font-family:'JetBrains Mono',monospace; color:#14b8a6 !important;">₹{strategy['net_optimized_yearly_return']:,.2f}</div>
                </div>
                """, unsafe_allow_html=True)
            with m3:
                st.markdown(f"""
                <div class="fintech-card">
                    <div style="font-size:0.72rem; color:#94a3b8 !important; text-transform:uppercase;">Effective Annual ROI</div>
                    <div style="font-size:1.7rem; font-weight:800; font-family:'JetBrains Mono',monospace; color:#a5b4fc !important;">{strategy['optimized_roi_pct']:.2f}%</div>
                </div>
                """, unsafe_allow_html=True)
            with m4:
                st.markdown(f"""
                <div class="fintech-card">
                    <div style="font-size:0.72rem; color:#94a3b8 !important; text-transform:uppercase;">Multi-Card Synergy Bonus</div>
                    <div style="font-size:1.7rem; font-weight:800; font-family:'JetBrains Mono',monospace; color:#f59e0b !important;">+₹{strategy['synergy_vs_single']:,.2f}/yr</div>
                </div>
                """, unsafe_allow_html=True)

            # Routing Table
            st.markdown('<div class="sec-heading">🧭 OPTIMAL CARD SWIPE ASSIGNMENT</div>', unsafe_allow_html=True)
            st.markdown("For each expense category, swipe the assigned card below:")

            assignments = strategy["category_assignments"]
            for cat, data in assignments.items():
                cap_tag = f"<span style='color:#f59e0b; font-size:0.75rem; margin-left:8px;'>⚠️ {data['cap_note']}</span>" if data["cap_note"] else ""
                st.markdown(f"""
                <div class="route-item">
                    <div style="min-width:200px;">
                        <span class="route-cat">{cat}</span>
                        <div style="font-size:0.78rem; color:#64748b !important;">Monthly Spend: ₹{data['spend']:,}</div>
                    </div>
                    <div style="min-width:260px;">
                        <div class="route-card-name">💳 {data['assigned_card']} {cap_tag}</div>
                        <div style="font-size:0.78rem; color:#94a3b8 !important;">{data['source']} ({data['effective_rate']}%)</div>
                    </div>
                    <div>
                        <div class="route-metric" style="color:#5eead4 !important;">₹{data['monthly_reward']:,.2f}/mo</div>
                        <div style="font-size:0.75rem; color:#64748b !important;">₹{data['yearly_reward']:,.2f}/yr</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

            # Visualizations
            st.markdown('<div class="sec-heading">📊 WALLET SPEND & REWARD DISTRIBUTION</div>', unsafe_allow_html=True)
            c_chart1, c_chart2 = st.columns(2)

            with c_chart1:
                # Doughnut chart of categories
                cat_names = [c for c, d in assignments.items()]
                cat_rewards = [d["monthly_reward"] for c, d in assignments.items()]
                fig_pie = px.pie(
                    names=cat_names,
                    values=cat_rewards,
                    hole=0.55,
                    color_discrete_sequence=["#14b8a6", "#6366f1", "#a855f7", "#3b82f6", "#f59e0b", "#ec4899", "#10b981", "#8b5cf6"]
                )
                fig_pie.update_traces(textinfo="label+value", texttemplate="%{label}<br>₹%{value:.0f}")
                fig_pie.update_layout(
                    title="Reward Contribution by Category (Monthly)",
                    height=360,
                    font=dict(family="Plus Jakarta Sans", size=11, color="#94a3b8"),
                    paper_bgcolor="rgba(0,0,0,0)",
                    margin=dict(t=35, b=20, l=10, r=10),
                    showlegend=False
                )
                st.plotly_chart(fig_pie, use_container_width=True)

            with c_chart2:
                # Workload distribution across cards
                dist = strategy["card_usage_distribution"]
                card_names_dist = list(dist.keys())
                card_spend_dist = [dist[c]["spend"] for c in card_names_dist]
                card_reward_dist = [dist[c]["reward"] for c in card_names_dist]

                fig_bar = go.Figure()
                fig_bar.add_trace(go.Bar(name="Monthly Spend (₹)", x=card_names_dist, y=card_spend_dist, marker_color="#6366f1"))
                fig_bar.add_trace(go.Bar(name="Monthly Reward (₹)", x=card_names_dist, y=card_reward_dist, marker_color="#14b8a6"))
                fig_bar.update_layout(
                    title="Card Volume vs Reward Yield",
                    height=360,
                    font=dict(family="Plus Jakarta Sans", size=11, color="#94a3b8"),
                    plot_bgcolor="rgba(0,0,0,0)",
                    paper_bgcolor="rgba(0,0,0,0)",
                    barmode="group",
                    margin=dict(t=35, b=40, l=10, r=10),
                    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
                )
                st.plotly_chart(fig_bar, use_container_width=True)

            # AI Summary
            st.markdown('<div class="sec-heading">🤖 AI EXECUTIVE PORTFOLIO SUMMARY</div>', unsafe_allow_html=True)
            strat_text = f"""
Total Monthly Spend: ₹{tot_monthly:,}
Net Optimized Annual Return: ₹{strategy['net_optimized_yearly_return']:,}
Single Card Benchmark ({strategy['best_single_card']['card']}): ₹{strategy['best_single_card']['net_yearly']:,}
Synergy Bonus: +₹{strategy['synergy_vs_single']:,}/yr
Assignments: {', '.join([f"{c} -> {d['assigned_card']}" for c, d in assignments.items()])}
"""
            exec_summary = explain_wallet_strategy(strat_text)
            st.markdown(f"""
            <div class="ai-executive-box">
                <div class="ai-badge">🧠 SwipeSmart Portfolio Intelligence</div>
                <div style="color:#e2e8f0 !important; font-size:0.95rem;">{exec_summary}</div>
            </div>
            """, unsafe_allow_html=True)


# =====================================================================
# TAB 3: AI CARD MATCHMAKER & GAP FINDER
# =====================================================================
with tab3:
    st.markdown('<div class="sec-heading">🎯 SPENDING LEAK ANALYSIS & CARD MATCHMAKER</div>', unsafe_allow_html=True)
    st.markdown("We analyze your monthly spend to find high-volume categories suffering from low reward rates, and calculate the exact incremental profit of adding new cards.")

    # Spend Gap Detection
    gaps = analyze_spend_gaps(st.session_state.user_wallet, st.session_state.spending_profile)

    if gaps:
        st.markdown("#### ⚠️ Detected Reward Leaks in Your Current Wallet")
        g_cols = st.columns(min(len(gaps), 3))
        for idx, g in enumerate(gaps[:3]):
            with g_cols[idx % 3]:
                st.markdown(f"""
                <div class="fintech-card" style="border-color:rgba(239,68,68,0.3); background:rgba(30,12,16,0.6);">
                    <div style="display:flex; justify-content:space-between;">
                        <span style="font-weight:700; color:#fca5a5 !important;">{g['category']}</span>
                        <span class="badge-pill" style="background:rgba(239,68,68,0.2); color:#fca5a5 !important;">{g['urgency']} Leak</span>
                    </div>
                    <div style="font-size:1.3rem; font-weight:800; font-family:'JetBrains Mono',monospace; color:#f87171 !important; margin:0.4rem 0;">
                        ₹{g['annual_leak_estimate']:,.0f}/yr leak
                    </div>
                    <div style="font-size:0.78rem; color:#94a3b8 !important;">
                        You spend ₹{g['monthly_spend']:,}/mo but only earn {g['current_rate']}% with {g['current_card']}.
                    </div>
                </div>
                """, unsafe_allow_html=True)
                st.write("")
    else:
        st.success("✅ Great job! Your current wallet has no glaring reward leaks (> ₹3k/mo at < 2.5%).")

    # Matchmaker Filters
    st.markdown('<div class="sec-heading">🏆 TOP RECOMMENDED CARDS TO ADD TO YOUR WALLET</div>', unsafe_allow_html=True)
    f1, f2 = st.columns([2, 2])
    with f1:
        lifestyle = st.selectbox("Lifestyle / Card Category Preference", ["All", "Lifetime Free", "Pure Cashback", "Travel & Lounges", "Super Premium"], index=0)
    with f2:
        max_fee_input = st.selectbox("Maximum Annual Fee Willing to Pay", ["Any Fee", "Under ₹1,000", "Under ₹3,000", "Zero Fee Only"], index=0)
        fee_limit = 0 if max_fee_input == "Zero Fee Only" else 1000 if max_fee_input == "Under ₹1,000" else 3000 if max_fee_input == "Under ₹3,000" else None

    recs = recommend_next_cards(st.session_state.user_wallet, st.session_state.spending_profile, lifestyle_filter=lifestyle, max_fee=fee_limit)

    if not recs:
        st.info("No unowned cards match your active filter criteria.")
    else:
        for idx, rec in enumerate(recs[:4]):
            is_top = (idx == 0)
            border_col = "rgba(20, 184, 166, 0.45)" if is_top else "rgba(99, 102, 241, 0.16)"
            badge_text = "🥇 #1 Top Match" if is_top else f"#{idx+1} Candidate"

            cats_conquered_str = ", ".join([f"**{c['category']}** ({c['new_rate']}%)" for c in rec["conquered_categories"][:3]]) if rec["conquered_categories"] else "General Spends"

            st.markdown(f"""
            <div class="fintech-card" style="border-color:{border_col}; margin-bottom:1rem;">
                <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap;">
                    <div>
                        <span class="hero-badge">{badge_text}</span>
                        <h3 style="margin:4px 0;">{rec['card']}</h3>
                        <div style="font-size:0.82rem; color:#94a3b8 !important;">{rec['bank']} · {rec['tier']} · Fee: ₹{rec['annual_fee']:,}/yr</div>
                    </div>
                    <div style="text-align:right;">
                        <div style="font-size:0.75rem; color:#94a3b8 !important; text-transform:uppercase;">Net Incremental Profit</div>
                        <div style="font-size:1.8rem; font-weight:800; font-family:'JetBrains Mono',monospace; color:#5eead4 !important;">+₹{rec['incremental_annual_profit']:,.2f}/yr</div>
                    </div>
                </div>
                <div style="margin-top:0.8rem; padding-top:0.8rem; border-top:1px solid rgba(99,102,241,0.12); display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px;">
                    <div style="font-size:0.85rem; color:#cbd5e1 !important;">
                        Takes over: {cats_conquered_str} · Lounge: {rec['domestic_lounges']}
                    </div>
                    <div>
                        <a href="{rec['apply_url']}" target="_blank" style="text-decoration:none;">
                            <button style="background:linear-gradient(135deg,#14b8a6,#0d9488); color:white; border:none; border-radius:8px; padding:6px 14px; font-weight:600; font-size:0.82rem; cursor:pointer;">
                                View Card Details ↗
                            </button>
                        </a>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        # AI Matchmaker Analysis
        top_rec = recs[0]
        st.markdown('<div class="sec-heading">🤖 AI MATCHMAKER RATIONALE</div>', unsafe_allow_html=True)
        spend_summary_str = f"Monthly spends: {', '.join([f'{c}: ₹{int(s):,}' for c, s in st.session_state.spending_profile.items() if s > 0])}"
        match_exp = explain_matchmaker_recommendation(top_rec["card"], top_rec["incremental_annual_profit"], top_rec["conquered_categories"], spend_summary_str)
        st.markdown(f"""
        <div class="ai-executive-box">
            <div class="ai-badge">🧠 Matchmaker Strategic Takeaway</div>
            <div style="color:#e2e8f0 !important; font-size:0.95rem;">{match_exp}</div>
        </div>
        """, unsafe_allow_html=True)


# =====================================================================
# TAB 4: SIDE-BY-SIDE CARD COMPARISON MATRIX
# =====================================================================
with tab4:
    st.markdown('<div class="sec-heading">⚖️ HEAD-TO-HEAD COMPARISON MATRIX</div>', unsafe_allow_html=True)
    st.markdown("Compare up to 4 credit cards side-by-side across fees, lounges, forex markup, reward rates, and milestone rules.")

    compare_selection = st.multiselect(
        "Select up to 4 cards to compare:",
        options=POPULAR_CARDS,
        default=["HDFC Infinia Metal", "Axis Atlas", "SBI Cashback Card", "ICICI Amazon Pay"],
        max_selections=4
    )

    if not compare_selection:
        st.warning("Please select at least one card to compare.")
    else:
        matrix_cols = st.columns(len(compare_selection))

        for idx, c_name in enumerate(compare_selection):
            c_data = CARDS_DATABASE[c_name]
            with matrix_cols[idx]:
                st.markdown(f"""
                <div class="fintech-card" style="height:100%; padding:1.2rem;">
                    <div style="font-size:0.75rem; color:#94a3b8 !important; text-transform:uppercase;">{c_data['bank']}</div>
                    <h3 style="font-size:1.15rem; margin:4px 0 8px;">{c_name}</h3>
                    <span class="badge-pill pill-{c_data['type']}">{c_data['type']}</span>
                    <span style="font-size:0.75rem; color:#64748b !important; margin-left:6px;">{c_data['network']}</span>
                    
                    <div style="margin:1rem 0; padding:0.8rem 0; border-top:1px solid rgba(99,102,241,0.12); border-bottom:1px solid rgba(99,102,241,0.12);">
                        <div style="font-size:0.72rem; color:#64748b !important; text-transform:uppercase;">Annual Fee</div>
                        <div style="font-size:1.3rem; font-weight:800; font-family:'JetBrains Mono',monospace; color:#f8fafc !important;">
                            {'₹0 (Free)' if c_data['annual_fee'] == 0 else f"₹{c_data['annual_fee']:,}"}
                        </div>
                        <div style="font-size:0.72rem; color:#94a3b8 !important;">
                            {'No fee' if c_data['annual_fee'] == 0 else f"Waived at ₹{c_data['fee_waiver_spend']:,}"}
                        </div>
                    </div>

                    <div style="font-size:0.78rem; line-height:1.8;">
                        <div>🛫 <b>Domestic Lounge:</b> {c_data['domestic_lounges']}</div>
                        <div>🌍 <b>Intl Lounge:</b> {c_data['intl_lounges']}</div>
                        <div>💱 <b>Forex Markup:</b> {c_data['forex_markup']}%</div>
                        <div>⛽ <b>Fuel Waiver:</b> {c_data['fuel_surcharge_waiver']}%</div>
                    </div>

                    <div style="margin-top:1rem; font-size:0.75rem; color:#64748b !important; text-transform:uppercase; font-weight:700;">Top Category Rates</div>
                """, unsafe_allow_html=True)

                for cat in ["Online Shopping", "Dining", "Travel", "Grocery", "Utilities"]:
                    rate = c_data["rewards"].get(cat, c_data["rewards"].get("Other", 1.0))
                    st.markdown(f"""
                    <div style="display:flex; justify-content:space-between; font-size:0.78rem; margin:2px 0;">
                        <span style="color:#94a3b8 !important;">{cat}</span>
                        <span style="font-weight:700; color:#5eead4 !important; font-family:'JetBrains Mono',monospace;">{rate}%</span>
                    </div>
                    """, unsafe_allow_html=True)

                st.markdown(f"""
                    <div style="margin-top:1rem;">
                        <a href="{c_data['apply_url']}" target="_blank" style="text-decoration:none;">
                            <button style="width:100%; background:rgba(99,102,241,0.15); border:1px solid rgba(99,102,241,0.3); color:#a5b4fc; border-radius:8px; padding:6px; font-weight:600; font-size:0.8rem; cursor:pointer;">
                                Official Page ↗
                            </button>
                        </a>
                    </div>
                </div>
                """, unsafe_allow_html=True)


# =====================================================================
# TAB 5: CARD RULES & RAG KNOWLEDGE HUB
# =====================================================================
with tab5:
    st.markdown('<div class="sec-heading">📚 CARD RULES & RAG KNOWLEDGE HUB</div>', unsafe_allow_html=True)
    st.markdown("Search official issuer terms, monthly capping limits, exclusions (fuel, rent, wallet load), and lounge entry criteria.")

    rag_q = st.text_input("🔍 Search Card Rules & Policies (e.g. 'capping', 'lounge access', 'fuel waiver', 'SmartBuy'):", value="capping")

    if rag_q:
        docs = search_knowledge_base(rag_q, top_k=4)
        st.markdown(f"Found **{len(docs)}** relevant policy documents:")

        for d in docs:
            st.markdown(f"""
            <div class="fintech-card" style="margin-bottom:0.8rem;">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <div style="font-weight:700; color:#5eead4 !important; font-size:1.02rem;">{d['card']}</div>
                    <span class="badge-pill" style="background:rgba(99,102,241,0.15); color:#a5b4fc !important;">{d['topic']}</span>
                </div>
                <div style="font-size:0.85rem; color:#cbd5e1 !important; margin-top:0.6rem; line-height:1.6; white-space:pre-line;">
                    {d['text']}
                </div>
            </div>
            """, unsafe_allow_html=True)

    # Universal Exclusions Box
    st.markdown('<div class="sec-heading">⚠️ UNIVERSAL INDIAN CREDIT CARD EXCLUSIONS</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="fintech-card">
        <ul style="margin:0; padding-left:1.2rem; font-size:0.86rem; line-height:1.8; color:#94a3b8 !important;">
            <li><b>Wallet Reloads:</b> Transactions to Paytm, Amazon Pay, or Mobikwik wallet incur a 1% to 2.5% surcharge and 0 reward points across almost all issuers.</li>
            <li><b>Rent Payments:</b> Rent payments via CRED, Magicbricks, or Paytm incur a 1% convenience fee + 18% GST and earn zero rewards on HDFC, Axis, SBI, and ICICI.</li>
            <li><b>Fuel Transactions:</b> Exempt from standard reward points; eligible instead for 1% fuel surcharge waiver on transactions between ₹400 and ₹4,000.</li>
            <li><b>Government / Tax Payments:</b> Advance tax, income tax, and municipal property payments are excluded from reward programs.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────
# 💬 SWIPESMART AI COPILOT CHAT DRAWER / POPUP
# ─────────────────────────────────────────────────────────────────────
# Float ring & button
if not st.session_state.chat_open:
    st.markdown('<div class="pulse-ring" style="position:fixed; bottom:2rem; right:2rem; width:56px; height:56px; border-radius:50%; border:2px solid rgba(99,102,241,0.5); z-index:99998; pointer-events:none;"></div>', unsafe_allow_html=True)

btn_holder = st.container()
with btn_holder:
    if st.button("🧠" if not st.session_state.chat_open else "✕", key="floating_copilot_btn", on_click=toggle_chat):
        pass

btn_holder.float("position:fixed; bottom:2rem; right:2rem; z-index:99999; width:56px;")

# Chat Window Container
if st.session_state.chat_open:
    chat_box = st.container()
    with chat_box:
        st.markdown("""
        <div style="background:rgba(12,14,30,0.98); backdrop-filter:blur(24px); border:1px solid rgba(99,102,241,0.25); border-radius:18px 18px 0 0; padding:1rem 1.2rem; border-bottom:1px solid rgba(99,102,241,0.15); display:flex; align-items:center; gap:10px;">
            <div style="width:34px; height:34px; background:linear-gradient(135deg,#6366f1,#14b8a6); border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:1.1rem;">🧠</div>
            <div>
                <div style="font-weight:700; color:#f8fafc !important; font-size:0.95rem;">SwipeSmart Copilot</div>
                <div style="font-size:0.72rem; color:#5eead4 !important;">● Online · Expert on Indian Credit Cards</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Messages area
        if not st.session_state.chat_history:
            st.markdown("""
            <div style="background:rgba(10,11,24,0.95); padding:1.2rem; border-left:1px solid rgba(99,102,241,0.2); border-right:1px solid rgba(99,102,241,0.2);">
                <div style="text-align:center; padding:1rem 0;">
                    <div style="font-size:2rem;">👋</div>
                    <div style="font-weight:700; color:#f1f5f9 !important; font-size:0.92rem; margin-top:4px;">Ask me anything about credit cards!</div>
                    <div style="font-size:0.78rem; color:#64748b !important; margin-top:2px;">Capping limits, lounge rules, fee waivers, card recommendations</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            msg_html = ""
            for m in st.session_state.chat_history[-6:]:
                is_u = m["role"] == "user"
                bg = "linear-gradient(135deg, #6366f1, #4f46e5)" if is_u else "rgba(22, 24, 52, 0.85)"
                align = "right" if is_u else "left"
                col = "white" if is_u else "#cbd5e1"
                msg_html += f"""
                <div style="text-align:{align}; margin-bottom:8px;">
                    <div style="display:inline-block; max-width:85%; background:{bg}; color:{col} !important; padding:8px 14px; border-radius:12px; font-size:0.83rem; text-align:left; line-height:1.5;">
                        {m['content']}
                    </div>
                </div>
                """
            st.markdown(f"""
            <div style="background:rgba(10,11,24,0.95); padding:1rem; max-height:300px; overflow-y:auto; border-left:1px solid rgba(99,102,241,0.2); border-right:1px solid rgba(99,102,241,0.2);">
                {msg_html}
            </div>
            """, unsafe_allow_html=True)

        # Input Area
        copilot_input = st.text_input("Ask SwipeSmart...", placeholder="e.g. Best card for Swiggy? Or compare Infinia vs Atlas", key=f"copilot_in_{st.session_state.chat_input_key}", label_visibility="collapsed")
        cs1, cs2 = st.columns([3, 1])
        with cs1:
            if st.button("Send 🚀", key="copilot_send_btn", use_container_width=True) and copilot_input:
                st.session_state.chat_history.append({"role": "user", "content": copilot_input})

                history_context = "\n".join([f"{m['role']}: {m['content']}" for m in st.session_state.chat_history[-4:]])
                card_db_summary = "\n".join([f"{k}: {v['type']}, Fee ₹{v['annual_fee']}, Lounges: {v.get('domestic_lounges','None')}" for k, v in CARDS_DATABASE.items()])

                with st.spinner("Analyzing..."):
                    reply = chat_with_copilot(copilot_input, card_db_summary, history_context)

                st.session_state.chat_history.append({"role": "assistant", "content": reply})
                st.session_state.chat_input_key += 1
                st.rerun()

        with cs2:
            st.button("🗑️", key="copilot_clear_btn", on_click=clear_chat, use_container_width=True)

    chat_box.float("""
        position: fixed;
        bottom: 6rem;
        right: 2rem;
        width: 390px;
        max-height: 520px;
        z-index: 99998;
        background: rgba(10, 11, 24, 0.98);
        border: 1px solid rgba(99, 102, 241, 0.3);
        border-radius: 18px;
        box-shadow: 0 20px 60px rgba(0,0,0,0.6), 0 0 35px rgba(99,102,241,0.15);
        padding: 0;
        overflow: hidden;
    """)