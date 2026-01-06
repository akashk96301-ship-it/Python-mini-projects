def get_total_marks(marks):
    total = 0
    for mark in marks:
        total += mark
    return total

def get_percentage(marks):
    total = 0
    for mark in marks:
        total += mark
        max_marks = len(marks) * 100
    percentage = (total / max_marks) * 100
    return round(percentage,2)

def get_result(pecentage):
    if pecentage >= 60:
        return "Pass"
    else:
        return "Fail"

def get_grade(percentage):
    if percentage >= 90:
        return "A"
    elif 75 <= percentage <= 89:
        return "B"
    elif 60 <= percentage <= 74:
        return "C"
    elif 40 <= percentage <= 59:
        return "D"
    else:
        return "F"

def get_performance_level(percentage):
    if percentage >= 85:
        return "Excellent"
    elif 60 <= percentage <= 84:
        return "Good"
    else:
        return "Poor"

def student_performance_analyzer(students):
    student = {}
    for name, marks in students.items():
        total = get_total_marks(marks)
        percentage = get_percentage(marks)
        result = get_result(percentage)
        grade = get_grade(percentage)
        performance = get_performance_level(percentage)
        student[name] = {"Total" : total, "Percentage" : percentage, "Result" : result, "Grade" : grade, "Performance" : performance}
    return student
students = {
    "Akash": [78, 85, 90, 66, 72],
    "Ravi": [45, 55, 60, 40, 50],
    "Neha": [95, 92, 88, 91, 94],
    "Aman": [30, 35, 25, 40, 20]
}
print(student_performance_analyzer(students))