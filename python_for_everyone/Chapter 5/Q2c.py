num1 = input("Enter your number")
num2 = input("Enter your number")
num3 = input("Enter your number")


def sorted(x,y,z):
    if x < y and y < z:
        return "true"
    else:
        return "false"


a = sorted(num1, num2, num3)

print(a)