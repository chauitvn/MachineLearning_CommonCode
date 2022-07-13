from extensions.technical_indicators.ai_indicators.neural_prophet import NeuralFbProphet
from extensions.technical_indicators.commons.common_indicators import CommonIndicator
from extensions.technical_indicators.indicator_base import Indicator_Base


class TechnicalIndicators(Indicator_Base):
    def __init__(self, data) -> None:
        self.DATA = data
        super().__init__()


    def calculate(self):
        # calculate common indicators
        common_indicator = CommonIndicator(self.DATA)
        self.DATA = common_indicator.calculate()
        # FB Prophet indicator
        neural_prophet = NeuralFbProphet(self.DATA)
        self.DATA = neural_prophet.calculate()