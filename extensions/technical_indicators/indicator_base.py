from abc import ABC, abstractmethod


class Indicator_Base(ABC):
    def __init__(self) -> None:
         self.args = self.arg_parser.parse_known_args()[0]
         self.parse_config()

    def parse_config(self):
        """
        Parsing of config.ini file
        """
        self.adj_close = self.args.adj_close
        self.high = self.args.high
        self.low = self.args.low
        self.date = self.args.date

    @abstractmethod
    def calculate(self):
        pass