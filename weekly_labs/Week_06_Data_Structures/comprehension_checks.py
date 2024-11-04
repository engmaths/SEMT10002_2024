
names = ["Martin", "Hemma", "Arthur", "Josh"]
print(names[1])

names = ["Martin", "Hemma", "Arthur", "Josh"]
print(names[3])

names = ["Martin", "Hemma", "Arthur", "Josh"]
print(names[4])

names = ["Martin", "Hemma", "Arthur", "Josh"]
print(names[-1])

names = ["Martin", "Hemma", "Arthur", "Josh"]
print(names[-5])

names = ["Martin", "Hemma", "Arthur", "Josh"]
print(names[-3]==names[0])

numbers = [1, 4, 9, 16, 25]
print(numbers[:2])

numbers = [1, 4, 9, 16, 25]
print(numbers[3:])

numbers = [1, 4, 9, 16, 25]
print(numbers[1:3])

numbers = [1, 4, 9, 16, 25]
print(numbers[100:200])

numbers = [1, 4, 9, 16, 25]
print(numbers[:-2])

numbers = [1, 4, 9, 16, 25]
print(numbers[:])

numbers = [1, 4, 9, 16, 25]
print(numbers[0:4:2])

numbers = [1, 4, 9, 16, 25]
print(numbers[::-1])

nested_numbers = [1, [2, 3], [4, 5, 6]]
print(nested_numbers[1])

nested_numbers = [1, [2, 3], [4, [5, 6]]]
print(len(nested_numbers[2]))

print(nested_numbers[0] - nested_numbers[2][0])

names = ["Martin", "Hemma", "Arthur", "Josh"]
print('martin' in names)

names = ["Martin", "Hemma", "Arthur", "Josh"]
print('Wilbur' not in names)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
evens = [2, 4, 6, 8]
for number in numbers:
	if number in evens:
		print(number)

robot_pose = (0, 0, 0)
print(robot_pose[1])

robot_pose[0] = 1
print(robot_pose[0])

grades = dict()
grades['martin'] = 'A'
grades['arthur'] = 'B'
print(grades['A'])
print(grades['arthur'])






