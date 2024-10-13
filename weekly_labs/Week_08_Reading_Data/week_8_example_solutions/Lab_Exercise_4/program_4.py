import csv

with open('sensor_data.csv') as file:
    file = csv.reader(file)
    file = list(file)
    print(file)

    # Remove header
    file = file[1:]

    # Remove time column
    file = [line[1:] for line in file]

    # Convert to floating point values
    file = [[float(item) for item in line] for line in file]
    print(file)

    # Convert to m
    file_as_m = [[item/1000 for item in line] for line in file]
    print(file_as_m)

    # Round to nearest cm
    file_as_m = [[round(item, 2) for item in line] for line in file]
    print(file_as_m[-1])

    # First sensor data
    sensor_1 = [line[0] for line in file_as_m]

    filtered_data = []

    # Window size
    N = 10

    # Filtered data 
    for i in range(len(sensor_1)):
        if i < N:
            continue

        else:
            total = sum(sensor_1[i-(N-1):i])
            average = total / N
            average = round(average, 2)
            filtered_data.append(average)

    print(filtered_data)

filtered_data = [[f] for f in filtered_data]

with open('filtered_sensor_data.csv', 'w') as f:
    f = csv.writer(f)
    f.writerows(filtered_data)

