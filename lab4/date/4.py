import datetime

print("ATTENTION: the second date have to be greater than the first date")
 
year_1 = int(input("Year 1: "))
month_1 = int(input("Month 1: "))
day_1 = int(input("Day 1: "))

year_2 = int(input("Year 2: "))
month_2 = int(input("Month 2: "))
day_2 = int(input("Day 2: "))

first_date = datetime.date(year_1 , month_1 , day_1)

second_date = datetime.date(year_2 , month_2 , day_2)

time_deference = second_date - first_date

print(time_deference.total_seconds())