# histogram.py

import sys
import matplotlib.pyplot as plt
from utils.data_loader import load_csv

def histogram(filepath):
    headers, data = load_csv(filepath)

    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    colors  = ["red", "yellow", "blue", "green"]

    skip = {"Index", "Hogwarts House", "First Name", "Last Name",
            "Birthday", "Best Hand"}

    # Index de la colonne maison
    house_idx = headers.index("Hogwarts House")

    # On garde uniquement les cours (colonnes numériques hors skip)
    courses = []
    course_indices = []
    for j, col in enumerate(headers):
        if col in skip:
            continue
        # Vérifier si la colonne est numérique
        for row in data:
            val = row[j]
            if val == '':
                continue
            try:
                float(val)
                courses.append(col)
                course_indices.append(j)
            except ValueError:
                pass
            break

    # Grille de subplots
    cols = 4
    rows = (len(courses) + cols - 1) // cols

    fig, axes = plt.subplots(rows, cols, figsize=(20, rows * 4))
    axes = axes.flatten()

    for i, (course, j) in enumerate(zip(courses, course_indices)):
        ax = axes[i]

        for house, color in zip(houses, colors):
            scores = []
            for row in data:
                if row[house_idx] != house:
                    continue
                val = row[j]
                if val == '':
                    continue
                try:
                    scores.append(float(val))
                except ValueError:
                    pass

            if scores:
                ax.hist(scores, bins=20, alpha=0.5,
                        color=color, label=house)

        ax.set_title(course, fontsize=9)
        ax.set_xlabel("Score")
        ax.set_ylabel("Count")
        ax.legend(fontsize=7)

    for k in range(i + 1, len(axes)):
        axes[k].set_visible(False)

    plt.suptitle("Score distribution per course per house", fontsize=14)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python histogram.py data/dataset_train.csv")
        sys.exit(1)
    histogram(sys.argv[1])
