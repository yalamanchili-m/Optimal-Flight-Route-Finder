import heapq
import math

def haversine(coord1, coord2):
    R = 6371  # Earth radius in km
    lat1, lon1 = map(math.radians, coord1)
    lat2, lon2 = map(math.radians, coord2)
    dlat, dlon = lat2 - lat1, lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1)*math.cos(lat2)*math.sin(dlon/2)**2
    return R * 2 * math.asin(math.sqrt(a))

def dijkstra(graph, airport_coords, start, end):
    q = [(0, start, [])]
    visited = set()
    while q:
        dist, node, path = heapq.heappop(q)
        if node in visited:
            continue
        visited.add(node)
        path = path + [node]
        if node == end:
            return path
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                coord1 = airport_coords[node]
                coord2 = airport_coords[neighbor]
                heapq.heappush(q, (dist + haversine(coord1, coord2), neighbor, path))
    return None

def a_star(graph, airport_coords, start, end):
    open_set = [(haversine(airport_coords[start], airport_coords[end]), 0, start, [])]
    visited = set()
    while open_set:
        est_total, cost_so_far, node, path = heapq.heappop(open_set)
        if node in visited:
            continue
        visited.add(node)
        path = path + [node]
        if node == end:
            return path
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                g = cost_so_far + haversine(airport_coords[node], airport_coords[neighbor])
                h = haversine(airport_coords[neighbor], airport_coords[end])
                heapq.heappush(open_set, (g + h, g, neighbor, path))
    return None
