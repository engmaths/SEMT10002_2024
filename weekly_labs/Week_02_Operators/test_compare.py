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
test_lines = test_result.stdout.splitlines()
for line in test_lines:
    # break into words and take tehe first and last
    words = [w for w in line.lower().split(' ') if w!='']
    starts_with_num = float(words.pop(0))
    ends_with_num = float(words.pop(-1))
    # discount negatives
    if 'not' in words:
        print('Negatives blow my mind')
        print('Cannot verify', line)
        raise ValueError('Cannot handle use of NOT')
    # check statements match numbers given
    if 'greater' in words or 'more' in words:
        assert starts_with_num>ends_with_num, f'You said \"{line}\" but {starts_with_num} is not greater than {ends_with_num}'
        print('Verified a>b:', line)
    elif 'less' in words:
        assert starts_with_num<ends_with_num, f'You said \"{line}\" but {starts_with_num} is not less than {ends_with_num}'
        print('Verified a<b:', line)
    elif 'equal' in words or 'equals' in words:
        assert starts_with_num==ends_with_num, f'You said \"{line}\" but {starts_with_num} is not equal to {ends_with_num}'
        print('Verified a==b:', line)
    elif '0.1%' in words:
        assert starts_with_num/ends_with_num<1.001, f'You said \"{line}\" but {starts_with_num} is {100*(starts_with_num/ends_with_num-1):.2f}% greater than {ends_with_num}'
        assert ends_with_num/starts_with_num<1.001, f'You said \"{line}\" but {ends_with_num} is {100*(ends_with_num/starts_with_num-1):.2f}% greater than {starts_with_num}'
        print('Verified a and b close within 0.1%:', line)
    else:
        print('Could not understand following statement')
        print(line)
        exit(1)

# everything OK if we got to here
print('Test passed: all lines verified')
