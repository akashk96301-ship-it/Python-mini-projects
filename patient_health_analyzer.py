def get_average_heart_rate(heart_rates):
    if not heart_rates:
        return 0
    total = 0
    for hr in heart_rates:
        total += hr
    return round(total / len(heart_rates), 2)

def get_average_bp(bp_list):
    if not bp_list:
        return 0
    total = 0
    for bp in bp_list:
        total += bp
    return round(total / len(bp_list), 2)

def get_heart_status(avg_hr):
    if avg_hr == 0:
        return "No Data"
    elif avg_hr < 60:
        return "Low"
    elif avg_hr <= 100:
        return "Normal"
    else:
        return "High"

def get_bp_status(avg_bp):
    if avg_bp == 0:
        return "No Data"
    if avg_bp < 120:
        return "Normal"
    elif avg_bp <= 139:
        return "Elevated"
    else:
        return "High"

def get_risk_level(age, diabetes, hr_status, bp_status):
    if age >= 60 and diabetes:
        return "High Risk"
    elif hr_status == "High" or bp_status == "High":
        return "Medium Risk"
    else:
        return "Low Risk"

def get_alert_message(risk):
    if risk == "High Risk":
        return "Immediate Attention"
    elif risk == "Medium Risk":
        return "Monitor Regularly"
    else:
        return "Stable"
    
def patient_health_analyzer(patients):
    result = {}
    for patient ,details in patients.items():
        age = details["age"]
        heart_rates = details["heart_rate"]
        bp_list = details["bp"]
        diabetes = details["diabetes"]

        avg_hr = get_average_heart_rate(heart_rates)
        avg_bp = get_average_bp(bp_list)

        hr_status = get_heart_status(avg_hr)
        bp_status = get_bp_status(avg_bp)

        risk = get_risk_level(age, diabetes,hr_status,bp_status)
        alert = get_alert_message(risk)

        result[patient] = {"Avg_Heart_Rate" : avg_hr, "Avg_BP" : avg_bp, "Heart_Status" : hr_status, "BP_Status" : bp_status, "Risk" : risk, "Alert" : alert}
    return result

patients = {
    "Patient1": {
        "age": 45,
        "heart_rate": [72, 75, 78, 80],
        "bp": [120, 130, 125],   # systolic BP readings
        "diabetes": True
    },
    "Patient2": {
        "age": 30,
        "heart_rate": [65, 60, 58],
        "bp": [110, 108],
        "diabetes": False
    },
    "Patient3": {
        "age": 70,
        "heart_rate": [],
        "bp": [],
        "diabetes": True
    }
}
print(patient_health_analyzer(patients))