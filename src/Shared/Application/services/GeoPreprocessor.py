from src.Shared.infrastructure.data_loader.csv_loader import DataRepository
from src.Shared.Domain.services.GeoServices import GeoDataProcessor
from src.Shared.infrastructure.config.config import config

class GeoApplicationService:

    """
        This service is responsible for handling geospatial and stations data operations.
    """

    def __init__(self):
        self.csv_data = DataRepository()
        self.geo_processor = GeoDataProcessor()

    def get_stations_processed_data(self):
        # Geospatial data processing
        df_stations = self.geo_processor.preprocess_lstat_data(self.csv_data.stations_data_loader().df,self.csv_data.geo_data_loader().df)
        return df_stations

    def get_stations_counts_per_postalcode(self):
        # Sorting by postal codeCounting charging station occurrences per postal code
        stations_count_df = self.geo_processor.count_plz_occurrences(self.get_stations_processed_data())
        return stations_count_df




