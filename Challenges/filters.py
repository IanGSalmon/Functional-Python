import datetime

dates = [
    datetime.datetime(2012, 12, 15),
    datetime.datetime(1987, 8, 20),
    datetime.datetime(1965, 2, 28),
    datetime.datetime(2015, 4, 29),
    datetime.datetime(2012, 6, 30),
]

# Write a function named is_2012 that accepts a single argument and returns whether that argument's year attr is == 2012
def is_2012(arg1):
    if arg1.year == 2012:
        return True

# Now create a variable named dt_2012 that uses filter() and is_2012 to return..
# only datetimes from dates that are from the year 2012
# I put in list to be able to view in print 
dt_2012 = list(filter(is_2012, dates))
print(dt_2012)