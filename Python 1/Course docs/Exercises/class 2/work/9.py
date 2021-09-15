# 9) Write a small menu with 4 items. Print a message letting the user know his selected choice.
# 1. Welcome to Python
# 2. Python is Fun
# 3. This could be a challenge
# 4. Exit
# Enter your choice (1 – 4):
# Every time the users selects a choice (1 to 3) we print a message (like "You chose welcome to Python") and then
# print the menu again and wait for another choice to be entered. Once the user enters 4, the program ends.

a = "1) Welcome to Python\n";
b = "2) Python is fun!\n";
c = "3) This could be a challenge\n";
d = "4) Exit \n\n";


while True:
    menu = input(
        "\n////////////////////// \nPlease select one of the following options: \n////////////////////// \n\n" + a + b + c + d + "Enter your choice: "
    );
    if menu == str(1):
        print("\nYour choice:");
        print(a);
        
    elif menu == str(2):
        print("\nYour choice:");
        print(b);
        
    elif menu == str(3):
        print("\nYour choice:");    
        print(c);
    
    elif menu == str(4):
        print("\nExiting...");
        break
            