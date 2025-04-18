import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    airports = pd.read_csv("data/airports.dat", header=None)
    routes = pd.read_csv("data/routes.dat", header=None)

    airports.columns = [
        "AirportID", "Name", "City", "Country", "IATA", "ICAO",
        "Lat", "Long", "Altitude", "Timezone", "DST", "Tz", "Type", "Source"
    ]
    routes.columns = [
        "Airline", "AirlineID", "Source", "SourceID", "Dest", "DestID",
        "Codeshare", "Stops", "Equipment"
    ]
    airports = airports[airports["IATA"] != "\\N"]
    return airports, routes
