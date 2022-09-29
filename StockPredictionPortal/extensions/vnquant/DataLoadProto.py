import extensions.vnquant.utils as utils


class DataLoadProto:
    def __init__(self, symbols, start, end, *arg, **karg):
        self.symbols = symbols
        self.start = utils.convert_text_dateformat(start, new_type='%d/%m/%Y')
        self.end = utils.convert_text_dateformat(end, new_type='%d/%m/%Y')
