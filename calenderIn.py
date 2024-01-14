

#program to print calender in Python

import calendar

years_full = input("Inter the Year You Want to Get Printed : ")

years_full = int(years_full)
print(calendar.calendar(years_full))