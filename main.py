import yfinance as yf
import numpy as np
from random import random
import matplotlib.pyplot as plt
from scipy.stats import norm

# get history of Apple
ticker = yf.Ticker('AAPL')
start_date = '1980-07-27'
end_date = '2023-07-01'
hist = ticker.history(start=start_date, end=end_date)
print(hist.head())

# get closing data
hist = hist[['Close']]
print(hist)
hist['Close'].plot(title='AAPL Stock Price', ylabel='Closing price $', figsize=[10, 6])
plt.grid()
plt.show()

# create lists
days = [i for i in range(1, len(hist['Close'])+1)]
orig_price = hist['Close'].tolist()
change = hist['Close'].pct_change().tolist()
change = change[1:]

# stats for model
mean = np.mean(change)
std_dev = np.std(change)
print('\nMean percent change: ' + str(round(mean*100, 2)) + '%')
print('Standard Deviation of percent change: ' +
      str(round(std_dev*100, 2)) + '%')

simulations = 300
days_to_sim = 252

fig = plt.figure(figsize=[10, 6])
plt.plot(days, orig_price)
plt.title("Monte Carlo Stock Prices [" + str(simulations) +
          " simulations]")
plt.xlabel("Trading Days After " + start_date)
plt.ylabel("Closing Price [$]")
plt.xlim([2000, len(days)+days_to_sim])
plt.grid()
plt.show()

# Initializing Lists for Analysis
close_end = []
above_close = []

# create each simulation
for i in range(simulations):
    num_days = [days[-1]]
    close_price = [hist.iloc[-1, 0]]

    # loop through each day
    for j in range(days_to_sim):
        num_days.append(num_days[-1]+1)
        perc_change = norm.ppf(random(), loc=mean, scale=std_dev)
        close_price.append(close_price[-1] * (1 + perc_change))

    if close_price[-1] > orig_price[-1]:
        above_close.append(1)
    else:
        above_close.append(0)

    close_end.append(close_price[-1])
    plt.plot(num_days, close_price)

plt.title("Monte Carlo Stock Prices [" + str(simulations) +
          " simulations]")
plt.xlabel("Trading Days After " + start_date)
plt.ylabel("Closing Price $")
plt.xlim([10700, len(days)+days_to_sim])
plt.grid()

# Average Closing Price and Probability of Increasing After 1 Year
average_closing_price = sum(close_end)/simulations
average_perc_change = (average_closing_price-
                       orig_price[-1])/orig_price[-1]
probability_of_increase = sum(above_close)/simulations
print('\nPredicted closing price after ' + str(simulations) +
      ' simulations: $' + str(round(average_closing_price, 2)))
print('Predicted percent increase after 1 year: ' +
      str(round(average_perc_change*100, 2)) + '%')
print('Probability of stock price increasing after 1 year: ' +
      str(round(probability_of_increase*100, 2)) + '%')

# Displaying the Monte Carlo Simulation Lines
plt.show()