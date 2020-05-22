#Exercise 38: Month Name to Number of Days

months = {
    'january':31,
    'february':28,
    'march':31,
    'april':30,
    'may':31,
    'june':30,
    'july':31,
    'august':31,
    'september':30,
    'october':31,
    'november':30,
    'december':31,
    }

month_entry = input("Enter month: ")

if month_entry.lower() in months[month_entry].title():
    print(month[month_entry].key())