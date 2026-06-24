#what is lambda function

addition = lambda a,b:a+b

print(addition(5,2))

even= lambda num:num%2 == 0
print(even(13))

numbers= [1,2,3,4,5]
numlambda = list(map(lambda x: x**2, numbers))
print(numlambda)