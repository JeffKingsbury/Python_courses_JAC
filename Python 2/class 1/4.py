# 4) Write a function call navigator. The function can receive a variable number of keyworded
# parameters (i.e. **kwargs)
# The parameters are:
# up, right, down, and left. (ex. navigator(up=6, right =1, down = 2, left = 0) )
# Assuming these are movements in a cartesian plane, with origin 0,0. Then the function will
# calculate the final position after all movements.

def navigator(**kwargs):
    up = kwargs.get('up', 0);
    down = kwargs.get('down', 0);
    left = kwargs.get('left', 0);
    right = kwargs.get('right',0);
    
    x=0
    y=0
    
    y += up;
    y -= down;
    x += right;
    x -= left;
    
    return x, y;

x, y = navigator(up=6, right=1, left=0, down =2);

print("The position is {},{}.".format(x,y))