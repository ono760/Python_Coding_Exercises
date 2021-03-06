# If I give you a date, can you tell me what day that date 
# is? For example, december 8th, 2015 is a tuesday.

# Your job is to write the function day(date) which takes a 
# string representation of a date as input, in the format 
# YYYYMMDD. The example would be "20151208". The function 
# needs to output the string representation of the day, so 
# in this case "Tuesday".

# Your function should be able to handle dates ranging from 
# January first, 1582 (the year the Gregorian Calendar was introduced) 
# to December 31st, 9999. You will not be given invalid dates. 
# Remember to take leap years into account.


import datetime
import calendar

def day(date):
    return calendar.day_name[datetime.datetime.strptime(date,"%Y%m%d").weekday()]

print(day('19890212'))
print(day('20151208'))

# def day(date):
#     return calendar.day_name[datetime.datetime.strptime(date,"%Y%m%d").weekday()]

