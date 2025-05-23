import matplotlib.pyplot as plt


def draw_cities_and_connections_from_matrix(xs: list[int], ys: list[int], matrix: list[list[int]], plotSize: int, pointsCount: int) -> None:

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


def draw_cities_and_connections_from_list(xs: list[int], ys: list[int], adj_list: list[list[tuple[int, int]]], plotSize: int) -> None:

    plt.rcParams['toolbar'] = 'None'
    plt.figure(figsize=(plotSize, plotSize))
    plt.title("connections and cities")
    plt.scatter(xs, ys, color='blue')

    # Keep track of drawn edges to avoid duplicates
    drawn_edges = set()

    # Draw connections
    for city1, neighbors in enumerate(adj_list):
        for neighbor_info in neighbors:
            city2, cost = neighbor_info  # Now unpacking a tuple
            # Create an edge identifier (using sorted tuple to handle both directions)
            edge = tuple(sorted([city1, city2]))

            # Only draw if we haven't drawn this edge yet
            if edge not in drawn_edges:
                plt.plot([xs[city1], xs[city2]], [
                         ys[city1], ys[city2]], 'k-', alpha=0.5)
                mid_x = (xs[city1] + xs[city2]) / 2
                mid_y = (ys[city1] + ys[city2]) / 2
                plt.text(
                    mid_x, mid_y, str(cost), color='red', fontsize=10, ha='center', va='center',
                    bbox=dict(facecolor='white', edgecolor='none', pad=1))

                # Mark this edge as drawn
                drawn_edges.add(edge)

    for i in range(len(xs)):
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
