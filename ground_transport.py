from abc import ABC
from abc import abstractmethod

class GroundTransport(ABC):
    @abstractmethod
    def roll(self):
        pass
    
    @abstractmethod
    def fill(self):
        pass