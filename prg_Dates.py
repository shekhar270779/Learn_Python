# Python has a module datetime to work with dates and times

import datetime

# Smallest and largest year number allowed in a datetime obj
print(datetime.MINYEAR, datetime.MAXYEAR)

# Commonly used classes in datetime module are
# date class
# time class
# datetime class
# timedelta class

########################

## datetime.date class

d1 = datetime.date(2020, 7, 25)
print(f"Date is {d1}")

# get today's date
today = datetime.date.today()
print(f"Today: {today}")

# extract different components fom date
print(f"Today is year:{today.year}, month:{today.month}, day:{today.day}")

# to get a date from a timestamp
d2 = datetime.date.fromtimestamp(1500000000)
print(f"Date from timestamp is {d2}")

# replace
d2 = d2.replace(year=2020)
print(d2)

# weekday - Monday is 0 and Sunday is 6
print(datetime.date.today().weekday())

# strftime - to format date
today = datetime.date.today()
print(f'Formatted date: {today.strftime("%B %d, %Y")}')

### datetime.time class
# A time object represents a (local) time of day
t1 = datetime.time(hour=15, minute=47, second=30, microsecond=23456)
print(t1)


### datetime.datetime
# it contains both date and time information
moment = datetime.datetime.now()
print(moment)

print(f"Now is {moment.day}th day of month {moment.month}th,{moment.year},{moment.hour}::{moment.minute}::{moment.second}")





