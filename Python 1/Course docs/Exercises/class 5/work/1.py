# 1) Write a program that defines the following dictionary:
# student_marks = {'Joe':15, 'Mary':20, 'Ralph':18, 'Annita':19}
# 1.1 Just print the dictionary (use a print )
# {'Joe':15, 'Mary':20, 'Ralph':18, 'Annita':19}
# 1.2 Add the key pair value {'Rob':16} to the dictionary
# 1.3 Assign the mark 17 to Joe
# 1.4 Write an If statement that checks for the existence of student 'Mary' in the dictionary.
# Print a message that lets you know if 'Mary' is or is not in the dictionary.
# Do the same logic, but this time prompt the user for a student name. Then apply the
# same logic as above.
# 1.5 Print the elements of the dictionary, first the key and then the value:
# As in:
# Joe 15
# Mary 20
# Ralph 18
# Annita 19

student_marks = {'Joe':15, 'Mary':20, 'Ralph':18, 'Annita':19};

#1.1
print(student_marks);

#1.2
student_marks['Rob'] = 16;
print(student_marks)

#1.3
student_marks['Joe'] = 17;
print(student_marks)

#1.4
if 'Mary' in student_marks:
    print('Mary exists in the dictionary.');
else:
    print("Mary does not exist in the dictionary.");
    
#1.4 part 2
checkStudent = input('Please enter a students name: ');

if checkStudent in student_marks:
    print(checkStudent, "exists in the dictionary.");
else:
    print(checkStudent, "does not exist.");
    
#1.5    
for x, i in student_marks.items():
    print(x, i)