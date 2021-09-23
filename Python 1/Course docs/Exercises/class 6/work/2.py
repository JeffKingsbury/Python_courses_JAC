# 2) Write a small text file in notepad (maybe 3 lines)
# Save the file somewhere in the pc where you have access
# Open the file and display all the lines on the screen (one line at a time). User the for loop
# method of reading text files.

file = open('test.txt', 'r');

for lines in file:
    print(lines, end='')