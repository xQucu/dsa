import matplotlib.pyplot as plt


def draw_cities_and_connections(xs: list[int], ys: list[int], matrix: list[list[int]], plotSize: int, pointsCount: int) -> None:

    plt.rcParams['toolbar'] = 'None'
    plt.figure(figsize=(plotSize, plotSize))
    plt.title("connections and cities")
    plt.scatter(xs, ys, color='blue')

    for i in range(pointsCount):
        for j in range(i):
            if matrix[i][j] != 0:
                plt.plot([xs[i], xs[j]], [ys[i], ys[j]], 'k-', alpha=0.5)
                mid_x = (xs[i] + xs[j]) / 2
                mid_y = (ys[i] + ys[j]) / 2
                plt.text(
                    mid_x, mid_y, str(matrix[i][j]), color='red', fontsize=10, ha='center', va='center', bbox=dict(facecolor='white', edgecolor='none', pad=1))

    for i in range(pointsCount):
        plt.text(xs[i], ys[i], str(i), color='blue', fontsize=12, ha='center',
                 va='center', bbox=dict(facecolor='white', edgecolor='none', pad=1))

    plt.grid(True)
    plt.show()


def draw_optimal_path(xs: list[int], ys: list[int], plotSize: int, path: list[int]) -> None:
    plt.rcParams['toolbar'] = 'None'
    plt.figure(figsize=(plotSize, plotSize))
    plt.title("Optimal path")
    plt.scatter(xs, ys, color='blue')

    for i in range(len(path) - 1):
        x0, y0 = xs[path[i]], ys[path[i]]
        x1, y1 = xs[path[i + 1]], ys[path[i + 1]]
        plt.plot([x0, x1], [y0, y1], 'g-', linewidth=2, alpha=0.8)

    for i in range(len(xs)):
        plt.text(xs[i], ys[i], str(i), color='blue', fontsize=12, ha='center',
                 va='center', bbox=dict(facecolor='white', edgecolor='none', pad=1))

    plt.grid(True)
    plt.show()
