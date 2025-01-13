import pytest
from src.Station_search.Domain.services.charging_station_service import finding_charging_station


class TestDomainLayer:
    def setup_method(self):
        self.service = finding_charging_station()

    # Section 1: Happy Path - test where a valid postal code is used.
    def test_finding_charging_station(self):
        stations = self.service("10999")
        assert len(stations) > 0
        assert all(s.postal_code == "10999" for s in stations)

    # Section 2: Edge Cases, test where the postal code is empty.
    def test_finding_charging_station_empty_postal_code(self):
        stations = self.service("")
        assert len(stations) == 0

    # Section 3: Error Scenarios where the postal code is invalid.
    def test_finding_charging_station_invalid_postal_code(self):
        with pytest.raises(ValueError, match="Invalid postal code"):
            self.service("INVALID")

    # Section 4: Domain Rules, where the postal code doesn't map to any stations.
    def test_finding_charging_station_non_existent_postal_code(self):
        stations = self.service("00000")
        assert len(stations) == 0
