# Infrastructure Layer: StationRepository
from src.Shared.infrastructure.config.config import config
import pandas as pd
from src.Shared.Domain.entities.entities import GeoData, Station

class DataRepository:
    """
        Initialize data factory with required configuration parameters
        and initialize dataframes for geographical data and charging stations
        This class should be responsible for loading data from the provided sources.
    """

    def __init__(self) -> None:
        print(config.GEODATA_BERLIN_PLZ)
        self.geodata_berlin_plz = config.GEODATA_BERLIN_PLZ
        self.charging_stations  = config.CHARGING_STATIONS
        self.geodata_dataframe  = config.NONE
        self.stations_dataframe = config.NONE

    def geo_data_loader(self) -> GeoData:
        # Load geographical data for Berlin postal codes
        self.geodata_dataframe  = pd.read_csv(str(self.geodata_berlin_plz),sep=config.SEPARATOR,encoding=config.ENCODING)
        return GeoData(self.geodata_dataframe)


    def stations_data_loader(self) -> Station:
        # Load charging station data
        self.stations_dataframe = pd.read_csv(self.charging_stations,sep=config.SEPARATOR,encoding=config.ENCODING,low_memory=config.LOW_MEMORY)
        return Station(self.stations_dataframe)


