import numpy as np
import pandas as pd

def train_test_split(X: np.ndarray, Y:np.ndarray, test_size: float = 0.2, random_state: int = 42) -> tuple:
    """
    Args:
        X            : (n_samples, n_features)
        y            : (n_samples,) — les 4 maisons
        test_size    : proportion du test set
        random_state : seed pour la reproductibilité
    Returns:
        X_train, X_test, y_train, y_test
    """
    rng = np.random.default_rng(random_state)

    train_indices = []
    test_indices = []
    for house in np.unique(Y):
        list_label = np.where(Y == house)[0]
        rng.shuffle(list_label)
        n_test = round(len(list_label) * test_size)
        test_indices += list(list_label[:n_test])
        train_indices += list(list_label[n_test:])
    X_train = X[train_indices]
    y_train = Y[train_indices]
    X_test = X[test_indices]
    y_test = Y[test_indices]
    return X_train, X_test, y_train, y_test


def init_logreg_ovr(X_train: np.ndarray,
                    y_train: np.ndarray) -> tuple:
    """
    Args:
        X_train : (n_samples, n_features)
        y_train : (n_samples,) — les 4 maisons
    Returns:
        classes : array des 4 noms de maisons
        weights : dict  { maison: θ de taille (n_features,) }
    """
    classes = np.unique(y_train)
    weights = {}
    n_features = X_train.shape[1]
    for classe in classes:
        theta = np.zeros(n_features)
        weights[classe] = theta
    return classes, weights

def sigmoid(z: np.ndarray) -> np.ndarray:
    return 1 / (1 + np.exp(-z))

def gradient_descent(X_train: np.ndarray,
                    y_train: np.ndarray,
                    weights: dict,
                    classes: np.ndarray,
                    alpha: float = 0.1,
                    epochs: int = 1000) -> dict:
    """
    Args:
        X_train : (n_samples, n_features)
        y_train : (n_samples,)
        weights : dict { maison: θ } — initialisé par init_logreg_ovr
        classes : array des 4 maisons
        alpha   : learning rate
        epochs  : nombre d'itérations
    Returns:
        weights : dict { maison: θ } — mis à jour
    """

    for classe in classes:
        y_true = (y_train == classe).astype(int)

        w_train = weights[classe]

        m = X_train.shape[0]

        for i in range(epochs):
            z = X_train.dot(w_train)
            y_hat = sigmoid(z)
            Loss = - np.mean(y_true * np.log(y_hat) + (1 - y_true) * np.log(1 - y_hat))
            gradient = X_train.T.dot(y_hat - y_true) / m
            w_train = w_train - alpha * gradient
        
        weights[classe] = w_train
    
    return weights


def predict(X_test: np.ndarray,
            weights: dict,
            classes: np.ndarray) -> np.ndarray:
    """
    Args:
        X_test  : (n_samples, n_features)
        weights : dict { maison: θ }
        classes : array des 4 maisons
    Returns:
        y_pred  : (n_samples,) — maison prédite pour chaque étudiant
    """
    proba = np.zeros((X_test.shape[0], 4))
    for i in range(classes.shape[0]):
        proba[:, i] = sigmoid(X_test.dot(weights[classes[i]]))
    y_pred = classes[np.argmax(proba, axis=1)]
    return y_pred

def evaluate(y_pred: np.ndarray,
             y_test: np.ndarray) -> float:
    """
    Args:
        y_pred : (n_samples,) — maisons prédites
        y_test : (n_samples,) — maisons réelles
    Returns:
        accuracy : float entre 0 et 1
    """
    return np.mean(y_pred == y_test)




df      = pd.read_csv("datasets/dataset_train.csv")
X       = df.select_dtypes(include=[np.number]).fillna(0).values
y       = df["Hogwarts House"].values

X_train, X_test, y_train, y_test = train_test_split(X, y)
classes, weights                 = init_logreg_ovr(X_train, y_train)
weights                          = gradient_descent(X_train, y_train, weights, classes)
y_pred                           = predict(X_test, weights, classes)
accuracy                         = evaluate(y_pred, y_test)

print(f"Accuracy : {accuracy:.2%}")