def calculate(results, target):
    for i in results:
        if target != i["subject"]:
            return 0
        else:
            b


data = [
    {"name": "Ali", "subject": "Math", "score": 80},
    {"name": "Sara", "subject": "Math", "score": 90},
    {"name": "Ali", "subject": "History", "score": 70}
]
target = "Math"

output = calculate(data, target)
print (output)

