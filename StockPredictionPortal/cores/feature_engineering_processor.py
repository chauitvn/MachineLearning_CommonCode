from feature_engineering.feature_engineering import FeatureEngineering


class FeatureEngineeringProcessor():
    def __init__(self, data):
        self.DATA = data

    def run(self):
        featurekObj = FeatureEngineering(self.DATA)
        self.DATA = featurekObj.calculate()
        return self.DATA