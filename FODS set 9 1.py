import pandas as pd
import numpy as np
def calculate_variability(closing_prices):
    daily_returns = closing_prices.pct_change().dropna()
    volatility = np.std(daily_returns)
    return volatility
def analyze_stock_data(stock_data):
    df = pd.DataFrame(stock_data)
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    stock_variability = calculate_variability(df['Close'])
    print(f"Variability of stock prices: {stock_variability:.4f}")
    return df
if __name__ == "__main__":
    stock_data = {
        'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
        'Close': [100, 105, 98, 102, 107]
    }
    stock_df = analyze_stock_data(stock_data)
    print("\nStock Data DataFrame:")
    print(stock_df)
