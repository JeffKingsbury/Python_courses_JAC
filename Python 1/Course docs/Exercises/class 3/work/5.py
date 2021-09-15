# 5) Prompt for 10 integers (one at a time) and add them to a list (MyList). Check to see if the
# numbers 10 , 5 and 3 are in the list and print a suitable message to let us know of their
# existence in the list.

MyList = [];

for x in range(10):
    item = int(input('Please enter a number: '));
    MyList.append(item);
    
if 10 in MyList:
    print('The number 10 exists in the list.');
if 5 in MyList:
    print('The number 5 exists in the list.');    
if 3 in MyList:
    print('The number 3 exists in the list.');