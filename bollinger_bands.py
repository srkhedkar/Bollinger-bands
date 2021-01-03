import pandas as pd
import matplotlib.pyplot as plt

# Block 1 for BSE SENSEX
################################################################################
# read the Indian BSE data file
stockprices = pd.read_csv('D:\\python\\data\\SensexHistoricalData.csv')

#setting date as index
stockprices['Date'] = pd.to_datetime(stockprices.Date)
stockprices.index = stockprices['Date']

# Following parameters should be decided by data analyst. 
# Refer bollinger bands rules for more details at official site https://www.bollingerbands.com/bollinger-band-rules
yearsOfData = 20
windowSizeFactor = 6
windowSize = 20 + yearsOfData * windowSizeFactor
stdDeviationFactor = 0.025
stdDeviation = 2 + (yearsOfData * stdDeviationFactor)

# Calculate moving average
stockprices['Moving_avg_n'] = stockprices['Close'].rolling(window=windowSize).mean()

# Calculate moving standard deviation
stockprices['Standard_deviation_n'] = stockprices['Close'].rolling(window=windowSize).std() 

# Calculate the upper band
stockprices['Upper_band'] = stockprices['Moving_avg_n'] + (stockprices['Standard_deviation_n'] * stdDeviation)

# Calculate the lower band
stockprices['Lower_band'] = stockprices['Moving_avg_n'] - (stockprices['Standard_deviation_n'] * stdDeviation)

# Plot the graph
stockprices[['Close','Upper_band','Lower_band']].plot(figsize=(10,4))
plt.grid(True)
plt.title(' Bollinger Bands ')
plt.axis('tight')
plt.ylabel('Price')
plt.legend(["Market Close", "Upper Band", "Lower Band"])
plt.show()