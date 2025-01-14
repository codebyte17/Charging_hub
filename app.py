import streamlit as st
from st_pages import add_page_title, get_nav_from_toml
st.set_page_config(layout="wide")

st.markdown("""
    <style>
        .block-container {
            padding-top: 1rem;  /* Adjust this value as needed */
            margin-top: 1rem;   /* Adjust this value as needed */
        }
    </style>
""", unsafe_allow_html=True)

nav = get_nav_from_toml("pages_sections.toml")

pg = st.navigation(nav)


add_page_title(pg)


# Render content based on the selected page
if pg.title == "Charging-Hub":
    from _pages.stations import display_stations
    display_stations()
elif pg.title == "Search":
    from _pages.search import display_search
    display_search()