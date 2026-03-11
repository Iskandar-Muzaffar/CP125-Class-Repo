# Lab 08 Exercise 3: Product Price Lookup
# Write your code below:
import csv

def calculate_order_total(products_file, order_file, output_file):
    """
    Calculate total cost for each product in order.

    Args:
        products_file: path to products CSV (product_id,product_name,price)
        order_file: path to order CSV (product_id,quantity)
        output_file: path to output CSV file

    Returns:
        float: grand total of all orders
    """
    # TODO: Implement this function

    files1 = open(products_file, 'r')
    files2 = open(order_file, 'r')
    output = open(output_file, 'w', newline='')

    product = csv.reader(files1)
    order = csv.reader(files2)
    writer = csv.writer(output)

    next(product)
    next(order)

    prices = {}


    for row in product:
        product_id = row[0]
        price = float(row[2])
        prices[product_id] = price

    writer.writerow(["product_id", "total_cost"])

    grand_total = 0

    for row in order:
        product_id = row[0]
        quantity = int(row[1])

        total_cost = prices[product_id] * quantity
        grand_total += total_cost

        writer.writerow([product_id, f"{total_cost:.2f}"])


    files1.close()
    files2.close()
    output.close()

    return grand_total



# Test your code here
result = calculate_order_total("labs/lab08/exercise3/data/products.csv", "labs/lab08/exercise3/data/order.csv", "labs/lab08/exercise3/data/total.csv")
print(f"Grand total: ${result:.2f}")
