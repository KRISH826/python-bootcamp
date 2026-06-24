lst = [1,2,3,4,5,7,8,9]

def even(num):
    if(num % 2 == 0):
        return True
    
listResult = list(filter(even, lst))
print(listResult)

numbers = [1,2,45,5,4]
finalResult = list(filter(lambda x: x > 5, numbers))
print(finalResult)

# lambda function with multiple function
numbers1 = [1,2,3,5,6,7,8,9,9,10,11]
even_and_geaterthan = list(filter(lambda x: x>5 and x % 2==0, numbers1))
print(even_and_geaterthan)

dict = [
    {
        'name': 'krish',
        'age': 32
    },
    {
        'name': 'debjit',
        'age': 17
    }
]

def condition_age(person):
    if person["age"] > 25:
        return person["age"] 

condition_age_result = list(filter(condition_age, dict))
print(condition_age_result)