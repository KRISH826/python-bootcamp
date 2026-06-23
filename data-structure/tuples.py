# Tuples
# introduction 
# tuples are ordered collections of items that are immutrable, they are similar to lists but they are immutiblilty makes theme diff, 
# they are used to store multiple items in a single variable
numbers = tuple([1,2,3,4,5,5])
print(numbers)

mix_tuple=(1,2,3,4,5,"krishnendu")
print(mix_tuple)

#accessing tuple
concatination_tuple = numbers + mix_tuple
print(concatination_tuple)

# immultable tuples of nature 
# tuple methods

print(numbers.count(5))
print(numbers.index(3)) #this count is begin in 0 

# packing and unpacking table
packed_tuple = 1, 'krishnend', 2.14
print(packed_tuple)

# unpacking tuple (if packed_table has 3 items u want to create 3 variables)
a,b,c = packed_tuple
print(a)
print(b)
print(c)

# unpacking with *
foods=('apple','banana','cherry', 1, 2.25, 'krishnendu')
first,*middle, last = foods
print(first)
print(middle)
print(last)

# nested tuple

nested_tuple = (1,2,3), (4,5,6), (7,8,9)
print(nested_tuple[0][1])

#with loop
for sub_tuple in nested_tuple:
        for item in sub_tuple:
            print(item, end = ' ')
        print()    