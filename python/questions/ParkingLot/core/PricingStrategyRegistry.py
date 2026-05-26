from typing import Dict
from ..enums import VehicleSize
from .PricingStrategy import PricingStrategy


class PricingStrategyRegistry:
    __registry: Dict[VehicleSize, PricingStrategy] = {}

    @classmethod
    def register(cls, vehicleType: VehicleSize, strategy: PricingStrategy) -> None:
        cls.__registry[vehicleType] = strategy

    @classmethod
    def get(cls, vehicleType: VehicleSize) -> PricingStrategy:
        strategy = cls.__registry.get(vehicleType)
        if strategy is None:
            raise ValueError(f"No pricing strategy registered for {vehicleType}")
        return strategy
