import random
import matplotlib.pyplot as plt
import math
from pprint import pprint

plt.rcParams['toolbar'] = 'None'
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


def draw_cities_and_connections(xs: list[int], ys: list[int], matrix: list[list[float]]) -> None:
    plt.figure(figsize=(PLOT_SIZE, PLOT_SIZE))
    plt.scatter(xs, ys, color='blue')

    for i in range(CITIES):
        for j in range(i):
            if matrix[i][j] != 0:
                plt.plot([xs[i], xs[j]], [ys[i], ys[j]], 'k-', alpha=0.5)
                mid_x = (xs[i] + xs[j]) / 2
                mid_y = (ys[i] + ys[j]) / 2
                plt.text(
                    mid_x, mid_y, str(matrix[i][j]), color='red', fontsize=10, ha='center', va='center', bbox=dict(facecolor='white', edgecolor='none', pad=1))

    for i in range(CITIES):
        plt.text(xs[i], ys[i], str(i), color='blue', fontsize=12, ha='center',
                 va='center', bbox=dict(facecolor='white', edgecolor='none', pad=1))

    plt.grid(True)
    plt.show()


def main() -> None:
    xs, ys = generate_cities(CITIES)
    matrix = generate_adjacency_matrix(xs, ys)

    draw_cities_and_connections(xs, ys, matrix)


if __name__ == "__main__":
    main()
