from cores.class_base.indicator_base import Indicator_Base


class HeikinAshiIndicator(Indicator_Base):
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

    def calculate(self):
        self._DATA["Open_Previous"] = self._DATA["open"].shift(periods=1)
        self._DATA["Close_Previous"] = self._DATA["close"].shift(periods=1)

        # Heiken-Ashi Open
        self._DATA["HA_Open"] = (self._DATA["Open_Previous"] + self._DATA["Close_Previous"]) / 2

        # Heiken-Ashi Close
        self._DATA["HA_Close"] = (self._DATA["open"] + self._DATA["high"] + self._DATA["low"] + self._DATA["close"]) / 4

        # Heiken-Ashi High
        self._DATA["HA_High"] = self._DATA.apply(lambda x: self.get_max_value(x["open"], x["high"], x["close"]), axis=1)

        # Heiken-Ashi Low
        self._DATA["HA_Low"] = self._DATA.apply(lambda x: self.get_min_value(x["open"], x["high"], x["close"]), axis=1)

        # Update data again
        self._DATA["open"] = self._DATA["HA_Open"]
        self._DATA["close"] = self._DATA["HA_Close"]
        self._DATA["high"] = self._DATA["HA_High"]
        self._DATA["low"] = self._DATA["HA_Low"]

        # Resample the time series data
        self._DATA = self._DATA.asfreq('D')
        self._DATA["adjust_weekly"] = self._DATA["close"].resample('W-MON').mean()
        self._DATA["adjust_monthly"] = self._DATA["close"].resample('M').mean()

        # removing the unused data
        drop_columns = ["Open_Previous", "Close_Previous", "HA_High", "HA_Low", "HA_Open", "HA_Close", "adjust"]
        self._DATA.drop(columns=drop_columns, axis=1, inplace=True)
        return self._DATA