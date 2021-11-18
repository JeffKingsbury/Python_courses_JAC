# 1) Global variables
# Define global variable (variable outside of any function) called balance. Initialize balance to 0.
# Define 2 functions inside your script as follows:
# a) bal_inc(increment)
# This function receives an integer argument and increments the value of
# the global variable balance with the amount received.
# b) bal_dec(decrement)
# This function receives an integer argument and decrements the value of
# the global variable balance by the amount received.
# . Then execute this instructions:
# increment = 5
# decrement = 3
#  for I in range(3):
#  bal_inc(increment)
#  for I in range(2):
#  bal_dec(decrement)
#  print(“Final balance:”, balance)


def bal_inc(increment):
    global balance;
    balance += increment;
    
def bal_dec(decrement):
    global balance;
    balance -= decrement;
    
balance = 0;
increment = 5
decrement = 3

for I in range(3):
    bal_inc(increment)
for I in range(2):
    bal_dec(decrement)
    
print("Final balance:", balance)