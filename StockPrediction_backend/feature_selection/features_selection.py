import xgboost as xgb
from sklearn.model_selection import train_test_split
from feature_engineering.feature_engineering_base import FeatureEngineeringBase


class FeatureSelection():
    def __init__(self, data) -> None:
        self.DATA = data
        super().__init__()

    def split_data(self, data):
        new_data = data.copy()
        y = new_data[self.close]
        X = new_data.iloc[:,1:]
        return X, y

    def calculate(self):
        # split data into X and y
        X, y = self.split_data(self.DATA)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=12)
        regressor = xgb.XGBRegressor(gamma=0.0,n_estimators=200,base_score=0.7,colsample_bytree=1,learning_rate=0.05)
        xgbModel = regressor.fit(X_train,y_train, eval_set = [(X_train, y_train), (X_test, y_test)], verbose=False)
        # eval_result = regressor.evals_result()
        xgbModel.feature_importances_