# 3) Using time.sleep() (time.sleep() takes a number of seconds as a parameter)
# Write a function called slowprint(phrase, secs) that receives two parameters: phrase and
# seconds (string and integer).
# The function will then print all the characters in the string with a delay of secs in between each
# character.
# Example. If you call the function this way: slowprint(“Hello how are you”, .5)
# The function will print all the characters in the phrase, with a delay of 0.5 secs in between each
# character. Therefore, it will look as it is printing slow.
# Tests your program by prompting for phrases and printing them with the slowprint() function. 

import time;

def slowprint(phrase, secs):
    for x in phrase:
        print(x);
        time.sleep(secs);
        
slowprint("Hello World", 2)