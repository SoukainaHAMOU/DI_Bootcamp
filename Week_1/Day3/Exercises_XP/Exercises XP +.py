#Exercise 1 : Student Grade Summary
student_averages = {}
student_grades = {
    "Alice": [88, 92, 100],
    "Bob": [75, 78, 80],
    "Charlie": [92, 90, 85],
    "Dana": [83, 88, 92],
    "Eli": [78, 80, 72]
}

#for i in student_grades:
    
#1
for key, value in student_grades.items() :
    marks = student_grades[key]
    average_mark = round(sum(marks)/len(marks),2)    
    student_averages[key] = {"average": average_mark}
    print(average_mark)
print(student_averages)
#2


for key, value in student_averages.items():
    avg = value["average"]
    if avg >= 90:
        value["grade"] = "A"
    elif avg >= 80:
        value["grade"] = "B"
    elif avg >= 70:
        value["grade"] = "C"
    elif avg >= 60:
        value["grade"] = "D"
    else:
        value["grade"] = "F"
print(student_averages)
print("\n Student Report:")
for name, info in student_averages.items():
    print(f"{name}: Average = {info['average']}, Grade = {info['grade']}")

