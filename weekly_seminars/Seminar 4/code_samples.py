
'''
A = 5
B = 2

print(A/B)

p = 4
q = 5
print(p**2 < 3*q)

e = 5/9
f = (1/3)*5*(1/3)
if e == f:
    print('e equals f')
if e != f:
    print('e not equal to f')

grade = 65 

if grade < 40:
    print('Fail')
else:
    print('Pass')
    if grade < 50:
        print('3rd')
    elif grade < 60:
        print('2:2')
    elif grade < 70:
        print('2:1')
    else:
        print('1st')

lower_bound = 2
upper_bound = 5

x = 1
while x < 7:
    print(lower_bound < x and upper_bound > x)
    x += 1

max_num = 5 # change from 1 to 100
my_sum = 0
for ii in range(max_num):
    # counter ii will run 0 to 9
    # so for 1 to 10, use ii+1
    my_sum = my_sum + (ii+1)
print('Sum from',1,'to',max_num,'is',my_sum)

numbers = [2, 4, 8, 10, 2, 4]
print(numbers[-6] == numbers[0])

numbers = [2, 4, 8, 10, 2, 4]
print(sum(numbers[1:3]))

numbers = [[1], [2, 3, 4], [5, 6], [7, [8, 9], 10]]
print(numbers[3][1][0])

verbs = ["eat", "sleep", "drink"]
gerunds = []
for verb in verbs:
	gerunds.append(verb + "ing")

print(gerunds)


value = 0
total = 0
while value < 10:
	if value % 2 == 0:
		pass
	elif value % 9 == 0:
		break
	else:
		total += value
	value += 1
print(total)


total = 0
factors = [2, 5, 10]
limit = 10
for i in range(limit):

	add = False

	for factor in factors:
		if i % factor == 0:
			add = True

	if add:
		total += i

print(total)
'''


start_list = [4, 1, 5, 6, 9, 0, 1, 6]


#Insertion sort
for i in range(1, len(start_list)):

	#Each element in the list will be the key, in order
	key = start_list[i]
	#j is the index of the element before the key
	j = i - 1

	#Step backwards through the list from the key, looking for values greater than than the key.
	while j>=0 and key < start_list[j]:
		#If a value is greater than the key, shift it along by one.
		start_list[j+1] = start_list[j]
		j -= 1

	#Place the key back into the list
	start_list[j+1] = key

print(start_list)



#This is a comment.
#This is another comment.

first_number = 10
second_number = 20

'''
if first_number > second_number:
	#You can put a comment inside an indented block of code
	print("First number is bigger")
else:
	print("Second number is bigger") #You can add comments after lines of code too
'''

for (a, x) in enumerate(matrix):
	for (b, y) in row:
		if y > a * b:
			y = a * b

for (row_index, row) in enumerate(matrix):
	for (col_index, value) in row:
		if value > row_index * col_index:
			value = row_index * col_index

#Variable names
camelCaseVariable = 1
CapitalizedVariable = 2
variable_with_underscores = 3

if camelCaseVariable == 1:
	print("Didn't skip a line")

if camelCaseVariable == 1:

	print("Skipped a line")












