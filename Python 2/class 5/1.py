# Write a program that prompts for a string. Make sure the string is 10 or more characters in length. The
# program will then check the entered string for the occurrence of the substring 'code-', at the beginning of the
# string. If you find the 'code-' followed by 2 digits, then print 'code-??', where ?? are the characters at position
# 8th and 9th of the string. Otherwise (if the regex pattern is not found), print the last two characters of the
# string

import re;

while True:
    text = input('Please enter a string longer than 10 characters: ');
    if len(text) > 10:
        break

stringsFound = re.search('^code-\d\d', text);
if str(stringsFound) == 'None':
    print(text[-2:])
else:
    print(stringsFound)