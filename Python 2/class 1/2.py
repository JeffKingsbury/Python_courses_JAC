# 2) Multi arguments functions (non-keyworded)
# 2.1 Write a function called multiprodavg() that receives integers (any number of integers). The
# function multiplies all the integers and then divides the result by the number of integers passed
# (number of arguments). Return the result.
# Test your program by calling the function multiprodavg() with the following arguments:
# 1, 2, 3, 4 (result: 6)
# 88, 77, 66 (result: 149072.0 )
# -1,1,-1,1 (result: 0.25 )
#  Dept. Conted
# Group Concept E
# Version 5
# 2.2 Collect (prompt) for 5 integers, add them to a list. Then use the integers in the list to call the
# function. Attention, you will need to unpack the list during the function call. 

def multiprodavg(*ints):
    result = 1
    for x in ints:
        result *= int(x)
    return result / len(ints)
    
print(multiprodavg(-1,1,-1,1))

number_list = [];

for x in range(5):
    while True:
        number = input("Please enter a number: ({} out of 5): ".format(x + 1));
        try:
            int(number)
        except:
            print("That was not a number.");
        else:
            number_list += number;
            break
    
print(number_list);
print(multiprodavg(*number_list))