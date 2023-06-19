# Excercise

# W.A.P. to find out how many daus, weeeks, months we have left if we live until 90 years old

age=int(input("Enter Your age"))

years_left=90-age

days_left=years_left*365

month_left=years_left*12

weeks_left=years_left*52


print(f"You have {days_left} days, {weeks_left} weeks amd {month_left} month left." )