import numpy as np
from sklearn.linear_model import LinearRegression

class PriceTrend:
    def __init__(self, historical_prices):
        self.historical_prices = historical_prices
        self.model = LinearRegression()

    def train_model(self):
        X = np.array(range(len(self.historical_prices))).reshape(-1, 1)
        y = np.array(self.historical_prices).reshape(-1, 1)
        self.model.fit(X, y)

    def predict_price(self, days_ahead):
        future_day = len(self.historical_prices) + days_ahead
        return self.model.predict([[future_day]])[0][0]
