#Guessing Game One
import random

guess = int(input("Enter your guess: "))
a = random.randint(1, 9)

if guess < a:
    print("Too Low")
elif guess > a:
    print("Too High")
elif guess == a:
    print("Exactly Right")