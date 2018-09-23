max = 0
min = 1000000
for i in range(4):
    num = int(input("Enter your number"))

    if num > max:
        max = num

    if num < min:
        min = num

print("max :", max)
print("min :", min)

