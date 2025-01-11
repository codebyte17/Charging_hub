
import geopandas as gpd
from src.Shared.infrastructure.config.config import  config

class GeoDataProcessor:
    """Handles geospatial data operations."""

    @staticmethod
    def sort_by_plz_add_geometry(dfr, dfg):
        dframe = dfr.copy()
        df_geo = dfg.copy()

        sorted_df = dframe.sort_values(by=config.DICT["GEOCODE"]).reset_index(drop=True).sort_index()
        sorted_df2 = sorted_df.merge(df_geo, on=config.DICT["GEOCODE"], how='left')
        sorted_df3 = sorted_df2.dropna(subset=['geometry'])

        sorted_df3['geometry'] = gpd.GeoSeries.from_wkt(sorted_df3['geometry'])
        return gpd.GeoDataFrame(sorted_df3, geometry='geometry')

    @staticmethod
    def preprocess_lstat_data(dfr, dfg):

        dframe = dfr.copy()
        df_geo = dfg.copy()
        print(dframe.head())
        dframe2 = dframe.loc[:,
                  ['Postleitzahl', 'Bundesland', 'Breitengrad', 'Längengrad', 'Nennleistung Ladeeinrichtung [kW]']]
        dframe2.rename(columns={"Nennleistung Ladeeinrichtung [kW]": "KW", "Postleitzahl": "PLZ"}, inplace=True)

        # Clean and format latitude and longitude
        dframe2['Breitengrad'] = dframe2['Breitengrad'].str.replace(',', '.')
        dframe2['Längengrad'] = dframe2['Längengrad'].str.replace(',', '.')

        # Filter for Berlin postal codes
        dframe3 = dframe2[(dframe2["Bundesland"] == 'Berlin') & (dframe2["PLZ"] > 10115) & (dframe2["PLZ"] < 14200)]

        return GeoDataProcessor.sort_by_plz_add_geometry(dframe3, df_geo)

    @staticmethod
    def count_plz_occurrences(df_lstat):
        """Counts occurrences of charging stations per postal code."""
        return df_lstat.groupby('PLZ').agg(
            Number=('PLZ', 'count'),
            geometry=('geometry', 'first')
        ).reset_index()
