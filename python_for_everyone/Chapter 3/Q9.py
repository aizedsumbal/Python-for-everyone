temperature = input("Enter your temperature:")
temperature = int(temperature)

if(temperature>=100):
    print("Water is in gaseous state")
elif(temperature>0):
    print("Water is in liquid state")
elif(temperature<=0):
    print("Water is in solid state")
