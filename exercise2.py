#Odd or Even
number = int(input("Please enter a number: "))
print("The number you entered is even") if number % 2 == 0 else print("The number you entered is odd")
if number % 4 == 0:
 print("The number is a multiple of 4")
num = int(input("Please enter number 1: "))
check = int(input ("Please enter number 2: "))
if check % num == 0:
    print("Number 1 divides evenly into Number 2")
else:
    print("Number 1 does not divide evenly into Number 2")