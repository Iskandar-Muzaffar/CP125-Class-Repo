# Lab 02 Exercise 1: Road Trip Budgeter
# Write your code below:

def is_budget_sufficient(one_way_km, km_per_liter, price_per_liter, budget):

    fuel = ( one_way_km*2 ) / km_per_liter
    total_cost = fuel * price_per_liter
    
    if budget >= total_cost:
        return True
    else:
        return False
    

    # TODO: Implement this function
    # Calculate round trip cost and checks if within budget

# Test your code here
#

