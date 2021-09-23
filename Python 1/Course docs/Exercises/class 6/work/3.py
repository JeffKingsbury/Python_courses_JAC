# 3) Write a program that prompts for strings and writes them to a file. The program stops asking
# for strings if we type ‘Q’ or ‘q’.
# Check the file in Notepad or any other editor.

file = open('test2.txt', 'w');

while True:
    text = input('Please enter a string, or press q to quit. ');
    if text == 'q' or text == 'Q':
        break;
    
    file.write(text + '\n');

file.close();