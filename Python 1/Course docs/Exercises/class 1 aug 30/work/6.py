# Write a programs that prompts for an amount in dollars (let’s say 23, no fractions) and breaks it down into
# 5$ bills, $2 coins and $1 coins. (Do not worry about decimal values in this exercise). If there are no 5$, 2$
# coins or 1$ coins, do not print a cero, just do not print the monetary denomination. 

dollar = int(input("Please enter a dollar amount: "))

print("Breakdown:")

dMf = int(dollar % 5);
five = int(dollar / 5);

if five >= 1:
    print(five, 'Five dollar bill(s)');
    if dMf / 2 >= 1:
        print(int(dMf / 2), "Toonie(s)");
        if int(dMf % 2) >= 1:
            print(int(dMf % 2), "Loonie(s)");
            
else:
    if dMf / 2 >= 1:
        print(int(dMf / 2), "Toonie(s)");
        if int(dMf % 2) >= 1:
            print(int(dMf % 2), "Loonie(s)");
    else:
        print(int(dMf % 2), "Loonie(s)");