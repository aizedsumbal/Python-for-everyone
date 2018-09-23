num1 = input("Enter first number:")
num2 = input("Enter second number:")
num3 = input("Enter third number:")

if (num1<num2 and num1<num3 and num2<num3) or (num1>num2 and num1>num3 and num2>num3)  :
    print("The numbers are in order")
else:
    print("The numbers are not in order")