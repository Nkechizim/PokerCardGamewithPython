from datetime import time

start = time()
print(start)
print(type(start))

print(start.hour)
print(start.minute)
print(start.second)

print(time(6))
print(time(hour = 6))
print(time(hour = 18))
print(time(12, 25))
print(time(hour = 18, minute = 25))
print(time(23, 34, 59))
print(time(hour = 18, minute=23, second=53, microsecond=34))