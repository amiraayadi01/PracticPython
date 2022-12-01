#String Lists
user_input = str(input("Enter a sentence: "))
palindrome = user_input[::-1]
if user_input == palindrome:
        print("Your sentence is a palindrome!")
else:
        print("Your string is not a palindrome")