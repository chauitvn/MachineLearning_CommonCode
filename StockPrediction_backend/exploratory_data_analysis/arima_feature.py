import numpy as np
import pandas as pd
from math import sqrt
from matplotlib import pyplot
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller
from sklearn.metrics import mean_squared_error
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from cores.class_base.stock_analysis_base import StockAnalysisBase


class ArimaCalc(StockAnalysisBase):
    def __init__(self, data) -> None:
        self.DATA = data
        super().__init__()

    def run(self):
        newdata = self.DATA[self.close]

        newdata.index = newdata.index.to_period('D')
        log_data = np.log(newdata)
        df_log_shift = log_data - log_data.shift()
        df_log_shift.dropna(inplace=True)

        # Dickey–Fuller test:
        result = adfuller(df_log_shift)
        print('ADF Statistic: {}'.format(result[0])) 
        print('p-value: {}'.format(result[1]))
        print('Critical Values:')
        for key, value in result[4].items():
            print('\t{}: {}'.format(key, value))

        plot_acf(df_log_shift.values)
        plot_pacf(df_log_shift.values, lags=50)
        pyplot.show()
        orders = [(1, 0, 1), (1, 0, 0), (0, 0, 1)]
        for order in orders:
            model = ARIMA(df_log_shift.values, order = order)
            model_fit = model.fit()
            model_name = 'ARIMA({},{},{})'.format(order[0], order[1], order[2])
            print('{} --> AIC={}; BIC={}'.format(model_name, model_fit.aic, model_fit.bic))
        #series = self.DATA[self.close].diff(periods=1)
        #model = ARIMA(df_log_shift, order=(1, 0, 1))
        #model_fit = model.fit()
        #print(model_fit.summary())
        #self.DATA['ARIMA'] = model_fit.forcast()[0]
        series = df_log_shift.values
        size = int(len(series) * 0.8)
        train, test = series[0:size], series[size:len(series)]
        history = [x for x in train]
        predictions = list()
        # walk-forward validation
        for t in range(len(test)):
            model = ARIMA(history, order = (0,0,1))
            model_fit = model.fit()
            output = model_fit.forecast()
            yhat = output[0]
            # revert to orginal
            predictions.append(yhat)
            #obs = test[t]
            #history.append(obs)
            #print('predicted=%f, expected=%f' % (yhat, obs))

        # evaluate forecasts
        rmse = sqrt(mean_squared_error(test, predictions))
        print('Test RMSE: %.3f' % rmse)
        # plot forecasts against actual outcomes
        pyplot.plot(test)
        pyplot.plot(predictions, color='red')
        pyplot.show()

        # revert to orginal
        test_diff = test.cumsum()
        org_test = np.exp(test_diff)
        predictions_diff = pd.Series(predictions, copy=True)
        org_predictions = np.exp(predictions_diff)
        pyplot.plot(org_test)
        pyplot.plot(org_predictions, color='green')