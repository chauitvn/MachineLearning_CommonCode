import requests
import pandas as pd
import extensions.vnquant.utils as utils

from extensions.vnquant.DataLoadProto import DataLoadProto


class DataLoaderFialda(DataLoadProto):
    def __init__(self, symbols, start, end, *arg, **karg):
        self.symbols = symbols
        self.start = start
        self.end = end
        super().__init__(symbols, start, end)

    def download_one_new(self):
        start_date = utils.convert_text_dateformat(self.start, origin_type='%d/%m/%Y', new_type='%Y-%m-%dT00:00:00.746')
        end_date = utils.convert_text_dateformat(self.end, origin_type='%d/%m/%Y', new_type='%Y-%m-%dT00:00:00.746')

        # to initialize the variables
        pageNumber = 1
        is_stop_flag = True
        result_df = pd.DataFrame()

        while is_stop_flag:
            API_FIALDA = f'https://fwtapi2.fialda.com/api/services/app/StockInfo/GetHistoricalData?symbol={self.symbols}&fromDate={start_date}&toDate={end_date}&pageNumber={pageNumber}&pageSize=50'
            res = requests.get(API_FIALDA)
            data = res.json()["result"]['items']
            if data:
                result_df = pd.concat([result_df, pd.DataFrame.from_dict(data)])
                pageNumber = pageNumber + 1
                is_stop_flag = True
            else:
                is_stop_flag = False
        result_df = result_df[::-1]
        return result_df
