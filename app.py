# =====================================================================
# 🧠 SWIPESMART AI — India's Smartest Credit Card Advisor
# Premium Fintech Dashboard + Floating AI Chatbot
# =====================================================================

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import json
from datetime import datetime
from streamlit_float import float_init

from cards_data import CARD_DATA, POPULAR_CARDS, CATEGORIES, VENDORS
from calculator import (
    compare_cards,
    compare_monthly,
    generate_smart_tips,
    get_reward_rate,
)
from llm import explain_recommendation, explain_monthly, chat_with_ai

# ─────────────────────────────────────────────
# INIT
# ─────────────────────────────────────────────

st.set_page_config(
    page_title="SwipeSmart AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Initialize float feature
float_init(theme=False)

# Session state
if "chat_open" not in st.session_state:
    st.session_state.chat_open = False
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "chat_input_key" not in st.session_state:
    st.session_state.chat_input_key = 0

def toggle_chat():
    st.session_state.chat_open = not st.session_state.chat_open

def clear_chat():
    st.session_state.chat_history = []


# ─────────────────────────────────────────────
# CARD DATABASE SUMMARY (for chatbot context)
# ─────────────────────────────────────────────

@st.cache_data
def build_card_summary():
    summary = ""
    for name, info in CARD_DATA.items():
        cats = ", ".join([f"{c}: {r}%" for c, r in info["rewards"].items()])
        vendors = ", ".join([f"{v}: {r}%" for v, r in info.get("vendor_rewards", {}).items()])
        summary += f"• {name} [{info['type']}] Fee: ₹{info['annual_fee']}/yr | {cats}"
        if vendors:
            summary += f" | Vendors: {vendors}"
        summary += "\n"
    return summary

CARD_SUMMARY = build_card_summary()


# ─────────────────────────────────────────────
# 🎨 CSS — EVERYTHING
# ─────────────────────────────────────────────

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

    /* ── Animations ── */
    @keyframes float { 0%,100%{transform:translateY(0)} 50%{transform:translateY(-8px)} }
    @keyframes shimmer { 0%{background-position:-200% center} 100%{background-position:200% center} }
    @keyframes glow-pulse { 0%,100%{box-shadow:0 0 20px rgba(99,102,241,0.15)} 50%{box-shadow:0 0 40px rgba(99,102,241,0.3)} }
    @keyframes border-glow { 0%,100%{border-color:rgba(99,102,241,0.3)} 50%{border-color:rgba(99,102,241,0.6)} }
    @keyframes fadeInUp { from{opacity:0;transform:translateY(20px)} to{opacity:1;transform:translateY(0)} }
    @keyframes pop-in { 0%{opacity:0;transform:scale(0.8) translateY(20px)} 100%{opacity:1;transform:scale(1) translateY(0)} }
    @keyframes pulse-ring { 0%{transform:scale(1);opacity:1} 100%{transform:scale(1.5);opacity:0} }

    /* ── Global ── */
    html, body, [class*="css"] { font-family: 'Space Grotesk', sans-serif; }
    .stApp {
        background: #07070e;
        background-image:
            radial-gradient(ellipse at 15% 10%, rgba(99,102,241,0.08) 0%, transparent 50%),
            radial-gradient(ellipse at 85% 30%, rgba(168,85,247,0.06) 0%, transparent 50%),
            radial-gradient(ellipse at 50% 80%, rgba(20,184,166,0.05) 0%, transparent 50%);
        color: #c8cad0;
    }
    h1,h2,h3,h4,h5,h6 { color: #f0f0f5 !important; }
    p,span,label,div,li { color: #a0a3b0 !important; }
    b,strong { color: #e0e0ea !important; }
    #MainMenu,footer,header { visibility: hidden; }
    .stDeployButton { display: none; }

    ::-webkit-scrollbar { width: 6px; }
    ::-webkit-scrollbar-track { background: #0a0a14; }
    ::-webkit-scrollbar-thumb { background: linear-gradient(180deg,#6366f1,#a855f7); border-radius: 3px; }

    /* ── Sidebar ── */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg,#0a0a18 0%,#0d0d1e 50%,#0a0a18 100%) !important;
        border-right: 1px solid rgba(99,102,241,0.15);
    }
    section[data-testid="stSidebar"] * { color: #b0b3c0 !important; }

    /* ── Hero ── */
    .hero {
        background: linear-gradient(135deg,#0f0f1e 0%,#13132b 100%);
        border: 1px solid rgba(99,102,241,0.2);
        border-radius: 24px; padding: 3rem 3.5rem; margin-bottom: 2rem;
        position: relative; overflow: hidden; animation: fadeInUp 0.6s ease-out;
    }
    .hero::before {
        content:''; position:absolute; top:0;left:0;right:0; height:2px;
        background: linear-gradient(90deg,transparent,#6366f1,#a855f7,#14b8a6,transparent);
        background-size: 200% auto; animation: shimmer 3s linear infinite;
    }
    .hero::after {
        content:''; position:absolute; top:-80px;right:-80px; width:250px;height:250px;
        background: radial-gradient(circle,rgba(99,102,241,0.1) 0%,transparent 70%); border-radius:50%;
    }
    .hero .brand {
        font-size:2.6rem; font-weight:700; margin:0;
        background: linear-gradient(135deg,#ffffff,#c7d2fe,#a5b4fc);
        -webkit-background-clip:text; -webkit-text-fill-color:transparent;
    }
    .hero .tagline { font-size:1.05rem; color:#6b70a0 !important; margin-top:0.5rem; }
    .hero .stats-row { display:flex; gap:2rem; margin-top:1.5rem; }
    .hero .stat-number { font-size:1.3rem; font-weight:700; color:#a5b4fc !important; font-family:'JetBrains Mono',monospace; }
    .hero .stat-label { font-size:0.8rem; color:#5a5d78 !important; text-transform:uppercase; letter-spacing:1px; }

    /* ── Winner ── */
    .winner-banner {
        background: linear-gradient(135deg,#0a1a1a 0%,#0d2626 50%,#0a1a1a 100%);
        border: 1px solid rgba(20,184,166,0.3); border-radius:20px;
        padding:2rem 2.5rem; text-align:center; margin:1.5rem 0;
        position:relative; overflow:hidden;
        animation: fadeInUp 0.5s ease-out, glow-pulse 3s ease-in-out infinite;
    }
    .winner-banner::before {
        content:''; position:absolute; top:0;left:0;right:0; height:2px;
        background: linear-gradient(90deg,transparent,#14b8a6,#10b981,transparent);
        background-size:200% auto; animation: shimmer 2s linear infinite;
    }
    .winner-banner .trophy { font-size:2.5rem; animation:float 3s ease-in-out infinite; display:inline-block; }
    .winner-banner h2 {
        font-size:1.8rem; font-weight:700; margin:0.5rem 0 0.3rem;
        background: linear-gradient(135deg,#5eead4,#14b8a6,#0d9488);
        -webkit-background-clip:text; -webkit-text-fill-color:transparent;
    }
    .winner-banner .detail { color:#6b9e9e !important; }
    .winner-banner .hl { color:#5eead4 !important; font-weight:700; font-family:'JetBrains Mono',monospace; }

    /* ── Card Tiles ── */
    .card-tile {
        background: rgba(15,15,30,0.5); backdrop-filter:blur(16px);
        border: 1px solid rgba(99,102,241,0.1); border-radius:18px;
        padding:1.5rem 1.2rem; text-align:center;
        transition: all 0.3s cubic-bezier(0.4,0,0.2,1);
        animation: fadeInUp 0.5s ease-out; position:relative; overflow:hidden;
    }
    .card-tile::after {
        content:''; position:absolute; bottom:0;left:0;right:0; height:3px;
        background: linear-gradient(90deg,#6366f1,#a855f7); opacity:0; transition:opacity 0.3s;
    }
    .card-tile:hover { border-color:rgba(99,102,241,0.35); transform:translateY(-5px); box-shadow:0 15px 40px rgba(99,102,241,0.12); }
    .card-tile:hover::after { opacity:1; }
    .card-tile.best { border:1px solid rgba(20,184,166,0.3); background:rgba(10,30,30,0.5); animation: fadeInUp 0.5s ease-out, border-glow 3s ease-in-out infinite; }
    .card-tile.best::after { background:linear-gradient(90deg,#14b8a6,#10b981); opacity:1; }
    .card-tile .card-name { font-size:0.95rem; font-weight:600; color:#e0e0ea !important; margin-bottom:0.8rem; }
    .card-tile .reward-amount { font-size:2rem; font-weight:700; font-family:'JetBrains Mono',monospace; margin:0.3rem 0; }
    .card-tile.best .reward-amount { background:linear-gradient(135deg,#5eead4,#14b8a6); -webkit-background-clip:text; -webkit-text-fill-color:transparent; }
    .card-tile:not(.best) .reward-amount { background:linear-gradient(135deg,#a5b4fc,#6366f1); -webkit-background-clip:text; -webkit-text-fill-color:transparent; }
    .card-tile .reward-meta { font-size:0.8rem; color:#5a5d78 !important; margin-top:0.3rem; }
    .tag { display:inline-block; padding:2px 10px; border-radius:20px; font-size:0.7rem; font-weight:600; text-transform:uppercase; letter-spacing:0.5px; margin-top:0.8rem; }
    .tag-cashback { background:rgba(20,184,166,0.15); color:#5eead4 !important; border:1px solid rgba(20,184,166,0.3); }
    .tag-points { background:rgba(99,102,241,0.15); color:#a5b4fc !important; border:1px solid rgba(99,102,241,0.3); }

    /* ── Section Header ── */
    .sec-header {
        font-size:0.9rem; font-weight:600; color:#8b8ec0 !important;
        margin:2.5rem 0 1.2rem; padding-bottom:0.6rem;
        border-bottom:1px solid rgba(99,102,241,0.15);
        text-transform:uppercase; letter-spacing:1.5px;
    }

    /* ── Tips ── */
    .tip { background:rgba(15,15,30,0.4); border-left:3px solid #6366f1; border-radius:0 12px 12px 0; padding:1rem 1.3rem; margin-bottom:0.7rem; transition:all 0.2s; }
    .tip:hover { background:rgba(99,102,241,0.06); border-left-color:#a855f7; }
    .tip .tip-title { font-weight:600; font-size:0.9rem; color:#d0d0e0 !important; }
    .tip .tip-body { font-size:0.85rem; color:#7a7d98 !important; margin-top:0.25rem; line-height:1.5; }

    /* ── AI Box ── */
    .ai-box {
        background:rgba(15,15,30,0.5); backdrop-filter:blur(16px);
        border:1px solid rgba(168,85,247,0.15); border-radius:16px;
        padding:1.5rem 1.8rem; line-height:1.8; color:#b0b3c8 !important;
        position:relative; overflow:hidden;
    }
    .ai-box::before {
        content:''; position:absolute; top:0;left:0;right:0; height:2px;
        background: linear-gradient(90deg,transparent,#a855f7,#6366f1,transparent);
        background-size:200% auto; animation:shimmer 4s linear infinite;
    }
    .ai-label {
        display:inline-flex; align-items:center; gap:0.4rem;
        background:rgba(168,85,247,0.12); border:1px solid rgba(168,85,247,0.25);
        color:#c4b5fd !important; font-size:0.7rem; font-weight:600;
        padding:3px 10px; border-radius:20px; text-transform:uppercase; letter-spacing:1px; margin-bottom:0.8rem;
    }

    /* ── Profile ── */
    .profile-card {
        background:rgba(15,15,30,0.5); backdrop-filter:blur(16px);
        border:1px solid rgba(99,102,241,0.12); border-radius:18px; padding:1.8rem;
    }
    .profile-tag { display:inline-block; padding:3px 12px; border-radius:20px; font-size:0.72rem; font-weight:600; text-transform:uppercase; letter-spacing:0.5px; }
    .profile-tag.cashback { background:rgba(20,184,166,0.12); color:#5eead4 !important; border:1px solid rgba(20,184,166,0.25); }
    .profile-tag.points { background:rgba(99,102,241,0.12); color:#a5b4fc !important; border:1px solid rgba(99,102,241,0.25); }
    .rate-row { display:flex; align-items:center; margin:6px 0; gap:8px; }
    .rate-label { width:150px; font-size:0.82rem; color:#7a7d98 !important; flex-shrink:0; }
    .rate-value { width:40px; font-size:0.82rem; font-weight:600; color:#d0d0e0 !important; font-family:'JetBrains Mono',monospace; flex-shrink:0; }
    .rate-bar-outer { flex:1; height:6px; background:#1a1a2e; border-radius:3px; overflow:hidden; }
    .rate-bar-inner { height:100%; border-radius:3px; transition:width 0.5s ease; }
    .bar-high { background:linear-gradient(90deg,#14b8a6,#5eead4); }
    .bar-mid { background:linear-gradient(90deg,#6366f1,#a5b4fc); }
    .bar-low { background:linear-gradient(90deg,#3a3a5c,#5a5a7c); }

    /* ── Monthly ── */
    .m-card { background:rgba(15,15,30,0.5); backdrop-filter:blur(16px); border:1px solid rgba(99,102,241,0.1); border-radius:16px; padding:1.3rem 1.6rem; margin-bottom:0.8rem; }
    .m-card.best { border-color:rgba(20,184,166,0.3); background:rgba(10,30,30,0.4); }
    .m-stats { display:flex; gap:2.5rem; flex-wrap:wrap; }
    .m-stat-label { font-size:0.72rem; color:#5a5d78 !important; text-transform:uppercase; letter-spacing:1px; }
    .m-stat-value { font-size:1.2rem; font-weight:700; font-family:'JetBrains Mono',monospace; margin-top:2px; }
    .spend-pill { display:inline-flex; align-items:center; gap:0.6rem; background:rgba(15,15,30,0.6); border:1px solid rgba(99,102,241,0.15); border-radius:30px; padding:0.6rem 1.5rem; margin:1rem 0; }

    /* ── Empty ── */
    .empty { text-align:center; padding:5rem 2rem; animation:fadeInUp 0.6s ease-out; }
    .empty .icon { font-size:4.5rem; animation:float 4s ease-in-out infinite; display:inline-block; }
    .empty h3 { color:#6b70a0 !important; font-size:1.2rem; font-weight:500; margin-top:1rem; }
    .empty p { color:#4a4d68 !important; font-size:0.9rem; max-width:450px; margin:0.5rem auto 0; line-height:1.6; }

    /* ── Buttons ── */
    .stDownloadButton > button {
        background:rgba(99,102,241,0.1) !important; border:1px solid rgba(99,102,241,0.25) !important;
        color:#a5b4fc !important; border-radius:12px !important; font-weight:600 !important; transition:all 0.3s !important;
    }
    .stDownloadButton > button:hover { background:rgba(99,102,241,0.2) !important; transform:translateY(-2px) !important; }
    .stButton > button {
        background:linear-gradient(135deg,#6366f1,#8b5cf6) !important; color:white !important;
        border:none !important; border-radius:12px !important; font-weight:600 !important; transition:all 0.3s !important;
    }
    .stButton > button:hover { background:linear-gradient(135deg,#7c3aed,#a78bfa) !important; transform:translateY(-2px) !important; box-shadow:0 8px 25px rgba(99,102,241,0.3) !important; }

    .stSelectbox > div > div, .stMultiSelect > div > div { background-color:rgba(15,15,30,0.8) !important; border-color:rgba(99,102,241,0.15) !important; border-radius:10px !important; }
    .stNumberInput > div > div > input { background-color:rgba(15,15,30,0.8) !important; border-color:rgba(99,102,241,0.15) !important; border-radius:10px !important; color:#c8cad0 !important; }
    hr { border-color:rgba(99,102,241,0.08) !important; }

    /* ══════════════════════════════════════════
       🧠 FLOATING CHATBOT
       ══════════════════════════════════════════ */

    /* Floating toggle button */
    .floating-chat-btn-wrap {
        position: fixed;
        bottom: 2rem;
        right: 2rem;
        z-index: 99999;
    }
    .floating-chat-btn-wrap button {
        width: 60px !important;
        height: 60px !important;
        border-radius: 50% !important;
        background: linear-gradient(135deg, #6366f1, #a855f7) !important;
        color: white !important;
        border: none !important;
        font-size: 1.5rem !important;
        cursor: pointer !important;
        box-shadow: 0 8px 30px rgba(99, 102, 241, 0.4) !important;
        transition: all 0.3s !important;
        padding: 0 !important;
        min-height: 0 !important;
        line-height: 60px !important;
    }
    .floating-chat-btn-wrap button:hover {
        transform: scale(1.1) !important;
        box-shadow: 0 12px 40px rgba(99, 102, 241, 0.6) !important;
    }

    /* Pulse ring behind button */
    .pulse-ring {
        position: fixed;
        bottom: 2rem;
        right: 2rem;
        width: 60px;
        height: 60px;
        border-radius: 50%;
        border: 2px solid rgba(99, 102, 241, 0.5);
        animation: pulse-ring 2s ease-out infinite;
        z-index: 99998;
        pointer-events: none;
    }

    /* Chat window */
    .floating-chat-window {
        position: fixed;
        bottom: 6rem;
        right: 2rem;
        width: 380px;
        max-height: 520px;
        z-index: 99999;
        animation: pop-in 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
    }
    .chat-window-inner {
        background: rgba(10, 10, 22, 0.95);
        backdrop-filter: blur(24px);
        border: 1px solid rgba(99, 102, 241, 0.2);
        border-radius: 20px;
        overflow: hidden;
        box-shadow:
            0 20px 60px rgba(0, 0, 0, 0.5),
            0 0 40px rgba(99, 102, 241, 0.1);
    }

    /* Chat header */
    .chat-header {
        background: linear-gradient(135deg, #13132b, #1a1a3e);
        padding: 1rem 1.2rem;
        border-bottom: 1px solid rgba(99, 102, 241, 0.15);
        display: flex;
        align-items: center;
        gap: 0.7rem;
    }
    .chat-header-avatar {
        width: 36px; height: 36px;
        background: linear-gradient(135deg, #6366f1, #a855f7);
        border-radius: 50%;
        display: flex; align-items: center; justify-content: center;
        font-size: 1.1rem;
    }
    .chat-header-info h4 {
        margin: 0; font-size: 0.95rem; color: #e0e0ea !important;
    }
    .chat-header-info span {
        font-size: 0.72rem; color: #14b8a6 !important;
    }
    .online-dot {
        width: 6px; height: 6px;
        background: #14b8a6;
        border-radius: 50%;
        display: inline-block;
        margin-right: 4px;
        animation: glow-pulse 2s infinite;
    }

    /* Chat messages area */
    .chat-messages {
        max-height: 320px;
        overflow-y: auto;
        padding: 1rem;
    }
    .chat-messages::-webkit-scrollbar { width: 4px; }
    .chat-messages::-webkit-scrollbar-thumb { background: rgba(99,102,241,0.3); border-radius: 2px; }

    .chat-msg { margin-bottom: 0.8rem; animation: fadeInUp 0.3s ease-out; }
    .chat-msg.user-msg { text-align: right; }
    .chat-msg.bot-msg { text-align: left; }

    .chat-msg .bubble {
        display: inline-block;
        max-width: 85%;
        padding: 0.7rem 1rem;
        border-radius: 14px;
        font-size: 0.85rem;
        line-height: 1.5;
        text-align: left;
    }
    .chat-msg.user-msg .bubble {
        background: linear-gradient(135deg, #6366f1, #8b5cf6);
        color: white !important;
        border-bottom-right-radius: 4px;
    }
    .chat-msg.user-msg .bubble * { color: white !important; }
    .chat-msg.bot-msg .bubble {
        background: rgba(25, 25, 50, 0.8);
        border: 1px solid rgba(99, 102, 241, 0.12);
        color: #c0c3d0 !important;
        border-bottom-left-radius: 4px;
    }
    .chat-msg.bot-msg .bubble * { color: #c0c3d0 !important; }

    .chat-msg .msg-time {
        font-size: 0.65rem;
        color: #4a4d68 !important;
        margin-top: 3px;
    }

    /* Welcome message */
    .chat-welcome {
        text-align: center;
        padding: 1.5rem 1rem;
    }
    .chat-welcome .welcome-icon {
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
    }
    .chat-welcome h4 {
        color: #c0c3d0 !important;
        font-size: 0.95rem;
        margin: 0;
    }
    .chat-welcome p {
        color: #5a5d78 !important;
        font-size: 0.8rem;
        margin-top: 0.3rem;
    }
    .quick-q {
        display: inline-block;
        background: rgba(99, 102, 241, 0.08);
        border: 1px solid rgba(99, 102, 241, 0.15);
        border-radius: 20px;
        padding: 4px 12px;
        font-size: 0.72rem;
        color: #a5b4fc !important;
        margin: 3px;
        cursor: default;
    }

    /* Chat input area in floating window */
    .floating-chat-window .stTextInput > div > div > input {
        background: rgba(15, 15, 30, 0.9) !important;
        border: 1px solid rgba(99, 102, 241, 0.2) !important;
        border-radius: 12px !important;
        color: #e0e0ea !important;
        font-size: 0.85rem !important;
        padding: 0.6rem 1rem !important;
    }
    .floating-chat-window .stTextInput > div > div > input::placeholder {
        color: #5a5d78 !important;
    }
    .floating-chat-window .stButton > button {
        width: 100% !important;
        padding: 0.5rem !important;
        font-size: 0.85rem !important;
        border-radius: 10px !important;
    }

    /* ── Footer ── */
    .app-footer { text-align:center; padding:2rem 1rem; margin-top:3rem; border-top:1px solid rgba(99,102,241,0.1); }
    .app-footer span { color:#3a3d58 !important; font-size:0.78rem; }
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# HERO
# ─────────────────────────────────────────────

st.markdown(f"""
<div class="hero">
    <div class="brand">🧠 SwipeSmart AI</div>
    <div class="tagline">India's smartest credit card reward advisor — powered by AI</div>
    <div class="stats-row">
        <div class="stat">
            <span class="stat-number">{len(CARD_DATA)}</span>
            <span class="stat-label">Cards</span>
        </div>
        <div class="stat">
            <span class="stat-number">{sum(len(v) for v in VENDORS.values())}</span>
            <span class="stat-label">Vendors</span>
        </div>
        <div class="stat">
            <span class="stat-number">{len(CATEGORIES)}</span>
            <span class="stat-label">Categories</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────

with st.sidebar:
    st.markdown("## 🧠 SwipeSmart AI")
    st.markdown("---")

    mode = st.radio("Mode", ["🛒 Single Purchase", "📅 Monthly Planner"], index=0)

    st.markdown("---")

    cards = st.multiselect("💳 Your Cards", options=POPULAR_CARDS, default=[], placeholder="Choose cards...")

    st.markdown("---")

    if mode == "🛒 Single Purchase":
        category = st.selectbox("📂 Category", CATEGORIES)
        available_vendors = VENDORS.get(category, [])
        if available_vendors:
            vendor = st.selectbox("🏪 Vendor", options=["— General —"] + available_vendors)
            vendor = None if vendor == "— General —" else vendor
        else:
            vendor = None
            st.caption(f"No vendor data for '{category}'")
        amount = st.number_input("💰 Amount (₹)", min_value=100, max_value=1000000, value=5000, step=500)
        find_button = st.button("🔍 Find Best Card", use_container_width=True, type="primary")
    else:
        find_button = False

    st.markdown("---")
    st.caption("SwipeSmart AI v2.0")


# ─────────────────────────────────────────────
# EMPTY STATE
# ─────────────────────────────────────────────

def show_empty_state():
    st.markdown("""
    <div class="empty">
        <div class="icon">🧠</div>
        <h3>Ready to swipe smarter?</h3>
        <p>Select your credit cards, pick a category, and hit <strong>Find Best Card</strong>.
        Or click the <strong>💬 chat button</strong> in the bottom-right corner to ask SwipeSmart AI anything!</p>
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────
# 🛒 SINGLE PURCHASE MODE
# ─────────────────────────────────────────────

if mode == "🛒 Single Purchase":
    if not find_button:
        show_empty_state()
    elif not cards:
        st.error("⚠️ Please select at least one card.")
    else:
        comparison = compare_cards(cards, category, amount, vendor)
        results = comparison["results"]
        best_card = comparison["best_card"]
        best_reward = comparison["best_reward"]

        vendor_label = f"at {vendor}" if vendor else f"in {category}"
        st.markdown(f"""
        <div class="winner-banner">
            <div class="trophy">🏆</div>
            <h2>{best_card}</h2>
            <div class="detail">Earns <span class="hl">₹{best_reward:.2f}</span> on ₹{amount:,} {vendor_label}</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="sec-header">📊 REWARD COMPARISON</div>', unsafe_allow_html=True)
        cols = st.columns(min(len(results), 4))
        for idx, r in enumerate(results):
            with cols[idx % len(cols)]:
                is_best = r["card"] == best_card
                cls = "card-tile best" if is_best else "card-tile"
                crown = "👑 " if is_best else ""
                st.markdown(f"""
                <div class="{cls}">
                    <div class="card-name">{crown}{r['card']}</div>
                    <div class="reward-amount">₹{r['reward']:.2f}</div>
                    <div class="reward-meta">{r['rate']}% · {r['source']}</div>
                    <div class="reward-meta">{r['network']} · Fee ₹{r['annual_fee']}/yr</div>
                    <div class="tag tag-{r['type']}">{r['type']}</div>
                </div>
                """, unsafe_allow_html=True)
                st.write("")

        st.markdown('<div class="sec-header">📈 VISUAL COMPARISON</div>', unsafe_allow_html=True)
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=[r["card"] for r in results], y=[r["reward"] for r in results],
            text=[f"₹{r['reward']:.2f}" for r in results], textposition="outside",
            marker_color=["#14b8a6" if r["card"]==best_card else "#6366f1" for r in results],
            marker_line=dict(width=0),
        ))
        fig.update_layout(
            xaxis_title=None, yaxis_title="Reward (₹)", height=400,
            font=dict(family="Space Grotesk", size=13, color="#6b70a0"),
            plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)",
            xaxis=dict(tickangle=-30, gridcolor="rgba(0,0,0,0)"),
            yaxis=dict(gridcolor="rgba(99,102,241,0.08)"),
            margin=dict(t=20, b=80),
        )
        st.plotly_chart(fig, use_container_width=True)

        tips = generate_smart_tips(results, best_card, amount, category, vendor)
        if tips:
            st.markdown('<div class="sec-header">💡 SMART TIPS</div>', unsafe_allow_html=True)
            for tip in tips:
                st.markdown(f"""
                <div class="tip">
                    <div class="tip-title">{tip['icon']} {tip['title']}</div>
                    <div class="tip-body">{tip['text']}</div>
                </div>
                """, unsafe_allow_html=True)

        st.markdown('<div class="sec-header">🤖 AI ANALYSIS</div>', unsafe_allow_html=True)
        comparison_text = ""
        for r in results:
            comparison_text += f"{r['card']}: {r['rate']}% ({r['source']}) = ₹{r['reward']:.2f} [{r['type']}, fee: ₹{r['annual_fee']}/yr]\n"
        with st.spinner("Analyzing..."):
            explanation = explain_recommendation(best_card, comparison_text, vendor)
        st.markdown(f"""
        <div class="ai-box">
            <div class="ai-label">🧠 SwipeSmart AI</div>
            <div>{explanation}</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="sec-header">📤 EXPORT</div>', unsafe_allow_html=True)
        export_data = {"app": "SwipeSmart AI", "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                       "category": category, "vendor": vendor, "amount": amount,
                       "best_card": best_card, "best_reward": best_reward, "results": results}
        c1, c2, c3 = st.columns(3)
        with c1:
            st.download_button("📥 JSON", json.dumps(export_data, indent=2, default=str), "swipesmart_report.json", "application/json", use_container_width=True)
        with c2:
            st.download_button("📥 TXT", f"Best: {best_card} → ₹{best_reward:.2f}\n\n{comparison_text}", "swipesmart_report.txt", "text/plain", use_container_width=True)
        with c3:
            csv = "Card,Rate,Reward,Type,Fee\n"
            for r in results: csv += f"{r['card']},{r['rate']},{r['reward']},{r['type']},{r['annual_fee']}\n"
            st.download_button("📥 CSV", csv, "swipesmart_report.csv", "text/csv", use_container_width=True)


# ─────────────────────────────────────────────
# 📅 MONTHLY PLANNER MODE
# ─────────────────────────────────────────────

elif mode == "📅 Monthly Planner":
    st.markdown('<div class="sec-header">📅 MONTHLY SPENDING PLANNER</div>', unsafe_allow_html=True)
    st.markdown("Enter your typical monthly spend per category.")

    if not cards:
        st.error("⚠️ Select at least one card.")
        st.stop()

    monthly_spend = {}
    input_cols = st.columns(3)
    icons = {"Dining":"🍽️","Travel":"✈️","Grocery":"🛒","Fuel":"⛽","Online Shopping":"🛍️",
             "Amazon":"📦","Utilities":"💡","International":"🌍","Shopping":"🏬","Movies/Entertainment":"🎬","Other":"📌"}

    for idx, cat in enumerate(CATEGORIES):
        with input_cols[idx % 3]:
            monthly_spend[cat] = st.number_input(f"{icons.get(cat,'📌')} {cat}", min_value=0, value=0, step=500, key=f"m_{cat}")

    total_spend = sum(monthly_spend.values())
    st.markdown(f"""
    <div class="spend-pill">
        <span style="color:#6b70a0 !important;">Total Monthly</span>
        <span style="color:#a5b4fc !important; font-size:1.1rem; font-weight:700; font-family:'JetBrains Mono',monospace;">₹{total_spend:,}</span>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🧮 Analyze", use_container_width=True, type="primary"):
        if total_spend == 0:
            st.warning("Enter spending in at least one category.")
            st.stop()

        monthly = compare_monthly(cards, monthly_spend)
        m_results = monthly["results"]
        m_best = monthly["best_card"]
        best_data = m_results[0]

        st.markdown(f"""
        <div class="winner-banner">
            <div class="trophy">🏆</div>
            <h2>{m_best}</h2>
            <div class="detail">Net Yearly: <span class="hl">₹{best_data['net_yearly']:,.2f}</span> · ₹{best_data['total_reward']:,.2f}/mo · Fee ₹{best_data['annual_fee']:,}</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="sec-header">📊 ANALYSIS</div>', unsafe_allow_html=True)
        for idx, r in enumerate(m_results):
            is_best = (idx == 0)
            cls = "m-card best" if is_best else "m-card"
            prefix = "👑 " if is_best else ""
            st.markdown(f"""
            <div class="{cls}">
                <h3 style="margin:0;">{prefix}{r['card']}</h3>
                <div class="m-stats" style="margin-top:0.6rem;">
                    <div><div class="m-stat-label">Monthly</div><div class="m-stat-value" style="color:#14b8a6 !important;">₹{r['total_reward']:,.2f}</div></div>
                    <div><div class="m-stat-label">Yearly</div><div class="m-stat-value" style="color:#6366f1 !important;">₹{r['yearly_reward']:,.2f}</div></div>
                    <div><div class="m-stat-label">Fee</div><div class="m-stat-value" style="color:#ef4444 !important;">₹{r['annual_fee']:,}</div></div>
                    <div><div class="m-stat-label">Net Yearly</div><div class="m-stat-value" style="color:{'#14b8a6' if r['net_yearly']>=0 else '#ef4444'} !important;">₹{r['net_yearly']:,.2f}</div></div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown('<div class="sec-header">📈 NET YEARLY</div>', unsafe_allow_html=True)
        fig2 = go.Figure()
        fig2.add_trace(go.Bar(
            x=[r["card"] for r in m_results], y=[r["net_yearly"] for r in m_results],
            text=[f"₹{r['net_yearly']:,.0f}" for r in m_results], textposition="outside",
            marker_color=["#14b8a6" if r["card"]==m_best else "#6366f1" for r in m_results], marker_line=dict(width=0),
        ))
        fig2.update_layout(xaxis_title=None, yaxis_title="Net Yearly (₹)", height=420,
            font=dict(family="Space Grotesk", size=13, color="#6b70a0"),
            plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)",
            xaxis=dict(tickangle=-30, gridcolor="rgba(0,0,0,0)"),
            yaxis=dict(gridcolor="rgba(99,102,241,0.08)"), margin=dict(t=20, b=80))
        st.plotly_chart(fig2, use_container_width=True)

        if best_data["breakdown"]:
            st.markdown(f'<div class="sec-header">🔍 {m_best} — BREAKDOWN</div>', unsafe_allow_html=True)
            fig3 = px.pie(names=list(best_data["breakdown"].keys()),
                values=[best_data["breakdown"][c]["reward"] for c in best_data["breakdown"]],
                hole=0.5, color_discrete_sequence=["#6366f1","#14b8a6","#a855f7","#f59e0b","#ef4444","#ec4899","#06b6d4","#84cc16","#f97316","#8b5cf6","#10b981"])
            fig3.update_traces(textinfo="label+value", texttemplate="%{label}<br>₹%{value:.0f}", textfont=dict(color="white", size=11))
            fig3.update_layout(height=400, font=dict(family="Space Grotesk", size=12, color="#6b70a0"),
                paper_bgcolor="rgba(0,0,0,0)", legend=dict(font=dict(color="#6b70a0")), margin=dict(t=10))
            st.plotly_chart(fig3, use_container_width=True)

        st.markdown('<div class="sec-header">🤖 AI INSIGHT</div>', unsafe_allow_html=True)
        summary = ""
        for r in m_results: summary += f"{r['card']}: ₹{r['total_reward']:,.2f}/mo, net ₹{r['net_yearly']:,.2f}/yr\n"
        with st.spinner("Analyzing..."):
            m_explanation = explain_monthly(m_best, summary)
        st.markdown(f'<div class="ai-box"><div class="ai-label">🧠 SwipeSmart AI</div><div>{m_explanation}</div></div>', unsafe_allow_html=True)


# ─────────────────────────────────────────────
# 🔎 CARD DEEP DIVE
# ─────────────────────────────────────────────

st.markdown("---")
st.markdown('<div class="sec-header">🔎 CARD DEEP DIVE</div>', unsafe_allow_html=True)

if cards:
    profile_card = st.selectbox("Explore a card:", options=cards, key="profile_select")
    if profile_card:
        cinfo = CARD_DATA[profile_card]
        p1, p2 = st.columns(2)
        with p1:
            st.markdown(f"""
            <div class="profile-card">
                <h3>{profile_card}</h3>
                <span class="profile-tag {cinfo['type']}">{cinfo['type']}</span>
                <span style="margin-left:8px; color:#5a5d78 !important;">{cinfo.get('network','Visa')}</span>
                <div style="margin-top:1rem; padding-top:0.8rem; border-top:1px solid rgba(99,102,241,0.1);">
                    <div style="font-size:0.75rem; color:#5a5d78 !important; text-transform:uppercase; letter-spacing:1px;">Annual Fee</div>
                    <div style="font-size:1.4rem; font-weight:700; font-family:'JetBrains Mono',monospace; color:#a5b4fc !important;">₹{cinfo['annual_fee']:,}</div>
                </div>
                <div style="margin-top:1rem; font-size:0.75rem; color:#5a5d78 !important; text-transform:uppercase; letter-spacing:1px;">Category Rewards</div>
            </div>
            """, unsafe_allow_html=True)
            for cat, rate in cinfo["rewards"].items():
                bar_pct = min(rate * 7, 100)
                bar_cls = "bar-high" if rate >= 5 else "bar-mid" if rate >= 3 else "bar-low"
                st.markdown(f'<div class="rate-row"><span class="rate-label">{cat}</span><span class="rate-value">{rate}%</span><div class="rate-bar-outer"><div class="rate-bar-inner {bar_cls}" style="width:{bar_pct}%;"></div></div></div>', unsafe_allow_html=True)

        with p2:
            vr = cinfo.get("vendor_rewards", {})
            if vr:
                st.markdown(f'<div class="profile-card"><h3>🏪 Vendor Rates</h3><div style="font-size:0.8rem; color:#5a5d78 !important;">Partner merchant rewards</div></div>', unsafe_allow_html=True)
                for v_name, v_rate in sorted(vr.items(), key=lambda x: -x[1]):
                    bar_pct = min(v_rate * 7, 100)
                    bar_cls = "bar-high" if v_rate >= 5 else "bar-mid" if v_rate >= 3 else "bar-low"
                    dot = "🟢" if v_rate >= 5 else "🟡" if v_rate >= 3 else "⚪"
                    st.markdown(f'<div class="rate-row"><span class="rate-label">{dot} {v_name}</span><span class="rate-value">{v_rate}%</span><div class="rate-bar-outer"><div class="rate-bar-inner {bar_cls}" style="width:{bar_pct}%;"></div></div></div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="profile-card"><p style="color:#5a5d78 !important;">No vendor-specific rates.</p></div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="empty" style="padding:2rem;"><p>Select cards from the sidebar to explore.</p></div>', unsafe_allow_html=True)


# ═══════════════════════════════════════════════
# 🧠 FLOATING CHATBOT — ALWAYS PRESENT
# ═══════════════════════════════════════════════

# Pulse ring (always visible behind button)
if not st.session_state.chat_open:
    st.markdown('<div class="pulse-ring"></div>', unsafe_allow_html=True)

# ── Floating Toggle Button ──
button_container = st.container()
with button_container:
    if st.button("🧠" if not st.session_state.chat_open else "✕", key="chat_toggle", on_click=toggle_chat):
        pass

button_css = """
    position: fixed;
    bottom: 2rem;
    right: 2rem;
    z-index: 99999;
    width: 60px;
    background: transparent;
"""
button_container.float(button_css)


# ── Floating Chat Window ──
if st.session_state.chat_open:
    chat_window = st.container()
    with chat_window:

        # Chat header (HTML)
        st.markdown("""
        <div class="chat-window-inner">
            <div class="chat-header">
                <div class="chat-header-avatar">🧠</div>
                <div class="chat-header-info">
                    <h4>SwipeSmart AI</h4>
                    <span><span class="online-dot"></span> Online · Ask anything</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Chat messages
        if not st.session_state.chat_history:
            st.markdown("""
            <div style="background:rgba(10,10,22,0.95); padding:1.2rem; border-left:1px solid rgba(99,102,241,0.2); border-right:1px solid rgba(99,102,241,0.2);">
                <div class="chat-welcome">
                    <div class="welcome-icon">👋</div>
                    <h4>Hi! I'm SwipeSmart AI</h4>
                    <p>Ask me about credit cards, rewards, comparisons...</p>
                    <div style="margin-top:0.8rem;">
                        <span class="quick-q">Best card for Swiggy?</span>
                        <span class="quick-q">Compare HDFC cards</span>
                        <span class="quick-q">Zero fee cards?</span>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            # Build messages HTML
            msgs_html = ""
            for msg in st.session_state.chat_history:
                if msg["role"] == "user":
                    msgs_html += f"""
                    <div class="chat-msg user-msg">
                        <div class="bubble">{msg['content']}</div>
                    </div>"""
                else:
                    msgs_html += f"""
                    <div class="chat-msg bot-msg">
                        <div class="bubble">{msg['content']}</div>
                    </div>"""

            st.markdown(f"""
            <div style="background:rgba(10,10,22,0.95); border-left:1px solid rgba(99,102,241,0.2); border-right:1px solid rgba(99,102,241,0.2);">
                <div class="chat-messages">
                    {msgs_html}
                </div>
            </div>
            """, unsafe_allow_html=True)

        # Input area
        user_input = st.text_input(
            "msg",
            placeholder="Ask SwipeSmart AI...",
            key=f"chat_input_{st.session_state.chat_input_key}",
            label_visibility="collapsed",
        )

        col_send, col_clear = st.columns([3, 1])
        with col_send:
            send_clicked = st.button("Send 🚀", key="send_msg", use_container_width=True)
        with col_clear:
            clear_clicked = st.button("🗑️", key="clear_chat", on_click=clear_chat, use_container_width=True)

        if send_clicked and user_input:
            st.session_state.chat_history.append({"role": "user", "content": user_input})

            history_text = ""
            for msg in st.session_state.chat_history[-6:]:
                role = "User" if msg["role"] == "user" else "SwipeSmart AI"
                history_text += f"{role}: {msg['content']}\n"

            response = chat_with_ai(user_input, CARD_SUMMARY, history_text)
            st.session_state.chat_history.append({"role": "assistant", "content": response})

            st.session_state.chat_input_key += 1
            st.rerun()

    # Float the chat window
    chat_window_css = """
        position: fixed;
        bottom: 6rem;
        right: 2rem;
        width: 380px;
        max-height: 520px;
        z-index: 99998;
        background: rgba(10, 10, 22, 0.98);
        backdrop-filter: blur(24px);
        border: 1px solid rgba(99, 102, 241, 0.2);
        border-radius: 20px;
        overflow: hidden;
        box-shadow: 0 20px 60px rgba(0,0,0,0.5), 0 0 40px rgba(99,102,241,0.1);
        animation: pop-in 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
        padding: 0;
    """
    chat_window.float(chat_window_css)


# ─────────────────────────────────────────────
#