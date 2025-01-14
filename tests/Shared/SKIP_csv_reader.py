from src.Station_search.infrastructure.data_loader.csv_loader import StationRepository
from src.Station_search.infrastructure.config.config import config
import pytest


class TestCSVReader:
    def setup_method(self):
        """Setup reusable resources for tests."""
        # Create a temporary CSV file
        self.temp_file = "test_csv.csv"
        self.required_columns = [
            'Betreiber', 'Straße', 'Hausnummer', 'Adresszusatz', 'Postleitzahl',
            'Ort', 'Bundesland', 'Kreis/kreisfreie Stadt', 'Breitengrad',
            'Längengrad', 'Inbetriebnahmedatum',
            'Nennleistung Ladeeinrichtung [kW]', 'Art der Ladeeinrichung',
            'Anzahl Ladepunkte', 'Steckertypen1', 'P1 [kW]', 'Public Key1',
            'Steckertypen2', 'P2 [kW]', 'Public Key2', 'Steckertypen3', 'P3 [kW]',
            'Public Key3', 'Steckertypen4', 'P4 [kW]', 'Public Key4'
        ]
        # Initialize the CSVReader instance
        self.reader = StationRepository(self.temp_file, sep=";", encoding="utf-8", low_memory=False)


    def test_file_not_found(self):
        """Test if FileNotFoundError is raised for a missing file."""
        reader = StationRepository("nonexistent_file.csv")
        with pytest.raises(FileNotFoundError):
            reader.load_stations()

    def test_invalid_file_extension(self):
        """Test if ValueError is raised for a non-CSV file."""
        self.temp_file = "invalid_file.txt"
        reader = StationRepository(self.temp_file)
        with pytest.raises(ValueError):
            reader.load_stations()


    def test_missing_required_columns(self):

        # Define required columns
        self.temp_file = config.CHARGING_STATIONS
        self.required_columns = ["foo", "bar"]
        reader = StationRepository()
        with pytest.raises(ValueError, match="Missing required columns"):
            reader.load_stations(required_columns=self.required_columns)


    def test_all_required_columns_present(self):
        """Test if the function works correctly when all required columns are present."""

        self.temp_file = config.CHARGING_STATIONS
        reader = StationRepository(self.temp_file,sep=';',encoding='utf-8',low_memory=False)
        # No exception should be raised
        df = reader.load_stations(required_columns= self.required_columns)

        # Assert the dataframe is loaded correctly
        assert not df.empty
        assert list(df.columns) == self.required_columns