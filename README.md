# 🛒 Product Price Comparison Web Application
A web-based Product Price Comparison System built using Python and Streamlit.
The application searches for a product on different e-commerce websites and compares their prices to help users identify the cheapest available option.

## ✨ Features

- 🔍 Search for products by name
- 🛒 Compare prices from Amazon and Flipkart
- 💰 Automatically identify the lowest price
- 📊 Display prices in a comparison table
- 🔗 Provide direct links to the websites
- ⚡ Fetch product information during the search

## 🛠️ Technologies Used

- **Python** – Main programming language
- **Streamlit** – Web application interface
- **BeautifulSoup** – Amazon web scraping
- **Requests** – Sending HTTP requests
- **Playwright** – Flipkart browser automation and dynamic content extraction
- **Pandas** – Price comparison and data handling

## 🔄 How It Works

```text
Enter Product Name
        ↓
Search Amazon & Flipkart
        ↓
Extract Product & Price
        ↓
Compare Prices
        ↓
Display Cheapest Option
```

### Web Scraping Approach

**Amazon:** Uses `Requests` and `BeautifulSoup` to extract product name and price from the HTML page.

**Flipkart:** Uses `Playwright` to load the webpage in a browser and extract dynamically loaded product information.

## 📂 Project Structure

```text
PriceCompare/
│
├── app.py
├── requirements.txt
└── README.md
```

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Install Playwright browser

```bash
playwright install chromium
```

### 4. Run the application

```bash
streamlit run app.py
```

## 📊 Example

Search for a product such as:

```text
iPhone 14
```

The application displays the available prices from Amazon and Flipkart and highlights the **cheapest price**.

## ⚠️ Limitations

- Website HTML structures may change, which can affect scraping.
- Prices and availability can change frequently.
- The application currently supports Amazon and Flipkart.
- Some websites may use anti-bot mechanisms.

## 🔮 Future Enhancements

- Add more e-commerce websites
- Add price history and price-drop alerts
- Improve product matching
- Add product image comparison
- Add AI-based product recognition

## 👩‍💻 Author

**Antra Chatterjee**  
B.Tech – Computer Science and Engineering

## 📜 Disclaimer

This project is developed for **educational purposes**. 
