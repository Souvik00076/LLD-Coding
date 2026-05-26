from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class PricingStrategy(ABC):
    price: float

    @abstractmethod
    def calculatePrice(self, hours: float) -> float:
        pass
