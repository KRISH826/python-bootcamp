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


# we have common opertaor also

# "__odd__(self,otger)": "Adds two objects using the + operator"
# "__sub__(self, other)": Substracts two objects using the - operator"
#"__mul__(self, other)": Multiplies two objects using the * operator"
#"__truediv__(self, other)": Divides two objects using the / operator
#"__eq__(self, other)": Compares two objects using the == operator
#"__it__(self, other)": checks if one obeject is less than another using the operator


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})" 

v1 = Vector(2,5) # that is default x y considered
v2 = Vector(3,8) #this is the otehr considered

print(v1 + v2)
print(v1 * v2)


# assignment









