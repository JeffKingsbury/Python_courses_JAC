# 4) Write a program that takes a list of numbers (for example, mylist = [5, 10, 15, 20, 25]) and
# makes a new list with only the first and last elements of the given list. Print the new list. 

mylist = [5, 10, 15, 20, 25];
newList = [];

newList.append(mylist.pop(0));
newList.append(mylist.pop(-1));

print(newList);