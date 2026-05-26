from dataclasses import dataclass
from .PricingStrategy import PricingStrategy


@dataclass
class CarPricingStrategy(PricingStrategy):
    price: float = 20.0

    def calculatePrice(self, hours: float) -> float:
        return self.price * hours
