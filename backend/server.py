# =====================================================================
# 🚀 SWIPESMART AI ENTERPRISE — FASTAPI BACKEND SERVER
# High-performance REST API for Tier-1 Consumer Fintech Experience
# =====================================================================

import os
from typing import Dict, List, Optional, Any
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Import existing core databases and engines
from data.cards_db import (
    CARDS_DATABASE,
    CATEGORIES,
    CARD_TIERS,
    CARD_ISSUERS,
    POPULAR_CARDS
)
from data.vendors_db import VENDORS_METADATA
from cards_data import VENDORS
from engine.calculator import (
    compare_cards,
    calculate_card_annual_net,
    generate_smart_tips,
    get_reward_rate
)
from engine.wallet_optimizer import find_optimal_wallet_strategy
from engine.matchmaker import analyze_spend_gaps, recommend_next_cards
from engine.rag_service import search_knowledge_base
from engine.llm_advisor import (
    explain_single_purchase,
    explain_wallet_strategy,
    explain_matchmaker_recommendation,
    chat_with_copilot
)

app = FastAPI(
    title="SwipeSmart AI Enterprise API",
    description="Backend services for Credit Card Reward Maximizer",
    version="3.0.0"
)

# Enable CORS for local React/Next.js frontend development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------------------------------------
# Pydantic Request Models
# ---------------------------------------------------------------------
class CompareRequest(BaseModel):
    cards: List[str]
    category: str
    amount: float
    vendor: Optional[str] = None
    valuation_mode: str = "default"
    include_ai: bool = True

class RouteWalletRequest(BaseModel):
    wallet_cards: List[str]
    monthly_spend: Dict[str, float]
    valuation_mode: str = "default"
    include_ai: bool = True

class MatchmakerRequest(BaseModel):
    wallet_cards: List[str]
    monthly_spend: Dict[str, float]
    lifestyle_filter: str = "All"
    max_fee: Optional[float] = None
    include_ai: bool = True

class CopilotChatRequest(BaseModel):
    message: str
    history: List[Dict[str, str]] = []

# ---------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------
@app.get("/api/health")
def health_check():
    return {"status": "ok", "version": "3.0.0"}

@app.get("/api/cards")
def get_cards():
    return {
        "cards": CARDS_DATABASE,
        "categories": CATEGORIES,
        "tiers": CARD_TIERS,
        "issuers": CARD_ISSUERS,
        "popular_cards": POPULAR_CARDS
    }

@app.get("/api/vendors")
def get_vendors():
    return {
        "metadata": VENDORS_METADATA,
        "category_vendors": VENDORS
    }

@app.post("/api/compare")
def api_compare(req: CompareRequest):
    comp = compare_cards(
        req.cards,
        req.category,
        req.amount,
        req.vendor,
        valuation_mode=req.valuation_mode
    )
    results = comp["results"]
    best_card = comp["best_card"]
    best_reward = comp["best_reward"]
    runner_up = comp["runner_up"]

    tips = generate_smart_tips(results, best_card, req.amount, req.category, req.vendor)
    
    # Calculate difference between best card and runner-up
    runner_up_reward = 0.0
    runner_up_obj = None
    if len(results) > 1:
        runner_up_obj = results[1]
        runner_up_reward = runner_up_obj["reward"]

    savings_delta = round(best_reward - runner_up_reward, 2)

    ai_rationale = ""
    if req.include_ai and best_card:
        comp_text = "\n".join([f"{r['card']}: {r['rate']}% ({r['source']}) = ₹{r['reward']:.2f}" for r in results[:5]])
        ai_rationale = explain_single_purchase(best_card, comp_text, req.amount, req.category, req.vendor)

    return {
        "results": results,
        "best_card": best_card,
        "best_reward": best_reward,
        "runner_up": runner_up,
        "runner_up_card": runner_up_obj,
        "savings_delta": savings_delta,
        "tips": tips,
        "ai_rationale": ai_rationale
    }

@app.post("/api/route-wallet")
def api_route_wallet(req: RouteWalletRequest):
    strategy = find_optimal_wallet_strategy(
        req.wallet_cards,
        req.monthly_spend,
        valuation_mode=req.valuation_mode
    )

    if "error" in strategy:
        return strategy

    ai_summary = ""
    if req.include_ai:
        total_monthly = sum(req.monthly_spend.values())
        assignments = strategy.get("category_assignments", {})
        best_single = strategy.get("best_single_card", {}).get("card", "Unknown")
        best_single_ret = strategy.get("best_single_card", {}).get("net_yearly", 0)
        strat_text = f"""
Total Monthly Spend: ₹{total_monthly:,.0f}
Net Optimized Annual Return: ₹{strategy['net_optimized_yearly_return']:,.0f}
Single Card Benchmark ({best_single}): ₹{best_single_ret:,.0f}
Synergy Bonus: +₹{strategy['synergy_vs_single']:,.0f}/yr
Assignments: {', '.join([f"{c} -> {d['assigned_card']}" for c, d in assignments.items()])}
"""
        ai_summary = explain_wallet_strategy(strat_text)

    strategy["ai_summary"] = ai_summary
    return strategy

@app.post("/api/matchmaker")
def api_matchmaker(req: MatchmakerRequest):
    gaps = analyze_spend_gaps(req.wallet_cards, req.monthly_spend)
    recs = recommend_next_cards(
        req.wallet_cards,
        req.monthly_spend,
        lifestyle_filter=req.lifestyle_filter,
        max_fee=req.max_fee
    )

    ai_rationale = ""
    if req.include_ai and recs:
        top_rec = recs[0]
        spend_summary_str = f"Monthly spends: {', '.join([f'{c}: ₹{int(s):,}' for c, s in req.monthly_spend.items() if s > 0])}"
        ai_rationale = explain_matchmaker_recommendation(
            top_rec["card"],
            top_rec["incremental_annual_profit"],
            top_rec["conquered_categories"],
            spend_summary_str
        )

    return {
        "gaps": gaps,
        "recommendations": recs,
        "ai_rationale": ai_rationale
    }

@app.get("/api/rules")
def api_rules(q: str = Query(default=""), top_k: int = Query(default=6), card: Optional[str] = None):
    docs = search_knowledge_base(q, top_k=top_k, card_filter=card)
    return {"query": q, "count": len(docs), "docs": docs}

@app.post("/api/copilot")
def api_copilot(req: CopilotChatRequest):
    history_context = "\n".join([f"{m.get('role', 'user')}: {m.get('content', '')}" for m in req.history[-6:]])
    card_db_summary = "\n".join([f"{k}: {v['type']}, Fee ₹{v['annual_fee']}, Lounges: {v.get('domestic_lounges','None')}" for k, v in CARDS_DATABASE.items()])
    reply = chat_with_copilot(req.message, card_db_summary, history_context)
    return {"reply": reply}

# ---------------------------------------------------------------------
# Serve Frontend Static Assets (Unified Single-Port / Standalone Mode)
# ---------------------------------------------------------------------
frontend_dist = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "frontend", "dist"))
if os.path.exists(frontend_dist) and os.path.isdir(frontend_dist):
    from fastapi.staticfiles import StaticFiles
    from fastapi.responses import FileResponse

    assets_dir = os.path.join(frontend_dist, "assets")
    if os.path.exists(assets_dir):
        app.mount("/assets", StaticFiles(directory=assets_dir), name="assets")

    @app.get("/{full_path:path}", include_in_schema=False)
    async def serve_spa_app(full_path: str):
        # Prevent intercepting API routes that returned 404
        if full_path.startswith("api/"):
            return {"error": "API route not found"}
        file_path = os.path.join(frontend_dist, full_path)
        if full_path and os.path.exists(file_path) and os.path.isfile(file_path):
            return FileResponse(file_path)
        return FileResponse(os.path.join(frontend_dist, "index.html"))

