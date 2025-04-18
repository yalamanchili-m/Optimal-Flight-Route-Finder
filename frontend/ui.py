import streamlit as st
import pydeck as pdk
import random
from backend.data_loader import load_data
from backend.graph import build_graph
from backend.algorithms import dijkstra, a_star, haversine

def run_app():
    st.set_page_config(page_title="JetSetGo: Optimal Flight Route", layout="wide")

    st.markdown(
        """
        <div style="display:flex; align-items:center; gap:10px;">
            <h1 style="color:#1f77b4;">JetSetGo: Optimal Flight Route Finder</h1>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown("---")

    airports, routes = load_data()
    graph, airport_coords, airport_names = build_graph(airports, routes)

    # Create list of "IATA - City" for selectbox display
    iata_city_list = sorted([f"{iata} - {airport_names.get(iata, '')}" for iata in airport_coords.keys()])

    st.sidebar.header("Flight Route Settings")
    src_display = st.sidebar.selectbox("✈️ Source Airport (IATA - City)", iata_city_list, index=next((i for i, v in enumerate(iata_city_list) if v.startswith("SIN")), 0))
    dst_display = st.sidebar.selectbox("🛬 Destination Airport (IATA - City)", iata_city_list, index=next((i for i, v in enumerate(iata_city_list) if v.startswith("LHR")), 1))

    # Extract IATA codes from selected display strings
    src = src_display.split(" - ")[0]
    dst = dst_display.split(" - ")[0]

    if st.sidebar.button("Find Optimal Route"):
        if src == dst:
            st.warning("Source and Destination are the same.")
        else:
            algo = random.choice(["Dijkstra", "A*"])
            with st.spinner("Finding your most efficient route..."):
                path = dijkstra(graph, airport_coords, src, dst) if algo == "Dijkstra" else a_star(graph, airport_coords, src, dst)

                if path:
                    st.success(f"Route found using {algo} ✅")

                    st.markdown("### 📍 Route Details")
                    for i, code in enumerate(path):
                        st.write(f"{i+1}. {code} - {airport_names.get(code, 'Unknown')}")

                    layovers = len(path) - 2
                    st.info(f"Number of layovers: {layovers}")

                    total_distance = sum(haversine(airport_coords[path[i]], airport_coords[path[i+1]]) for i in range(len(path)-1))
                    st.write(f"Total estimated distance: {total_distance:.2f} km")

                    lines_data = [
                        {
                            "coordinates": [
                                [airport_coords[path[i]][1], airport_coords[path[i]][0]],
                                [airport_coords[path[i+1]][1], airport_coords[path[i+1]][0]]
                            ]
                        }
                        for i in range(len(path) - 1)
                    ]

                    airport_points = [
                        {"position": [airport_coords[code][1], airport_coords[code][0]], "name": f"{code} - {airport_names.get(code, '')}"}
                        for code in path
                    ]

                    line_layer = pdk.Layer(
                        "LineLayer",
                        data=lines_data,
                        get_source_position="coordinates[0]",
                        get_target_position="coordinates[1]",
                        get_width=3,
                        get_color=[200, 30, 0],
                        pickable=True
                    )

                    scatter_layer = pdk.Layer(
                        "ScatterplotLayer",
                        data=airport_points,
                        get_position="position",
                        get_radius=100000,
                        get_fill_color=[0, 0, 0],
                        pickable=True,
                    )

                    tooltip = {"html": "<b>{name}</b>", "style": {"backgroundColor": "steelblue", "color": "white"}}

                    view_state = pdk.ViewState(
                        latitude=sum(airport_coords[code][0] for code in path) / len(path),
                        longitude=sum(airport_coords[code][1] for code in path) / len(path),
                        zoom=2.2,
                        pitch=35,
                    )

                    st.pydeck_chart(pdk.Deck(
                        map_style="https://basemaps.cartocdn.com/gl/positron-gl-style/style.json",
                        initial_view_state=view_state,
                        layers=[line_layer, scatter_layer],
                        tooltip=tooltip
                    ))

                else:
                    st.error("No valid route found.")
