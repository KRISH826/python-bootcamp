# __package__
from math import sqrt, pi, pow, floor
from package.maths import *
# from package.maths import addition
import numpy as np

numbers = 24587.58555
print(floor(numbers))
print(sqrt(4))
print(pi)

print(addition(2,4))
print(substraction(4, 1))
# numpy

import random
print(random.randint(1, 100)),
print(random.choice(["apple", "banana", "mango"]))


# file and directories
# import os
# print(os.getcwd())
# os.mkdir('test_dir')

# high level opertations
import shutil
# shutil.copyfile('source.txt', 'destination.txt')


# data serialization

import json
data={
    'name': 'krishnendu',
    'age': 32
}
json_str = json.dumps(data)
print(type(json_str))
# json.loads()

import csv

with open('example.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['name', 'age'])
    writer.writerow(['krish', 32])

with open('example.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)    

# Date Time
from datetime import datetime,timedelta
    
now = datetime.now()
print(now)

yesterday = now - timedelta(days=2)
print(yesterday)


# time

import time

print(time.time())
time.sleep(2)
print(time.time())

import re
# for match pattern





