Optimal Flight Route Finder
A Python-based application that finds the **most optimal flight route** between two airports using **graph algorithms** and provides an **interactive UI built with Streamlit**.

Overview
This project allows users to:
- Input source and destination airports
- Select optimization criteria (cost, duration, or stops)
- View the **best available route** based on the dataset
- See flight details, total cost, and total duration — all in a simple Streamlit web interface.

Project Structure
Optimal-Flight-Route-Finder/
├── backend/ # Core logic: graph algorithms, data processing
├── data/ # Flight & airport datasets
├── frontend/ # Streamlit app files (UI)
├── main.py # Entry point to run the Streamlit app
└── requirements.txt # Python dependencies

Features
- ✈️ Optimal route calculation using shortest path algorithms  
- ⏱️ Supports optimization by cost, time, or number of stops  
- 🧭 Streamlit interface for easy interaction  
- 📊 CSV/JSON dataset support for flight data  
- 🧮 Clean architecture separating logic and UI

Tech Stack
- **Frontend:** [Streamlit](https://streamlit.io)  
- **Backend:** Python (with NetworkX for graph algorithms)  
- **Data:** CSV / JSON datasets stored in `data/`  
- **Other Libraries:** Pandas, NumPy, etc.

Installation
1. **Clone the repository**
   git clone https://github.com/yalamanchili-m/Optimal-Flight-Route-Finder.git
   cd Optimal-Flight-Route-Finder
Create and activate virtual environment (optional but recommended)
  python -m venv venv
  source venv/bin/activate         # On Windows: venv\Scripts\activate
Install dependencies
  pip install -r requirements.txt
Add your flight dataset
  Place flights.csv or any dataset inside the data/ folder.
Running the App
Simply run:
  streamlit run main.py
This will launch the Streamlit UI in your browser, typically at:
  http://localhost:8501

How It Works
Backend reads and processes flight data from the data/ folder.
Graph is constructed with airports as nodes and flights as weighted edges.

User enters:
Source airport
Destination airport
Optimization criteria (e.g., minimum cost)
The algorithm (e.g., Dijkstra) finds the best route.

Streamlit displays:
Route details
Total cost
Total duration
Number of stops
Example Usage

Input:
Source: DEL
Destination: LON
Criteria: min_cost

Output:

yaml
Copy code
DEL -> DXB -> LON
Total cost: ₹12,000
Total duration: 10h
Stops: 1
🧪 Testing
To run tests (if present in backend/tests):

bash
Copy code
pytest
Or using built-in unittest:

bash
Copy code
python -m unittest
🛠️ Future Enhancements
🗺️ Map visualization of routes (e.g., using Folium or Plotly with Streamlit)

⏳ Multi-criteria optimization (cost + time)

📍 Real-time data integration (APIs)

🧑 User accounts & saved searches

🤝 Contributing
Fork the repository

Create a new branch (git checkout -b feature-branch)

Make your changes

Push and open a pull request 🚀

📜 License
MIT License © 2025 yalamanchili-m

🙏 Acknowledgements
Streamlit for frontend framework

NetworkX for graph algorithms

Pandas & NumPy for data handling

Open flight / airport datasets
