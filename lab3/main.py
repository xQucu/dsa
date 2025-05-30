import random
import math
from pprint import pprint
from typing import Literal


from matplotlib.pyplot import plot

from drawing import *
from mst import approximate_TSP_MST_DFS


CITIES = 10
CITY_CONNECTIONS_CHANCE = 80
PLOT_SIZE = 10
MAX_POSITION = 100
MIN_POSITION = -100


def generate_cities(n: int) -> tuple[list[int], list[int]]:
    x, y = [], []
    for _ in range(n):
        rand = random.randint(MIN_POSITION, MAX_POSITION)
        x.append(rand)
        rand = random.randint(MIN_POSITION, MAX_POSITION)
        y.append(rand)
    return x, y


def generate_adjacency_matrix(xs: list[int], ys: list[int]) -> list[list[int]]:
    matrix: list[list[int]] = [
        [-1 for _ in range(CITIES)] for _ in range(CITIES)]
    for c1 in range(CITIES):
        for c2 in range(CITIES):
            if (c1 == c2 or random.randint(1, 100) > CITY_CONNECTIONS_CHANCE) and matrix[c2][c1] == -1:
                matrix[c1][c2] = 0
            else:
                if matrix[c2][c1] != -1:
                    matrix[c1][c2] = matrix[c2][c1]
                else:
                    matrix[c1][c2] = int(
                        math.sqrt((xs[c1]-xs[c2])**2+(ys[c1]-ys[c2])**2))

    return matrix


def solveTSP(matrix: list[list[int]], source: int, verticesCount: int, mode: Literal["BFS", "DFS"]) -> tuple[int, int, list[int]]:

    current = source
    distance = 0
    path = [source]

    q: list[tuple[int, int, list[int]]] = []
    q.append((current, distance, path))

    possibleSolutions: list[tuple[int, int, list[int]]] = []

    while len(q) > 0:
        current, distance, path = q.pop(0) if mode == "BFS" else q.pop()
        if (len(path) == verticesCount):
            possibleSolutions.append((current, distance, path))
            continue
        for i in range(verticesCount):
            currDistance = matrix[current][i]

            if i == current or currDistance == 0 or i in path:
                continue

            currPath = path.copy()
            currPath.append(i)

            q.append((i, currDistance+distance, currPath))

    smallestDistance = 0
    smallestDistanceIdx = 0

    for i, (curr, dist, path) in enumerate(possibleSolutions):
        if matrix[path[-1]][source] == 0:
            continue
        newDistance = dist + matrix[path[-1]][source]
        if smallestDistance == 0 or newDistance < smallestDistance:
            smallestDistance = newDistance
            smallestDistanceIdx = i
        possibleSolutions[i] = (
            curr, newDistance, path + [source])

    if len(possibleSolutions) == 0 or len(possibleSolutions[smallestDistanceIdx][2]) < verticesCount+1:
        return (0, 0, [])

    return possibleSolutions[smallestDistanceIdx]


def approximateTSPGreedy(matrix: list[list[int]], source: int, verticesCount: int) -> tuple[int, list[int]]:
    current = source
    totalDistance = 0
    path = [source]

    while len(path) < verticesCount:
        if len(path) == verticesCount-1:
            if matrix[current][source] == 0:
                tmp = path.pop()
                path.pop()
                path.append(tmp)
                continue

        minDistance = 0
        idxForMinDistance = -1

        for idx, distance in enumerate(matrix[current]):
            if distance == 0:
                continue
            if (minDistance == 0 or minDistance > distance) and idx not in path:
                minDistance = distance
                idxForMinDistance = idx

        if idxForMinDistance == -1:
            return (0, [])

        path.append(idxForMinDistance)
        totalDistance += minDistance
        current = idxForMinDistance
    path.append(source)
    totalDistance += matrix[current][source]
    return (totalDistance, path)


def reconstructPathAfterBidirectionalSearch(prevFromSource, prevFromDest, mutual) -> list[int]:
    current = prevFromDest[mutual]
    out = []

    while prevFromDest[current] != -1:
        out.insert(0, current)
        current = prevFromDest[current]
    out.insert(0, current)

    current = mutual
    while prevFromSource[current] != -1:
        out.append(current)
        current = prevFromSource[current]

    out.append(current)
    out.reverse()
    return out


def indirectPathBetweenTwoVertices(matrix: list[list[int]], source: int, dest: int, verticesCount: int) -> list[int]:
    prevFromSource = [-1 for _ in range(verticesCount)]
    seenFromSource = [source]
    qSource = []
    qSource.append(source)

    prevFromDest = [-1 for _ in range(verticesCount)]
    seenFromDest = [source]
    qDest = []
    qDest.append(dest)

    while len(qSource) > 0 or len(qDest) > 0:
        if len(qSource) > 0:
            current = qSource.pop(0)
            if current == dest:
                break
            for idx in range(verticesCount):
                if idx in seenFromSource or matrix[idx][current] == 0:
                    continue
                seenFromSource.append(idx)
                prevFromSource[idx] = current
                qSource.append(idx)
                if idx in seenFromDest:
                    return reconstructPathAfterBidirectionalSearch(prevFromSource, prevFromDest, idx)

        if len(qDest) > 0:
            current = qDest.pop(0)
            if current == source:
                break
            for idx in range(verticesCount):
                if idx in seenFromDest or matrix[idx][current] == 0:
                    continue
                seenFromDest.append(idx)
                prevFromDest[idx] = current
                qDest.append(idx)
                if idx in seenFromSource:
                    return reconstructPathAfterBidirectionalSearch(prevFromSource, prevFromDest, idx)

    return []


def main() -> None:
    # xs = [66, 53, 33, 38, 39, -41, -96, -11, 87, -50]
    # ys = [92, -65, -3, -50, 78, 33, -29, -94, 58, -59]
    # matrix = [
    #     [0, 158, 101, 145, 30, 122, 202, 201, 40, 0],
    #     [158, 0, 65, 21, 144, 136, 153, 70, 128, 103],
    #     [101, 65, 0, 0, 81, 82, 0, 101, 81, 100],
    #     [145, 21, 0, 0, 128, 115, 136, 0, 0, 88],
    #     [30, 144, 81, 128, 0, 92, 0, 179, 52, 163],
    #     [122, 136, 82, 115, 92, 0, 83, 0, 130, 92],
    #     [202, 153, 0, 136, 0, 83, 0, 107, 0, 55],
    #     [201, 70, 101, 0, 179, 0, 107, 0, 181, 52],
    #     [40, 128, 81, 0, 52, 130, 0, 181, 0, 180],
    #     [0, 103, 100, 88, 163, 92, 55, 52, 180, 0]
    # ]
    # matrix = [
    #     [0, 0, 0, 0, 30, 0, 0, 0, 40, 0],
    #     [0, 0, 0, 21, 0, 0, 0, 15, 128, 0],
    #     [0, 0, 0, 47, 81, 82, 0, 0, 0, 0],
    #     [0, 21, 47, 0, 0, 0, 0, 0, 0, 0],
    #     [30, 0, 81, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 82, 0, 0, 0, 77, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 77, 0, 0, 0, 44],
    #     [0, 15, 0, 0, 0, 0, 0, 0, 0, 25],
    #     [40, 128, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 44, 25, 0, 0]
    # ]

    xs, ys = generate_cities(CITIES)
    matrix: list[list[int]] = generate_adjacency_matrix(xs, ys)

    draw_cities_and_connections_from_matrix(
        xs, ys, matrix, PLOT_SIZE, CITIES, "Cities with connections")

    # startingCity = 0
    # destCity = 6

    startingCity = random.randint(0, CITIES - 1)
    destCity = random.randint(0, CITIES - 1)
    print(f"Starting city: {startingCity}")
    print(f"Destination city: {destCity}")

    _, distance, path = solveTSP(matrix, startingCity, CITIES, 'BFS')
    print(f"Optimal path from BFS is of length {distance}")
    pprint(path)
    draw_optimal_path(xs, ys, PLOT_SIZE, path, "Optimal path from BFS")

    _, distance, path = solveTSP(matrix, startingCity, CITIES, 'DFS')
    print(f"Optimal path from DFS is of length {distance}")
    pprint(path)
    draw_optimal_path(xs, ys, PLOT_SIZE, path, "Optimal path from DFS")

    distance, path = approximate_TSP_MST_DFS(
        matrix, startingCity)
    print(f"Optimal path from MST is of length {distance}")
    pprint(path)
    draw_optimal_path(xs, ys, PLOT_SIZE, path, "Optimal path from MST")

    distance, path = approximateTSPGreedy(matrix, startingCity, CITIES)
    print(f"Optimal path from greedy is of length {distance}")
    pprint(path)
    draw_optimal_path(xs, ys, PLOT_SIZE, path, "Optimal path from greedy")

    path = indirectPathBetweenTwoVertices(
        matrix, startingCity, destCity, CITIES)
    print("indirect path between two cities")
    pprint(path)
    draw_optimal_path(xs, ys, PLOT_SIZE, path,
                      "indirect path between two cities")


if __name__ == "__main__":
    main()
