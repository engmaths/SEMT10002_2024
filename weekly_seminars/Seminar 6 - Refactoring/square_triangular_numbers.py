'''
This program finds how many square and triangular numbers upto a specified limit.
It then finds how many numbers are both square and triangular
'''

squares = []
number = 1
limit = 1000

while number**2 < limit:
	squares.append(number**2)
	number += 1

triangles = []
number = 1
Tn = (number * (number+1)) / 2

while Tn < limit:
	triangles.append(Tn)
	number += 1
	Tn = (number * (number+1)) / 2

both = []
for number in squares:
	if number in triangles:
		both.append(number)

print("I found", len(squares), "square numbers")
print("I found", len(triangles), "triangular numbers")
print("I found", len(both), "numbers that are both square and triangular")