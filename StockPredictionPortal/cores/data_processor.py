from data_processors.vnstock import VnStock
from cores.class_base.data_processor_base import DataProcessorBase
from extensions.technical_indicators.commons.heikin_ashi_indicator import HeikinAshiIndicator
from extensions.technical_indicators.commons.smoothed_heikin_ashi_indicator import SmoothedHeikinAshiIndicator


class DataProcessor(DataProcessorBase):
    def __init__(self, symbol: str, data_source:str, start_date: str, end_date: str, **kwargs):
        self.start_date = start_date
        self.end_date = end_date
        self.symbol = symbol
        self.data_source = data_source
        super().__init__()

    def download_data(self):
        vnStockObj = VnStock(self.symbol, self.data_source, self.start_date, self.end_date)
        return vnStockObj.get_raw_data()

    def run(self):
        self.DATA = self.download_data()
        # convert candlestick data to heikin ashi data
        #heikin_ashi = HeikinAshiIndicator(self.DATA)
        #self.DATA  = heikin_ashi.calculate()
        smoothed_heikin_ashi = SmoothedHeikinAshiIndicator(self.DATA)
        self.DATA  = smoothed_heikin_ashi.calculate()
        return self.DATA

    def get_raw_data(self):
        pass