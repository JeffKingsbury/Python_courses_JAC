# 7) Write a program that prompts for a string and displays the vowels found in the string as well as how many
# vowels were found in total (use a for loop)

str = input("Please enter a string: ");
vowels = ['a','e','i','o','u'];
vowelCount = 0;
for x in str:
    if x.lower() in vowels:
        print(x); 
        vowelCount += 1;
        
print(vowelCount);