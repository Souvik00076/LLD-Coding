from dataclasses import dataclass
from .PricingStrategy import PricingStrategy


@dataclass
class CyclePricingStrategy(PricingStrategy):
    price: float = 5.0

    def calculatePrice(self, hours: float) -> float:
        return self.price * hours
