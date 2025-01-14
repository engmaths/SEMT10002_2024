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

totals = []

for (index, name) in enumerate(names):
	totals.append(Q1[index] + Q2[index] + Q3[index])

mean = sum(totals) / len(names)


deviations = []

for total in totals:
	deviations.append((total - mean)**2)

standard_deviation = math.sqrt(sum(deviations) / len (names))

normalised_marks = []

for total in totals:
	normalised_marks.append(total - mean)

grades = dict()

for (index, mark) in enumerate(normalised_marks):
	if mark < -standard_deviation:
		grades[names[index]] = "Fail"
	elif mark < 0:
		grades[names[index]] = "C"
	elif mark < standard_deviation:
		grades[names[index]] = "B"
	else:
		grades[names[index]] = "A"

with open("grade_file.csv", 'w') as f:
	f.write('mean, ' + str(mean) + '\n')
	f.write('standard_deviation, ' + str(standard_deviation) + '\n')
	for name in names:
		f.write(name + ', ' + grades[name] + '\n')

with open("grade_file.csv", "r") as f:
	data = f.readlines()

	assert len(data) == 6, "File should contain 6 lines, but actually contains %d" % len(data)
	
	mean = float(data[0].split(',')[1])
	assert mean == 14.0, "Mean should be 14.0, but is actually %.3f" % mean

	standard_deviation = float(data[1].split(',')[1])
	assert standard_deviation > 1.87 and standard_deviation < 1.88, "Standard deviation should be between 1.87 and 1.88, but is actually %.3f" % standard_deviation

	martin_grade = data[2].split(',')[1].strip()
	assert martin_grade == 'Fail', "Martin's grade should be Fail, but is actually %s" % martin_grade

	arthur_grade = data[3].split(',')[1].strip()
	assert arthur_grade == 'B', "Arthur's grade should be B, but is actually %s" % arthur_grade

	hemma_grade = data[4].split(',')[1].strip()
	assert hemma_grade == 'A', "Hemma's grade should be A, but is actually %s" % hemma_grade

	josh_grade = data[5].split(',')[1].strip()
	assert josh_grade == 'B', "Josh's grade should be A, but is actually %s" % josh_grade




