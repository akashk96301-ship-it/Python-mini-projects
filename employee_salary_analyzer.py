def get_annual_salary(monthly_salary):
    return monthly_salary * 12

def get_bonus(monthly_salary, attendance, overtime):
    annual_salary = get_annual_salary(monthly_salary)
    if attendance >= 26 and overtime >= 10:
        return annual_salary * 0.15
    elif attendance >= 22:
        return annual_salary * 0.10
    elif attendance >= 18:
        return annual_salary * 0.05
    else:
        return 0

def get_salary_status(annual_salary,bonus):
    if annual_salary >= 500000 and bonus > 0:
        return "Excellent"
    elif annual_salary >= 300000:
        return "Good"
    else:
        return "Average"

def get_status(attendance):
    if attendance < 18:
        return "At risk"
    else:
        return "Stable"

def employee_salary_analyzer(employees):
    result = {}
    for name, details in employees.items():
        salary = details["salary"]
        attendance = details["attendance"]
        overtime = details["overtime"]
        annual = get_annual_salary(salary)
        bonus = get_bonus(salary,attendance,overtime)
        peformance = get_salary_status(annual, bonus)
        final_salary = annual + bonus
        status = get_status(attendance)
        result[name] = {"Annual_salary" : annual, "Bonus" : bonus, "Performance" : peformance, "Final_salary" : final_salary, "Status" : status}
    return result
employees = {
    "Akash":  {"salary": 30000, "attendance": 26, "overtime": 12},
    "Ravi":   {"salary": 18000, "attendance": 20, "overtime": 5},
    "Neha":   {"salary": 45000, "attendance": 28, "overtime": 20},
    "Aman":   {"salary": 15000, "attendance": 15, "overtime": 0},
}
print(employee_salary_analyzer(employees))