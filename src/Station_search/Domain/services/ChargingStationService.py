from src.Station_search.Domain.entities.entities import Postalcode
import pandas as pd
class ChargingStationService:
    """
    This service is responsible for managing and retrieving charging stations data.
    """
    def __init__(self,postal_code : Postalcode,stations : pd.DataFrame):
        self.plz = postal_code.plz
        self.stations_df = stations

    def find_by_post_code(self):
        # Raise exception if the input DataFrame is empty
        if self.stations_df.empty:
            raise ValueError("The input DataFrame is empty.")

            # Raise exception if the postal code length is not 5
        if len(str(int(self.plz))) != 5:
            raise ValueError(f"Invalid postal code: {self.plz}. Postal code must have 5 digits.")

        if self.plz in self.stations_df["PLZ"].values:
            self.stations_df = self.stations_df[self.stations_df["PLZ"] == self.plz]
        else:
            self.stations_df = pd.DataFrame()  # Set to empty DataFrame if no match