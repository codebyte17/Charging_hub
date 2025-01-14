from src.Station_search.infrastructure.config.config import config
import pandas as pd
import os
class StationRepository:
    """
    This class is responsible for managing and storing the charging stations data.
    """
    def __init__(self,file_name=config.CHARGING_STATIONS,sep=config.SEPARATOR,encoding=config.ENCODING,low_memory=config.LOW_MEMORY):
        self.file_name = file_name
        self.sep = sep
        self.encoding = encoding
        self.low_memory = low_memory


    def load_stations(self,required_columns=None):
        # Check if the file has a .csv extension
        if not self.file_name.endswith('.csv'):
            raise ValueError("The provided file is not a CSV file.")

        if not os.path.exists(self.file_name):
            raise FileNotFoundError(f"The file at {self.file_name} does not exist.")

        # Load the charging station data
        df = pd.read_csv(self.file_name, sep=self.sep, encoding=self.encoding, low_memory=self.low_memory)
        if required_columns:
            missing_columns = [col for col in required_columns if col not in df.columns]
            if missing_columns:
                raise ValueError(f"Missing required columns: {', '.join(missing_columns)}")

        return df


