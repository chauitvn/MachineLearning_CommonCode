from data_processors.vnstock import VnStock


class DataProcessor():
    def __init__(self, data_source: str, symbols:str, start_date: str, end_date: str, **kwargs):
        self.data_source = data_source
        self.symbols = symbols
        self.start_date = start_date
        self.end_date = end_date


    def download_data(self):
        vnStockObj = VnStock(self.symbols, self.start_date, self.end_date)
        vnStockObj.get_raw_data()

    def add_technical_indicator(self):
        pass

    def run(self):
        self.DATA = self.download_data()
        self.add_technical_indicator()