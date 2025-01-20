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

# This is a list containing the total score in the same order as in names
totals = []
for i in range(len(names)):
	totals.append(Q1[i]+Q2[i]+Q3[i])

print(totals)

#Write your code for calculating the mean score here

mean = sum(totals)/len(totals)

print('mean', mean)

#Write your code for calculating the standard deviation here

variance = 0

for total in totals:
	variance += ((total-mean)**2)/len(totals)

standard_deviation = math.sqrt(variance)

print('standard_deviation', standard_deviation)

#Write your code for calculating the normalised marks here

normalised_marks = [mark-mean for mark in totals]

#Write your code for assigning grades here

grades = dict()

for index, name in enumerate(names):
	normalised_mark = normalised_marks[index]
	grade = ""
	if normalised_mark < -1*standard_deviation:
		grade = "Fail"
	elif -1*standard_deviation < normalised_mark < 0:
		grade = "C"
	elif 0 <= normalised_mark < standard_deviation:
		grade = "B"
	elif standard_deviation < normalised_mark:
		grade = "A"
	
	grades[name] = grade

for name in names:
	print(name, grades[name])


