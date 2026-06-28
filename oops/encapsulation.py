class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def getName(person):
    print(f"{person.name}")

person = Person("krishnendu", 25)
getName(person)


# class Animal:
#     def __init__(self, category, name, gender):
#         self.__name = name #private variable
#         self.__category = category #private variable
#         self.gender = gender

# def get_animal_name(person):
#     print(person.__name)


# animal = Animal("dog", "tom", 12)
# get_animal_name(animal)


class Animal:
    def __init__(self, category, name, gender):
        self._name = name #protected variable
        self._category = category #protected variable
        self.gender = gender

class Pet(Animal):
    def __init__(self, category, name, gender, owner):
        super().__init__(category, name, gender)
        self.owner = owner

def get_animal_name(person):
    print(person._name)

def get_animal_owner(owner, name):
    print(f"{owner} is the owner of {name}")

animal = Animal("dog", "tom", 12)
get_animal_name(animal)

pet = Pet("dog", "tom", 12, "krishnendu")
get_animal_owner(pet.owner, pet._name)


# getter and setter method with encapsulation
class Player:
    def __init__(self, name, category):
        self.__name = name
        self.__category = category
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name

    def get_category(self):
        return self.__category
    
    def set_category(self, category):
        if category == 'Football':
            self.__category = category
        else:
            print("not a valid category")


player = Player("krishnendu", "Football")
print(player.get_name())
print(player.get_category())

print(player.set_name("panja"))
print(player.set_category("cricket"))



