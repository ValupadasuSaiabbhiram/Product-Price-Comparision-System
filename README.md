# Product-Price-Comparision-System

This project is a web-based application that allows users to search for products and compare prices from Amazon. It also predicts the price trends for the next 7 days using a linear regression model. The application is built with Flask, Python, and uses web scraping techniques to extract product data from Amazon.

## Features

- **Search for Products**: Users can search for products by name.
- **Price Comparison**: Displays a list of products with prices scraped from Amazon.
- **Price Trend Prediction**: Predicts the price trends for the next 7 days using historical price data.
- **Responsive UI**: A clean and responsive user interface for both desktop and mobile views.

## Technologies Used

- **Flask**: Web framework for building the application.
- **Python**: Backend logic, data scraping, and machine learning.
- **BeautifulSoup**: Web scraping to extract product details from Amazon.
- **Scikit-learn**: Linear regression model for predicting price trends.
- **HTML/CSS**: Frontend for displaying the product data and results.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/product-price-comparison.git
   cd product-price-comparison

2. Create and activate a virtual environment:
    ```python
    python3 -m venv venv
    source venv/bin/activate  # For Windows: venv\Scripts\activate

3. Install the required dependencies:
    ```python
    pip install -r requirements.txt

## Usage

Run the Flask application:
   ```python
    python3 app.py

Open your browser and navigate to http://127.0.0.1:5000/ to access the application.

On the home page, enter the product name (e.g., "laptop") and click Search.

The results page will show:
       A list of products with prices from Amazon.
       Predicted price trends for the next 7 days.