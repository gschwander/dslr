import math

# ─── STATISTIQUES ───────────────────────────────────

def count(values):
    return len(values)

def mean(values):
    return sum(values) / len(values)

def std(values):
    m = mean(values)
    variance = sum((x - m) ** 2 for x in values) / len(values)
    return math.sqrt(variance)

def minimum(values):
    m = values[0]
    for v in values:
        if v < m:
            m = v
    return m

def maximum(values):
    m = values[0]
    for v in values:
        if v > m:
            m = v
    return m

def percentile(values, p):
    """Calcule le percentile p (ex: 25, 50, 75)"""
    sorted_vals = sorted(values)
    n = len(sorted_vals)
    index = (p / 100) * (n - 1)
    lower = int(index)
    upper = lower + 1
    if upper >= n:
        return sorted_vals[lower]
    # Interpolation linéaire
    fraction = index - lower
    return sorted_vals[lower] + fraction * (sorted_vals[upper] - sorted_vals[lower])

# ─── MACHINE LEARNING ───────────────────────────────

# def sigmoid(z):
#     return 1 / (1 + math.exp(-z))

# def sigmoid_vector(z_list):
#     return [sigmoid(z) for z in z_list]

# def dot_product(theta, x):
#     """θᵀx"""
#     return sum(t * xi for t, xi in zip(theta, x))
