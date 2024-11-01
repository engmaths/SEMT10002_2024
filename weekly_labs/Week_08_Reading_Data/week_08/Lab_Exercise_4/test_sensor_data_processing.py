# Test script for comparison assignment
#
# run python test_compare.py <your script name>
#
# Test script will run your file and check the statements for inconsistency
#
# Note there are security issues with code like this.  Calling user-supplied code from your
# own is not recommended.  This is just a workaround to make it easy to assess.
#

from sys import argv
from subprocess import run
from math import sin
import ast
import os
import csv

# check right number of arguments
if len(argv)!=2:
    print('Usage: python', argv[0], '<script filename>')
    raise ValueError('Script name not provided')

# run supplied script and capture output
script_name = argv[1]
print('Running Python script', script_name)
test_result = run(['python', script_name],
                  capture_output=True,
                  text=True,
                  check=False)

# print some information if there's an error
exit_code = test_result.returncode
if exit_code==0:
    print('Script ran OK')
else:
    print('Script had error, code', exit_code)
    print('Output is below')
    print()
    print(test_result.stdout)
    print(test_result.stderr)
    raise ValueError('Script terminated with error')


# script ran - so check outputs make sense
test_lines = test_result.stdout

# # check the script prints an output
# if test_lines=='':
#     raise ValueError('The script did not print an output')

# # convert string to python object 
# test_lines = ast.literal_eval(test_lines)
# print(type(test_lines))

# # check the output is a list
# if isinstance(test_lines, list):
#     print('A list of sensor values is printed')
# else:
#     raise ValueError('A list of sensor values was not printed')

# # check number if list values is correct
# if len(test_lines) == 3:
#     print('The correct number of values appear in the list printed')
# else:
#     raise ValueError('An incorrect number of values appear in the list printed')

# # check list values are correct
# if test_lines[0] == 0.31 and test_lines[1] == 0.3 and test_lines[2] == 0.3:
#     print('The values in the list are correct')
# else:
#     raise ValueError('At least one of the values in the list printed is incorrect')

# check if output file was created and read its contents
output_filename = "filtered_sensor_data.csv"  # Change as needed based on your script
if os.path.exists(output_filename):

    print(f'Output data file created: {output_filename}')

    with open(output_filename, 'r') as file:

        file = csv.reader(file)
        file = list(file)

        if len(file) == 297:
            print('Correct number of rows in output file')
        else:
            raise ValueError('Incorrect number of rows in output file')

        # if float(file[0][0]) == 1.33 and float(file[-1][0]) == 0.29:
        #     print('Correct values in output file')
        # else:
        #     raise ValueError('Inorrect values in output file')

        if round(float(file[0][0]), 2) == 250.96 and round(float(file[-1][0]),2) == 53.15:
            print('Correct values in output file')
        else:
            raise ValueError('Inorrect values in output file')

else:
    raise ValueError(f"Cannot find output file: {output_filename}")

# everything OK if we got to here
print('Test passed: Sensor data processed correctly')
