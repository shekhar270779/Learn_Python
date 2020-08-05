# timedelta object is useful if we want to represent an instance of time, as an object
# Python timedelta object is very useful for datetime manipulations.
# The support for basic arithmetic operators makes it very easy to use.

from datetime import timedelta

td = timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
print(td)

zd = timedelta()
print(zd)

# basic operations on timedelta objects
a = timedelta(hours=4, seconds=100)
b = timedelta(hours=2, seconds=50)
print(a+b)
print(a-b)

# get current datetime
from datetime import datetime
curr_time = datetime.now()
print(curr_time)

# create future dates
two_days_ahead = curr_time + timedelta(days=2)
one_year_ahead = curr_time + timedelta(days=365)
halfanhour_ahead = curr_time + timedelta(minutes=30)

print(two_days_ahead)
print(one_year_ahead)
print(halfanhour_ahead)

# past dates
one_and_half_hour_back = curr_time - timedelta(hours=1, minutes=30)
month_back = curr_time - timedelta(days=30)
print(one_and_half_hour_back)
print(month_back)

# timezone
# pip install pytz

# to find current time in different timezones
from pytz import timezone, common_timezones

import random
for _ in range(4):
    zone = random.choice(common_timezones)
    print(f"Timezone: {zone}")
    dt_obj = datetime.now(timezone(zone))
    print(dt_obj, dt_obj + timedelta(minutes=30))
