from datetime import datetime

print(datetime(1999, 7, 24))
print(datetime(1999, 7, 24, 14))
print(datetime(1999, 7, 24, 14, 16))
print(datetime(1999, 7, 24, 14, 16, 56))
print(datetime(1999, 7, 24, 14, 16, 56).weekday())

print(datetime.now())
today = datetime.today()
print(today)
print(today.year)
print(today.month)
print(today.day)
print(today.hour)
print(today.minute)
print(today.second)
print(today.microsecond)

#weekday starts counting from monday at 0
print(today.weekday())

same_time_twenty_years_ago = today.replace(year = 1999)
print(same_time_twenty_years_ago)
same_time_in_january = today.replace(month = 1)
print(same_time_in_january)
start_of_january_1999 = today.replace(year = 1999, month = 1, day = 1)
print(start_of_january_1999)