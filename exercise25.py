#Guessing Game Two
#Topics: Binary Search

i = 0
j = 100
m = 50

condition = int(input("Is your guess " + str(m) + "? (0 = too low, 1, = right, 2 = too high)"))

while condition != 1:
    if condition == 0:
        i = m + 1
    elif condition == 2:
        j = m - 1

    m = (i + j) / 2
    condition = int(input("Is your guess " + str(m) + "? (0 = too low, 1, = right, 2 = too high)"))



