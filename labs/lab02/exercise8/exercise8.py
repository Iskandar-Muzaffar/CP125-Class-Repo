# Lab 02 Exercise 8: Bouncing Ball Simulation
# Write your code below:

def calculate_bounce_height(current_height):
    """Calculate next bounce height (80% of current)."""
    # TODO: Implement this function
    return current_height * 0.80


def is_ball_stopped(height):
    """Return True if height < 1, False otherwise."""
    # TODO: Implement this function
    return height < 1
    

def simulate_bouncing_ball(start_height):
    """
    Simulate bouncing ball.
    Returns: (bounce_count, total_distance)
    """
    # TODO: Implement using calculate_bounce_height and is_ball_stopped
    height = start_height
    total_distance = 0
    bounce = 0

    while not is_ball_stopped(height):
        total_distance += height
        height = calculate_bounce_height(height)
        total_distance += height
        bounce += 1

    return bounce, total_distance
# Test your code here
print("Testing Bouncing Ball Simulation...")
