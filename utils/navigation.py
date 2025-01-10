# utils/navigation.py

import streamlit as st

def display_navigation():
    st.sidebar.header("Navigation")
    menu = ["Home", "Search by Postal Code"]
    choice = st.sidebar.selectbox("Go to", menu)
    return choice
