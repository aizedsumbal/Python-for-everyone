num1 = input("Enter your first number")
num2 = input("Enter your second number")
num3 = input("Enter your third number")

if(num1 == num2 and num1 == num3 and num2 == num3):
    print("All are the same")
elif(num1 != num2 and num1 != num3 and num2 != num3):
    print("All are different")
else:
    print("Neither")
