# 8) Prompt the user for a string and print out whether the string is a palindrome or not. (A palindrome is a
# string that reads the same forwards and backwards.)

str = input('Please enter a word: ');

if str[::-1] == str:
    print(str, "is a palindrome!");
    
else:
    print(str, "is not a plaindrome. :(");