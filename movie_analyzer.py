def get_total_rating(ratings):
    if not ratings:
        return 0
    total = 0
    for rate in ratings:
        total += 1
    return total

def get_average_rating(ratings):
    if not ratings:
        return 0
    count = get_total_rating(ratings)
    total = 0
    for rate in ratings:
        total += rate
    average = total/count
    return round(average,2)

def get_popularity(avg_rating):
    if avg_rating >= 4.5:
        return "Blockbuster"
    elif avg_rating >= 3.5:
        return "Popular"
    elif avg_rating >= 2.5:
        return "Average"
    else:
        return "Flop"

def get_viewer_reaction(avg_rating):
    if avg_rating >= 4:
        return "Loved"
    elif avg_rating >= 3:
        return "Liked"
    else:
        return "Disliked"

def get_recommendation(avg_rating):
    if avg_rating >= 4:
        return "Recommended"
    else:
        return "Not Recommended"

def movie_analyzer(movies):
    result = {}
    for name, ratings in movies.items():
        total = get_total_rating(ratings)
        average = get_average_rating(ratings)
        popularity = get_popularity(average)
        reaction = get_viewer_reaction(average)
        recommendation = get_recommendation(average)
        result[name] = {"Total_ratings" : total, "Average_rating" : average, "Popularity" : popularity, "Reaction" : reaction, "Recommendation" : recommendation}
    return result
movies = {
    "Inception": [5, 4, 5, 5, 4, 5],
    "Avatar": [4, 4, 3, 4, 3],
    "Joker": [5, 5, 5, 4, 5, 5, 5],
    "RandomMovie": []
}
print(movie_analyzer(movies))