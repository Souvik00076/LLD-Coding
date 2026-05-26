
from dataclasses import dataclass
from ..enums import VehicleSize


@dataclass
class Vehicle:
    vehicleNumber: str
    vehicleType: VehicleSize
