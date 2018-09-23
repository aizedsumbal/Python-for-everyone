odd = 0
even = 0
for i in range(4):
    num = int(input("Enter your number"))

    if num%2!=0 :
        odd = odd + 1

    elif num % 2 == 0:
        even = even + 1

print("Even", even)
print("Odd", odd)