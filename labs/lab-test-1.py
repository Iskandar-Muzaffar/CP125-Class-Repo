# Iskandar
# Determine student grade 

def determine_grade(mark):
    if mark> 80:
        return "A"
    elif 60 < mark < 79:
        return "B"
    elif 50 < mark < 59:
        return "C"
    elif 40 < mark < 49:
        return "D"
    else:
        return "F"

mark = int(input("Enter the student's mark: "))
print(f"Mark: {mark:.1f}") 
results = determine_grade(mark)
print(f"Grade: {results}")
