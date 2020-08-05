## Python time module

# Epoch: An epoch is a fixed point in time from which other times can then be represented as "distances" from that time.
# In windows/Unix, the epoch is Jan 01, 1970 mid night.

#  -2 <-  -1 <- Epoch  -> 1 -> 2

# Basic time module functions
# time() : returns the current time in seconds from the epoch
# time_ns() : returns the current time in nano-seconds from the epoch
# ctime([seconds]) : returns the time in timestamp format
# gmtime([seconds]): returns the gmt time as struct_time object
# localtime[seconds]) : returns the local time as struct_time object

import time

print(time.gmtime(0))

print(time.time()) # no. of seconds since epoch

seconds_in_year = 365 * 24 * 60 * 60

print(time.time() / seconds_in_year)

print(time.ctime())

t1 = time.time()
time.sleep(3)
t2 = time.time()
print((t2-t1))

# Timezones
# UTC : Coordinated Universal Time
# UTC is a reference timezone
# as epoch is for time, UTC is for time zones
# Other timezones are defines as offset from UTC
# GMT : Greenwich Mean Time , UTC + 0.0

print(time.localtime())

print(time.localtime().tm_zone)

print(time.localtime().tm_gmtoff / (60*60))

print(time.gmtime())

print(time.localtime().tm_year)

# String representations of time

print(time.asctime())

print(time.strftime("%Y-%m-%d", time.localtime()))

print(time.strftime("Today is %A, %d/%m/%Y", time.localtime()))

print(time.strptime("2020-07-22", "%Y-%m-%d"))