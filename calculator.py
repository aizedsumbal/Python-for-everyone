def add(x,y):
    '''
    This function takes in two integers, they are x and y.
    It adds the parameters
    returns the sum of the parameters.
    '''
    return(x+y)
# print(add(12,5))

def sub(x,y):
    return(x-y)
# print(sub(12,5))

def mult(x,y):
    return(x*y)
# print(mult(12,5))

def div(x,y):
    return(x/y)
# print(div(12,5))
z=input("Enter your operation number 1.Addition 2.Subtraction 3.Mutiplication 4.Division :")
x=input("Enter your first number:")
y=input("Enter your second number:")

try:
    z=int(z)
    x=int(x)
    y=int(y)
# ---------------------------------------------------------------------------------------------------------------------
    if (z==1):
        print(add(x,y))
    elif (z==2):
        print(sub(x,y))
    elif (z==3):
        print(mult(x,y))
    elif (z==4):
        print(div(x,y))
    else:
        print("Write the correct number")
# ---------------------------------------------------------------------------------------------------------------------
except :
    print("Please enter an integer instead")
