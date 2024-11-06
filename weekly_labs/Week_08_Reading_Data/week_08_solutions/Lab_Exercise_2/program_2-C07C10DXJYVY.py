import csv

with open('rainfall.csv', encoding='utf-8-sig') as file:
    file = csv.reader(file)
    data = list(file)
    print(data)

    # Get numerical rainfall values
    data = data[1]

    # Convert to numerical data
    rainfall = []
    for item in data:
        rainfall.append(float(item))

    # Calculate the mean
    mean = sum(rainfall)/len(rainfall)
    print(mean)

    # Calculate the standard deviation
    variance = 0
    for r in rainfall:
        variance += ((r - mean)**2) 
    
    variance = variance / len(rainfall)

    standard_deviation = variance ** (1/2)

    # print(standard_deviation)






    # # # Calculate the standard deviation (alternative methods using list comprehensions)
    # SD = (sum([(v - mean)**2 for v in rainfall]) / len(rainfall))** 1/2
    # print(SD)

    # SD = sum([(v - mean)**2/ len(values) for v in values])** 1/2
    # print(SD)

    