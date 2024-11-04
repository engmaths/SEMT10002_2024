import csv

with open('rainfall.csv') as file:
    print(file.read())

with open('../unit_description.txt') as f:
    f = list(f)
    print(f[2])

with open('data/xyz_data.csv', encoding='utf-8-sig') as file:
    file = csv.reader(file)

    # Make subscriptable
    file = list(file)

    # Remove header
    file = file[1:]

    product = []

    for f in file:
        product.append(int(f[0]) * int(f[2]))

    print(product) 

    # # An alternative method using list comprehensions
    # product = [int(f[0]) * int(f[2]) for f in file]
    # print(product)   