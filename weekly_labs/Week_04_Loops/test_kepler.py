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
mean_anomaly = None
ecc_anomaly = None
eccentricity = None

# script ran - so check outputs make sense
test_lines = test_result.stdout.splitlines()
for line in test_lines:
    # break into words and take tehe first and last
    words = [w for w in line.lower().split(' ') if w!='']
    # look for key reports
    if 'mean' in words:
        try:
            mean_anomaly = float(words[-1])
        except ValueError:
            raise(ValueError('Could not get numerical value for mean anomaly from last word in line:',line))
        print('Got mean anomaly',mean_anomaly,'from line',line)
    elif 'eccentricity' in words:
        try:
            eccentricity = float(words[-1])
        except ValueError:
            raise(ValueError('Could not get numerical value for eccentricity from last word in line:',line))
        print('Got eccentricity',eccentricity,'from line',line)
    elif 'eccentric' in words:
        try:
            ecc_anomaly = float(words[-1])
        except ValueError:
            raise(ValueError('Could not get numerical value for eccentric anomaly from last word in line:',line))
        print('Got eccentric anomaly',ecc_anomaly,'from line',line)
    else:
        print('Ignoring line',line)

# check we got every value needed
assert mean_anomaly is not None, 'Did not report a mean anomaly'
assert ecc_anomaly is not None, 'Did not report an eccentric anomaly'
assert eccentricity is not None, 'Did not report an eccentricity'
print('Got all the data we needed')

# check error
kepler_err = ecc_anomaly - eccentricity*sin(ecc_anomaly) - mean_anomaly
print('M is',mean_anomaly)
print('E - e sin(E) is', ecc_anomaly - eccentricity*sin(ecc_anomaly))
assert kepler_err**2 < (1e-4*mean_anomaly)**2, f'Equation not close enough: error is {kepler_err}'

# everything OK if we got to here
print('Test passed: equation solved to sufficient tolerance')
