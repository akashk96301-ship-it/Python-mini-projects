def get_temperature_type(temperature):
    if temperature < 15:
        return "Cold"
    elif 15 <= temperature <= 30:
        return "Moderate"
    elif temperature > 30:
        return "Hot"

def get_rainfall_category(rainfall):
    if rainfall == 0:
        return "No Rain"
    elif rainfall < 20:
        return "Light Rain"
    elif 20 <= rainfall <= 50:
        return "Moderate Rain"
    else:
        return "Heavy Rain"

def get_climate_condition(temperature,rainfall):
    temp = get_temperature_type(temperature)
    rain = get_rainfall_category(rainfall)
    if temp == "Hot" and rain == "No Rain":
        return "Dry Heat"
    elif temp == "Hot" and rain == "Heavy Rain":
        return "Humid"
    elif temp == "Cold" and rain == "No Rain":
        return "Cold & Dry"
    elif temp == "Moderate" and (rain == "Light Rain" or rain == "Moderate Rain"):
        return "Pleasant"
    else:
        return "Unstable"

def get_alert_status(temperature,rainfall):
    temp = get_temperature_type(temperature)
    rain = get_rainfall_category(rainfall)
    if rain == "Heavy Rain":
        return "Flood Alert"
    elif temperature > 40:
        return "Heat Alert"
    elif temp == "Cold" and rain == "No Rain":
        return "Cold Wave Alert"
    else:
        return "Normal"

def weather_data_analyzer(weather):
    result = {}
    for day , details in weather.items():
        temperature = details["temperature"]
        rainfall = details["rainfall"]
        temp_type = get_temperature_type(temperature)
        rain_type = get_rainfall_category(rainfall)
        climate = get_climate_condition(temperature, rainfall)
        alert = get_alert_status(temperature, rainfall)
        result[day] = {"Temperature" : temperature, "Rainfall" : rainfall, "Temp Type" : temp_type, "Rain Type" : rain_type, "Climate" : climate, "Alert" : alert}
    return result
weather_data = {
    "Day1": {"temperature": 18, "rainfall": 5},
    "Day2": {"temperature": 35, "rainfall": 0},
    "Day3": {"temperature": 28, "rainfall": 40},
    "Day4": {"temperature": 10, "rainfall": 0},
    "Day5": {"temperature": 42, "rainfall": 60}
}
print(weather_data_analyzer(weather_data))