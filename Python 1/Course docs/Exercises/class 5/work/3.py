# 3) Write a program that reads a string and prints a table of the letters that appear in the string
# in alphabetical order. Besides the letter, print the number of times the letter is found in the
# string. Case should be ignored.
# A sample output of the program when the user enters the string 'This is a String with Upper and
# lower case Letters', would look this this:
# a: 3, c: 1, d: 1, e: 5, g: 1, h: 2, i: 4, l: 2, n: 2, o: 1, p: 2, r: 4, s: 5, t: 5, u: 1, w: 2

string = "This is a sting, obviously.";
letters = {};

for x in string.lower():
    if x.isalpha():
        letters[x] = letters.get(x, 0) + 1;
        
for x, i in sorted(letters.items()):
    print(x,i)
    
    
    