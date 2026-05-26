from dataclasses import dataclass
from .PricingStrategy import PricingStrategy


@dataclass
class BikePricingStrategy(PricingStrategy):
    price: float = 10.0

    def calculatePrice(self, hours: float) -> float:
        return self.price * hours
