'''temperatures = [9.1, 8.8, 7.6]
words = ['hello','how','you']
round_temp = []
for letter in "sharib zafar":
    round_temp.append(letter))

print(round_temp)

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for value in phone_numbers.values():
    print(value.replace('+', '00'))

def mean(*args):
    return sum(args)/len(args)
print(mean(1,3,4))'''

import pandas
import time
import os

while True:
    if os.path.exists("files/temps-today.csv"):
            data = pandas.read_csv("files/temps-today.csv")
            print(data.mean())
    else:
        print("file doesn't exist")
    time.sleep(20)