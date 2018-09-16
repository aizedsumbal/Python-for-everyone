def bad_code():
    radius = 3
    velocity = [1, 10, 20, 40]
    mass = input("Write the mass.")
    tension1 = float(mass) * velocity[0] ** 2 / radius
    tension2 = float(mass) * velocity[1] ** 2 / radius
    tension3 = float(mass) * velocity[2] ** 2 / radius
    tension4 = float(mass) * velocity[3] ** 2 / radius

    valid = []
    if (tension1 < 60):
        valid.append(tension1)

    if (tension2 < 60):
        valid.append(tension2)

    if (tension3 < 60):
        valid.append(tension3)

    if (tension4 < 60):
        valid.append(tension4)

    print(valid)
    max_tension = max(valid)

    if (max_tension == tension1):
        print(max_tension)
        print("maximum velocity: ", velocity[0])
    elif (max_tension == tension2):
        print(max_tension)
        print("maximum velocity: ", velocity[1])
    elif (max_tension == tension3):
        print(max_tension)
        print("maximum velocity: ", velocity[2])
    elif (max_tension == tension4):
        print(max_tension)
        print("maximum velocity: ", velocity[3])

def good_code():
    mass = input("Enter the mass of the object: ")
    mass = float(mass)

    radius = 3.0
    velocity = [1,10,20,40]
    tension = []
    valid = []
    for i in velocity:
        t = (mass * (i**2))/radius
        tension.append(t)

    for i in tension:
        if (i<60):
            valid.append(i)
        else:
            valid.append(0)

    max_tension = max(valid)
    i = valid.index(max_tension)


    print("Maximum Velocity is: ",velocity[i])
good_code()