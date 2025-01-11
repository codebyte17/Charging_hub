
import streamlit as st
import folium
from streamlit_folium import folium_static
from branca.colormap import LinearColormap
from src.Shared.Application.services.GeoPreprocessor import GeoApplicationService
from folium.plugins import MarkerCluster

# def display_heatmap():
#     obj = GeoApplicationService()
#     dframe1 = obj.get_stations_count()
#
#     st.title('Heatmaps: Electric Charging Stations')
#
#     # Create a Folium map
#     m = folium.Map(location=[52.52, 13.40], zoom_start=10)
#
#     # Color map for the data
#     color_map = LinearColormap(colors=['yellow', 'red'], vmin=dframe1['Number'].min(), vmax=dframe1['Number'].max())
#
#     # Add GeoJson features
#     for idx, row in dframe1.iterrows():
#         folium.GeoJson(
#             row['geometry'],
#             style_function=lambda x, color=color_map(row['Number']): {
#                 'fillColor': color,
#                 'color': 'black',
#                 'weight': 1,
#                 'fillOpacity': 0.7
#             },
#             tooltip=f"PLZ: {row['PLZ']}, Number: {row['Number']}"
#         ).add_to(m)
#
#     # Add the color map to the map
#     color_map.add_to(m)
#
#     # Display the map
#     folium_static(m, width=800, height=500)


def display_stations():
    obj = GeoApplicationService()
    dframe1 = obj.get_stations_count()
    dframe3 = obj.get_geo_processed_data()


    # Create a Folium map
    m = folium.Map(location=[52.52, 13.40], zoom_start=10)

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
           <b>Details:</b> {row.get('Details', 'No additional details')}
           """

        # Add a circle marker with detailed popup
        folium.CircleMarker(
            location=[row['Breitengrad'], row['Längengrad']],
            radius=radius,
            color=color,
            fill=True,
            fill_color=color,
            fill_opacity=0.6,
            popup=folium.Popup(popup_content, max_width=300),  # Added max_width for better visibility
            tooltip=f"PLZ: {row['PLZ']}, KW: {kw} kW"
        ).add_to(m)
    # Display the map
    folium_static(m, width=1000, height=600)

display_stations()
