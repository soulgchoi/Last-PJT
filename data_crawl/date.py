from datetime import datetime

now = datetime.now()
date = str(now.year) + str(now.month) + str(now.day)
print(now.year)
print(now.month)
print(now.day)
print(date)