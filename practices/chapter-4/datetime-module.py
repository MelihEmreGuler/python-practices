import datetime

print("dir(datetime):", dir(datetime))
print("help(datetime):", help(datetime))

# date CLASS
date = datetime.date(2023, 12, 10)
print("date:", date)  # 2023-12-10 default format is yyyy-mm-dd
print("date.year:", date.year)
print("date.month:", date.month)
print("date.day:", date.day)

# today function returns the current date
today = datetime.date.today()
print("today:", today)

# .weekday() returns the day of the week as an integer, where Monday is 0 and Sunday is 6
print("today.weekday():", today.weekday())

# .isoweekday() returns the day of the week as an integer, where Monday is 1 and Sunday is 7
print("today.isoweekday():", today.isoweekday())

# timedelta CLASS
# timedelta is a duration expressing the difference between two dates.

diff = datetime.timedelta(days=10)
print("diff:", diff)  # 10 days, 0:00:00

# timedelta can be added to a date
print(f"today + diff: {today} + {diff} = {today + diff}")

# timedelta can be subtracted from a date
print(f"today - diff: {today} - {diff} = {today - diff}")

# timedelta can be multiplied by an integer
diff = datetime.timedelta(days=10, hours=5, minutes=30, seconds=10)
print("diff:", diff)  # 10 days, 5:30:10

# timedelta can be called with no named arguments
diff = datetime.timedelta(10, 5, 30, 10)
print("diff:", diff)  # 10 days, 5:30:10

