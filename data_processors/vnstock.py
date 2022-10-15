from extensions.vnquant.DataLoader import DataLoader
from cores.class_base.data_processor_base import DataProcessorBase


class VnStock(DataProcessorBase):
    def __init__(self, symbol: str, data_source:str, start_date:str, end_date:str):
        self.stock_symbol = symbol
        self.data_source = data_source
        self.start_date = start_date
        self.end_date = end_date

        super().__init__()

    def get_raw_data(self):
        loader = DataLoader(symbols=self.stock_symbol, start=self.start_date,  end=self.end_date, minimal=True,
                            data_source=self.data_source)
        data = loader.download()
        data.columns = data.columns.droplevel(1)
        # data = data.reset_index(drop=False, inplace=False)
        # the date default is 2016-01-26
        # data["date"] = pd.to_datetime(data["date"], format="%Y-%m-%d")
        return data