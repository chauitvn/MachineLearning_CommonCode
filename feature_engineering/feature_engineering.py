from extensions.technical_indicators.technical_indicators import TechnicalIndicators
from feature_engineering.feature_engineering_base import FeatureEngineeringBase


class FeatureEngineering(FeatureEngineeringBase):
    def __init__(self, data) -> None:
        self.DATA = data
        super().__init__()

    def calculate(self):
        # calculate feature indicators
        obj = TechnicalIndicators(self.DATA)
        self.DATA = obj.calculate()
        return self.DATA
        