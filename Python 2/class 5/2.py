# 2) Write a script that calls a function called checkPhone(passing a phone string). This function will use the
# regex module (re) to validate a pattern. Find a suitable regex expression on the net (google it).
# The script will prompt for a phone number and validate it with the function. Return the phone number
# string if the format is correct. Otherwise return None.
# Sample phone string: (514) 990-0909, 1 (438) 887-9090, 57 (300)794-5529
# if the phone is valid, print it. Otherwise, print “Invalid phone” (Do not print inside the function). 

import re;

def checkPhone(num):
    regex = '^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$';
    phone = re.search(regex,num);
    if str(phone) == 'None':
        return "Invalid phone number";
    else:
        return phone;
    
number = input('Please enter a valid phone number (xxx)xxx-xxxx : ');
print(checkPhone(number));