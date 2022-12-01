#File Overlap
#Topics: Reading a file, Converting data types, Lists

with open('primenumbers.txt', 'r') as prime_file:
    data = prime_file.read()
    data_into_list = data.replace("\n", " ").split()

with open('happynumbers.txt', 'r') as happy_file:
    data1 = happy_file.read()
    data1_into_list = data1.replace("\n", " ").split()

print([x for x in data_into_list if x in data1_into_list])


