"""
Completed this by myself (Gilad), as I had to miss the in person session!
Note this script assumes all longsitudes are north and all latitudes are west!
"""


from datetime import datetime
from pyproj import Transformer
import matplotlib.pyplot as plt
from math import sqrt

gps_file = "consolidation_exercises\\Week_11_gps\\gps_walk.txt"

def get_locations(file_path):
    """
    Opens gps data file and gets parses location data
    """
    with open(file_path,"r") as file:
        # Get all lines that start with '$GPGGA', these are the lines that contain location data
        location_lines = [line.strip() for line in file if line.startswith("$GPGGA")]
        # Format each line and create a list of lists of format [time, latidue (N), longitude(W)]
        formatted_locations = [[line.split(",")[i] for i in [1,2,4]] for line in location_lines]
        return formatted_locations

def convert_to_time(time_string):
    """Converts the time data point to a string"""
    return datetime.strptime(time_string, '%H%M%S.%f')

def convert_coordinate_string_to_digit(coordinate_string, negative=False):
    """Converts a coordinate string into a digit, whose units is just decimal degrees (i.e. the minutes are converted into decimals)"""
    split_string = coordinate_string.split(".")
    degrees = int(split_string[0][:-2])
    minutes = float(split_string[0][-2:] + "." + split_string[1])
    # Convert into decimal degrees
    decimal_degrees = degrees + (minutes/60)
    if negative:
        decimal_degrees *= -1
    return decimal_degrees


def convert_locations(locations: list[list[str]]):
    """
    Converts values into useable data types.
    Converts time into time object.
    Converts latitudes and longitudes into decimal numbers (making sure to make the longitude negative).
    """

    converted_location_data = [[convert_to_time(time), convert_coordinate_string_to_digit(latitude), convert_coordinate_string_to_digit(longitude, negative=True)] for time, latitude, longitude in locations]
    
    return converted_location_data

def project_locations(locations):
    """Projects coordinates from GPS coordinate system to UK national grid coordinate system"""
    transformer = Transformer.from_crs(4326, 27700)
    projected_locations = [[time, transformer.transform(latitude, longitude)] for time, latitude, longitude in locations]
    return projected_locations

def plot_walk(eastings, northings):
    """Plots the walk on a grid"""
    plt.plot(eastings,northings)
    plt.xlabel('Easting (m)')
    plt.ylabel('Northing (m)')
    plt.grid(True)
    plt.gca().set_aspect('equal',adjustable='datalim')
    plt.show()

def get_easting_and_northing(locations):
    """Our data is in lists, each corresponding of one location. We want a long list consisting of every easting, and another list consisting of every northing"""
    eastings = []
    northings = []
    for data_point in locations:
        time = data_point[0]
        easting, northing = data_point[1]
        eastings.append(easting)
        northings.append(northing)
    return eastings, northings


def calculate_distance(p1: tuple,p2: tuple):
    """Calculates distance between two coordinate points using pythagoras."""
    return sqrt((p2[1]-p1[1])**2+(p2[0]-p1[0])**2)

def get_total_distance(eastings, northings):
    """
    Calculates total distance walked.
    Finds the distance between each adjacent location data point and sums them.
    """
    total = 0
    coordinates = list(zip(eastings,northings))
    for i in range(1, len(coordinates)):
        total += calculate_distance(coordinates[i-1],coordinates[i])
    return total


def get_total_time(locations):
    """Calculates the total time of the walk."""
    times = [i[0] for i in locations]
    time_diff =  max(times)-min(times)
    return time_diff.total_seconds()


def main():

    locations = get_locations(gps_file)
    formatted_locations = convert_locations(locations)

    projected_locations = project_locations(formatted_locations)
    easting, northing = get_easting_and_northing(projected_locations)

    # Calculate average speed
    distance_walked = get_total_distance(easting,northing)
    total_time = get_total_time(projected_locations)

    average_speed = distance_walked/total_time
    print(f"The average walking speed was: {average_speed} m/s\n\nTravelled: {distance_walked} metres\nTime: {total_time} seconds")

    #Plots the walk
    plot_walk(easting,northing)

if __name__ == "__main__":
    main()
