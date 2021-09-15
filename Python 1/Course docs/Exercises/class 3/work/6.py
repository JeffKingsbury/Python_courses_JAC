# 6) Prompt for 10 integers (one at a time) and add them to a list (MyList). Then create a new
# list (MySecondList) which includes all the element of the first list without duplicates (for the
# time being use for loops for this exercise, we will see a different way of doing this later on). 

MyList = []

for x in range(10):
    newNum = input('Please enter a number: ');
    MyList.append(newNum);
    
MySecondList = [];

for x in MyList:
    if x not in MySecondList:
        MySecondList.append(x);
        
print(MySecondList)
    