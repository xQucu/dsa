import matplotlib.pyplot as plt


def draw_cities_and_connections(xs: list[int], ys: list[int], matrix: list[list[float]], plotSize: int, pointsCount: int) -> None:
    plt.rcParams['toolbar'] = 'None'
    plt.figure(figsize=(plotSize, plotSize))
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
