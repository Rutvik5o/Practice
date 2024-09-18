import datetime

today = datetime.date.today()

birthday = datetime.date(1923,4,3)

diff = today - birthday

print(diff.days)