def get_total_borrow_days(borrowed_days):
    if not borrowed_days:
        return 0
    total = 0
    for borrowed in borrowed_days:
        total += borrowed
    return total

def get_average_borrow_days(borrowed_days):
    if not borrowed_days:
        return 0
    total = get_total_borrow_days(borrowed_days)
    average = total / len(borrowed_days)
    return round(average, 2)

def get_popularity_level(avg_days):
    if avg_days >= 15:
        return "Highly Popular"
    elif 7 <= avg_days <= 14:
        return "Popular"
    else:
        return "Less Popular"

def get_fine_amount(late_returns):
    return late_returns * 100

def get_restock_status(avg_days, late_returns):
    if avg_days == 0:
        return "Ignore"
    if avg_days >= 15 and late_returns < 3:
        return "Restock"
    elif late_returns >= 3:
        return "Restricted"
    else:
        return "Normal"

def library_analyzer(library):
    result = {}
    for key ,values in library.items():
        borrowed = values["borrowed_days"]
        late = values["late_returns"]
        total = get_total_borrow_days(borrowed)
        average = get_average_borrow_days(borrowed)
        popularity = get_popularity_level(average)
        fine = get_fine_amount(late)
        status = get_restock_status(average, late)
        result[key] = {"Total_Days" : total, "Average_Days" : average, "Popularity" : popularity, "Fine" : fine, "Status" : status}
    return result
library = {
    "Book A": {
        "borrowed_days": [3, 5, 2, 4],
        "late_returns": 1
    },
    "Book B": {
        "borrowed_days": [15, 18, 20],
        "late_returns": 4
    },
    "Book C": {
        "borrowed_days": [],
        "late_returns": 0
    }
}
print(library_analyzer(library))