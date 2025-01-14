from src.Station_search.Domain.services.ChargingStationService import ChargingStationService
from src.Station_search.infrastructure.ChargingStationRepository import  ChargingRepository
from src.Station_search.Domain.entities.entities import Postalcode
import pandas as pd


class SearchService:

    def __init__(self,plz):

        self.postal_code = Postalcode(plz)  # Intialization of postal code entity with plz (Postal code)
        self.station_repo = ChargingRepository()  # Intialization of ChargingStationRepository to get the station data
        self.station_repo.load_charging_data() # Load the station data
        self.charging_station_service = ChargingStationService(self.postal_code,self.station_repo.dataframe) # Get postal code stations


    def get_stations(self):
        self.charging_station_service.find_by_post_code()
        if self.charging_station_service.stations_df.empty:
            return "Stations for postal code {0} not found!".format(self.postal_code.plz)
        else:
            return self.charging_station_service.stations_df
