# Domain Layer: Repository Interface
from abc import ABC, abstractmethod
from domain import Station  # Importing the Station entity


class IStationRepository(ABC):
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, station_id):
        pass

    @abstractmethod
    def save(self, station):
        pass

    @abstractmethod
    def delete(self, station_id):
        pass
