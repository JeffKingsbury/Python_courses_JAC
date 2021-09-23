# 2) Try the same type of code but inside a function (call the function inputint()). The function will
# receive a string parameter containing the prompt to be displayed. When you call the function,
# the function will return an integer. The function never exits until you enter an integer and it is
# successfully returned. 


def inputint():
    while True:
        number = input('Please enter a number: ');
        try:
            int(number);
        except Exception as e:
            print("The following error occurred:", e);
        else:
            return number;
        
print(inputint())    