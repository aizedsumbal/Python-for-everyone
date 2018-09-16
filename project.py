Grade = input("Enter your score here:")
##-----------------------------------------------------------------------------
try:
    Grade = int(Grade)
##-----------------------------------------------------------------------------


    if (Grade>100 or Grade<0):
        print("The score of a student should be between 0 and 100 including the bounds")

    elif(Grade>=90):
        print("Your Grade is:","A")

    elif(Grade>=80):
        print("Your Grade is:","B")

    elif(Grade>=70):
        print("Your Grade is:","C")

    elif(Grade>=60):
        print("Your Grade is:","C")

    elif(Grade>=50):
        print("Your Grade is:","D")
        
    else:
        print("Your Grade is:","UG")


##-----------------------------------------------------------------------------
except:
    print("Enter a number instead of alphabets")
##-----------------------------------------------------------------------------



