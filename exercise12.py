#List Ends

numInput = input("Enter a list: ")
numList = list(numInput)

def first_last(a_list):
    return [a_list[0], a_list[len(a_list) - 1]]

print(first_last(numList))