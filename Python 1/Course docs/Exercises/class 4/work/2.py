# 2) Write a function that receives 3 parameters. The first parameter is a positional parameter (it
# is mandatory to pass the parameter, there are no default values). The other two parameters
# contain default values (The default values are 1 and 10 respectively).


# As in: def myfunction(myvalue, defvalue1 = 1, defvalue2=10):
# totalvalue = (myvalue * defvalue2) + 1
#  return totalvalue


# Test you function for each of the following cases:


# 4.1 myfunction(1)
# myfunction(10) 
# myfunction(1,1)
# myfunction(1,1,5)
#  myfunction(10,defvalue2 = 5, defvalue1=10)
#  myfunction(10,defvalue2 = 5)


# What happens in these cases?
#  myfunction(defvalue1 = 2) < error (missing myvalue)
#  myfunction(defvalue1 = 2, defvalue2 = 10) < error (missing myvalue)
#  myfunction() < error (missing myvalue)
#  myfunction(1, defvalue3 = 5) < error undefiened

def myfunction(myvalue, defvalue1 = 1, defvalue2=10):
    totalvalue = (myvalue * defvalue2) + 1
    return totalvalue

print(myfunction(10))
print(myfunction(1,1))
print(myfunction(1,1,5))
print(myfunction(10,defvalue2 = 5, defvalue1=10))
print( myfunction(10,defvalue2 = 5))