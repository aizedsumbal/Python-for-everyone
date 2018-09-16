thelist =[]
i=True
while i:
    x=input("Write a name:")
    thelist.append(x)
    y=input("Do you want to continue Yes or No:")
    if(y=="No"):
        print(len(thelist))
        break
