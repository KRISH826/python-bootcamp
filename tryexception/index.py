try:
    result = 10/0
    print(result)
except Exception as e:
    print(e)


try: 
    a= b
except NameError as err:
    print(err)

try:
    result = 1/0
except ZeroDivisionError as err:
    print(err)
    print("Please enter the denominator greater than o")


# try:
#     num = int(input("Enter a number: "))
#     result = 10/num
# except ValueError as err:
#     print(err)
# except ZeroDivisionError as err:
#     print(err)
# except Exception as err:
#     print(err)
# else:
#     print(f"the result is {err}")


#try, catch, else and finally

try:
    num = int(input("Enter a number: "))
    result = 10/num
except ValueError as err:
    print(err)
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print(err)
else:
    print(f"the result is {result}")
finally:
    print("excution complete")


try:
    file = open("example.txt", 'r')
    result = file.read()
    print(result)
except FileNotFoundError:
    print("file is not found")
finally:
    print("the file is completed to read")












  