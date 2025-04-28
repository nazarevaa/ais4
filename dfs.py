def dfs_path_length(graph, start, end, visited=None, depth=0):
    # Инициализируем список посещённых вершин
    if visited is None:
        visited = []
    visited.append(start)

    # Если мы достигли конечной вершины, возвращаем текущую длину пути
    if start == end:
        return depth

    # Проходим по соседям текущей вершины
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            # Рекурсивно вызываем dfs для соседа
            path_length = dfs_path_length(graph, neighbor, end, visited, depth + 1)
            if path_length is not None:
                return path_length
    # Если путь не найден, возвращаем None
    return None

if __name__ == "__main__":
    # Список рёбер графа
    edges = [(4, 2), (1, 3), (2, 4)]
    graph = {}
    
    # Строим граф из рёбер
    for u, v in edges:
        graph.setdefault(u, []).append(v)
        graph.setdefault(v, []).append(u)

    start_vertex = 2
    end_vertex = 5  # Некорректная вершина для проверки

    # Проверяем, существуют ли стартовая и конечная вершины в графе
    if start_vertex not in graph or end_vertex not in graph:
        print(f"Ошибка: одна из вершин ({start_vertex}, {end_vertex}) отсутствует в графе")
    else:
        # Если вершины существуют, ищем путь и его длину
        path_length = dfs_path_length(graph, start_vertex, end_vertex)
        if path_length is not None:
            print(f"Длина пути из {start_vertex} в {end_vertex}: {path_length}")
        else:
            print(f"Пути из {start_vertex} в {end_vertex} не существует")
