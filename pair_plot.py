import sys
import matplotlib.pyplot as plt
from utils.data_loader import load_csv, get_numeric_columns

# Couleurs par maison
HOUSE_COLORS = {
    "Gryffindor": "red",
    "Slytherin":  "green",
    "Ravenclaw":  "blue",
    "Hufflepuff": "yellow"
}

def get_house_index(headers):
    # Trouve la colonne "Hogwarts House"
    for i, h in enumerate(headers):
        if h == "Hogwarts House":
            return i
    return -1

def pair_plot(filepath):
    headers, data = load_csv(filepath)
    numeric = get_numeric_columns(headers, data)
    
    # On garde seulement les cours qu'on veut comparer
    courses = list(numeric.keys())
    n = len(courses)
    
    house_idx = get_house_index(headers)
    
    fig, axes = plt.subplots(n, n, figsize=(n * 2, n * 2))
    fig.tight_layout(pad=1.0)

    for i, course_y in enumerate(courses):
        for j, course_x in enumerate(courses):
            ax = axes[i][j]
            ax.set_xticks([])
            ax.set_yticks([])

            if i == j:
                # Diagonale → histogram par maison
                for house, color in HOUSE_COLORS.items():
                    vals = []
                    for row in data:
                        if row[house_idx] == house:
                            try:
                                vals.append(float(row[headers.index(course_x)]))
                            except:
                                pass
                    ax.hist(vals, bins=20, color=color, alpha=0.5)

            else:
                # Scatter → un point par élève
                for house, color in HOUSE_COLORS.items():
                    x_vals = []
                    y_vals = []
                    for row in data:
                        if row[house_idx] == house:
                            try:
                                x = float(row[headers.index(course_x)])
                                y = float(row[headers.index(course_y)])
                                x_vals.append(x)
                                y_vals.append(y)
                            except:
                                pass
                    ax.scatter(x_vals, y_vals, color=color, s=1, alpha=0.5)

            # Noms sur les bords
            if j == 0:
                ax.set_ylabel(course_y, fontsize=6)
            if i == n - 1:
                ax.set_xlabel(course_x, fontsize=6, rotation=45)

    plt.suptitle("Pair Plot", y=1.02)
    plt.savefig("pair_plot.png", bbox_inches="tight")
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 pair_plot.py <dataset>")
        sys.exit(1)
    pair_plot(sys.argv[1])
