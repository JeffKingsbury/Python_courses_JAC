# 7) Write a program that prompts for names and continues to prompt until you type either a ‘q’
# or a ‘Q’. Add all the names to a list and then print the names sorted in reverse order. 

myList = [];

while True:
    name = input("Please enter a name (Enter Q to stop): ");
    if name == 'q' or name == 'Q':
        break
    else:
        myList.append(name);
    
if len(myList) != 0:
    myList.reverse();
    print(myList, end=" ");
else:
    print('No names were entered.')