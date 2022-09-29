import talib as ta
import plotly.graph_objects as go
from cores.class_base.indicator_base import Indicator_Base


class SmoothedHeikinAshiIndicator(Indicator_Base):
    def __init__(self, data) -> None:
        self._DATA = data
        super().__init__()

    def get_max_value(self, open, high, close):
        values = [open, high, close]
        return_value = max(values)
        return return_value
    
    def get_min_value(self, open, high, close):
        values = [open, high, close]
        return_value = min(values)
        return return_value

    def buiding_indicator(self):
        self._DATA["Open_Previous"] = self._DATA["open"].shift(periods=1)
        self._DATA["Close_Previous"] = self._DATA["close"].shift(periods=1)

        # Calculate EMA
        self._DATA["ema_open"] = ta.EMA(self._DATA["open"], 6)
        self._DATA["ema_close"] = ta.EMA(self._DATA["close"], 6)
        self._DATA["ema_high"] = ta.EMA(self._DATA["high"], 6)
        self._DATA["ema_low"] = ta.EMA(self._DATA["low"], 6)
        self._DATA["ema_open_previous"] = ta.EMA(self._DATA["Open_Previous"], 6)
        self._DATA["ema_close_previous"] = ta.EMA(self._DATA["Close_Previous"], 6)


        # Heiken-Ashi Open
        self._DATA["HA_Open"] = (self._DATA["ema_open_previous"] + self._DATA["ema_close_previous"]) / 2

        # Heiken-Ashi Close
        self._DATA["HA_Close"] = (self._DATA["ema_open"] + self._DATA["ema_high"] + self._DATA["ema_low"] + self._DATA["ema_close"]) / 4

        # Heiken-Ashi High
        self._DATA["HA_High"] = self._DATA.apply(lambda x: self.get_max_value(x["ema_open"], x["ema_high"], x["ema_close"]), axis=1)

        # Heiken-Ashi Low
        self._DATA["HA_Low"] = self._DATA.apply(lambda x: self.get_min_value(x["ema_open"], x["ema_high"], x["ema_close"]), axis=1)

        # Update data again
        self._DATA["open"] = self._DATA["HA_Open"]
        self._DATA["close"] = self._DATA["HA_Close"]
        self._DATA["high"] = self._DATA["HA_High"]
        self._DATA["low"] = self._DATA["HA_Low"]

        # removing the unused data
        drop_columns = ["Open_Previous", "Close_Previous", "HA_High", "HA_Low", "HA_Open", "HA_Close", "adjust", "ema_open","ema_close",
                    "ema_high","ema_low","ema_open_previous","ema_close_previous"]
        self._DATA.drop(columns=drop_columns, axis=1, inplace=True)


    def calculate(self):
        self.buiding_indicator()
        return self._DATA


    def plot(self):
        sampleData = self._DATA.tail(200)
        
        date = sampleData.index
        fig = go.Figure(data=[go.Candlestick(x=date,
                open=sampleData[self.open],
                high=sampleData[self.high],
                low=sampleData[self.low],
                close=sampleData[self.close],)])
        fig.update_layout(
            title='The Smoothed Heiki Ashi',
            yaxis_title='{} Stock'.format(self.stock_symbol)
        )
        fig.show()