# Lab 08 Exercise 4: Student Grade Calculator
# Write your code below:

import csv

def calculate_final_grades(input_file, output_file):
    """
    Calculate final grades from midterm and final scores.

    Args:
        input_file: path to scores CSV (student_id,midterm,final)
        output_file: path to output CSV file

    Returns:
        float: average of all final grades
    """
    # TODO: Implement this function
    file = open(input_file,'r')
    output = open(output_file,'w', newline='')

    exam = csv.reader(file)
    writer = csv.writer(output)

    next(exam)

    total_grades = []
    writer.writerow(['student_id', 'final_grade'])

    for row in exam:
        student_id = row[0]
        midterm = float(row[1])
        final = float(row[2])

        final_grade = (midterm * 0.4) + (final * 0.6)
        total_grades.append(final_grade)

    writer.writerow([student_id, f"{final_grade:.2f}"])

    file.close()
    output.close()

    average = sum(total_grades) / len(total_grades)

    return average

# Test your code here
result = calculate_final_grades("labs/lab08/exercise4/data/scores.csv", "labs/lab08/exercise4/data/grades.csv")
print(f"Average final grade: {result:.2f}")
