import csv

# For week 9 exercise
import matplotlib.pyplot as plt

# with open('sensor_data.csv') as file:
with open('sensor_data.csv') as file:
    file = csv.reader(file)
    file = list(file)

    # Remove header
    file = file[1:]

    # Convert all data to numerical
    data_numerical = []
    for line in file:
        line_numerical = []
        for item in line:
            line_numerical.append(float(item))
        data_numerical.append(line_numerical)
    
    # # Alternative method with list comprehension
    # data_numerical = [[float(item) for item in line] for line in file]

    # Get time and sensor 1 column
    time, sensor_1 = [], []
    for line in data_numerical :
        time.append(line[0]*10**(-3)) # Time in s
        sensor_1.append(line[1])

    # # Alternative method using list comprehensions 
    # time = [line[0]*10**(-3) for line in data_numerical]
    # sensor_1 = [line[1] for line in data_numerical]


    ###########################################################
    ##    WEEK 8 ANSWER
    ###########################################################

    # Window size
    N = 5

    # Filtered data 
    filtered_data = []
    for n in range(len(sensor_1)):

        # Skip the first 4 values 
        if n < N-1:
            continue

        else:
            total = sum(sensor_1[n-(N-1):n+1])
            average = total / N
            filtered_data.append(average)

    # Save filtered data as column
    with open('filtered_sensor_data.csv', 'w') as f:
        f = csv.writer(f)
        for d in filtered_data:
            f.writerow([d])

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

        # # Save filtered data as column
        # with open('filtered_sensor_data.csv', 'w') as f:
        #     f = csv.writer(f)
        #     for d in filtered_data:
        #         f.writerow([d])

        filtered[str(N)] = filtered_data

    # Week 9 exercise
    plt.plot(time, sensor_1)
    # plt.plot(time[N-1:], filtered_data)

    for N in window:
        plt.plot(time[N-1:], filtered[str(N)])
    plt.xlabel('Time s')
    plt.ylabel('Distance mm')
    plt.show()



