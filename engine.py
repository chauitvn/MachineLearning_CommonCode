from datetime import date
from cores.data_processor import DataProcessor


class Engine:
    def __init__(self):
        pass

    def run(self):
        print("Running")
        self.garthering_data()
        self.feature_engineering()
        self.exploratory_data_analysis()
        self.feature_selection()
        self.cross_validation()
        self.training_valuation_model()
        self.hyper_parameter_tuning()
        self.deploying_monitoring_maintaining()
        self.retraining_redeploying()

    def garthering_data(self):
        print("Start to run garthing data....")
        # Initial input data
        data_source = "vnd"
        symbol = 'VPB'
        start_date = "2000-01-01"
        today = date.today().strftime("%Y-%m-%d")
        
        dpObj = DataProcessor(data_source, symbol, start_date, today)
        dpObj.run()
        print("End to run garthing data....")

    def feature_engineering(self):
        print("Start to run feature engineering....")
        print("End to run feature engineering....")

    def exploratory_data_analysis(self):
        print("Start to run exploratory data analysis....")
        print("End to run exploratory data analysis....")

    def feature_selection(self):
        print("Start to run feature selection....")
        print("End to run feature selection....")

    def cross_validation(self):
        print("Start to run cross validation....")
        print("End to run cross validation....")

    def training_valuation_model(self):
        print("Start to run training valuation model....")
        print("End to run training valuation model....")

    def hyper_parameter_tuning(self):
        print("Start to run hyper parameter tuning....")
        print("End to run hyper parameter tuning....")

    def deploying_monitoring_maintaining(self):
        print("Start to run deploying monitoring maintaining....")
        print("End to run deploying monitoring maintaining....")

    def retraining_redeploying(self):
        print("Start to run retraining redeploying....")
        print("End to run retraining redeploying....")