import pandas as pd
from scipy.fft import rfft, rfftfreq, irfft
from extensions.technical_indicators.indicator_base import Indicator_Base


class FourierTransform(Indicator_Base):
    def __init__(self, data) -> None:
        self.DATA = data
        super().__init__()
    
    def calculate(self):
        orginal_df = self.DATA[[self.close]]
        trend_df = rfft(orginal_df[self.close].values)
        trend_df[39:-39] = 0
        merge_df = pd.DataFrame(irfft(trend_df), columns=["Fourier"])

        # merger Fourier data into parent data
        orginal_df.reset_index(drop=False, inplace=True)
        orginal_df = pd.concat([orginal_df, merge_df], axis=1)
        # to make sure the index of two data frame is the same type.
        orginal_df.set_index("date", inplace=True)

        self.DATA["Fourier"] = orginal_df["Fourier"]
        return self.DATA