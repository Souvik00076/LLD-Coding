from ParkingLot.core.ParkingSpot import ParkingSpot
from ParkingLot.core.ParkingSpotManager import ParkingSpotManager
from ParkingLot.core.ParkingLotFacade import ParkingLotFacade
from ParkingLot.core.Vehicle import Vehicle
from ParkingLot.core.CarPricingStrategy import CarPricingStrategy
from ParkingLot.core.BikePricingStrategy import BikePricingStrategy
from ParkingLot.core.CyclePricingStrategy import CyclePricingStrategy
from ParkingLot.core.PricingStrategyRegistry import PricingStrategyRegistry
from ParkingLot.enums.VehicleSize import VehicleSize


def main():
    # register pricing strategies
    PricingStrategyRegistry.register(VehicleSize.CAR, CarPricingStrategy())
    PricingStrategyRegistry.register(VehicleSize.BIKE, BikePricingStrategy())
    PricingStrategyRegistry.register(VehicleSize.CYCLE, CyclePricingStrategy())

    # setup parking spots
    manager = ParkingSpotManager()
    manager.addParkingSpot(ParkingSpot(VehicleSize.CAR))
    manager.addParkingSpot(ParkingSpot(VehicleSize.CAR))
    manager.addParkingSpot(ParkingSpot(VehicleSize.BIKE))
    manager.addParkingSpot(ParkingSpot(VehicleSize.CYCLE))

    facade = ParkingLotFacade(manager)

    # park vehicles
    car = Vehicle("KA-01-1234", VehicleSize.CAR)
    bike = Vehicle("KA-02-5678", VehicleSize.BIKE)

    carTicket = facade.parkVehicle(car)
    bikeTicket = facade.parkVehicle(bike)

    print(f"Car parked. Ticket: {carTicket.getTicketNumber()}")
    print(f"Bike parked. Ticket: {bikeTicket.getTicketNumber()}")

    # checkout
    price = facade.checkoutTicket(carTicket.getTicketNumber())
    print(f"Car checkout price: {price}")


if __name__ == "__main__":
    main()
