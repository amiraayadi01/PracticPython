#List Overlap Comprhensions
#With random generated lists
import random

a = random.sample(range(1, 30), 12)
b = random.sample(range(1, 30), 12)

c = [i for i in a if i in b]
print(c)