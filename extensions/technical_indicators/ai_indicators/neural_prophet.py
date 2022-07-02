from extensions.technical_indicators.indicator_base import Indicator_Base


class NeuralProphet(Indicator_Base):
    def __init__(self, data) -> None:
        self.data = data
        super().__init__()

    def calculate(self):
        pass