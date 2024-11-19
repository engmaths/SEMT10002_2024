def get_square_numbers(limit):
	
	squares = []

	while number**2 < limit:
		squares.append(number**2)
		number += 1

	return squares

def get_triangular_numbers(limit):

	triangles = []
	number = 1
	Tn = (number * (number+1)) / 2

	while Tn < limit:
		triangles.append(Tn)
		number += 1
		Tn = (number * (number+1)) / 2

	return triangles

def get_square_and_triangular_numbers(squares, triangles):

	both = []
	for number in squares:
		if number in triangles:
			both.append(number)


squares = get_square_numbers(limit)
triangles = get_triangular_numbers(limit)
both = get_square_and_triangular_numbers(squares, triangles)
print("I found", len(squares), "square numbers")
print("I found", len(triangles), "triangular numbers")
print("I found", len(both), "numbers that are both square and triangular")

