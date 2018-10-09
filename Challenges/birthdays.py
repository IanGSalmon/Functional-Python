import datetime

birthdays = [
    datetime.datetime(2012, 4, 29),
    datetime.datetime(2006, 8, 9),
    datetime.datetime(1978, 5, 16),
    datetime.datetime(1981, 8, 15),
    datetime.datetime(2001, 7, 4),
    datetime.datetime(1999, 12, 30)
]

today = datetime.datetime.today()

# Create a function named is_over_13 that takes a datetime and returns whether or not the difference between
# that datetime and today is 4745 days or more
def is_over_13(new_dates):
    return (today - new_dates).days >= 4745

# Now create a new function named date_string that takes a dateitme and 
# returns a string like "May 20" using strftime, format is "%B %d"
def date_string(nw_date):
    frmt = "%B %d"
    return nw_date.strftime(frmt)

# Finally make a variable named birth_dates
# Using map() and filter(), along with your two functions
# create date strings for every datetime in birthdays so long as the datetime is more than 13 yrs old
birth_dates = map(date_string, filter(is_over_13, birthdays))