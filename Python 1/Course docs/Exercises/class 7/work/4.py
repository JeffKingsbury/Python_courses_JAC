# 4) Prompt the user for a filename that does not exists. Try opening the file. Catch the exception
# and give a suitable error. Prompt for the file again or ‘q’ to exit. Use a while loop.


while True:
    fileName = input('Please enter a file name: ');
    
    if fileName == 'q' or fileName == 'Q':
        break;
    
    else:
        try:
            file = open(fileName, 'r');
            
        except Exception as e:
            print('The following error occurred:',e);
            
        else:
            for lines in file:
                print(lines, end ='');
                
            file.close()
            break   

