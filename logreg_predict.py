import pandas as pd
import numpy as np
import sys
from logreg_train import predict

def save_house(y_pred: np.ndarray,
               path: str = "house.csv") -> None:
    """
    Sauvegarde prediction houses.
    """
    df = pd.DataFrame({
        "Index": range(len(y_pred)),
        "Hogwarts House": y_pred
    })
    df.to_csv(path, index=False)

def main():
    if len(sys.argv) != 2:
        print("Usage: python logreg_predict.py dataset_test.csv")
        return

    df = pd.read_csv(sys.argv[1])


    X = df.select_dtypes(include=[np.number])
    X = X.drop(columns=["Index", "Hogwarts House"], errors="ignore")

    X = X.fillna(X.mean())

    df = pd.read_csv("weights.csv", index_col=0)
    if df is None:
        print("Usage: exec logreg_train.py before")
        return

    means = df.loc["mean"]
    stds = df.loc["std"]
    X = (X - means) / stds
    X = X.values

    weights = {}
    for index in df.index:
        if index not in ["mean", "std"]:
            weights[index] = df.loc[index].values
    classes = np.array(list(weights.keys()))
    y_pred = predict(X, weights, classes)
    save_house(y_pred)
    



if __name__ == "__main__":
    main()
