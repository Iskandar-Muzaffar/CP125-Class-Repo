import csv

def calculate_average(file):

    file = open(file,'r', newline='')
    reader = csv.reader(file)

    next(reader)

    total = 0
    count = 0

    for row in reader:
        print(row)
        total += float(row[1])
        count += 1

    file.close()

    average = total / count
    print (f'Total Average: {average}')

def add_data(new_file):

    gender = input("Enter Gender:" )
    height = input("Enter Height:" )
    weight = input("Enter Weight:" )
    bmi = input("Enter BMI:" )

    file = open(new_file,'a', newline='')
    writer = csv.writer(file)

    writer.writerow([gender,height,weight,bmi])

    file.close()

    file = open(new_file,'r', newline='')
    reader = csv.reader(file)

    for row in reader:
        print(row)
    file.close()
   
calculate_average("labs/bmi.csv")
add_data("labs/bmi.csv")