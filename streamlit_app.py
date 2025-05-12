import streamlit as st
from openai import OpenAI
import requests

# 🔑 Keys
import streamlit as st
openai_key = st.secrets["OPENAI_KEY"]
serpapi_key = st.secrets["SERPAPI_KEY"]


client = OpenAI(api_key=openai_key)

# 🔍 Search Function
def fetch_products(query):
    params = {
        "engine": "google",
        "q": f"{query} site:amazon.com",
        "api_key": serpapi_key
    }
    response = requests.get("https://serpapi.com/search", params=params)
    results = response.json()
    products = []
    for r in results.get("organic_results", [])[:5]:
        products.append({
            "title": r.get("title"),
            "link": r.get("link"),
            "desc": r.get("snippet", "")
        })
    return products

# 🧠 GPT Ranking
def rank_products(products):
    prompt = f"""
You are a shopping assistant. Rank the following products based on value and usefulness.
Output the top 3 with pros and cons, and include the product links.

Products:
{products}
    """
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# 🎨 Streamlit UI
st.title("🛍️ AI Deal Hunter")

query = st.text_input("What product are you searching for?", "weighted vest")

if st.button("Find Best Picks"):
    with st.spinner("Searching Amazon..."):
        products = fetch_products(query)
        result = rank_products(products)
        st.markdown("### 🧠 GPT's Top Picks:")
        st.markdown(result, unsafe_allow_html=True)