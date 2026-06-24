def default(parameter):
    if(parameter % 2 ==0):
        print('this is even')
    else:
        print('this is odd')

default(20)

def plusFunc(a,b):
    c = a+b
    print(c)
    return c

plusFunc(2,5)

# variablr length arguments
def print_numbers(*args):
    for numbers in args:
        print(numbers)

print_numbers(1,2,3,4,5,8,5,8,5)

# keywords arguments -- all the arguments all the valur is key pair arguments
def print_details(*args, **kargs):
    for number in args:
        print (f"position arguments: {number}")
    for key, value in kargs.items():
        print(f"{key} : {value}")

print_details(1,2,3,4,name= 'krish', age= "27")


# return statement

def multiplyFunc(a,b):
    return a*b   # we can return multiple value

multiple = multiplyFunc(2,4)   
print(multiple)



# PRACTICALE

def convert_tempt(temp, unit):
    if unit == "C":
        return temp * 9/5 + 32
    elif unit == "F":
        return (temp-32)*5/9
    else:
        return None

print(convert_tempt(10, "F"))        

# password checker

def passwordChecker(password):
    if len(password) < 6:
        print("that must be 6 characters")
    if not any(char.isdigit() for char in password):
        return False
    if not any (char.islower() for char in password):
        return False
    if not any (char.isupper() for char in password):
        return False
    if not any (char in '!@#$%^&*()_+' for char in password):
        return False
    else: 
        True

print(passwordChecker("Kris123**")) # its not working

# calculate the total cost of items in the shopping cart
cart = [
    {
        "name": "banana",
        "quantity": 3,
        "price": 25
    },
    {
        "name": "mango",
        "quantity": 1,
        "price": 10
    }
]

def calculate_total_cost():
   total_cost= 0
   for item in cart:
       total_cost += item["price"] * item["quantity"]
    
   return total_cost

print(calculate_total_cost())


# if string is palindrome

def is_palindrome(word):
    result = word.lower().replace(" ", "")
    print(result)
    return word == result[::-1]

print(is_palindrome("aba"))



