Optimal Flight Route Finder
A Python-based application that finds the **most optimal flight route** between two airports using **graph algorithms** and provides an **interactive UI built with Streamlit**.

Overview
This project allows users to:
- Input source and destination airports
- Select optimization criteria (cost, duration, or stops)
- View the **best available route** based on the dataset
- See flight details, total cost, and total duration — all in a simple Streamlit web interface.

Project Structure
Optimal-Flight-Route-Finder
- `backend/` — Core logic including graph algorithms and data processing  
- `data/` — Flight and airport datasets  
- `frontend/` — Streamlit app files (UI)  
- `main.py` — Entry point to run the Streamlit app  


Features
- ✈️ Optimal route calculation using shortest path algorithms  
- ⏱️ Supports optimization by cost, time, or number of stops  
- 🧭 Streamlit interface for easy interaction  
- 📊 CSV/JSON dataset support for flight data  
- 🧮 Clean architecture separating logic and UI

Tech Stack
- **Frontend:** Streamlit
- **Backend:** Python 
- **Data:** CSV / JSON datasets stored in `data/`  

How It Works
- Backend reads and processes flight data from the data/ folder.
- Graph is constructed with airports as nodes and flights as weighted edges.

User enters:
- Source airport
- Destination airport
- Optimization criteria (e.g., minimum cost)
- The algorithm (e.g., Dijkstra) finds the best route.

Streamlit displays:
- Route details
- Total cost
- Total duration
- Number of stops

Future Enhancements
- Map visualization of routes (e.g., using Folium or Plotly with Streamlit)
- Multi-criteria optimization (cost + time)
- Real-time data integration (APIs)
- User accounts & saved searches

