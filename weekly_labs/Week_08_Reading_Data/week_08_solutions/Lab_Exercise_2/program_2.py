import csv

with open('rainfall.csv', encoding='utf-8-sig') as file:
    file = csv.reader(file)
    file = list(file)
    
    print(file)

    values = [int(f) for f in file[1]]
    print(values)

    mean = sum(values)/len(values)
    print(mean)

    SD = (sum([(v - mean)**2 for v in values]) / len(values))** -2
    print(SD)

    SD = sum([(v - mean)**2/ len(values) for v in values])** -2
    print(SD)

    