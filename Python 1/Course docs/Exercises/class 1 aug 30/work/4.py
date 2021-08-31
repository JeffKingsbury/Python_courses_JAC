# Write a program that prompts the user for a string. Then check the first and last characters of the string. If
# both characters are equal, then print the string, otherwise print the message
# “First and last character do not match”.

str = input("Please enter a word or sentence: ");
if str[0] == str[len(str) -1]:
    print(str)
else:
    print("First and Last characters do not match.")