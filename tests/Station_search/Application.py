import pytest
from unittest.mock import MagicMock
from src.Station_search.Application.ui import search_station, showing_list_of_found_stations


class TestApplicationLayer:
    def setup_method(self):
        self.mock_domain_service = MagicMock()   # creating a mock object and is used to simulate the behavior of the domain service in the application layer

    # Section 1: Happy Path - Tests the happy path where a valid postal code is provided.
    def test_search_station(self):
        self.mock_domain_service.finding_charging_station.return_value = ["Station1", "Station2"]
        stations = search_station("10999", self.mock_domain_service)
        assert stations == ["Station1", "Station2"]

    # Section 2: Edge Cases where the postal code is empty.
    def test_search_station_empty_postal_code(self):
        self.mock_domain_service.finding_charging_station.return_value = []
        stations = search_station("", self.mock_domain_service)
        assert stations == []

    # Section 3: Error Scenarios where the postal code is invalid.
    def test_search_station_invalid_postal_code(self):
        self.mock_domain_service.finding_charging_station.side_effect = ValueError("Invalid postal code")
        with pytest.raises(ValueError, match="Invalid postal code"):
            search_station("INVALID", self.mock_domain_service)

    # Section 4: Domain Rules, where the postal code doesn't correspond to any station and Ensures an empty list is returned.
    def test_search_station_non_existent_postal_code(self):
        self.mock_domain_service.finding_charging_station.return_value = []
        stations = search_station("00000", self.mock_domain_service)
        assert stations == []

    # Verifies that the formats and displays the list of stations correctly.
    def test_showing_list_of_founded_stations(self):
        output = showing_list_of_founded_stations(["Station1", "Station2"])
        assert "Station1" in output
        assert "Station2" in output
