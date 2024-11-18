def transform_number(number):
	new_number = number**2 + 4
	return new_number

first_number = 2
transformed_number =  transform_number(first_number)
print(transformed_number)


import math 

vector1 = (2, 3, 4)
vector1_length = math.sqrt(vector1[0]**2 + vector1[1]**3 + vector1[2]**2)

vector2 = (4, 5, 6)
vector2_length = math.sqrt(vector2[0]**2 + vector2[1]**3 + vector2[2]**2)

vector3 = (7, 8, 9)
vector3_length = math.sqrt(vector3[0]**2 + vector3[1]**3 + vector3[2]**2)

def calculate_vector_length(x, y, z):
	return math.sqrt(x**2 + y**2 + z**2)

vector1 = (2, 3, 4)
vector1_length = calculate_vector_length(vector1)

vector2 = (4, 5, 6)
vector2_length = calculate_vector_length(vector2)

vector3 = (7, 8, 9)
vector3_length = calculate_vector_length(vector3)