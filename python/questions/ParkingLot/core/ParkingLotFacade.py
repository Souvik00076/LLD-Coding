from . import ParkingSpotManager, PricingStrategy, Ticket, Vehicle, PricingStrategyRegistry
from datetime import date


class ParkingLotFacade:

    def __init__(self, manager: ParkingSpotManager):
        self.__manager: ParkingSpotManager = manager
        self.__tickets: dict[str, Ticket] = {}

    def parkVehicle(self, vehicle: Vehicle) -> Ticket:
        spot = self.__manager.parkVehicle(vehicle)
        if not spot:
            raise ValueError("No spot available")
        ticket: Ticket = Ticket(vehicle, spot, date.today())
        self.__tickets[ticket.getTicketNumber()] = ticket
        return ticket

    def checkoutTicket(self, ticketNumber: str):
        if ticketNumber not in self.__tickets:
            raise ValueError("Invalid ticket number")
        ticket: Ticket = self.__tickets.get(ticketNumber)
        vehicle: Vehicle = ticket.getVehicle()
        pricing: PricingStrategy = PricingStrategyRegistry.get(
            vehicle.vehicleType)
        hours: float = (date.today() - ticket.getCreatedDate()
                        ).total_seconds() / 3600
        price: float = pricing.calculatePrice(hours)
        ticket.setCheckOutDate(date.today())
        self.__manager.unparkVehicle(ticket.getSpot())
        return price
