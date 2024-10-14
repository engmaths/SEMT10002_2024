import json

with open('sensor_data.json') as file:

    dictionary = json.load(file)

    print(dictionary)

    new_dictionary = {}

    for i in range(1, 4):
        sensor = dictionary['sensor_' + str(i)]
        mean = sum(sensor)/len(sensor)
        new_dictionary['mean_sensor_' + str(i)] = mean

with open('mean_sensor_data.json', 'w') as file:
    json.dump(new_dictionary, file)