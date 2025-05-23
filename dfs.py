def dfs_path_length(graph, start, end, visited=None, depth=0):
    if visited is None:
        visited = []
    visited.append(start)

    if start == end:
        return depth

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            path_length = dfs_path_length(graph, neighbor, end, visited, depth + 1)
            if path_length is not None:
                return path_length
    return None

if __name__ == "__main__":
    edges = [(4, 2), (1, 3), (2, 4)]
    graph = {}
    for u, v in edges:
        graph.setdefault(u, []).append(v)
        graph.setdefault(v, []).append(u)

    # Часть для обхода в глубину
    start_vertex = 1
    path = dfs(graph, start_vertex)
    print("Обход в глубину:", path)

    # Часть для вычисления длины пути
    start_vertex = 2
    end_vertex = 4
    path_length = dfs_path_length(graph, start_vertex, end_vertex)
    if path_length is not None:
        print(f"Длина пути из {start_vertex} в {end_vertex}: {path_length}")
    else:
        print(f"Пути из {start_vertex} в {end_vertex} не существует")
