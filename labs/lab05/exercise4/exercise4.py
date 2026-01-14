import math

def filter_query_times(times):
    """
    Remove slow outliers (mean + std deviation) and return sorted times.
    """

    if not times:
        return []

    mean = sum(times) / len(times)
    variance = sum((x - mean)**2 for x in times) / len(times)
    std_dev = math.sqrt(variance)
    upper_limit = mean + std_dev

    result = []
    for x in times:
        if x <= upper_limit:  # keep only non-outliers
            result.append(x)

    return sorted(result)

    
# Test
query_times = [45, 52, 48, 180, 51, 47, 50, 12]
result = filter_query_times(query_times)
print(f"Filtered Times: {result}")  
# Expected: [12, 45, 47, 48, 50, 51, 52]
