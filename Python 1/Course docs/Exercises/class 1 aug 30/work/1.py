# Write a program that prompts the user for two numbers. The program then prints the SUM of the
# numbers and the PRODUCT of the two number (multiplication). Print both results with a descriptive
# message. Assume the numbers are integers.

num1 = input("Please enter a number: ");
num2 = input("Please enter a second number: ");
ansSum = int(num1) + int(num2);
ansProduct = int(num1) * int(num2);
print("The sum of those numbers is: " + str(ansSum));
print("And, the product of those numbers is: " + str(ansProduct));