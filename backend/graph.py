def build_graph(airports, routes):
    airport_coords = {
        row["IATA"]: (row["Lat"], row["Long"])
        for _, row in airports.iterrows()
    }
    airport_names = {
        row["IATA"]: f"{row['Name']} ({row['City']})"
        for _, row in airports.iterrows()
    }
    graph = {}
    for _, row in routes.iterrows():
        src, dst = row["Source"], row["Dest"]
        if src in airport_coords and dst in airport_coords:
            graph.setdefault(src, []).append(dst)
    return graph, airport_coords, airport_names
