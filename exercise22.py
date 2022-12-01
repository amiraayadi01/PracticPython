#Read From File
counter_dict = {}
with open('Training_01.txt', 'r') as open_file:
    line = open_file.readline()
    while line:
        line = line.strip()
        if line in counter_dict:
            counter_dict[line] += 1
        else:
            counter_dict[line] = 1
        line = open_file.readline()

print(counter_dict)


