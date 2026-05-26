from typing import Optional
from ..enums import VehicleSize
from .Vehicle import Vehicle


class ParkingSpot:
    def __init__(self, spotType: VehicleSize) -> None:
        self.__spotType = spotType
        self.__isAvailable = True
        self.__vehicle: Optional[Vehicle] = None

    def setVehicle(self, vehicle: Vehicle) -> None:
        self.__vehicle = vehicle
        self.__isAvailable = False

    def getSpotType(self):
        return self.__spotType

    def getAvailable(self) -> bool:
        return self.__isAvailable

    def unpark(self) -> None:
        self.__vehicle = None
        self.__isAvailable = True
