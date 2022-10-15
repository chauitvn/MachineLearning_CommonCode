import numpy as np
from math import sqrt
from matplotlib import pyplot
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from cores.class_base.indicator_base import Indicator_Base

class StockAnalysis(Indicator_Base):
    def __init__(self, data) -> None:
        self.DATA = data
        super().__init__()

    def calculate(self):
        self.arima_calc()

    def arima_calc(self):
        log_data = np.log(self.DATA[self.close])
        df_log_shift = log_data - log_data.shift()
        df_log_shift.dropna(inplace=True)

        # Dickey–Fuller test:
        result = adfuller(df_log_shift)
        print('ADF Statistic: {}'.format(result[0]))
        print('p-value: {}'.format(result[1]))
        print('Critical Values:')
        for key, value in result[4].items():
            print('\t{}: {}'.format(key, value))

        train_size = int(len(log_data) * 0.80)
        train, test = log_data[0:train_size], self.DATA[self.close][train_size:]
        # walk-forward validation
        history = [x for x in train]
        predictions = list()
        for i in range(len(test)):
            series = train.diff(periods=1)
            model = ARIMA(series, order=(2, 1, 2))
            model_fit = model.fit()
            yhat = model_fit.forcast()[0]
            yhat = self.inverse_difference(history, yhat)
            predictions.append(yhat)
            # observation
            obs = test[i]
            history.append(obs)
            print('>Predicted=%.3f, Expected=%.3f' % (yhat, obs))
        # report performance
        rmse = sqrt(mean_squared_error(test, predictions))
        print('RMSE: %.3f' % rmse)

    # create a differenced series
    def difference(dataset, interval=1):
        diff = list()
        for i in range(interval, len(dataset)):
            value = dataset[i] - dataset[i - interval]
            diff.append(value)
        return diff
    # invert differenced value
    def inverse_difference(history, yhat, interval=1):
        return yhat + history[-interval]

    def autocorrelation(self):
        series = self.DATA[self.close]
        #plot_acf(series)
        plot_pacf(series, lags=50)
        pyplot.show()