import pandas as pd

def compare_averages(filename):
    df = pd.read_csv(filename)
    
    subjects = ['Math', 'Science', 'English']
    

result = compare_averages("labs/lab09/data/students.csv")
print(result)