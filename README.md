# ARIMA Forecasting Script for Stock Prices

This Python script downloads historical stock data, fits an ARIMA model to the closing prices, and forecasts future prices using the ARIMA model. The forecast is then visualized alongside the observed data with Matplotlib.

## Features

- Downloads historical stock data from Yahoo Finance for a specified ticker and date range.
- Handles missing data and validates the data set.
- Fits an ARIMA model to the cleaned closing prices.
- Forecasts the next 5 business days of stock prices.
- Visualizes both historical and forecasted data with a confidence interval.

## Prerequisites

- Python 3.x
- The following Python libraries:
  - pandas
  - matplotlib
  - yfinance
  - statsmodels

Install the required libraries using pip:

```bash
pip install pandas matplotlib yfinance statsmodels
```
## Usage

- Update the ticker variable in the script to your desired stock symbol (example: 'NVDA' or 'MSTR').

- Modify the start and end dates if necessary.

## Run the script in your terminal:
```bash
python your_script_name.py
```
- or run it in a Jupiter notebook

## Script Overview

- Data Downloading: Uses yfinance to download historical data for the specified ticker.

- Data Cleaning: Extracts and cleans the 'Close' prices from the downloaded data.

- ARIMA Model Fitting: Constructs and fits an ARIMA model to the time series data.

- Forecasting: Generates a forecast for the next 5 business days along with a confidence interval.

- Visualization: Uses Matplotlib to display the historical data, forecast, and confidence intervals.

# Troubleshooting

- Ensure that the ticker symbol and date range provided return valid data.

- If the script raises a ValueError, check that the downloaded data is not empty and that there are no issues with network connectivity.

## License
This project is open source and available under the MIT License.
