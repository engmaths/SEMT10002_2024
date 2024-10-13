import csv

with open('sense.csv') as file:
    file = csv.reader(file)
    file = list(file)
    print(file)
    file = file[1:]
    file = [[float(item) for item in line] for line in file]
    file_as_mm = [[round(item,1)*10 for item in line] for line in file]
    print(file_as_mm)

with open('sense_mm.csv', 'w') as f:
    f = csv.writer(f)
    f.writerows(file_as_mm)