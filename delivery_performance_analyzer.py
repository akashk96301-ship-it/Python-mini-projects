def get_total_deliveries(deliveries):
    if not deliveries:
        return 0
    total = 0
    for delivery in deliveries:
        total += delivery
    return total

def get_average_deliveries(deliveries):
    if not deliveries:
        return 0
    total = get_total_deliveries(deliveries)
    average = total / len(deliveries)
    return average

def get_delivery_level(avg):
    if avg >= 20:
        return "Outstanding"
    elif avg >= 10:
        return "Good"
    else:
        return "Poor"

def get_penalty(delays):
    return delays * 500

def get_risk_status(delays):
    if delays >= 3:
        return "High Risk"
    elif delays >= 1:
        return "Medium Risk"
    else:
        return "Low Risk"

def get_final_status(level, risk, total):
    if total == 0:
        return 0
    if level == "Outstanding" and risk == "Low Risk":
        return "Top Performer"
    elif risk == "High Risk":
        return "Needs Warning"
    else:
        return "Average Performer"

def delivery_performance_analyzer(drivers):
    result = {}
    for driver, details in drivers.items():
        deliveries = details["deliveries"]
        delays = details["delays"]
        total = get_total_deliveries(deliveries)
        average = get_average_deliveries(deliveries)
        level = get_delivery_level(average)
        penalty = get_penalty(delays)
        risk = get_risk_status(delays)
        status = get_final_status(average,risk,total)
        result[driver] = {"Total_Deliveries" : total, "Average_Deliveries" : average, "Level" : level, "Penalty" : penalty, "Risk" : risk, "Status" : status}
    return result

drivers = {
    "Akash": {
        "deliveries": [12, 15, 14, 10],
        "delays": 1,
        "distance": 320
    },
    "Ravi": {
        "deliveries": [5, 6],
        "delays": 3,
        "distance": 90
    },
    "Neha": {
        "deliveries": [20, 18, 22],
        "delays": 0,
        "distance": 540
    },
    "Aman": {
        "deliveries": [],
        "delays": 0,
        "distance": 0
    }
}

print(delivery_performance_analyzer(drivers))