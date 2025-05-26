from abc import ABC, abstractmethod
import logging

logging.basicConfig(
    format="%(asctime)s %(levelname)s %(message)s",
    level=logging.INFO,
    handlers=[logging.StreamHandler()],
)


# Створення абстрактного класу Vehicle
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self) -> None:
        pass


class Car(Vehicle):
    def __init__(self, make: str, model: str, spec_region: str) -> None:
        self.make = make
        self.model = model
        self.spec_region = spec_region

    def start_engine(self) -> None:
        logging.info(
            "%s %s (%s Spec): Двигун запущено", self.make, self.model, self.spec_region
        )


class Motorcycle(Vehicle):
    def __init__(self, make: str, model: str, spec_region: str) -> None:
        self.make = make
        self.model = model
        self.spec_region = spec_region

    def start_engine(self) -> None:
        logging.info(
            "%s %s (%s Spec): Мотор заведено", self.make, self.model, self.spec_region
        )


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make, model) -> Car:
        pass

    @abstractmethod
    def create_motorcycle(self, make, model) -> Motorcycle:
        pass


class USVehicleFactory(VehicleFactory):
    def __init__(self):
        self.spec_region = "US"

    def create_car(self, make, model) -> Car:
        return Car(make, model, self.spec_region)

    def create_motorcycle(self, make, model) -> Motorcycle:
        return Motorcycle(make, model, self.spec_region)


class EUVehicleFactory(VehicleFactory):
    def __init__(self):
        self.spec_region = "EU"

    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, self.spec_region)

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, self.spec_region)


# Використання
us_factory = USVehicleFactory()

eu_factory = EUVehicleFactory()

vehicle1 = us_factory.create_car("Toyota", "Corolla")
vehicle1.start_engine()

vehicle2 = eu_factory.create_motorcycle("Harley-Davidson", "Sportster")
vehicle2.start_engine()
