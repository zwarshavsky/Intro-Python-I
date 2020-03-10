"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import date, timedelta, datetime


def days_cur_month(m=None,y=None):
    if m == None:
      m = datetime.now().month
    else:
      m = m 
    if y == None:
      y = datetime.now().year
    else:
      y = y 
    ndays = (date(y, m+1, 1) - date(y, m, 1)).days
    d1 = date(y, m, 1)
    d2 = date(y, m, ndays)
    delta = d2 - d1

    return [(d1 + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(delta.days + 1)]


system_argument = sys.argv

if len(system_argument) == 1:
  print(days_cur_month())

elif len(system_argument) == 2:
  month_string = system_argument[1]
  full_month_convert = datetime.strptime(month_string, '%B').replace(year=2020)
  month_digit = int(str(full_month_convert)[5:7])
  print(days_cur_month(month_digit))

elif len(system_argument) == 3:
  month_string = system_argument[1]
  full_month_convert = datetime.strptime(month_string, '%B').replace(year=2020)
  month_digit = int(str(full_month_convert)[5:7])
  year = int(system_argument[2])
  print(days_cur_month(month_digit,year))

else:
  print("Usage: script.py [month_name] [year]")