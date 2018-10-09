# Use sorted() and attrgetter() to sort date_list by the day attribute of each datetime obj
# Save this sorting into a variable named sorted_dates

import datetime
from operator import attrgetter

date_list = [
    datetime.datetime(2015, 4, 29, 10, 15, 39),
    datetime.datetime(2006, 8, 15, 14, 59, 2),
    datetime.datetime(1981, 5, 16, 2, 10, 42),
    datetime.datetime(2012, 8, 9, 14, 59, 2),
]

sorted_dates = sorted(date_list, key=attrgetter('day'))
print(sorted_dates)