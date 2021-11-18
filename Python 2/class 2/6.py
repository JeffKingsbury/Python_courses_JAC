# 1) List Comprehensions (Simple)
# Write a program that uses a List Comprehension to do the following:
# . Starting with the following list:
# [2,-5,4,6,0,-3,-4,7,8,-8,-7,-1,1]
# . Create a new list with the square of all integers that are positive and odd.
# . Create a new list with the square of all integers that are positive and even.
# The result will be the following lists:
# [49,1]
# [4, 16, 36, 0, 64]


list1 = [2,-5,4,6,0,-3,-4,7,8,-8,-7,-1,1];
list2 = [y**2 for y in list1 if y % 2 == 1 and y >= 0];
list3 = [y**2 for y in list1 if y % 2 != 1 and y >= 0];
print(list2, list3)