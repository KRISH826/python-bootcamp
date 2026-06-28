import os
new_directory = "package"

# create
# os.mkdir(new_directory)
# print(f"Directory '{new_directory}' created successfully.")

#listing file and directions
items = os.listdir('.')
print(items)

path = "example.txt"
if os.path.exists(path):
    print(f"the file '{path}' exists")
else:
    print(f"the file '{path}' does not exist")    


# checking its a file or directory

path = "package"

if os.path.isfile(path):
    print(f"the file '{path}' is a file")
elif os.path.isdir(path):
    print(f"the file '{path}' is a directory")
else:
    print(f"the file '{path}' does not exist and is neither a file nor a directory")        