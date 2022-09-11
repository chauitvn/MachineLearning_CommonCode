import configargparse
from abc import ABC, abstractmethod


class EngineBase(ABC):
    arg_parser = configargparse.get_argument_parser()
    arg_parser.add('--isExportHisData', help='the key is True. it means to allow exporting data to the csv file')
    arg_parser.add('--source_data', help='the key value is csv. it means that source data comes from the csv file.')
    arg_parser.add('--stock_symbol', help='this is the stock symbol which needs to get historical data.')

    def __init__(self) -> None:
         self.args = self.arg_parser.parse_known_args()[0]
         self.parse_config()

    def parse_config(self):
        """
        Parsing of config.ini file
        """
        self.isExportHisData = self.args.isExportHisData
        self.source_data = self.args.source_data
        self.stock_symbol = self.args.stock_symbol

    @abstractmethod
    def run(self):
        pass