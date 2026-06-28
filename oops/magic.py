# "__init__": "initializer method (initializes a new instance of a class)",
# "__str__": "string representation of an object",
# "__repr__": "official string representation of an object",
# "__len__": "length of an object",
# "__getitem__": "get an item from an object",
# "__setitem__": "set an item in an object",
# "__delitem__": "delete an item from an object",


# class Person:
#     pass

# person = Person()
# print(dir(person))

# # basic magic methods
# class PersonClass:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# personclass = PersonClass("krishnendu", 25)
# print(personclass)
# <__main__.PersonClass object at 0x00000229A6D18830> -- thats the default message how to change it ??

class PersonClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"    
    
    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})" 

personclass = PersonClass("krishnendu", 25)
print(personclass)

print(repr(personclass))




