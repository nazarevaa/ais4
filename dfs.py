def dfs(graph, start, visited=None):
    if visited is None:
        visited = []
    visited.append(start)
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited

if __name__ == "__main__":
    edges = [(4, 2), (1, 3), (2, 4)]
    graph = {}
    for u, v in edges:
        graph.setdefault(u, []).append(v)
        graph.setdefault(v, []).append(u)

    start_vertex = 1
    path = dfs(graph, start_vertex)
    print("Обход в глубину:", path)
