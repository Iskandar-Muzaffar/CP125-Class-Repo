# Lab 08 Exercise 5: Sales Summary
# Write your code below:
import csv

def summarize_sales(input_file, output_file):
    """
    Calculate sales statistics: total, average, highest, and lowest revenue.

    Args:
        input_file: path to sales CSV (product,quantity,price)
        output_file: path to output text file

    Returns:
        tuple: (total, average, highest, lowest)
    """
    # TODO: Implement this function
    
    input = open(input_file,'r')
    output = open(output_file,'w', newline='')

    sales = csv.reader(input)
    

    next(sales)


    for row in sales:
        



    



# Test your code here
result = summarize_sales("labs/lab08/exercise5/data/sales.csv", "labs/lab08/exercise5/data/summary.txt")
print(f"Total: ${result[0]:.2f}, Avg: ${result[1]:.2f}, High: ${result[2]:.2f}, Low: ${result[3]:.2f}")
