from data_processors.vnstock import VnStock
from extensions.technical_indicators.commons.heikin_ashi_indicator import HeikinAshiIndicator


class DataProcessor():
    def __init__(self, data_source: str, symbols:str, start_date: str, end_date: str, **kwargs):
        self.data_source = data_source
        self.symbols = symbols
        self.start_date = start_date
        self.end_date = end_date

    def download_data(self):
        vnStockObj = VnStock(self.symbols, self.start_date, self.end_date)
        return vnStockObj.get_raw_data()

    def run(self):
        self.DATA = self.download_data()
        # convert candlestick data to heikin ashi data
        heikin_ashi = HeikinAshiIndicator(self.DATA)
        self.DATA  = heikin_ashi.calculate()
        self.add_technical_indicator()