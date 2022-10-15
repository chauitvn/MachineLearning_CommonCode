import pandas as pd
from darts import TimeSeries
from darts.datasets import AirPassengersDataset


series = AirPassengersDataset().load()
series.plot()