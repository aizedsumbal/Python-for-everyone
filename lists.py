# lists in python

# declaring a list
list = [1,2,"Aized",3.01,'a','@#^']

# adding elements to a list

# concatenation
list = list + ["aized"]

# using the append method
list.append("sumbal")

# using the extend method
list.extend("sumbal")


list_2 = ["ammar", "saqib"]

# list.append(list_2)
list.extend(list_2)

# checking the length of the list
print(len(list))

# printing the elements of the list inside of a loop
for i in range(0, len(list)):
    print("element", i, "=", list[i])
