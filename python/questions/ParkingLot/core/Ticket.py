from datetime import date
from typing import Optional
from .Vehicle import Vehicle
from .ParkingSpot import ParkingSpot


class Ticket:
    __counter: int = 0

    def __init__(self, vehicle: Vehicle, spot: ParkingSpot, createdDate: date) -> None:
        Ticket.__counter += 1
        self.__ticketNumber: str = str(Ticket.__counter)
        self.__vehicle = vehicle
        self.__spot = spot
        self.__createdDate = createdDate
        self.__checkOutDate: Optional[date] = None

    def getTicketNumber(self) -> str:
        return self.__ticketNumber

    def getVehicle(self) -> Vehicle:
        return self.__vehicle

    def getSpot(self) -> ParkingSpot:
        return self.__spot

    def getCreatedDate(self) -> date:
        return self.__createdDate

    def setCheckOutDate(self, checkOutDate: date) -> None:
        self.__checkOutDate = checkOutDate
