# read a file

# with open("index.txt", 'r') as file:
#     content = file.read()
#     for line in content:
#          print(line.strip())  

# with open("index.txt", 'w') as file:
#     file.write('Hello World!\n')
#     file.write('I am krishnendu panja')
        
#append mode
with open("index.txt", 'a') as file:
    file.write('hey google\n') 
    file.write('hey ashiqui how are you??')

#writing a list of lines

lines= ['\nfirst line \n', 'second line \n', 'third line \n']
with open("index.txt", 'a') as file:
    file.writelines(lines)

# binary files
with open('example.bin', 'wb') as file:
    file.write(b'\x01\x02\x03')

with open('example.bin', 'rb') as file:
    content = file.read()
    print(content)


# read the content from source text file and write to a destination text file #copying a text file
with open('index.txt', 'r') as source_file:
    content = source_file.read()

with open('destination.txt', 'w') as destination_file:
    destination_file.write(content)


# read a text file and count the number of lines,words and charactors
def count_text_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        linesLen = len(lines)
        words = sum(len(line.split()) for line in lines)
        char_len = sum(len(line) for line in lines)
        print(linesLen, words, char_len)

count_text_file('index.txt')


# writng and then reading the file

with open("example2.txt", 'w+') as file:
    file.write('Hello World!\n')
    file.write('I am krishnendu panja')  

    file.seek(0)

    content = file.read()
    print(content)
