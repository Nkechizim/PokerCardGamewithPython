#import datetime
from datetime import date

birthday = date(1998, 5, 27)
print(birthday)
print(type(birthday))

moon_landing = date(year = 1969, day = 20, month = 7)
print(moon_landing)

hey = date(year = 2020, day = 29, month = 2)
print(hey)

print(birthday.year)
print(birthday.month)
print(birthday.day)

today = date.today()
print(today)