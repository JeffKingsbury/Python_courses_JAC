# 1) Write a script that prompts for an integer. During the input you will convert the entered string
# into an integer (int function). Trap any exceptions and print a message letting the user know
# there was an error. Try entering letters instead of an integer, what happens? Are you able to
# trap the exception? 


while True:
    number = input('Please enter a number: ');
    try:
        int(number);
    except Exception as e:
        print("The following error occurred:", e);
    else:
        break;
    