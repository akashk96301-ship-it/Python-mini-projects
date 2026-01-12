def get_total_visits(visits):
    if not visits:
        return 0
    total = 0
    for visit in visits:
        total += visit
    return total

def get_average_visits(visits):
    if not visits:
        return 0
    total = get_total_visits(visits)
    average = total / len(visits)
    return average

def get_traffic_level(avg_visits):
    if avg_visits >= 1500:
        return "High Traffic"
    elif 700 <= avg_visits <= 1499:
        return "Medium Traffic"
    else:
        return "Low Traffic"

def get_engagement_level(bounce_rate):
    if bounce_rate < 40:
        return "Highly Engaged"
    elif 40 <= bounce_rate <= 60:
        return "Moderately Engaged"
    else:
        return "Poor Engagement"

def get_site_status(avg_visits, bounce_rate):
    traffic = get_traffic_level(avg_visits)
    bounce = get_engagement_level(bounce_rate)
    if traffic == "High Traffic" and bounce == "Highly Engaged":
        return "Excellent"
    elif traffic == "Medium Traffic":
        return "Growing"
    elif traffic == "Low Traffic" and bounce == "Poor Engagement":
        return "Critical"
    else:
        return "Needs Improvement"

def website_traffic_analyzer(websites):
    result = {}
    for website ,details in websites.items():
        visits = details["visits"]
        bounce = details["bounce_rate"]
        total_visits = get_total_visits(visits)
        average = get_average_visits(visits)
        traffic_level = get_traffic_level(average)
        engagement = get_engagement_level(bounce)
        status = get_site_status(average, bounce)
        result[website] = {"Total visits" : total_visits, "Average visits" : average, "Traffic level" : traffic_level, "Engagement" : engagement, "Status" : status}
    return result
websites = {
    "Google": {
        "visits": [1200, 1500, 1800, 2000],
        "bounce_rate": 35
    },
    "MyBlog": {
        "visits": [200, 180, 220],
        "bounce_rate": 65
    },
    "ShopSite": {
        "visits": [800, 950, 1100, 1050],
        "bounce_rate": 45
    },
    "NewSite": {
        "visits": [],
        "bounce_rate": 80
    }
}
print(website_traffic_analyzer(websites))