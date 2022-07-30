from statsmodels.tsa.arima.model import ARIMA
from extensions.technical_indicators.indicator_base import Indicator_Base

class ArimaIndicator(Indicator_Base):
    def __init__(self, data) -> None:
        self.DATA = data
        super().__init__()

    def calculate(self):
        series = self.DATA[self.close].diff(periods=1)
        model = ARIMA(series, order=(5, 1, 0))
        model_fit = model.fit()
        print(model_fit.summary())
        self.DATA['ARIMA'] = model_fit.predict(steps=7)[0]
        return self.DATA