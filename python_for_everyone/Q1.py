mass=2
radius=3
velocity=input("Enter your velocity: ")
Tension= mass*(int(velocity)**2)/radius

if(Tension>60):
    print("The string will break.")

else:
    print("The string can withstand the velocity.")