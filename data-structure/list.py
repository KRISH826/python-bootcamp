list=["krishnendu", "debjit", "panja", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list)
print(list[1])

fruits=["apple","banana", "guava", "kiwi", "mango", "orange"]

print(fruits[1:]) #this is the range of the list index 1 to end
print(fruits[1:3]) #this is the range of the list index 1 to 3 will be show
print(fruits[-1]) # last index

# how to change the value of any index
fruits[2] = "cherry"
print(fruits)
# how to do that charactor by charactor
fruits[1:] = "watermelon"
print(fruits)


students = ["krish", "debkot", 'ranju', 'krishnendu']
students.append('panja') # u can append this list to the end
print(students)

# add any item in the index
students.insert(2, "debjit")
print(students)

popped_stu = students.pop()
print(popped_stu)
print(students)

index1=students.index("ranju") #how to see the index of the item
print(index1)

print(students.count("krishnendu")) #how many krishnendu in the list


kitchen=["pan", "bowl", "fork", "spoon", "knife"]
kitchen.sort() #sort the list
print(kitchen)

#reverse the list
kitchen.reverse()
print(kitchen)

# kitchen.clear() # clear the list
# print(kitchen)

# slicing method

brands=['pete england', 'titan', 'turtle','raymond', 'nike']
numbers=[1,2,3,4,5,6,7,8,9,10]

print(numbers[::2]) #::2 is step


# iterate the list
def enumerateList():
    for index, brand in enumerate(brands):
        print('the index of', index, 'is', index, brand)

enumerateList()


# list comprehension
brandList=[]
for b in range(10):
    brandList.append(b**2)
print(brandList)

[x**2 for x in range(10)]

#basic
square=[n**2 for n in range(5)]
print(square)

# with condition
even = [num for num in range(10) if num%2 == 0]  
print(even)

list1=[1,2,3,4]
list2=['a','b','c','d']

pair = [[i,j] for i in list1 for j in list2]

print(pair)

words = ["hello", "krishnendu", "tanu", "rittik"]
lengths = [len(word) for word in words]
print(lengths)






