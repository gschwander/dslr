import sys
from utils.data_loader import load_csv, get_numeric_columns
from utils.math_utils import count, mean, std, minimum, maximum, percentile

def describe(filepath):
    
    # ── 1. Charger les données ──────────────────────
    headers, data = load_csv(filepath)
    numeric = get_numeric_columns(headers, data)

    # ── 2. Les métriques à calculer ────────────────
    metrics = ['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max']

    # ── 3. Affichage header ─────────────────────────
    col_width = 12
    cols = list(numeric.keys())
    
    print(' ' * 8, end='')
    for col in cols:
        print(f'{col:>{col_width}}', end='')
    print()

    # ── 4. Calculer et afficher chaque métrique ─────
    for metric in metrics:
        print(f'{metric:<8}', end='')
        
        for col in cols:
            values = numeric[col]
            
            if metric == 'count':
                result = count(values)
            elif metric == 'mean':
                result = mean(values)
            elif metric == 'std':
                result = std(values)
            elif metric == 'min':
                result = minimum(values)
            elif metric == '25%':
                result = percentile(values, 25)
            elif metric == '50%':
                result = percentile(values, 50)
            elif metric == '75%':
                result = percentile(values, 75)
            elif metric == 'max':
                result = maximum(values)
            
            print(f'{result:>{col_width}.4f}', end='')
        print()

# ── 5. Point d'entrée ───────────────────────────────
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python describe.py dataset_train.csv')
        sys.exit(1)
    
    describe(sys.argv[1])
