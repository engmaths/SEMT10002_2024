from sys import argv
from subprocess import run
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

# default values of what we're looking for
expected_mean = 14.0
expected_standard_deviation = 1.8708286933869707
expected_grades = {'martin': 'Fail', 'arthur': 'B', 'hemma': 'A', 'josh': 'B'}
grades = dict()

# script ran - so check outputs make sense
test_lines = test_result.stdout.splitlines()
for line in test_lines:
    # break into words and take tehe first and last
    words = [w for w in line.lower().split(' ') if w!='']
    # look for key reports
    if 'mean' in words:
        try:
            mean = float(words[-1])
        except ValueError:
            raise(ValueError('Could not get a float for totals from last word in line:',line))
        print('Got mean score', mean,'from line',line)
    elif 'standard_deviation' in words:
        try:
            standard_deviation = float(words[-1])
        except ValueError:
            raise(ValueError('Could not get numerical value for standard_deviation from last word in line:',line))
        print('Got standard_deviation',standard_deviation,'from line',line)
    elif 'martin' in words:
        try:
            grades['martin'] = words[-1]
        except ValueError:
            raise(ValueError('Could not get value for Martins grade anomaly from last word in line:',line))
        print('Got grade for Martin',words[-1],'from line',line)
    elif 'arthur' in words:
        try:
            grades['arthur'] = words[-1]
        except ValueError:
            raise(ValueError('Could not get value for Arthurs grade anomaly from last word in line:',line))
        print('Got grade for Arthur',words[-1],'from line',line)
    elif 'hemma' in words:
        try:
            grades['hemma'] = words[-1]
        except ValueError:
            raise(ValueError('Could not get value for Hemmas grade anomaly from last word in line:',line))
        print('Got grade for hemma',words[-1],'from line',line)
    elif 'josh' in words:
        try:
            grades['josh'] = words[-1]
        except ValueError:
            raise(ValueError('Could not get value for Joshs grade anomaly from last word in line:',line))
        print('Got grade for Josh',words[-1],'from line',line)
    else:
        print('Ignoring line',line)

# check we got every value needed
assert mean is not None, 'Did not report a mean'
assert standard_deviation is not None, 'Did not report a standard_deviation'
assert len(grades.keys()) == 4, 'Did not report all grades'
print('Got all the data we needed')

# check error

assert(mean == expected_mean, f'Mean does not match. I expected {expected_mean}, but got {mean}')
assert((standard_deviation - expected_standard_deviation) < 1E-6, f'Standard deviation does not match. \
    I expected {expected_standard_deviation}, but got {standard_deviation}')

for key in expected_grades:
    assert(grades[key] == expected_grades[key], f'Wrong grade for martin. I expected {expected_grades[key]} but got {grades[key]}')


# check if output file was created and read its contents
output_filename = "grades.csv"  # Change as needed based on your script
if os.path.exists(output_filename):

    print(f'Output data file created: {output_filename}')

    with open(output_filename, 'r') as file:

        file = csv.reader(file)
        file = list(file)

        if len(file) == 5:
            print('Correct number of rows in output file')
        else:
            raise ValueError('Incorrect number of rows in output file')


        if (file[0] == ['Student', 'Question 1', 'Question 2', 'Question 3', 'Grade'] and 
            file[-1] == ['Josh', '4', '7', '3', 'A']):
            print('Correct values in output file')
        else:
            raise ValueError(f'Incorrect values in output file, got {file[0]} for first row of saved table and {file[-1]} for last row')

else:
    raise ValueError(f"Cannot find output file: {output_filename}")


# everything OK if we got to here
print('All tests passed')