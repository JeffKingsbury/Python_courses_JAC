# 6) Write a program that prompts for a string and then prints it backwards. There is a shortcut way to this in
# python y using slicing ( [::-1] ) , but can you try do it using indexing and a while loop (or a for loop)?

str = input("Please enter a string: ");
strBackwards = ""
x=0;
while True:
    x -= 1;
    strBackwards += str[x];
    if x == -len(str):
        break;
    
print(strBackwards)