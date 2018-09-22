print("Aizedtech welcomes you to the place where you get paid ")

name = (input("What is your full name:"))
Salary = int(input("Write your hourly wage."))
Employeeid = int(input("Write your Employee ID:"))

PIN = input("Please enter your Personal Identification Number")
hours = input("How many hours did you work:")
hours = float(hours)

if hours > 40 :
    newwage = (Salary / 100)*150
    overtime = hours-40
    overtmesalary = overtime * newwage
    normal_salary = 40 * Salary
    total_salary = overtmesalary + normal_salary
else :
    total_salary = hours * Salary

print("Name:", name)
print("Employee ID", Employeeid)
print("You are going to receive $", total_salary)