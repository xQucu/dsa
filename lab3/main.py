import random
import math
from pprint import pprint

from drawing import draw_cities_and_connections


CITIES = 5
CITY_CONNECTIONS_CHANCE = 80
PLOT_SIZE = 10
MAX_POSITION = 100
MIN_POSITION = 0


def generate_cities(n: int) -> tuple[list[int], list[int]]:
    x, y = [], []
    for _ in range(n):
        rand = random.randint(MIN_POSITION, MAX_POSITION)
        x.append(rand)
        rand = random.randint(MIN_POSITION, MAX_POSITION)
        y.append(rand)
    return x, y


def generate_adjacency_matrix(xs: list[int], ys: list[int]) -> list[list[float]]:
    matrix: list[list[float]] = [
        [-1 for _ in range(CITIES)] for _ in range(CITIES)]
    for c1 in range(CITIES):
        for c2 in range(CITIES):
            if (c1 == c2 or random.randint(1, 100) > CITY_CONNECTIONS_CHANCE) and matrix[c2][c1] == -1:
                matrix[c1][c2] = 0
            else:
                if matrix[c2][c1] != -1:
                    matrix[c1][c2] = matrix[c2][c1]
                else:
                    matrix[c1][c2] = round(
                        math.sqrt((xs[c1]-xs[c2])**2+(ys[c1]-ys[c2])**2), 2)

    pprint(matrix)

    return matrix


def main() -> None:
    xs, ys = generate_cities(CITIES)
    matrix = generate_adjacency_matrix(xs, ys)

    draw_cities_and_connections(xs, ys, matrix, PLOT_SIZE, CITIES)


if __name__ == "__main__":
    main()
