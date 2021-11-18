# 4) Datetime module
# Write a function called extradays() that receives a date and an integer representing a number of
# extra days to be added to the passed date.
# Calculate the new date inside the function and return it
import datetime as dt;

def extradays(date,int):
    extras = dt.timedelta(days = int);
    dateRetrun = date + extras
    
    return dateRetrun 

date = dt.date.today();
print(extradays(date, 2))