# utils/normalizer.py

def normalize(X):
    """
    X = liste de listes (chaque ligne = un élève)
    
    Retourne :
    - X_norm  : données normalisées
    - means   : moyenne de chaque colonne
    - stds    : std de chaque colonne
    (on garde means et stds pour normaliser les données de test)
    """
    
    n_features = len(X[0])
    
    # ── 1. Calculer mean et std de chaque colonne ──
    means = []
    stds  = []
    
    for j in range(n_features):
        col = [X[i][j] for i in range(len(X))]
        means.append(mean(col))
        stds.append(std(col))
    
    # ── 2. Appliquer la formule ────────────────────
    X_norm = []
    
    for row in X:
        norm_row = []
        for j in range(n_features):
            if stds[j] == 0:          # éviter division par 0
                norm_row.append(0.0)
            else:
                norm_row.append((row[j] - means[j]) / stds[j])
        X_norm.append(norm_row)
    
    return X_norm, means, stds
