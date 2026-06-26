# a class is blueprint for creating objects.attrubutes, methods

class Car:
    pass

audi = Car()
print(audi)
print(type(Car))

audi.window = 4
print(audi.window)

tata =Car()
tata.doors=4
print(tata.doors)
tata.windows=4
print(tata.windows)

print(dir(tata))


# instance variables and methods

class Dog:
    # constrictor
    def __init__(aself,name,age):
        aself.name = name
        aself.age = age

# create objects
dog1= Dog("buddy", 28)
print(dog1)
print(dog1.name) 

dog2 = Dog("tommy", 22)
print(dog2)
print(dog2.name)


# instance method
# define a class with instance method
class Cats:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def barkingDog(self):
        print (f"{self.name} is barking")
        # print (f"{self.age} is barking")
    def deadDog(self):
        print(f"{self.name} is dead")     
        

cat1 = Cats('Tommy', 26)
print(cat1)

# bank modelling
class BankAccounts:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Deposit of {amount} is successful")
    def withDraw(self, amount):
        self.balance = self.balance - amount
        print(f"Withdrawal of {amount} is successful")


account = BankAccounts('krishnendu', 50000)
print(account.balance)
print(account.owner)

account.deposit(10000)
print(account.balance)

account.withDraw(5000)
print(account.balance)




