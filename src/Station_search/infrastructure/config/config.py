import os
import dotenv
dotenv.load_dotenv()

print(os.environ.get('SEPARATOR'))
class AppConfig:
    GEODATA_BERLIN_PLZ = os.environ.get('GEODATA_BERLIN_PLZ')
    CHARGING_STATIONS = os.environ.get('CHARGING_STATIONS')
    NONE = os.environ.get('NONE')
    LOW_MEMORY = os.environ.get('MEMORY_LOW')
    SEPARATOR = os.environ.get('SEPARATOR')
    ENCODING = os.environ.get('ENCODING_')
    DICT= { 'PICKLEFOLDER': os.getenv('PICKLEFOLDER'),
            'GEOCODE': os.getenv('GEOCODE'),
            'FILE_LSTATIONS': os.getenv('FILE_LSTATIONS'),
            'FILE_RESIDENTS': os.getenv('FILE_RESIDENTS'),
            'FILE_GEODAT_PLZ': os.getenv('FILE_GEODAT_PLZ'),
            'FILE_GEODAT_DIS': os.getenv('FILE_GEODAT_DIS')
            }

config = AppConfig()