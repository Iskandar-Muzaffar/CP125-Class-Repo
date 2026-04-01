import pandas as pd

def explore_data(filename):
    df = pd.read_csv(filename)

    total_students = len(df)
    subjects = ['Maths', 'Science','English']
    math_average = df['Math'].mean()
    highest_math_student = df.loc[df['Math'].idxmax(), 'Name']

    result = {
        'total_students': total_students,
        'subjects': subjects,
        'math_average': math_average,
        'highest_math_student': highest_math_student
    }
    
    return result

result = explore_data("labs/lab09/data/students.csv")
print(result)