import streamlit as st

def display_search():
    postal_code = st.text_input("Enter Postal Code (PLZ)", "")
    search_button = st.button("Search")

