number = int(input("Enter a number: "))
a = range(1, number + 1)
for i in a:
    if number % i == 0:
        print(i)