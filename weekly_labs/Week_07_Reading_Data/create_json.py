import csv
import json

with open('sense.csv', newline='', encoding='utf-8-sig') as file:
	file = csv.reader(file) 
	file = list(file)
	headings = file[0]
	file = [[float(i) for i in j] for j in file[1:]]
	file = list(zip(*file))
	print(file)

dictionary = {}
for i in range(3):
	dictionary[headings[i]] = file[i]

print(dictionary)

with open('sensor_data.json', 'w') as file:
    json.dump(dictionary, file)