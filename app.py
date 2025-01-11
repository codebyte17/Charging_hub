
from src.Shared.Application.services.GeoPreprocessor import  GeoApplicationService


obj =   GeoApplicationService()


# Load Geographical Data
print(obj.get_geo_processed_data().head())

