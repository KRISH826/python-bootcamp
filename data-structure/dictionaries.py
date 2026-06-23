# Dictionary Python ka ek built-in mutable data structure hai jo data ko key-value pairs ke form mein store karta hai.

# Har value ek unique key ke saath associated hoti hai, aur hum key ki help se value ko access, update ya delete kar sakte hain.

students= {
    "name": "krishnendu",
    "age": 32,
    "grade": 55
}
print(type(students))
print(students["name"])

# accessing dictionaries
students2= {
    "name": "debjit",
    "age": 32,
    "grade": 80
}

print(students2.get("name"))
print(students2.get("grade"))
print(students2.get("school", "Not found"))

# add new key value
students2["school"] = "Kendriya Vidyalaya"
print(students2)

# delete key values
del students2["school"]
print(students2)

# get all the keys
print(students2.keys())

# get all the values
print(students2.values())

#get all key valye pairs
print(students2.items()) #its return form of tuples

# shallow copy
student3 = students2.copy()
students2["name"] = "panja"
print(students2)
print(student3)


# Itetrators in dictionaries
# you can use loops to iterate over dictionaries,keys values or items

# for student in students2.values():
#     print(student)

# for stu in students2.items():
#     print(stu)


for key,values in students2.items():
    print(f"key is {key} and value is {values}")

# nested dictonaries 
nested_students= {
    "student1": {
        "name": "krishnendu",
        "age": 32,
        "grade": 55
    },
    "student2": {
        "name": "debjit",
        "age": 32,
        "grade": 80
    }
}

# access nested dictionaries
print(nested_students["student1"]["grade"])

for students_id, stu_info in nested_students.items():
    print(students_id, stu_info)
    for key, value in stu_info.items():
        print(key, value)



# dictonary comprehension
sqaures = {x: x**2 for x in range(10) if x%2 == 0}
print(sqaures)

# practical questions
numbers = [1,2,2,3,4,5,6,6,7,7,7,8,1]
frequency={}

for number in numbers:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1

print(frequency)


# merge 2 dictonaries
dict1={"a":1, "b":2, "c":3}
dict2={"a": 2, "c": 5, "d": 6}

merge_dict= {**dict1, **dict2} #merge dictonaries
print(merge_dict)





