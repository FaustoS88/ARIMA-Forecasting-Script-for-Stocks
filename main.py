import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from statsmodels.tsa.arima.model import ARIMA

# Specify a ticker and date range; try 'MSFT' instead of 'AAPL'
ticker = 'NVDA'
data = yf.download(ticker, start='2018-01-01', end='2025-02-19')

if data.empty:
    raise ValueError(f"No data found for ticker {ticker} between the specified dates.")

close_prices = data['Close'].dropna()  # Clean NaNs

if close_prices.empty:
    raise ValueError(f"Closing prices series for {ticker} is empty after cleaning.")

# Fit an ARIMA model with relaxed constraints
model = ARIMA(close_prices, order=(1, 1, 1),
              enforce_stationarity=False,
              enforce_invertibility=False)
model_fit = model.fit()
print(model_fit.summary())

# Forecast the next 5 business days
forecast_steps = 5
forecast = model_fit.get_forecast(steps=forecast_steps)
forecast_mean = forecast.predicted_mean
forecast_ci = forecast.conf_int()

# Plot the observed data and forecast
plt.figure(figsize=(10, 6))
plt.plot(close_prices.index, close_prices, label='Observed', color='blue')

# Create a date range for the forecast using the last date in close_prices
last_date = close_prices.index[-1]
forecast_index = pd.date_range(start=last_date, periods=forecast_steps + 1, freq='B')[1:]
plt.plot(forecast_index, forecast_mean, label='Forecast', color='red')
plt.fill_between(forecast_index, forecast_ci.iloc[:, 0], forecast_ci.iloc[:, 1],
                 color='pink', alpha=0.3, label='Confidence Interval')

plt.xlabel('Date')
plt.ylabel('Price')
plt.title(f'{ticker} ARIMA Forecast')
plt.legend()
plt.show()