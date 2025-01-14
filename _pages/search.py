import streamlit as st
from src.Station_search.Application.services.SearchStationsServices import SearchService


import streamlit as st
import folium
from streamlit_folium import folium_static
from branca.colormap import LinearColormap
from src.Shared.Application.services.GeoPreprocessor import GeoApplicationService
from folium.plugins import MarkerCluster

def display_stations(searched_stations):
    obj = GeoApplicationService()
    dframe1 = obj.get_stations_counts_per_postalcode()  # Build the heatmap based on number of stations in each PLZ
    dframe3 = searched_stations # get stations processed data only to show on map

    # Create a Folium map
    m = folium.Map(location=[52.52, 13.40], zoom_start=12)

    # Color map for the data
    color_map = LinearColormap(colors=['yellow', 'red'], vmin=dframe1['Number'].min(), vmax=dframe1['Number'].max())

    # Add GeoJson features
    for idx, row in dframe1.iterrows():
        folium.GeoJson(
            row['geometry'],
            style_function=lambda x, color=color_map(row['Number']): {
                'fillColor': color,
                'color': 'black',
                'weight': 1,
                'fillOpacity': 0.7
            },
            tooltip=f"PLZ: {row['PLZ']}, Number: {row['Number']}"
        ).add_to(m)

    # Add the color map to the map
    color_map.add_to(m)
    marker_cluster = MarkerCluster().add_to(m)
    # Add stations to the map with KW-based symbolization
    dframe3['KW'] = dframe3['KW'].str.replace(',', '')  # Remove any commas if present (some might have commas)
    dframe3['KW'] = dframe3['KW'].astype(float)  # Convert to float
    for _, row in dframe3.iterrows():
        # Using KW to determine size and color

        kw = row['KW']
        color = "green" if kw > 100 else "blue"  # Color based on KW
        radius = kw / 100  # Scale the size of the marker

        popup_content = f"""
           <b>PLZ:</b> {row['PLZ']}<br>
           <b>Bundesland:</b> {row['Bundesland']}<br>
           <b>KW:</b> {kw} kW<br>
           """

        # Add a circle marker with detailed popup
        # folium.CircleMarker(
        #     location=[row['Breitengrad'], row['Längengrad']],
        #     radius=radius,
        #     color=color,
        #     fill=True,
        #     fill_color=color,
        #     fill_opacity=0.6,
        #     popup=folium.Popup(popup_content, max_width=300),  # Added max_width for better visibility
        #     tooltip=f"PLZ: {row['PLZ']}, KW: {kw} kW"
        # ).add_to(m)
        folium.Marker(
            location=[row['Breitengrad'], row['Längengrad']],
            icon=folium.Icon(icon="bolt", prefix="fa", color="blue"),  # Use "bolt" icon for charging
            popup=folium.Popup(popup_content, max_width=300),  # Added max_width for better visibility
            tooltip=f"PLZ: {row['PLZ']}, KW: {kw} kW"
        ).add_to(marker_cluster)
    # Display the map
    folium_static(m, width=1000, height=600)


def display_search():


    postal_code = st.text_input("Enter Postal Code (PLZ)", "")
    search_button = st.button("Search")
    if search_button:
        search_service = SearchService(float(postal_code))  # Create new instance for each search
        result = search_service.get_stations()
        if isinstance(result, str):
            st.error(result)
        else:
            display_stations(result)




