import pytest
import pandas as pd
from src.Station_search.Domain.services.ChargingStationService import ChargingStationService

class Postalcode:
    def __init__(self, plz):
        self.plz = plz


class TestChargingStationService:
    @classmethod
    def setup_class(cls):
        """
        Set up the shared mock DataFrame used for all test cases.
        """
        cls.mock_stations_data = {
            "PLZ": [12345.0, 67890.0, 54321.0, 98765.0],
            "StationName": ["Station A", "Station B", "Station C", "Station D"],
            "Capacity": [10, 15, 8, 12],
        }
        cls.mock_stations_df = pd.DataFrame(cls.mock_stations_data)

    def setup_method(self):
        """
        Prepare resources for each test case.
        """
        self.service = None

    def test_data_frame_is_not_empty(self):
        """
        Test that the input DataFrame is not empty.
        """
        postal_code = Postalcode(12345)
        self.service = ChargingStationService(postal_code, self.mock_stations_df)
        self.service.find_by_post_code()
        # Assert the input DataFrame is not empty
        assert not self.service.stations_df.empty, "Input DataFrame should not be empty."

    def test_data_frame_is_empty(self):
        """
        Test the behavior when the input DataFrame is empty.
        """
        empty_df = pd.DataFrame()
        postal_code = Postalcode(12345)
        self.service = ChargingStationService(postal_code, empty_df)
        with pytest.raises(ValueError) as excinfo:
            self.service.find_by_post_code()
        assert str(excinfo.value) == "The input DataFrame is empty."

    def test_postal_code_length_valid(self):
        """
        Test that the postal code has the required length.
        """
        postal_code = Postalcode(12345)
        self.service = ChargingStationService(postal_code, self.mock_stations_df)
        self.service.find_by_post_code()
        # Assert the postal code length is valid
        assert len(str(self.service.plz)) == 5, "Postal code should have a length of 5."

    def test_postal_code_length_invalid(self):
        """
        Test the behavior with an invalid postal code length.
        """
        postal_code = Postalcode(1234)  # Invalid 4-digit postal code
        self.service = ChargingStationService(postal_code, self.mock_stations_df)
        with pytest.raises(ValueError) as excinfo:
            self.service.find_by_post_code()
        assert str(excinfo.value) == "Invalid postal code: 1234. Postal code must have 5 digits."

    def test_find_by_post_code_match(self):
        """
        Test when the postal code matches an entry in the DataFrame.
        """
        postal_code = Postalcode(12345)
        self.service = ChargingStationService(postal_code, self.mock_stations_df)
        self.service.find_by_post_code()
        assert not self.service.stations_df.empty
        assert len(self.service.stations_df) == 1
        assert self.service.stations_df.iloc[0]["StationName"] == "Station A"

    def test_find_by_post_code_no_match(self):
        """
        Test when the postal code does not match any entry in the DataFrame.
        """
        postal_code = Postalcode(12343)
        self.service = ChargingStationService(postal_code, self.mock_stations_df)
        self.service.find_by_post_code()
        assert self.service.stations_df.empty