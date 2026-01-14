
def was_backward_detected(waypoints):
    
    for i in range(1, len(waypoints)):
        if (waypoints[i][0] < waypoints[i - 1][0] or waypoints[i][1] < waypoints[i - 1][1]):
            return True
    return False


    """
    Return True if drone moved backward in x or y, False otherwise.
    Use tuple unpacking.
    """



# Test
path = ((0, 0, 10), (5, 5, 12), (4, 6, 10), (10, 10, 15))
result = was_backward_detected(path)
print(f"Backward Movement: {result}")  # Expected: True
