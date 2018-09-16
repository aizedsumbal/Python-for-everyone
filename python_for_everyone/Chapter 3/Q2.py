check=input("Enter any decimal number:")
check=float(check)
if (check<0):
    print(" negative.")
elif (check>0):
    print(" positive.")
elif(check==0):
    print(" nuetral.")



if (check<0):
    check=check*-1
if (check<1):
    print("Your number is small")
elif (check<100000):
    print("Your number is large")