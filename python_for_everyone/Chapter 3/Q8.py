num1 = input("Enter your first number")
num2 = input("Enter your second number")
num3 = input("Enter your third number")
num4 = input("Enter your fourth number")

if(num1==num2 or num1==num3 or num1==num4 or num2==num3 or num2==num4 or num3==num4 and num1==num2 or num1==num3 or num1==num4 or num2==num3 or num2==num4 or num3==num4):
    print("There are two pairs")
else:
    print('There are not two pairs')
