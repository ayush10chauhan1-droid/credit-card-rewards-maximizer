import streamlit as st
from web_fetcher import fetch_card_page
from rag import build_vector_store, retrieve_rules, retrieve_rules_for_cards
from llm import choose_card
from cards_data import POPULAR_CARDS, CATEGORIES, VENDORS

# Page configuration
st.set_page_config(page_title="Credit Card Reward Maximizer", layout="wide")

# Custom CSS to reduce spacing and increase sidebar width
st.markdown("""
<style>
    [data-testid="stVerticalBlock"] > [style*="flex-direction: column"] > [data-testid="stVerticalBlock"] {
        gap: 0rem;
    }
    .stSelectbox, .stNumberInput, .stMultiSelect {
        margin-bottom: 0.5rem !important;
    }
    [data-testid="stHorizontalBlock"] {
        gap: 0.5rem;
    }
    /* Increase sidebar width */
    [data-testid="stSidebar"] {
        width: 400px !important;
        min-width: 400px !important;
    }
    [data-testid="stSidebar"] > div {
        width: 400px !important;
    }
</style>
""", unsafe_allow_html=True)

st.title("💳 Credit Card Reward Maximizer")
st.markdown("Find the best credit card to maximize your rewards with AI-powered analysis.")

# Sidebar for inputs
with st.sidebar:
    st.header("🎯 Your Preferences")
    
    # Credit card selection
    st.markdown("**💳 Credit Cards**")
    cards = st.multiselect(
        "Select or type cards to compare",
        options=POPULAR_CARDS,
        placeholder="Type to search or add custom cards...",
        help="Type to search existing cards or type a new name",
        label_visibility="collapsed",
        default=[]
    )
    
    # Category selection
    st.markdown("**📂 Spending Category**")
    category = st.selectbox(
        "Select category",
        CATEGORIES,
        label_visibility="collapsed",
        key="category_select"
    )
    
    # Vendor selection
    st.markdown("**🏪 Vendor (Optional)**")
    vendor = st.selectbox(
        "Select vendor",
        ["None"] + VENDORS,
        label_visibility="collapsed",
        key="vendor_select"
    )
    
    # Amount input
    st.markdown("**💰 Purchase Amount**")
    amount = st.number_input("Amount ($)", min_value=1, value=100, label_visibility="collapsed")
    
    st.write("")
    
    # Find Best Card button
    find_card_button = st.button("🔍 Find Best Card", use_container_width=True, type="primary")

# Main content area
if find_card_button:
    card_list = cards
    if not card_list:
        st.error("❌ Please select or enter at least one credit card")
        st.stop()
    
    progress_placeholder = st.empty()
    
    combined_text = ""
    with st.spinner("Fetching credit card information..."):
        for idx, card in enumerate(card_list):
            progress_placeholder.info(f"Processing: {card} ({idx+1}/{len(card_list)})")
            
            # Build search queries based on category and vendor
            search_queries = [
                f"{card} rewards program",
                f"{card} cashback {category}",
                f"{card} benefits"
            ]
            # Add vendor-specific search if selected
            if vendor != "None":
                search_queries.insert(1, f"{card} {vendor} rewards")
                search_queries.insert(2, f"{card} {vendor} cashback")
            
            card_text_combined = ""
            for query in search_queries:
                url = f"https://www.google.com/search?q={query}"
                card_text = fetch_card_page(url)
                if card_text and not card_text.startswith("Error"):
                    card_text_combined += f"\n{card_text}"
            combined_text += f"\n\n=== {card} ===\n{card_text_combined}"
    
    progress_placeholder.empty()
    
    if not combined_text.strip():
        st.error("Failed to fetch credit card information. Please try again.")
        st.stop()
    
    # Build vector store (cached automatically based on text content)
    store = build_vector_store(combined_text)
    # Use improved retrieval that searches per card
    vendor_context = f" at {vendor}" if vendor != "None" else ""
    rules = retrieve_rules_for_cards(store, card_list, category, k_per_card=6)

    # Convert card_list to tuple for hashability in cache (sort for consistent caching)
    result = choose_card(
        cards=tuple(sorted(card_list)),
        purchase=f"{category} purchase{vendor_context} of ${amount}",
        rules=rules
    )

    # Display result with improved UI
    st.divider()
    st.subheader("✨ Recommended Card")
    
    if isinstance(result, dict):
        # Display recommended card
        if "recommended_card" in result:
            recommended = result["recommended_card"]
            st.success(f"### 🏆 {recommended}")
            
            # Show why it's recommended
            if "quote" in result:
                st.markdown("**Why this card?**")
                st.info(f'> {result["quote"]}')
        
        # Display all cards comparison
        if "rewards" in result:
            st.markdown("---")
            st.markdown("### 📊 Reward Comparison")
            
            # Create comparison display
            comparison_data = []
            for card_name, reward_info in result["rewards"].items():
                is_recommended = card_name == result.get("recommended_card", "")
                # Format reward info - handle "not found" case
                if "not found" in reward_info.lower() or "information not available" in reward_info.lower():
                    formatted_reward = "No rewards information available for this category"
                else:
                    formatted_reward = reward_info
                
                comparison_data.append({
                    "Card": f"🏆 {card_name}" if is_recommended else card_name,
                    "Rewards": formatted_reward
                })
            
            # Display as columns for better visualization
            if len(comparison_data) > 1:
                cols = st.columns(len(comparison_data))
                for idx, col_item in enumerate(comparison_data):
                    with cols[idx]:
                        is_best = "🏆" in col_item["Card"]
                        if is_best:
                            st.success(f"**{col_item['Card'].replace('🏆 ', '')}**\n\n{col_item['Rewards']}")
                        else:
                            st.info(f"**{col_item['Card']}**\n\n{col_item['Rewards']}")
            else:
                # Single card case
                for item in comparison_data:
                    reward_text = item['Rewards']
                    st.write(f"**{item['Card']}**: {reward_text}")
    else:
        st.write(result)
