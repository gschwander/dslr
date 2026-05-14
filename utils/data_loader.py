import csv

def load_csv(filepath):
    """Lit un CSV et retourne headers + données"""
    with open(filepath, 'r') as f:
        reader = csv.reader(f)
        headers = next(reader)
        data = []
        for row in reader:
            data.append(row)
    return headers, data

def get_numeric_columns(headers, data):
    """
    Identifie et retourne uniquement les colonnes numériques
    Ignore les NaN
    """
    numeric = {}
    for i, col in enumerate(headers):
        values = []
        for row in data:
            try:
                val = float(row[i])
                values.append(val)
            except:
                pass  # On ignore NaN et strings
        if values:
            numeric[col] = values
    return numeric
