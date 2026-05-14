# utils/math_utils.py

def count(values):
    total = 0
    for _ in values:
        total += 1
    return total

def mean(values):
    return sum(values) / count(values)

def std(values):
    m = mean(values)
    variance = 0
    for x in values:
        variance += (x - m) ** 2
    variance /= count(values)
    return variance ** 0.5

def minimum(values):
    m = values[0]
    for x in values:
        if x < m:
            m = x
    return m

def maximum(values):
    m = values[0]
    for x in values:
        if x > m:
            m = x
    return m

def percentile(values, p):
    sorted_vals = sorted(values)
    n = count(sorted_vals)
    
    index = (p / 100) * (n - 1)
    
    lower = int(index)
    upper = lower + 1
    fraction = index - lower
    
    if upper >= n:
        return sorted_vals[-1]
    
    return sorted_vals[lower] + fraction * (sorted_vals[upper] - sorted_vals[lower])
