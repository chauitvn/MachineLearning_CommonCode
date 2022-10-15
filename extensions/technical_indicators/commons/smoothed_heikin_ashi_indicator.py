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

    def buiding_indicator(self, periods, is_plot):
        self._DATA["Open_Previous"] = self._DATA["open"].shift(periods=1)
        self._DATA["Close_Previous"] = self._DATA["close"].shift(periods=1)

        # Calculate EMA
        self._DATA["ema_open"] = ta.EMA(self._DATA["open"], periods)
        self._DATA["ema_close"] = ta.EMA(self._DATA["close"], periods)
        self._DATA["ema_high"] = ta.EMA(self._DATA["high"], periods)
        self._DATA["ema_low"] = ta.EMA(self._DATA["low"], periods)
        self._DATA["ema_open_previous"] = ta.EMA(self._DATA["Open_Previous"], periods)
        self._DATA["ema_close_previous"] = ta.EMA(self._DATA["Close_Previous"], periods)


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

        if is_plot == False:
            # Resample the time series data
            self._DATA = self._DATA.asfreq('D')
            self._DATA["adjust_weekly"] = self._DATA["close"].resample('W-MON').mean()
            self._DATA["adjust_monthly"] = self._DATA["close"].resample('M').mean()

            self._DATA.fillna(method ='bfill', inplace=True)
            self._DATA.fillna(method ='ffill', inplace=True)

        # removing the unused data
        drop_columns = ["Open_Previous", "Close_Previous", "HA_High", "HA_Low", "HA_Open", "HA_Close", "adjust", "ema_open","ema_close",
                    "ema_high","ema_low","ema_open_previous","ema_close_previous"]
        self._DATA.drop(columns=drop_columns, axis=1, inplace=True)


    def calculate(self, is_plot):
        self.buiding_indicator(5, is_plot)
        return self._DATA