from openai import OpenAI

# ✅ Replace with your OpenAI API key
client = OpenAI(api_key="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")

# 🛍️ Example product list (can change later)
products = [
    {"title": "Weighted Vest 20kg Adjustable", "price": "$89", "rating": "4.5", "link": "https://example.com/1"},
    {"title": "Breathable Weighted Vest 15kg", "price": "$79", "rating": "4.7", "link": "https://example.com/2"},
    {"title": "Compact Weight Vest 10kg", "price": "$99", "rating": "4.6", "link": "https://example.com/3"}
]
import requests

def fetch_products_from_amazon(query):
    api_key = "fbc8b52cf2e9f841f1396434f6102cbafdd1b7a3e6be1ad5206ea85f039f85cf"
    params = {
        "engine": "google",
        "q": f"{query} site:amazon.com",
        "api_key": api_key
    }

    response = requests.get("https://serpapi.com/search", params=params)
    results = response.json()

    products = []

    for result in results.get("organic_results", [])[:5]:
        title = result.get("title")
        link = result.get("link")
        snippet = result.get("snippet", "")
        products.append({
            "title": title,
            "price": "N/A",
            "rating": "N/A",
            "link": link,
            "desc": snippet
        })

    return products

def ask_gpt_to_rank(products):
    prompt = f"""
You are a shopping assistant. Rank the following products from best to worst based on value and quality. 
List your top 3 choices, and for each, explain pros and cons.

Products:
{products}
    """

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

# ▶️ MAIN
if __name__ == "__main__":
    query = "noise cancelling headphones"  # You can change this
    products = fetch_products_from_amazon(query)
    result = ask_gpt_to_rank(products)
    print("\n🧠 GPT's Top Picks:\n")
    print(result)
def fetch_products_from_amazon(query):
    api_key = "fbc8b52cf2e9f841f1396434f6102cbafdd1b7a3e6be1ad5206ea85f039f85cf"
    params = {
        "engine": "google",
        "q": f"{query} site:amazon.com",
        "api_key": api_key
    }

    response = requests.get("https://serpapi.com/search", params=params)
    results = response.json()

    products = []

    for result in results.get("organic_results", [])[:5]:
        title = result.get("title")
        link = result.get("link")
        snippet = result.get("snippet", "")
        products.append({
            "title": title,
            "price": "N/A",
            "rating": "N/A",
            "link": link,
            "desc": snippet
        })

    return products
def fetch_products_from_amazon(query):
    api_key = "fbc8b52cf2e9f841f1396434f6102cbafdd1b7a3e6be1ad5206ea85f039f85cf"
    params = {
        "engine": "google",
        "q": f"{query} site:amazon.com",
        "api_key": api_key
    }

    response = requests.get("https://serpapi.com/search", params=params)
    results = response.json()

    products = []

    for result in results.get("organic_results", [])[:5]:
        title = result.get("title")
        link = result.get("link")
        snippet = result.get("snippet", "")
        products.append({
            "title": title,
            "price": "N/A",
            "rating": "N/A",
            "link": link,
            "desc": snippet
        })

    return products