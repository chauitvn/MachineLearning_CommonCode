from extensions.vnquant.DataLoader import DataLoader
from data_processors.data_processor_base import DataProcessorBase


class VnStock(DataProcessorBase):
    def __init__(self, symbols: str, start_date:str, end_date:str):
        self.symbols = symbols
        self.start_date = start_date
        self.end_date = end_date

    def get_raw_data(self):
        loader = DataLoader(symbols=self.symbols, start=self.start_date,  end=self.end_date, minimal=True,
                            data_source="vnd")
        data = loader.download()
        data.columns = data.columns.droplevel(1)
        # data = data.reset_index(drop=False, inplace=False)
        # the date default is 2016-01-26
        # data["date"] = pd.to_datetime(data["date"], format="%Y-%m-%d")
        return data