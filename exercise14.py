#list Remove Duplicates

#Using the set() keyword
def no_duplicates(a_list):
    return list(set(a_list))

#Using a loop and constructing a list
def no_duplicates_loop(a_list):
    b = []
    for i in a_list:
        if i not in b:
            b.append(i)
    return b


a_list = [1, 2, 2, 2, 3, 4, 4, 5, 5, 6]
print(no_duplicates_loop(a_list))
print(no_duplicates(a_list))

