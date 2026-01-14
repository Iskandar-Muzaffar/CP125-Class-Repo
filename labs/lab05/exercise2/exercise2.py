
def find_largest_drop(readings):

    maximum_single_drop = 0.0

    for i in range (1, len(readings)):
        if readings[i-1] - readings[i] > maximum_single_drop:
            maximum_single_drop = readings[i-1] - readings[i]

    return abs(maximum_single_drop)
        
    return 0.0


    """
    Return the largest consecutive temperature drop, or 0.0 if none.
    """
    pass


# Test
temps = (32.5, 31.0, 31.5, 28.0, 24.5)
result = find_largest_drop(temps)
print(f"Largest Drop: {result}")  # Expected: 3.5
