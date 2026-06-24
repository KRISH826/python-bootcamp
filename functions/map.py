numbers = [1,2,3,4,5]

def _square(x): x**2
_square(10)

list(map(_square, numbers))

# lambda function with map

numbers1 = [1,2,3,4,5]

listing= list(map(lambda x: x*2, numbers1 ))
print(listing)

# can we map multiple iterables
numbers2=[2,1,5]
numbers3=[4,5,7]

added_num= list(map(lambda x,y: x+y, numbers2, numbers3))
print(added_num)

# map() convert list of strings into the integar
str_numbers= ['1', '2', '3', '4']
integar_num= list(map(int, str_numbers))
print(integar_num)


