def get_average_score(scores):
    if not scores:
        return 0
    total = 0
    for score in scores:
        total += score
    average = total / len(scores)
    return round(average, 2)

def get_performance_level(avg_score):
    if avg_score >= 90:
        return "Excellent"
    elif 75 <= avg_score <= 89:
        return "Good"
    elif 50 <= avg_score <= 74:
        return "Average"
    else:
        return "Poor"

def get_engagement_level(hours_spent):
    if hours_spent >= 50:
        return "High"
    elif 20 <= hours_spent <= 49:
        return "Medium"
    else:
        return "Low"

def get_completion_status(completed):
    if completed == True:
        return "Completed"
    else:
        return "Incomplete"

def get_final_recommendation(avg_score, completed):
    if completed and avg_score >= 80:
        return "Promote"
    elif completed and avg_score < 80:
        return "Improve"
    else:
        return "At Risk"

def course_performance_analyzer(students):
    result = {}
    for name, details in students.items():
        scores = details["scores"]
        hour = details["hours_spent"]
        completed = details["completed"]
        average = get_average_score(scores)
        performance = get_performance_level(average)
        engagement = get_engagement_level(hour)
        complete = get_completion_status(completed)
        recommendation = get_final_recommendation(average,completed)
        result[name] = {"Average_scores" : average, "Performance" : performance, "Engagement" : engagement, "Completion" : complete, "Recommendation" : recommendation}
    return result
students = {
    "Akash": {
        "scores": [78, 85, 90, 88],
        "completed": True,
        "hours_spent": 45
    },
    "Ravi": {
        "scores": [45, 50, 40],
        "completed": False,
        "hours_spent": 20
    },
    "Neha": {
        "scores": [92, 95, 94, 96],
        "completed": True,
        "hours_spent": 60
    },
    "Aman": {
        "scores": [],
        "completed": False,
        "hours_spent": 5
    }
}
print(course_performance_analyzer(students))