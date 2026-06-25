# read a file

# with open("index.txt", 'r') as file:
#     content = file.read()
#     for line in content:
#          print(line.strip())  

with open("index.txt", 'w') as file:
    file.write('Hello World!\n')
    file.write('I am krishnendu panja')
        