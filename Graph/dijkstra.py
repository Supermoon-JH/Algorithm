import heapq


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distances[current_node] < current_distance:
            continue

        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, (distance, adjacent))

    return distances


def dijkstra_route(graph, start, end):
    distances = {node: [float('inf'), start] for node in graph}
    distances[start] = [0, start]
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distances[current_node][0] < current_distance:
            continue

        for adj, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[adj][0]:
                distances[adj] = [distance, current_node]
                heapq.heappush(queue, [distance, adj])

    path = end
    path_output = end + '->'

    while distances[path][1] != start:
        path_output += distances[path][1] + '->'
        path = distances[path][1]

    path_output += start
    print(path_output)

    return distances

mygraph = {
	'A': {'B': 8, 'C': 1, 'D': 2},
	'B': {},
	'C': {'B': 5, 'D': 2},
	'D': {'E': 3, 'F': 5},
	'E': {'F': 1},
	'F': {'A': 5}
}

print(dijkstra(mygraph, 'A'))
print(dijkstra_route(mygraph, 'A', 'F'))