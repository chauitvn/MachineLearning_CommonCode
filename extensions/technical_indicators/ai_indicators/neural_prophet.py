import pandas as pd
from neuralprophet import NeuralProphet
from extensions.technical_indicators.indicator_base import Indicator_Base


class NeuralFbProphet(Indicator_Base):
    def __init__(self, data) -> None:
        self.DATA = data
        super().__init__()

    def calculate(self):
        new_df = self.DATA[[self.close]]
        new_df.reset_index(drop=False, inplace=True)
        new_df = new_df.rename(columns={self.date: 'ds', self.close: 'y'})
        # fit the model
        model = NeuralProphet()
        model.fit(new_df, freq='D')
        # Using the model to make a forecast
        future = model.make_future_dataframe(new_df, periods=7, n_historic_predictions=len(new_df))
        forecast_df = model.predict(future)
        # renaming column names to understand easily
        forecast_df.rename(
            columns={"yhat1": "neural_prophet_prediction", "trend": "neural_prophet_trend"}, inplace=True)
        drop_columns = ['residual1', 'season_yearly', 'season_weekly', "y"]
        forecast_df.drop(drop_columns, axis=1, inplace=True)
        forecast_df.set_index("ds", inplace=True)
        new_data = pd.merge(self.DATA, forecast_df, left_index=True, right_index=True, how="left")
        return new_data