from statsmodels.tsa.arima_model import ARIMA
from extensions.technical_indicators.indicator_base import Indicator_Base

class ArimaIndicator(Indicator_Base):
    def __init__(self, data) -> None:
        self.DATA = data
        super().__init__()

    def calculate(self):
        series = self.data[self.close].diff(periods=1)

        model = ARIMA(series, order=(5, 1, 0))
        model_fit = model.fit(disp=0)
        output = model_fit.forecast()
        self.DATA['ARIMA'] = output[0]
        return self.DATA