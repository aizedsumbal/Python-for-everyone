sums = 0
cum = ""
for i in range(4):
    num = int(input("Enter your number:"))
    sums = sums + num
    cum += str(sums) + ", "
print(cum)