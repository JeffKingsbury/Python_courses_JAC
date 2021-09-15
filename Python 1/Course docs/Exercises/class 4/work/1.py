# 1) Write a function that receives a float number indicating the radius of a circle.
# The function should calculate the area of the circle according to the following equation:
# area = PI x radius2
# (you can approximate Pi to 3.1415)
#  Return the area to the calling section of the program. Test it. 

def getArea(radius):
    area = 3.1415 * (radius * 2);
    return area;

while True:
    try:
        num = float(input("Please enter the radius of the circle you'd like the area of: "));
    except ValueError:
        print('That was not a number.');    
    else:
        break;
        
print(getArea(num));