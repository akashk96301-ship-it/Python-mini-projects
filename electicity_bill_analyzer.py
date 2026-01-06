def unit_category(unit):
    if unit < 50:
        return "Low usage"
    elif 50 <= unit <= 150:
        return "Normal usage"
    else:
        return "High usage"

def bill_calculation(units):
    bill = 0
    if units > 150:
        bill += 50 * 5
        bill += 100 * 8
        bill += (units - 150) * 10
    elif units > 50:
        bill += 50 * 5
        bill += (units - 50)* 8
    else:
        bill += units * 5
    return bill
def bill_status(bill):
    if bill < 1000:
        return "Affordable"
    elif 1000 <= bill <= 2500:
        return "Expensive"
    else:
        return "Very expensive"

def electicity_bill_analyzer(customers):
    result = {}
    for name, bill in customers.items():
        category = unit_category(bill)
        calculate_bill = bill_calculation(bill)
        status = bill_status(calculate_bill)
        result[name] = {"Units" : bill, "Usage_type" : category, "Bill_amount" : calculate_bill, "Status" : status}
    return result
customers = {
    "Akash": 120,
    "Ravi": 80,
    "Neha": 250,
    "Aman": 40
}
print(electicity_bill_analyzer(customers))