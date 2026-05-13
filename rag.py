import os
from dotenv import load_dotenv
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# Load environment variables
load_dotenv()

# Local HuggingFace embeddings (FREE, no API required)
embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)


def build_vector_store(text):
    """
    Builds FAISS vector store from scraped text.
    """
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=800,
        chunk_overlap=100,
        length_function=len
    )

    chunks = text_splitter.split_text(text)

    vector_store = FAISS.from_texts(chunks, embeddings)

    return vector_store


def retrieve_rules(vector_store, query, k=5):
    """
    Retrieve relevant rules based on a query.
    """
    docs = vector_store.similarity_search(query, k=k)
    return "\n\n".join([doc.page_content for doc in docs])


def retrieve_rules_for_cards(vector_store, card_list, category, k_per_card=5):
    """
    Retrieve reward rules separately for each card.
    Matches app.py expected function signature.
    """
    results = {}

    for card in card_list:
        query = f"{card} rewards for {category}"
        docs = vector_store.similarity_search(query, k=k_per_card)
        combined_text = "\n\n".join([doc.page_content for doc in docs])
        results[card] = combined_text

    return results