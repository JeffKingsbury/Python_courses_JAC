# 2) Write a program that creates a dictionary with student names and marks. Input the names
# and marks from the user (2 separate lines). Stop entering names and marks, whenever the
# user enters a 'Q' or 'q' in the name field.

studentList = {}
while True:
    name = input("Please enter the students name: ");
    
    if name == 'q' or name == 'Q':
        break;
    
    grade = input("Please enter the students grade: ");
    studentList[name] = grade;
    
for x, i in studentList.items():
    print(x,i);
    