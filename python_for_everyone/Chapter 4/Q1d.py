a = int(input("Write your starting number:"))
b = int(input("Write your ending number:"))
sum = 0
for i in range(a,b+1):
    if(i%2 != 0):
        sum = sum + i
print(sum)
