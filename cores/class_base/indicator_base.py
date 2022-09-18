import configargparse
from abc import ABC, abstractmethod


class Indicator_Base(ABC):
    arg_parser = configargparse.get_argument_parser()
    arg_parser.add('--high', help='this is a high column')
    arg_parser.add('--low', help='this is a low column')
    arg_parser.add('--close', help='this is  an Close Price Column')
    arg_parser.add('--open', help='this is  an Open Price Column')
    arg_parser.add('--date', help='this is a Date column')

    def __init__(self) -> None:
         self.args = self.arg_parser.parse_known_args()[0]
         self.parse_config()

    def parse_config(self):
        """
        Parsing of config.ini file
        """
        self.close = self.args.close
        self.open = self.args.open
        self.high = self.args.high
        self.low = self.args.low
        self.date = self.args.date

    @abstractmethod
    def calculate(self):
        pass