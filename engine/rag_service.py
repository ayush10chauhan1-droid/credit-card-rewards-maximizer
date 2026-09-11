# =====================================================================
# 🧠 SWIPESMART RAG RETRIEVAL SERVICE
# Fast semantic & keyword search over official credit card terms,
# capping rules, lounge criteria, and exclusions.
# =====================================================================

import re
from typing import List, Dict, Any
from data.card_rules_knowledge import CARD_RULES_CORPUS


def clean_tokenize(text: str) -> set:
    """Extract clean lowercase word tokens."""
    return set(re.findall(r'\b[a-z0-9]{3,}\b', text.lower()))


def search_knowledge_base(query: str, top_k: int = 4, card_filter: str = None) -> List[Dict[str, Any]]:
    """
    Retrieves the most relevant card rule documents based on query keywords,
    BM25/TF-IDF style relevance scoring, and optional card filter.
    """
    if not query:
        return CARD_RULES_CORPUS[:top_k]

    query_tokens = clean_tokenize(query)
    results = []

    for doc in CARD_RULES_CORPUS:
        if card_filter and card_filter.lower() not in doc["card"].lower():
            continue

        doc_text = f"{doc['card']} {doc['topic']} {doc['text']}"
        doc_tokens = clean_tokenize(doc_text)

        # Calculate keyword overlap score
        matches = query_tokens.intersection(doc_tokens)
        score = len(matches)

        # Boost score if card name or topic appears in query
        if any(w in query.lower() for w in doc["card"].lower().split()):
            score += 3
        if any(w in query.lower() for w in doc["topic"].lower().split()):
            score += 2

        if score > 0:
            results.append({
                "card": doc["card"],
                "topic": doc["topic"],
                "text": doc["text"],
                "score": score
            })

    results.sort(key=lambda x: -x["score"])

    # Fallback to top cards if no exact token overlap
    if not results:
        results = [
            {"card": d["card"], "topic": d["topic"], "text": d["text"], "score": 0}
            for d in CARD_RULES_CORPUS[:top_k]
        ]

    return results[:top_k]


def build_rag_context(query: str, card_filter: str = None) -> str:
    """Format retrieved snippets into structured context for Gemini LLM."""
    docs = search_knowledge_base(query, top_k=3, card_filter=card_filter)
    context_lines = []

    for idx, doc in enumerate(docs, 1):
        context_lines.append(f"[{idx}] {doc['card']} — {doc['topic']}:\n{doc['text']}\n")

    return "\n".join(context_lines)
