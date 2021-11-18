# 3) Write a program that prompts for a file name (codefile.txt). The file (codefile.txt) is provided in the
# documents under the exercises section. Opens the file, scans all the lines that start with the characters
# ‘AA’ followed by an integer between 1-9, followed by one of the characters a, b, c, d and followed by
# another integer between 1 and 9. If the pattern is matched at the beginning of the line, add up (sum) the
# values of the 10th and 11th characters of each line. Print the total number of lines read, and the total of the
# sum. 

import re;

while True:
    file = input('Please enter a file name: ');
    try:
        fileOpen = open(file, 'r');
    except:
        print('Invalid file name.');
    else:
        break
    
count = 0;
xSum = 0;

for x in fileOpen:
    regex = '^AA\d[a-d]{1}\d';
    output = re.search(regex,x);
    if str(output) != 'None':
        count += 1;
        xSum += int(x[11]);
        xSum += int(x[12]);
        
print("There were {} entries that matched the regex format. The sum of the 10th and 11th number of each entry is {}".format(count, xSum));
fileOpen.close();