a = input("Write your number:")
sum = 0
for i in a:
    if(int(i) % 2 != 0):
        sum = sum + int(i)
print(sum)