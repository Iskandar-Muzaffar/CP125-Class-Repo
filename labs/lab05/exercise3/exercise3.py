
def find_bottleneck_index(traceroute):
    
    """
    Find the index of the hop where the largest latency jump begins.
    """

    largest_latency = 0
    bottleneck_index = 0

    for i in range (1, len(traceroute)):
        if traceroute[i][1] - traceroute[i-1][1] > largest_latency:
            largest_latency = traceroute[i][1] - traceroute[i-1][1]
            bottleneck_index = i-1

    return bottleneck_index 


   

   


# Test
traceroute = ((1, 5), (2, 8), (3, 45), (4, 48), (5, 50))
result = find_bottleneck_index(traceroute)
print(f"Bottleneck Index: {result}")  # Expected: 1
