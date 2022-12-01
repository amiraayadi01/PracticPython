#Password Generator

import random
import string
import secrets

"""
l = [0,1,2,3,4,5,6,7,8,9,10,'a','b','c']
print("Your password is: ")
print(random.choices(l, k = 10))
"""

letters = string.ascii_letters
numbers = string.digits
symbol = string.punctuation

sequence = letters + numbers + symbol
pwd_len = 12

pwd =''
for i in range(pwd_len):
    pwd += ''.join(secrets.choice(sequence))
print(pwd)