import datetime
import plotly.graph_objects as go
from plotly.offline import plot
from django.shortcuts import render
from django.http import JsonResponse
from cores.data_processor import DataProcessor
from django.views.generic import TemplateView, View, DeleteView


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
        self.DATA = dpObj.run()
        
        self.open ="open"
        self.high = "high"
        self.low = "low"
        self.close ="close"

        #Plot Stock Historical Data
        sampleData = self.DATA.tail(200)
        
        date = sampleData.index
        fig = go.Figure(data=[go.Candlestick(x=date,
                open=sampleData[self.open],
                high=sampleData[self.high],
                low=sampleData[self.low],
                close=sampleData[self.close],)])
        fig.update_layout(
            title='The Smoothed Heiki Ashi',
            yaxis_title='{} Stock'.format(symbol)
        )

        plot_div = plot(fig,output_type='div')

        data = {
            'fig': plot_div
        }
        return JsonResponse(data)