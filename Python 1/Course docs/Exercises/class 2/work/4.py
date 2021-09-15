# 4) Write a program that prompts the user for a number and then prints out a list of all the divisors of that
# number. A divisor is a number that divides evenly into another number. For example, 13 is a divisor of 26
# because 26 / 13 has no remainder. (use a for loop)


while True:
    num = input("Please enter a whole number: ");
    try:
       int(num)
       break
    except ValueError:
        next

numDivisor = int(num);
count=0;

while int(numDivisor) // 2 != 1 or 0:
    count += 1;
    numDivisor = numDivisor // 2;
    if numDivisor == 0:
        break
    
for x in range(int(count)):
    num = int(num) // int(2);
    print(num);