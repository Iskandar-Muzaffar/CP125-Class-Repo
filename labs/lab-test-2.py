#ISKANDAR'S CODE
#CREATING A PROGRAM THAT GIVES NUMBER IN ASCENDING ORDER, SUM AND LARGEST NUMBER


def ascending_number(number):

    ascending_number = sorted(number)

    return ascending_number

def calculate_sum_of_number(number):

    sum_numbers = sum(number)

    return sum_numbers

def determine_largest_number(number):

    largest_number = max(number)

    return largest_number
    


number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))
number3 = int(input("Enter number 3: "))
number4 = int(input("Enter number 4: "))
number5 = int(input("Enter number 5: "))

result = (number1,number2,number3,number4,number5)

result1 = ascending_number(result)
print(f"Number in ascending order: {result1}")

result2 = calculate_sum_of_number(result)
print(f"Sum of all numbers: {result2}")

result3 = determine_largest_number(result)
print(f"Largest Number: {result3}")






