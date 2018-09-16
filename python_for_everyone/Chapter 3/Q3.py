number=input("Enter an number:")

number = abs(int(number))

if(number >= 10000000000):
    print("Number has ELEVEN digits")
elif(number>=1000000000):
    print("Number has TEN digits")
elif(number>=100000000):
    print("Number has NINE digits")
elif(number>=10000000):
    print("Number has EIGHT digits")
elif(number>=1000000):
    print("Number has SEVEN digits")
elif(number>=100000):
    print("Number has SIX digits")
elif(number>=10000):
    print("Number has FIVE digits")
elif(number>=1000):
    print("Number has FOUR digits")
elif(number>=100):
    print("Number has THREE digits")
elif(number>=10):
    print("Number has TWO digits")
elif(number>=0):
    print("Number has ONE digits")
else:
    print("You have exceeded the limit of number")