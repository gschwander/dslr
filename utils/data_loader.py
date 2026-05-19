# utils/data_loader.py

def load_csv(filepath):
    """
    Retourne :
    - headers : liste des noms de colonnes
    - data    : liste de listes (chaque ligne = un élève)
    """
    headers = []
    data    = []

    with open(filepath, 'r') as f:
        lines = f.readlines()

    # Première ligne = headers
    headers = lines[0].strip().split(',')

    # Reste = données
    for line in lines[1:]:
        row = line.strip().split(',')
        data.append(row)

    return headers, data


def get_numeric_columns(headers, data):
    """
    Retourne un dict :
    {
        'Astronomy' : [98.5, 72.1, ...],
        'Potions'   : [71.0, 85.3, ...],
        ...
    }
    Ignore les colonnes non-numériques et les NaN
    """
    numeric = {}

    for j, col_name in enumerate(headers):
        values = []
        for row in data:
            val = row[j]
            if val == '' or val == 'NA' or val == 'nan':
                continue
            try:
                values.append(float(val))
            except ValueError:
                break   # colonne non-numérique, on skip
        else:
            if values:
                numeric[col_name] = values

    return numeric

def fill_missing_values(headers, data):
    # Pour chaque colonne numérique
    # on remplace les NaN par la moyenne de cette colonne
    
    for col_idx, header in enumerate(headers):
        # Étape 1 : collecter toutes les valeurs valides de cette colonne
        valid_vals = []
        for row in data:
            try:
                val = float(row[col_idx])
                valid_vals.append(val)
            except:
                pass  # on ignore les NaN et les strings
        
        # Étape 2 : si pas de valeur valide, on skip
        if len(valid_vals) == 0:
            continue
        
        # Étape 3 : calculer la moyenne
        col_mean = sum(valid_vals) / len(valid_vals)
        
        # Étape 4 : remplacer les valeurs manquantes par la moyenne
        for row in data:
            try:
                float(row[col_idx])
            except:
                row[col_idx] = str(col_mean)  # on remplace
    
    return data
