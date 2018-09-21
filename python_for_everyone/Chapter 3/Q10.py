altitude = input("Enter your altitude:")
altitude = int(altitude)

temperature = input("Enter your temperature:")
temperature = int(temperature)

boiling = 100
melting = 0

if altitude >= 300:
    boiling = boiling-1

if temperature >= boiling:
    print("Water is in gaseous state")
elif temperature > melting:
    print("Water is in liquid state")
elif temperature <= melting:
    print("Water is in solid state")
