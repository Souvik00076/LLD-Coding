from . import ParkingSpot, Vehicle
from typing import List, Optional


class ParkingSpotManager:
    __instance: Optional['ParkingSpotManager'] = None

    def __new__(cls) -> 'ParkingSpotManager':
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__spots = list()
        return cls.__instance

    def __init__(self):
        pass

    def addParkingSpot(self, spot: ParkingSpot):
        self.__spots.append(spot)

    def parkVehicle(self, vehicle: Vehicle) -> Optional[ParkingSpot]:
        parkedSpot: Optional[ParkingSpot] = None
        for spot in self.__spots:
            if spot.getSpotType() == vehicle.vehicleType and spot.getAvailable():
                parkedSpot = spot
                break

        if not parkedSpot:
            return None

        parkedSpot.setVehicle(vehicle)
        return parkedSpot

    def unparkVehicle(self, spot):
        spot.unpark()
