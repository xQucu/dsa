from drawing import draw_cities_and_connections_from_list


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
    tmp = 0
    verticesConnected = 0

    while len(edgesList) > 0 and not (verticesConnected == len(matrix) and colorCounter == 1):

        (node1, node2, cost) = edgesList.pop(0)
        if colors[node1] == 0 and colors[node2] == 0:
            colorCounter += 1
            tmp += 1
            colors[node1] = tmp
            colors[node2] = tmp
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


def DFS_traversal_on_adj_list(adj_list: list[list[tuple[int, int]]], verticesCount: int, source: int) -> tuple[int, list[int]]:
    route: list[int] = []
    q = [source]

    while len(q) > 0:
        current = q.pop()
        if current in route:
            continue
        route.append(current)
        connections = adj_list[current]
        for node, cost in connections:
            q.append(node)

    route.append(source)

    totalCost = 0
    for i in range(len(route)-1):
        connections = adj_list[route[i]]
        currentCost = 0
        for c in connections:
            if c[0] == route[i+1]:
                currentCost += c[1]
        totalCost += currentCost
    return totalCost, route


def approximate_TSP_MST_DFS(matrix: list[list[int]], xs, ys, verticesCount, source: int) -> tuple[int, list[int]]:
    adjacency_list = create_MST(matrix)

    # show MST
    # draw_cities_and_connections_from_list(xs, ys, adjacency_list, 7)

    return DFS_traversal_on_adj_list(adjacency_list, verticesCount, source)
