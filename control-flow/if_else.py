age=int(input("Enter your age: "))



# def _intage():
#     if (age>=18 and age<=25):
#         print("You can Tenegare")
#     elif (age>=15 and age<=18):
#         print("You can drive")
#     else:
#         print("You can not drive")

# _intage()

# def ageBase():
#     if(age> 16 and age <= 20):
#         print("You are Young")
#     elif(age>=21 and age <=28):
#         print("You are Mature")
#     elif(age>=29 and age <=35):
#         print("You are Old")
#         if(age>32 and age<34):
#             print("good age")
#     else:
#         print("You are Super Old")

# ageBase()        


# num= int(input("Enter your number: "))

# if(num>0):
#     print("Positive")
#     if(num % 2 == 0):
#         print("Even")
#     else:
#         print("Odd")    
# elif(num<0):
#     print("Negative")
# else:
#     print("Zero")

#determine if a year is a leap year 
# year=int(input("Enter your year: "))

# if(year% 4 == 0):
#     if(year% 100 == 0):
#         if(year% 400 == 0):
#             print(year, "Leap Year")
#         else:
#             print(year, "Not Leap Year")
#     else:
#         print(year, "Leap Year")
# else: 
#     print(year, "Not Leap Year")        



# assignment
#simple calculator program

# num1 = float(input("enter first num"))
# num2 = float(input("enter second num"))
# operation = input("enter operation(+, -, *, /)", )

# def calculator():
#     if(operation == '+'):
#         print(num1 + num2)
#     elif(operation == '-'):
#         print(num1 - num2)
#     elif(operation == '*'):
#         print(num1 * num2)
#     elif(operation == '/'):
#         print(num1 / num2)
#     else:
#         print("Invalid Operation")



# calculator()                

personAge=int(input("Enter your age: "))
is_student= input("Are you a student? (yes/no): ")

def studentageBase():
    if(age > 5):
        price = 10
        if(is_student == "yes"):
            price = 'free'
    elif(age>10 and age<=18):
        price = 20
        if(is_student == "yes"):
            price = 'free'
    else:
        price = 500
    return price    

studentageBase()
