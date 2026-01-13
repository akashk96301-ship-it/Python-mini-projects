def get_total_units(daily_units):
    if not daily_units:
        return 0
    total = 0
    for units in daily_units:
        total += units
    return total

def get_average_units(daily_units):
    if not daily_units:
        return 0
    total = get_total_units(daily_units)
    average = total / len(daily_units)
    return round(average, 2)

def get_consumption_level(avg_units):
    if avg_units >= 30:
        return "Very High"
    elif 20 <= avg_units <= 29:
        return "High"
    elif 10 <= avg_units <= 19:
        return "Medium"
    else:
        return "Low"

def get_electricity_cost(total_units):
    cost = total_units * 6
    return cost

def get_efficiency_status(avg_units, solar_installed):
    if solar_installed and avg_units < 20:
        return "Efficient"
    elif not solar_installed and avg_units >= 30:
        return "Inefficient"
    else:
        return "Normal"

def get_alert(avg_units):
    if avg_units >= 35:
        return "Overuse Alert"
    elif avg_units < 10:
        return "Underuse"
    else:
        return "Normal Usage"

def energy_usage_analyzer(homes):
    result = {}
    for home, details in homes.items():
        units = details["daily_units"]
        solar = details["solar_installed"]
        total_units = get_total_units(units)
        average_units = get_average_units(units)
        consumption_level = get_consumption_level(average_units)
        cost = get_electricity_cost(total_units)
        efficiency = get_efficiency_status(average_units, solar)
        alert = get_alert(average_units)
        result[home] = {"Total_Units" : total_units, "Average_Units" : average_units, "Consumption_Level" : consumption_level, "Cost" : cost, "Efficiency" : efficiency, "Alert" : alert}
    return result
homes = {
    "House1": {
        "daily_units": [12, 15, 10, 14, 13, 16, 18],
        "solar_installed": True
    },
    "House2": {
        "daily_units": [30, 28, 35, 40, 38],
        "solar_installed": False
    },
    "House3": {
        "daily_units": [],
        "solar_installed": False
    }
}

print(energy_usage_analyzer(homes))