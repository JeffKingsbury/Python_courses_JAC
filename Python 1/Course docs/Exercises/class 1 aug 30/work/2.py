# Write a program that prompts for a number. Depending on whether the number is even or odd, print a
# message stating the nature of the number. Hint: how does an even / odd number reacts when divided by
# 2?

print("\n **** Welcome to the even or odd machine (tm) **** \n")
num = input("Please enter a number: ");

if int(num) % 2 == 0:
    print(str(num) + " is an even number.");
else:
    print(str(num) + " is an odd number.");
     