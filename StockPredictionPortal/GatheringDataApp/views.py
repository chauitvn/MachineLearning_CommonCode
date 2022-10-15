import os
import datetime
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from plotly.offline import plot
from django.shortcuts import render
from django.http import JsonResponse
from neuralprophet import NeuralProphet
from cores.data_processor import DataProcessor
from django.views.generic import TemplateView, View, DeleteView
from extensions.technical_indicators.ai_indicators.neural_prophet import NeuralFbProphet


# Create your views here.
def index(request):
    return render(request, 'gathering_data_index.html')

# Crawling Data
class CrawlingHistoryData(View):
    def  get(self, request):
        symbol = request.GET.get('stockName', None)
        start_date = "2000-01-01"
        today = datetime.date.today().strftime("%Y-%m-%d")
        dpObj = DataProcessor(symbol, "vnd", start_date, today)

        is_plot = True
        self.DATA = dpObj.run(is_plot)

        date = datetime.date.today().strftime("%Y-%m-%d")
        directory = f"D:\OutsourceViet//SourceCode//MachineLearning_CommonCode//datasets//{date}"
        if not os.path.isdir(directory):
            os.mkdir(directory)

        self.DATA.to_csv(f"{directory}//{symbol}.csv")
        
        self.open ="open"
        self.high = "high"
        self.low = "low"
        self.close ="close"

        #Plot Stock Historical Data
        sampleData = self.DATA.tail(100)
        
        date = sampleData.index
        fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
               vertical_spacing=0.03, subplot_titles=('OHLC', 'Volume'), 
               row_width=[0.2, 0.7])

        fig.add_trace(go.Candlestick(x=date,
                open=sampleData[self.open],
                high=sampleData[self.high],
                low=sampleData[self.low],
                close=sampleData[self.close],),row=1, col=1)
        # Bar trace for volumes on 2nd row without legend
        fig.add_trace(go.Bar(x=date, y= sampleData['volume'] , showlegend=False), row=2, col=1)

        fig.update_layout(
            title='The Smoothed Heiki Ashi',
            yaxis_title='{} Stock'.format(symbol), 
            xaxis_rangeslider_visible= False
        )

        plot_div = plot(fig,output_type='div')

        data = {
            'fig': plot_div
        }
        return JsonResponse(data)

#Analysis Data
class StockAnalysis(View):
    def get(self, request):
        analysis_model = request.GET.get('analysis_model', None)

        date = datetime.date.today().strftime("%Y-%m-%d")
        DATA = pd.read_csv(f"D:\OutsourceViet//SourceCode//MachineLearning_CommonCode//datasets//{date}//FUEVFVND.csv")

        close ="close"
        date = "date"

        result = None

        # Get Data Source
        if analysis_model =="on":
            new_df = DATA[[date, close]]
            new_df = new_df.rename(columns={date: 'ds', close: 'y'})
            # fit the model
            model = NeuralProphet()
            model.fit(new_df, freq='D')
            future = model.make_future_dataframe(new_df, periods=20, n_historic_predictions=len(new_df))
            forecast_df = model.predict(future)
            forecast_df.set_index("ds", inplace=True)
            result = forecast_df.tail(200)

        fig = go.Figure()
        fig.add_trace(go.Scatter(x =result.index, y= result['y'],  mode='lines', name="price", line=dict(color='blue', width=2)))
        fig.add_trace(go.Scatter(x=result.index, y=result['yhat1'].values,  mode='lines', name="pridiction price", line=dict(color='red', width=2)))

        plot_div = plot(fig,output_type='div')

        data_return = {
            'fig': plot_div
        }
        return JsonResponse(data_return)