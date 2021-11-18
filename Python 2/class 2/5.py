# 5) Write a function datecomp() that receives two dates. The function calculates the number of days
# between the two dates and returns it. The function will also return the Boolean value True if the
# first date is earlier than the second date. The function returns two values.
# Test the function by prompting for two date values and passing them to the function
# Note: Use the method datetime.datetime.strptime() from the datetime module
# to convert your string dates (from input()) to date variables.


import datetime as dt;
import time;

def datecomp(date1,date2):
    date1 = dt.datetime.strptime(date1, '%Y/%m/%d');
    date2 = dt.datetime.strptime(date2, '%Y/%m/%d');
    datediff = date2 - date1;
    smaller = date1 < date2;
    
    return ("There is a difference of {} days, between those two dates.").format(abs(datediff.days)), smaller;

dateStr1 = input("Please enter the first date (YYYY/MM/DD): ");
dateStr2 = input("Please enter the second date (YYYY/MM/DD): ");

print(datecomp(dateStr1, dateStr2));