from abc import ABC, abstractmethod

class DataProcessorBase(ABC):
    @abstractmethod
    def get_raw_data(self):
        pass