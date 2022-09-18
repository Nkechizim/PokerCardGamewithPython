from datetime import datetime, timedelta

birthday = datetime(1998, 5, 27)
now = datetime.today()

lifespan = now - birthday
print(lifespan)
print(type(lifespan))
print(lifespan.total_seconds())

five_hundred_days = timedelta(days=500, hours=12)
print(five_hundred_days)
print(five_hundred_days + five_hundred_days)
print(now + five_hundred_days)