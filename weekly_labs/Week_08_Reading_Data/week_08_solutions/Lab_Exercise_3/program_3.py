import csv

cities = ['London', 'Bristol', 'Manchester', 'Reading', 'Liverpool', 'Brighton']

populations = [8982000, 467000, 553000, 174224, 496000, 290000]

with open('data_1.csv', 'w') as file:
    file = csv.writer(file)
    file.writerow(cities)

with open('data_2.csv', 'w') as file:
    file = csv.writer(file)
    file.writerows([cities, populations])

# Convert rows to columns
data_as_cols = []
for c,p in zip(cities, populations):
    data_as_cols.append([c, p])

# # Alternative method using list comprehension
# data_as_cols = [[c, p] for c,p in zip(cities, populations)]

with open('data_3.csv', 'w') as file:
    file = csv.writer(file)
    file.writerows(data_as_cols)







