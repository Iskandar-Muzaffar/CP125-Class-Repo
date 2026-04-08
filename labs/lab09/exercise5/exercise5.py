import pandas as pd

def high_performers(filename):
    df = pd.read_csv(filename)

    exceptional_students = df[
        (df['Math'] > 85) &
        (df['Science'] > 85) &
        (df['English'] > 85) &
        (df['Physics'] > 85) &
        (df['Chemistry'] > 85)
    ]

    high_performers_set = set(exceptional_students['Name'])

    result = {
        "count": len(high_performers_set),
        "names": high_performers_set
    }

    return result


result = high_performers("labs/lab09/data/students.csv")
print(result)