# 1) Trying some of the file system functions that come with the OS module.
# 1.1 Start by importing the os module (i.e. import os)
# 1.2 Check your current directory by using the os.getcwd() method
# Store the path in a string variable (the path returned by os.getcwd() )
# 1.3 List the files in your current directory by using the os.listdir() method.
# 1.4 List all files in your current directory with a name of 8 characters or less (including
# extension)
# 1.5 Create (with notepad) a text file in your current directory and check if the file exist from
# inside your python script by using the os.path.isfile(p). Prompt the user for the file name,
# and display a suitable message (file exists or does not exist!)
# 1.6 Create a new directory (by hand) inside your current working directory. Then, from inside
# your python script, change directories so that you point to the new directory you just
# created, use the os.chdir() method. Display your new current directory by using os.getcwd()
# 1.7 Create a new directory, but this time from inside your python script by using the os.mkdir()
# method.

import os;

filePath = os.getcwd();

for files in os.listdir():
    if os.path.isfile(files):
        print(files)
        if len(files) <= 8:
            print(files, "Is 8 or less characters long.")
            
fileName = input('Enter a file name: ')
if os.path.isfile(fileName):
    print(fileName, "Exists.");
else:
    print(fileName, "Does not exist");
    
os.chdir('/Users/jeffkingsbury/Documents/GitHub/Python_courses_JAC/python 1/')
filePath = os.getcwd();
os.mkdir('test')
