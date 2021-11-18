# 1) Time Module
# Write a program that:
# . Prompts you for a word.
# . Once you have entered the word, the programs displays the amount of seconds it took you
# (approx.) to type the word. (Display seconds up to one decimal place, as in 1.5 secs, hint
# remember your format notes from course I)
# Hint: You have to use the time.time() function to capture the time in seconds just before and
# just after you type your word. 

import time;

timeStart = time.time();

input('Please type "hello": ');

timeEnd = round(time.time() - timeStart, 2);

print(timeEnd)