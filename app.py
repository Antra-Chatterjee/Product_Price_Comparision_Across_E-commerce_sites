import streamlit as st
import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import quote_plus
from playwright.sync_api import sync_playwright

# -------------------------
# HEADERS for requests
# -------------------------
HEADERS = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
}

# -------------------------
# AMAZON SCRAPER (BeautifulSoup)
# -------------------------
def get_amazon(product):
    try:
        query = quote_plus(product)
        url = f"https://www.amazon.in/s?k={query}"
        r = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")

        name = soup.select_one("h2 span")
        price = soup.select_one(".a-price-whole")

        if name and price:
            return {
                "Website": "Amazon",
                "Product": name.get_text(strip=True),
                "Price": int(price.get_text(strip=True).replace(",", "")),
                "Link": url
            }
    except Exception as e:
        print("Amazon error:", e)

    return {"Website": "Amazon", "Product": "Not Found", "Price": None, "Link": url}

# -------------------------
# FLIPKART SCRAPER (Playwright)
# -------------------------
def get_flipkart(product):
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            url = f"https://www.flipkart.com/search?q={quote_plus(product)}"
            page.goto(url)

            # Wait for price element
            page.wait_for_selector("div._30jeq3", timeout=5000)

            title = page.query_selector("div._4rR01T")
            price = page.query_selector("div._30jeq3")

            browser.close()

            if title and price:
                p_clean = ''.join(ch for ch in price.inner_text() if ch.isdigit())
                return {
                    "Website": "Flipkart",
                    "Product": title.inner_text(),
                    "Price": int(p_clean),
                    "Link": url
                }
    except Exception as e:
        print("Flipkart error:", e)

    return {"Website": "Flipkart", "Product": "Not Found", "Price": None, "Link": f"https://www.flipkart.com/search?q={product}"}

# -------------------------
# STREAMLIT UI
# -------------------------
st.set_page_config(page_title="Price Comparison", page_icon="🛒", layout="wide")
st.title("🛒 Product Price Comparison")

product = st.text_input("Enter Product Name", value="iPhone 14")

if st.button("Compare Prices"):
    with st.spinner("Searching..."):
        results = [get_amazon(product), get_flipkart(product)]

    valid = [x for x in results if x["Price"] is not None]

    col1, col2 = st.columns(2)
    for col, item in zip([col1, col2], results):
        with col:
            st.subheader(item["Website"])
            st.write(item["Product"])
            if item["Price"] is not None:
                st.success(f"₹{item['Price']:,}")
            else:
                st.error("Price not found")
            st.link_button(f"Open {item['Website']}", item["Link"])

    st.divider()

    if len(valid) >= 2:
        cheapest = min(valid, key=lambda x: x["Price"])
        st.success(f"🏆 Cheapest Price: {cheapest['Website']} (₹{cheapest['Price']:,})")

        df = pd.DataFrame(valid)
        st.subheader("Price Comparison")
        st.dataframe(df[["Website", "Price"]], use_container_width=True)
    else:
        st.warning("Less than two websites returned prices.")
