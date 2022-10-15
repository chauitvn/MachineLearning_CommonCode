from StockPrediction_backend.exploratory_data_analysis.arima_feature import ArimaCalc


class StockAnalysisProcessor:
    def __init__(self, data):
        self.DATA = data

    def run(self):
        analysis_obj = ArimaCalc(self.DATA)
        self.DATA = analysis_obj.run()
        return self.DATA