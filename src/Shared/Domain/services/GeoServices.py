
import geopandas as gpd


class GeoDataProcessor:
    """Handles geospatial data operations."""

    @staticmethod
    def sort_by_plz_add_geometry(dfr, dfg, dict):
        dframe = dfr.copy()
        df_geo = dfg.copy()

        sorted_df = dframe.sort_values(by=dict.GEOCODE).reset_index(drop=True).sort_index()
        sorted_df2 = sorted_df.merge(df_geo, on=dict.GEOCODE, how='left')
        sorted_df3 = sorted_df2.dropna(subset=['geometry'])

        sorted_df3['geometry'] = gpd.GeoSeries.from_wkt(sorted_df3['geometry'])
        return gpd.GeoDataFrame(sorted_df3, geometry='geometry')

    @staticmethod
    def preprocess_lstat_data(dfr, dfg, dict):
        print(dfr.df.head())
        dframe = dfr.copy()
        df_geo = dfg.copy()

        dframe2 = dframe.loc[:,
                  ['Postleitzahl', 'Bundesland', 'Breitengrad', 'Längengrad', 'Nennleistung Ladeeinrichtung [kW]']]
        dframe2.rename(columns={"Nennleistung Ladeeinrichtung [kW]": "KW", "Postleitzahl": "PLZ"}, inplace=True)

        # Clean and format latitude and longitude
        dframe2['Breitengrad'] = dframe2['Breitengrad'].str.replace(',', '.').astype(float)
        dframe2['Längengrad'] = dframe2['Längengrad'].str.replace(',', '.').astype(float)

        # Filter for Berlin postal codes
        dframe3 = dframe2[(dframe2["Bundesland"] == 'Berlin') & (dframe2["PLZ"] > 10115) & (dframe2["PLZ"] < 14200)]

        return GeoDataProcessor.sort_by_plz_add_geometry(dframe3, df_geo, dict)

    @staticmethod
    def count_plz_occurrences(df_lstat):
        """Counts occurrences of charging stations per postal code."""
        return df_lstat.groupby('PLZ').agg(
            Number=('PLZ', 'count'),
            geometry=('geometry', 'first')
        ).reset_index()
