from src.Station_search.Domain.repositories.ChargingStationRepository import ChargingStationRepository
from src.Station_search.Domain.entities.entities import Postalcode
from src.Shared.Application.services.GeoPreprocessor import GeoApplicationService

class ChargingRepository(ChargingStationRepository):
    """
    This class is responsible for handling the database operations related to finding charging stations.
    """
    def __init__(self):
        self.processed_stations_data = GeoApplicationService()
        self.dataframe = None

    def load_charging_data(self,required_columns=None):
        # Load the data related to stations from the Shared module ):-
        self.dataframe = self.processed_stations_data.get_stations_processed_data()