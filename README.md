# Monte Carlo Stock Price Prediction

![Alt text]('/Users/nataliehill/Desktop/Screenshot 2023-07-27 at 8.29.11 PM.png')

## Overview

This Python script performs a Monte Carlo simulation to predict future stock prices of Apple Inc. (ticker symbol: AAPL) based on historical closing price data. The simulation uses statistical analysis to generate multiple potential stock price paths and provides insightful metrics for analysis.

## Prerequisites

Before running this code, ensure you have the required libraries installed. You can install them using pip:

```
pip install yfinance numpy matplotlib scipy
```

## Usage

1. Import the necessary libraries:
   ```python
   import yfinance as yf
   import numpy as np
   from random import random
   import matplotlib.pyplot as plt
   from scipy.stats import norm
   ```

2. Set the start and end dates for historical data:
   ```python
   start_date = '1980-07-27'
   end_date = '2023-07-01'
   ```

3. Retrieve historical data for Apple stock using Yahoo Finance:
   ```python
   ticker = yf.Ticker('AAPL')
   hist = ticker.history(start=start_date, end=end_date)
   ```

4. Display and visualize the historical closing price data:
   ```python
   hist = hist[['Close']]
   hist['Close'].plot(title='AAPL Stock Price', ylabel='Closing price $', figsize=[10, 6])
   plt.grid()
   plt.show()
   ```

5. Calculate statistical information for the model:
   ```python
   change = hist['Close'].pct_change().tolist()
   mean = np.mean(change)
   std_dev = np.std(change)
   ```

6. Perform the Monte Carlo simulation:
   ```python
   simulations = 300
   days_to_sim = 252
   for i in range(simulations):
       # Simulation code here...
   ```

7. Display the results of the Monte Carlo simulation:
   ```python
   # Average Closing Price and Probability of Increasing After 1 Year
   average_closing_price = sum(close_end) / simulations
   average_perc_change = (average_closing_price - orig_price[-1]) / orig_price[-1]
   probability_of_increase = sum(above_close) / simulations
   ```

8. View the simulated stock price predictions:
   ```python
   plt.title("Monte Carlo Stock Prices [" + str(simulations) + " simulations]")
   plt.xlabel("Trading Days After " + start_date)
   plt.ylabel("Closing Price $")
   plt.xlim([10700, len(days) + days_to_sim])
   plt.grid()
   plt.show()
   ```

## Analytical Results

After running the Monte Carlo simulation with 300 iterations, the following insightful results are obtained:

1. **Mean percent change**: The average percentage change in the simulated stock price over one trading day is approximately 0.11%. This metric provides an indication of the expected daily growth or decline in the stock price.

2. **Standard Deviation of percent change**: The standard deviation of the percent change in the simulated stock price is about 2.82%. This metric measures the volatility or dispersion of the daily price changes and highlights the stock's sensitivity to market fluctuations.

3. **Predicted closing price after 300 simulations**: The average closing price projected by the Monte Carlo simulation is approximately $255.02. This prediction represents an aggregated estimate based on multiple potential stock price paths.

4. **Predicted percent increase after 1 year**: The predicted percent increase in the stock price after one year is approximately 31.47%. This metric offers insights into the potential long-term growth of the stock based on the simulation's results.

5. **Probability of stock price increasing after 1 year**: The probability of the stock price increasing after one year is approximately 65.0%. This probability estimate helps assess the likelihood of a positive stock performance in the coming year.

## Notes

- The script utilizes historical stock price data to generate simulated future stock price scenarios. However, it's important to remember that stock market behavior is complex and subject to numerous unpredictable factors.

- The Monte Carlo simulation provides a statistical approach to understand potential outcomes, but it should not be used as the sole basis for making financial decisions.

- Feel free to adjust the number of simulations (`simulations`) and the number of days to simulate (`days_to_sim`) to explore different scenarios and refine the predictions further.

- For more detailed information about the functions and libraries used in this script, refer to the official documentation of `yfinance`, `numpy`, `matplotlib`, and `scipy`.

- This Python script for predicting stock prices using Monte Carlo methods was inspired by and references the article titled "Predicting Stock Prices Using Monte Carlo Methods in Python" available on Medium (https://medium.com/illumination/predicting-stock-prices-using-monte-carlo-methods-in-python-2b099c408162). 

Enjoy exploring the Monte Carlo simulation results and use the provided metrics to gain insights into the potential future stock prices of Apple Inc. If you have any questions or suggestions, feel free to reach out. Happy coding and happy investing!
