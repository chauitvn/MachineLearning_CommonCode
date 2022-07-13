import talib as ta
from extensions.technical_indicators.indicator_base import Indicator_Base


class CommonIndicator(Indicator_Base):
    def __init__(self, data) -> None:
        self.DATA = data
        super().__init__()

    def calculate(self):
        # Create 7 and 21 days Moving Average
        self.DATA["ma7"] = ta.MA(self.DATA[self.close], 7)
        self.DATA["ma21"] = ta.MA(self.DATA[self.close], 7)
        #Create MACD
        macd, macdsignal, macdhist = ta.MACD(self.DATA[self.close], fastperiod=12, slowperiod=26, signalperiod=9)
        self.DATA["ma21"] = macd
        #Create Bollinger Bands
        upperband, middleband, lowerband = ta.BBANDS(self.DATA[self.close], timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)
        self.DATA["upper_band"] = upperband
        self.DATA["lower_band"] = lowerband
        #Create Exponential moving average
        self.DATA['ema'] = ta.EMA(self.DATA[self.close], timeperiod=21)

        #Create Momentum
        self.DATA['momentum'] = (self.DATA[self.close]/100)-1

        return self.DATA
