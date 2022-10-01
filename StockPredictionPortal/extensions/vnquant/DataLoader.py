import logging as logging
import requests
import pandas as pd
from extensions.vnquant.DataLoaderCAFE import DataLoaderCAFE
from extensions.vnquant.DataLoaderFialda import DataLoaderFialda
from extensions.vnquant.DataLoaderVND import DataLoaderVND
#from requests.packages.urllib3.exceptions import InsecureRequestWarning
#requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


class DataLoader:
    def __init__(self, symbols, start, end, data_source='CAFE', minimal=True, *arg, **karg):
        self.symbols = symbols
        self.start = start
        self.end = end
        self.data_source = data_source
        self.minimal = minimal

    def download(self):
        if str.lower(self.data_source) == 'vnd':
            # raise "Data source VND does not remain support, kindly change data_source='cafe'"
            loader = DataLoaderVND(self.symbols, self.start, self.end)
            stock_data = loader.download()
            # logging.info('Data Symbols: {}, start: {}, end: {}'.format(stock_data, start, end))
            # logging.info('Data VND: {}'.format(stock_data))
        elif str.lower(self.data_source) == 'cafef':
            loader = DataLoaderCAFE(self.symbols, self.start, self.end)
            stock_data = loader.download()
            # logging.info('Data CAFE: {}'.format(stock_data))
        else:
            loader = DataLoaderFialda(self.symbols, self.start, self.end)
            stock_data = loader.download_one_new()
            stock_data.rename(columns={"adjClose": "adjust", "totalVolume": "volume", "tradingTime": "date"},
                              inplace=True)
            stock_data["date"] = pd.to_datetime(stock_data["date"], format='%Y-%m-%d')
            stock_data.set_index("date", inplace=True)

        if self.minimal:
            # logging.info(stock_data)
            if str.lower(self.data_source) == 'vnd':
                try:
                    data = stock_data[['high', 'low', 'open', 'close', 'adjust', 'volume']]
                except ValueError:
                    data = stock_data[['high', 'low', 'open', 'close', 'adjust', 'volume']]
                return data
            else:
                data = stock_data[['high', 'low', 'open', 'close', 'adjust', 'volume']]
                return data
        else:
            return stock_data
