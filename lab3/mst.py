def list_edges(matrix):
    edgesList: list[tuple[int, int, int]] = []

    for rowIndex, row in enumerate(matrix):
        for cellIndex in range(rowIndex + 1, len(row)):
            cost = matrix[rowIndex][cellIndex]
            if cost != 0:
                edgesList.append(
                    (min(rowIndex, cellIndex), max(rowIndex, cellIndex), cost))

    edgesList.sort(key=lambda e: e[2])
    return edgesList


def create_MST(matrix: list[list[int]]):

    edgesList = list_edges(matrix)

    adjacencyList: list[list[tuple[int, int]]] = [[]
                                                  for _ in range(len(matrix))]

    colors: list[int] = [0 for _ in range(len(matrix))]
    colorCounter = 0
    newColor = 0
    verticesConnected = 0

    while len(edgesList) > 0 and not (verticesConnected == len(matrix) and colorCounter == 1):

        (node1, node2, cost) = edgesList.pop(0)
        if colors[node1] == 0 and colors[node2] == 0:
            colorCounter += 1
            newColor += 1
            colors[node1] = newColor
            colors[node2] = newColor
            adjacencyList[node1].append((node2, cost))
            adjacencyList[node2].append((node1, cost))
            verticesConnected += 2

        elif colors[node1] != 0 and colors[node2] == 0:
            colors[node2] = colors[node1]
            adjacencyList[node1].append((node2, cost))
            adjacencyList[node2].append((node1, cost))
            verticesConnected += 1

        elif colors[node2] != 0 and colors[node1] == 0:
            colors[node1] = colors[node2]
            adjacencyList[node1].append((node2, cost))
            adjacencyList[node2].append((node1, cost))
            verticesConnected += 1

        elif colors[node1] == colors[node2]:
            continue
        else:
            colorCounter -= 1
            colorToErase = colors[node1]
            for i in range(len(colors)):
                if (colors[i] == colorToErase):
                    colors[i] = colors[node2]

            adjacencyList[node1].append((node2, cost))
            adjacencyList[node2].append((node1, cost))

    return adjacencyList


def DFS_traversal_on_adj_list(adj_list: list[list[tuple[int, int]]], source: int, matrix: list[list[int]]) -> tuple[int, list[int]]:
    route: list[int] = []
    q = [source]

    while len(q) > 0:
        current = q.pop()
        if current in route:
            continue
        route.append(current)
        connections = adj_list[current]
        for node, _ in connections:
            q.append(node)

    route.append(source)

    totalCost = 0
    for i in range(len(route)-1):
        totalCost += matrix[route[i]][route[i+1]]
    return totalCost, route


def approximate_TSP_MST_DFS(matrix: list[list[int]], source: int) -> tuple[int, list[int]]:
    adjacency_list_MST = create_MST(matrix)

    # draw_cities_and_connections_from_list(xs, ys, adjacency_list, 7)

    return DFS_traversal_on_adj_list(adjacency_list_MST, source, matrix)
