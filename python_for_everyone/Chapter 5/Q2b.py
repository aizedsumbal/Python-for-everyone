num1 = input("Enter your number")
num2 = input("Enter your number")
num3 = input("Enter your number")


def alldifferent(x, y, z):
    if x != y and x != z and y != z:
        return "true"
    else:
        return "false"


a = alldifferent(num1, num2, num3)

print(a)