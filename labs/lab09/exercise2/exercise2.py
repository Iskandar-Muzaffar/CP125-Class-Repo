import pandas as pd

def compare_averages(filename):
    df = pd.read_csv(filename)
    
    subjects = ['Math', 'Science', 'English']
    
    # Calculate averages
    averages = {
        'Math': round(df['Math'].mean(), 1),
        'Science': round(df['Science'].mean(), 1),
        'English': round(df['English'].mean(), 1)
    }
    
    # Determine best and worst subject
    best_subject = df[subjects].mean().idxmax()
    worst_subject = df[subjects].mean().idxmin()
    
    # Combine into a single dictionary
    result = {
        'averages': averages,
        'best_subject': best_subject,
        'worst_subject': worst_subject
    }
    
    return result

result = compare_averages("labs/lab09/data/students.csv")
print(result)