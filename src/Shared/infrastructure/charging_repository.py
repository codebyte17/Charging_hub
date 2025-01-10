# Infrastructure Layer: StationRepository
class StationRepository:
    def __init__(self, csv_path):
        self.csv_path = csv_path

    def get_all(self):
        data = pd.read_csv(self.csv_path)
        return [Station(row['id'], row['name'], row['latitude'], row['longitude'], row['other_info']) for _, row in data.iterrows()]
