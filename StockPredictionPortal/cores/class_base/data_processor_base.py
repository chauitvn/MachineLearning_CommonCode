import configargparse
from abc import ABC, abstractmethod

class DataProcessorBase(ABC):
    #arg_parser = configargparse.get_argument_parser()
    #arg_parser.add('--sha', help='using the Smoothing Heikin Ashi (1) or the Heikin Ashi (0)')
    #arg_parser.add('--data_source', help='the key value is csv. it means that source data comes from the csv file.')
    #arg_parser.add('--stock_symbol', help='this is the stock symbol which needs to get historical data.')

    def __init__(self) -> None:
         #self.args = self.arg_parser.parse_known_args()[0]
         #self.parse_config()
         pass

    def parse_config(self):
        """
        Parsing of config.ini file
        """
        self.data_source = self.args.data_source
        self.stock_symbol = self.args.stock_symbol

    @abstractmethod
    def get_raw_data(self):
        pass