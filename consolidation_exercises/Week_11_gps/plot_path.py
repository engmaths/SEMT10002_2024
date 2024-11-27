"""
Please note this script assumes all longitudes are north and all latitudes are west!
"""


from datetime import datetime
from pyproj import Transformer, CRS
import matplotlib.pyplot as plt

gps_file = "gps_walk.txt"

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


def main():
    print("\n\n\n\n")

    locations = get_locations(gps_file)
    formatted_locations = convert_locations(locations)
    longitudes = []
    for data in locations:
        longitudes.append(float(data[2]))


    projected_locations = project_locations(formatted_locations)
    projected_locations.sort(key=lambda x: x[0])
    easting, northing = get_easting_and_northing(projected_locations)
    # a = [i for i in range(len(northing))]
    plot_walk(easting,northing)
    # plt.scatter(a,northing,s=10)
    # plt.show()

    

if __name__ == "__main__":
    main()
