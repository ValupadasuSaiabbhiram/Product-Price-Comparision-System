from flask import Flask, render_template, request
from scraper import AmazonScraper
from price_trends import PriceTrend

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        query = request.form.get("query")
        amazon_scraper = AmazonScraper()

        try:
            content = amazon_scraper.get_page_content(query)
            products = amazon_scraper.parse_page(content)
        except Exception as e:
            return f"Error fetching data: {e}"

        # Sample historical prices for trend analysis (real-world: collect over time)
        historical_prices = [product["price"] for product in products[:5]]
        trend_model = PriceTrend(historical_prices)
        trend_model.train_model()

        # Predict price trends for the next 7 days
        price_trends = [trend_model.predict_price(i) for i in range(1, 8)]
        return render_template("results.html", products=products, trends=price_trends)

    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)
