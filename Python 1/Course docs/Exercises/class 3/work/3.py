# 3) Prompt the user for 10 integers (one at a time) and add them to a list (MyList). Then print
# the list using a for loop. 


MyList = [];

for x in range(10):
    NumInput = int(input('Please enter a number: '));
    MyList.append(NumInput);
    
print(MyList);    