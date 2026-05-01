import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import LLMChain

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)


def choose_card(cards, rules, purchase):
    """
    Matches exactly how your app.py is calling the function.
    """

    combined_context = ""

    for card in cards:
        combined_context += f"\n\nCard: {card}\n"
        combined_context += rules.get(card, "")

    prompt = ChatPromptTemplate.from_template(
        """
You are a credit card rewards expert.

Using the reward information below, determine which card gives the best rewards.

Purchase Amount: ${purchase}

Reward Information:
{context}

Instructions:
1. Compare all cards.
2. Calculate estimated rewards.
3. Clearly mention the best card.
4. Provide reasoning.
5. Include supporting quotes.

Return a clear recommendation.
"""
    )

    chain = LLMChain(llm=llm, prompt=prompt)

    response = chain.run(
        context=combined_context,
        purchase=purchase
    )

    return response