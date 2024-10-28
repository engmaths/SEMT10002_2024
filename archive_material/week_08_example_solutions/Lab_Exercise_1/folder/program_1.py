import csv

with open('rainfall.csv') as file:
    print(file.read())

with open('../unit_description.txt') as f:
    f = list(f)
    print(f[2])

with open('data/xyz_data.csv', encoding='utf-8-sig') as file:
    file = csv.reader(file)
    file = list(file)
    print(file)
    file = file[1:]
    x = [int(f[0]) for f in file]
    z = [int(f[2]) for f in file]
    print(x, z) 

    product = [i*j for i, j in zip(x, z)]
    print(product)   