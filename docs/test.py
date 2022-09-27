# line plot of time series
from pandas import read_csv
from statsmodels.tsa.arima.model import ARIMA
from matplotlib import pyplot
import numpy as np
# load dataset
series = read_csv('docs\daily-min-temperatures.csv', header=0, index_col=0)
# display first few rows
# line plot of dataset
#series.plot()
#pyplot.show()

# split the dataset
split_point = len(series) - 7
dataset, validation = series[0:split_point], series[split_point:]
print('Dataset %d, Validation %d' % (len(dataset), len(validation)))
#dataset.to_csv('dataset.csv', index=False)
#validation.to_csv('validation.csv', index=False)

# create a differenced series
def difference(dataset, interval=1):
	diff = list()
	for i in range(interval, len(dataset)):
		value = dataset[i] - dataset[i - interval]
		diff.append(value)
	return np.array(diff)

# seasonal difference
X = series.values
days_in_year = 1
differenced = difference(X, days_in_year)
# fit model
model = ARIMA(differenced, order=(7,0,1))
model_fit = model.fit()

# one-step out-of sample forecast
start_index = len(differenced)
end_index = start_index + 6
forecast = model_fit.forecast()

# print summary of fit model
print("test:"+forecast)

# invert differenced value
def inverse_difference(history, yhat, interval=1):
    print("history %f"%history[-interval])
    return yhat + history[-interval]

history = [x for x in X]
day = 1
for yhat in forecast:
	inverted = inverse_difference(history, yhat, day)
	print('Day %d: %f' % (day, inverted))
	history.append(inverted)
	day += 1