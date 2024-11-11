'''
Student	Question 1	Question 2	Question 3
Martin	6	1	4
Arthur	3	8	4
Hemma	7	4	5
Josh	4	7	3
'''

import math 

names = ["Martin", "Arthur", "Hemma", "Josh"]
Q1 = [6, 3, 7, 4]
Q2 = [1, 8, 4, 7]
Q3 = [4, 4, 5, 3]


#Write your code for calculating the total score for each student here.
total = []

for i in range(len(names)):
	total.append(Q1[i] + Q2[i] + Q3[i])

#Write your code for calculating the mean score here

mean = sum(total)/len(total)

print('mean', mean)


# #Write your code for calculating the standard deviation here


vals_to_sum = []

for t in total:
	vals_to_sum.append((t - mean)**2 / len(total))

standard_deviation = math.sqrt(sum(vals_to_sum))

print('standard_deviation', standard_deviation)

#Write your code for calculating the normalised marks here

normalised_marks = []

for t in total:
	normalised_marks.append(t-mean)


#Write your code for assigning grades here

grades = {}

for student, mark in zip(names, normalised_marks):

	if mark < -standard_deviation:
		grade = 'Fail'
	elif -standard_deviation <= mark < 0:
		grade = 'C'
	elif 0 <= mark < standard_deviation:
		grade = 'B'
	else:
		grade = 'A'

	grades[student] = grade


for name in names:
	print(name, grades[name])

