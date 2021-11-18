# 2) time.asctime()
# time.asctime() returns a string containing a date and time. Use the value provided by this
# function to write a function called header_log(str). The function header_log will receive a name
# (as in “Caroline”) and will print the following message to the screen:
# Date: Thu Jan 28 2016 Welcome: Caroline
# Notice that the actual time is not included in the message (hint: use slicing to extract the parts
# of the date and time string that you require).
# Have your program prompt the user for his/hers name, and use it as the parameter to the
# function header_log. 

import time;

def header_log(str):
    date = time.asctime()[:10] + time.asctime()[19:]
    
    return("Date: {}, Welcome: {}".format(date, str));
    
name = input("Please enter your name: ");

print(header_log(name));