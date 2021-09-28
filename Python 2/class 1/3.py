# 3) Multi arguments functions (non-keyworded)
# Write a function that receives several lists of 3 positive integers each (ex. [2,4,6] and [0,2,2])
# The function finds the largest integer from all the lists. (Hint, use the max function with a list,
# as in max(mylist). Try the function max() to explore how it works.
# The function should return the largest integer and the corresponding list. Print the returned
# values in the main section of your script. Notice that the function returns two values, make sure
# you assign two values when you call the function. (i.e. a, b = myfunction(…) )

def findMax(*listed):
    count = 0;
    largest = 0;
    largetCount = 0;
    for x in listed:
        count += 1;
        if max(x) > largest:
            largest = max(x);
            largetCount = count;
            
    return largest, largetCount;
            

a,b = findMax([0,1,2], [0,23,4]);
print("The largest number is: {}, which can be found in list: {}.".format(a,b));