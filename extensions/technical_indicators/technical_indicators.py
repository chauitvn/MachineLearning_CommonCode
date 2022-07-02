from extensions.technical_indicators.ai_indicators.neural_prophet import NeuralFbProphet
from extensions.technical_indicators.indicator_base import Indicator_Base


class TechnicalIndicators(Indicator_Base):
    def __init__(self, data) -> None:
        self.DATA = data
        super().__init__()


    def calculate(self):
        neural_prophet = NeuralFbProphet(self.DATA)
        self.DATA = neural_prophet.calculate()