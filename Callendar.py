# Python program to display calendar
# as the user set its year and month dates

import calendar

year = int(input("Year...: "))
month = int(input("Month...: "))


print(calendar.month(year, month))
