import pytest
from src.Station_search.infrastructure.repository import find_by_postalcode


class TestInfrastructureLayer:
    def setup_method(self):
        self.repository = find_by_postalcode()

    # Section 1: Happy Path, where a valid postal code is provided.
    def test_find_by_postalcode(self):
        stations = self.repository("10999")
        assert len(stations) > 0
        assert all(s.postal_code == "10999" for s in stations)

    # Section 2: Edge Cases, where the postal code is empty.
    def test_find_by_postalcode_empty_postal_code(self):
        stations = self.repository("")
        assert stations == []

    # Section 3: Error Scenarios. Tests the error scenario where the postal code format is invalid.
    def test_find_by_postalcode_invalid_postal_code(self):
        with pytest.raises(ValueError, match="Invalid postal code"):
            self.repository("INVALID")

    # Section 4: Domain Rules. where the postal code doesn't match any stations in the database.
    def test_find_by_postalcode_non_existent_postal_code(self):
        stations = self.repository("00000")
        assert len(stations) == 0
