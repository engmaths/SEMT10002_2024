import csv

# For week 9 exercise
import matplotlib.pyplot as plt

# with open('sensor_data.csv') as file:
with open('sensor_data.csv') as file:
    file = csv.reader(file)
    file = list(file)
    # print(file)

    # Remove header
    file = file[1:]

    # Remove time column
    time = [float(line[0])*10**(-3) for line in file]
    file = [line[1:] for line in file]

    # Convert to floating point values
    file = [[float(item) for item in line] for line in file]

    # First sensor data
    sensor_1 = [line[0] for line in file]


    ###########################################################
    ##    WEEK 8 ANSWER
    ###########################################################

    # Window size
    N = 5

    # Filtered data 
    filtered_data = []
    for n in range(len(sensor_1)):
        if n < N-1:
            continue

        else:
            total = sum(sensor_1[n-(N-1):n+1])
            average = total / N
            filtered_data.append(average)

    # Arrange as columns before saving 
    filtered_data_columns = [[f] for f in filtered_data]

    with open('filtered_sensor_data.csv', 'w') as f:
        f = csv.writer(f)
        f.writerows(filtered_data_columns)



    ###########################################################
    ##    WEEK 9 ANSWER
    ###########################################################

    # Window size
    window = [20, 10, 5]

    # Filtered data 
    filtered = {}
    

    for N in window:

        filtered_data = []
        
        for n in range(len(sensor_1)):
            if n < N-1:
                continue

            else:
                total = sum(sensor_1[n-(N-1):n+1])
                average = total / N
                filtered_data.append(average)

        # # Arrange as columns before saving 
        # filtered_data_columns = [[f] for f in filtered_data]

        # with open('filtered_sensor_data.csv', 'w') as f:
        #     f = csv.writer(f)
        #     f.writerows(filtered_data_columns)

        filtered[str(N)] = filtered_data


# Week 9 exercise
plt.plot(time, sensor_1)
# plt.plot(time[N-1:], filtered_data)

for N in window:
    plt.plot(time[N-1:], filtered[str(N)])
plt.xlabel('Time s')
plt.ylabel('Distance mm')
plt.show()



