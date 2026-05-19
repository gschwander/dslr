# scatter_plot.py

import sys
import matplotlib.pyplot as plt
from utils.data_loader import load_csv, get_numeric_columns

def scatter_plot(filepath):
    headers, data = load_csv(filepath)
    numeric = get_numeric_columns(headers, data)

    courses = list(numeric.keys())
    n = len(courses)

    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    colors  = ["red", "yellow", "blue", "green"]

    house_idx = headers.index("Hogwarts House")

    # Grille n x n
    fig, axes = plt.subplots(n, n, figsize=(n * 2, n * 2))

    for i, course_y in enumerate(courses):
        for j, course_x in enumerate(courses):
            ax = axes[i][j]

            if i == j:
                # Diagonale : juste le nom du cours
                ax.text(0.5, 0.5, course_x,
                        ha='center', va='center',
                        fontsize=6, transform=ax.transAxes)
                ax.set_visible(True)
            else:
                for house, color in zip(houses, colors):
                    x_vals = []
                    y_vals = []

                    for row_idx, row in enumerate(data):
                        if row[house_idx] != house:
                            continue
                        # On cherche les index des colonnes
                        col_x = headers.index(course_x)
                        col_y = headers.index(course_y)

                        vx = row[col_x]
                        vy = row[col_y]

                        if vx == '' or vy == '':
                            continue
                        try:
                            x_vals.append(float(vx))
                            y_vals.append(float(vy))
                        except ValueError:
                            pass

                    ax.scatter(x_vals, y_vals,
                               color=color, alpha=0.3,
                               s=1, label=house)

            # Labels uniquement sur les bords
            if i == n - 1:
                ax.set_xlabel(course_x, fontsize=5)
            if j == 0:
                ax.set_ylabel(course_y, fontsize=5)

            ax.tick_params(labelsize=4)

    plt.suptitle("Scatter plot matrix — find similar features", fontsize=12)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scatter_plot.py data/dataset_train.csv")
        sys.exit(1)
    scatter_plot(sys.argv[1])
