#Check Primality Functions
def get_input(text = "Enter a number: "):
    return int(input(text))

num = get_input()
if num > 1:
 for i in range(2, num):
   if (num % i) == 0: #divisible
    print("prime")
   else: #not divisibile
    print("not prime")
