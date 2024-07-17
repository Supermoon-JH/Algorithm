import heapq

def prim(graph, start):
    mst = []
    visited = set()
    keys = {node: float('inf') for node in graph}
    parent = {node: None for node in graph}
    total_weight = 0
    keys[start] = 0
    pq = [(0, start)]

    while pq:
        current_key, current_node = heapq.heappop(pq)
        if current_node in visited:
            continue
        
        visited.add(current_node)
        if parent[current_node] is not None:  # start 노드가 아닌 경우에만 MST에 추가
            mst.append([parent[current_node], current_node, current_key])
            total_weight += current_key
        
        for adj, weight in graph[current_node].items():
            if adj not in visited and weight < keys[adj]:
                keys[adj] = weight
                parent[adj] = current_node
                heapq.heappush(pq, (weight, adj))

    return mst, total_weight


mygraph = {
    'A': {'B': 7, 'D': 5},
    'B': {'A': 7, 'D': 9, 'C': 8, 'E': 7},
    'C': {'B': 8, 'E': 5},
    'D': {'A': 5, 'B': 9, 'E': 7, 'F': 6},
    'E': {'B': 7, 'C': 5, 'D': 7, 'F': 8, 'G': 9},
    'F': {'D': 6, 'E': 8, 'G': 11},
    'G': {'E': 9, 'F': 11}    
}

mst, total_weight = prim(mygraph, 'A')
print('MST:', mst)
print('Total Weight:', total_weight)