# Lab 02 Exercise 2: Camping Logistics
# Write your code below:

import math

def calculate_event_cost(participants, tent_capacity, tent_price, meal_price):

    cost_of_tent = math.ceil(participants / tent_capacity) * tent_price
    cost_of_food = participants * meal_price
    total_cost =  cost_of_tent + cost_of_food

    return total_cost


    # TODO: Implement this function
    # Calculate total cost for tents and meals
    pass

# Test your code here
print("Testing Camping Logistics...")
