# Cows and Bulls

import random


def compare(number, user):
    cowbull = [0,0]
    for i in range(len(number)):
        if number[i] == user[i]:
            cowbull[1] +=1
        else:
            cowbull[0] +=1
    return cowbull

def cow_bull(list):
    # Counter Variables
    cow_count = 0
    bull_count = 0
    guess_count = 0

    for i, j in usernum:
        guess_count += 1
        if usernum == list:
            return True
        elif usernum[i] == list[j]:
            cow_count += 1
            print(cow_count + "cow")
        elif i == j:
            bull_count += 1
            print(bull_count + "bull")
        return guess_count

if __name__ == "__main__":
    usernum = list(input("Enter a random 4 digit number: "))
    print(cow_bull(comp_random_guess()))