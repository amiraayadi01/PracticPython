#Element Search

def binary_search(ordered_list, number):
    start = 0
    end = len(ordered_list) - 1
    while end >= start:
        mid = (start + end) // 2
    if ordered_list[mid] == number:
        return True
    else:
        if number < ordered_list[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return False

list = [1, 2, 3, 4, 5]
x = 3
binS = binary_search(list, x)

if binS != -1:
    print(str(x) + " is inside the list")
else:
    print(str(x) + " is not inside the list")


