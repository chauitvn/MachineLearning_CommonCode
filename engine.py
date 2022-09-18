import pandas as pd
from datetime import date
from cores.data_processor import DataProcessor
from cores.class_base.engine_base import EngineBase
from cores.feature_engineering_processor import FeatureEngineeringProcessor
from cores.stock_analysis_processor import StockAnalysisProcessor


class Engine(EngineBase):
    def __init__(self):
        super().__init__()

    def run(self):
        print("Running")
        self.garthering_data()
        #self.feature_engineering()
        #self.exploratory_data_analysis()
        #self.feature_selection()
        #self.cross_validation()
        #self.training_valuation_model()
        #self.hyper_parameter_tuning()
        #self.deploying_monitoring_maintaining()
        #self.retraining_redeploying()

    def garthering_data(self):
        print("Start to run garthing data....")
        symbol = self.stock_symbol

        if(self.source_data =='csv'):
            self.DATA = pd.read_csv('datasets\{0}.csv'.format(symbol), parse_dates = ['date'], index_col = ['date'])
        else:
            # Initial input data
            start_date = "2000-01-01"
            today = date.today().strftime("%Y-%m-%d")
        
            dpObj = DataProcessor(start_date, today)
            self.DATA = dpObj.run()
            # to check whether do we need to export stock data to local or not.
            if(self.isExportHisData):
                self.DATA.to_csv('datasets\{0}.csv'.format(symbol))
        print("End to run garthing data....")

    def feature_engineering(self):
        print("Start to run feature engineering....")
        featureObj = FeatureEngineeringProcessor(self.DATA)
        self.DATA = featureObj.run()
        print("End to run feature engineering....")

    def exploratory_data_analysis(self):
        print("Start to run exploratory data analysis....")
        analysisObj = StockAnalysisProcessor(self.DATA)
        self.DATA = analysisObj.run()
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