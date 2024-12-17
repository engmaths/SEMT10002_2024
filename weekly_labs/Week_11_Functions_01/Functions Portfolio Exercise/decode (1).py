''' Task 1 - Caesar cipher
Write your code for implementing the Caesar cipher here.
'''
def caesar_cipher(plaintext, shift):
	encoded_text = ""
	for character in plaintext:
		encoded_text += shift_character(character, shift)
	
	return encoded_text

def shift_character(character, shift):
	"""Shifts a character within 'a'-'z' range."""
	if 'a' <= character <= 'z':
		# Convert ascii character to integer equivalent
		ascii_integer_equivalent = ord(character)
		# Shift the character
		shifted_value = ascii_integer_equivalent + shift

		# Check to see if shifted value has gone further than 'z'
		if shifted_value > 122:
			shifted_value -= 26
		elif shifted_value < 97:
			shifted_value += 26

		# Convert back into unicode equivalent
		encoded_character = chr(shifted_value)
		return encoded_character
	return character

'''
The code below is a test function for your code. It will run automatically when you run the script. Do not modify it. 
To pass this assignment, your code must pass all the tests.
'''

def test_caesar_cipher():

	#The assert function will raise an error if the expression contained within it doesn't evaluate to True
	assert caesar_cipher('a', 1) == 'b', "Test 1 failed"
	assert caesar_cipher('a', 2) == 'c', "Test 2 failed"
	assert caesar_cipher('z', 1) == 'a', "Test 3 failed"
	assert caesar_cipher('a', -1) == 'z', "Test 4 failed"
	assert caesar_cipher('hello', 3) == 'khoor', "Test 5 failed"
	assert caesar_cipher('khoor', -3) == 'hello', "Test 6 failed"

	print("Encoding tests passed - great job!")

''' Task 2 - Decoding
Write your code for decoding a message when we don't know the shift. 
You are given a list of words that the message may be composed of. 
Your code should work by *brute force* i.e it should check all possible shifts until it finds a match
'''

word_list_file = 'word_list.txt'

def get_allowed_words(file_path):
	allowed_words = []
	with open(file_path,"r") as allowed_words_file:
		for word in allowed_words_file:
			allowed_words.append(word.strip())
	return allowed_words

def contains_uppercase(word):
	"""
	Returns True if the word contains any uppercase characters
	"""
	return any([i for i in word if i.isupper()])




def decode_message(words, file):
	"""
	Takes a string assumed to be encoded using Caesar cipher, and attempts to decode it using bruteforce.
	Checks every possible shift of caesar cipher and check's if decoded message contains words found in 'file'. If so, it returns the new decoded message.
	"""
	# Get list of allowed words
	allowed_words = get_allowed_words(file)


	# If input contains uppercase, rejects input
	if contains_uppercase(words):
		return "Invalid character in message"

	# Decoding caesar cipher is the same as encoding with negative value of shift. 
	# E.g. If 'hello' is encoded with shift 3 it becomes 'khoor'.
	#      If 'khoor' is encoded with shift -3 it becomes 'hello'.
	
	deciphered_words = ""
	# Check all shifts
	for shift in range(26):
		decoded_message = caesar_cipher(words,-shift)
		deocded_words = decoded_message.split()
		if all([word in allowed_words for word in deocded_words]):
			return " ".join(deocded_words)

	return f"Can't decode word: {words}"
	

'''
The code below is a test function for task 2. It will run automatically when you run the script. Do not modify it.
To pass this assignment, your code must pass all the tests.
'''

def test_decode_message():

	assert decode_message("khoor", word_list_file) == "hello", "Test 1 failed. Output was %s" % decode_message("khoor", word_list_file)
	assert decode_message("Khoor", word_list_file) == "Invalid character in message", "Test 2 failed. Output was %s" % decode_message("Khoor", word_list_file)
	assert decode_message("khoor khoor", word_list_file) == "hello hello", "Test 3 failed. Output was %s" % decode_message("khoor khoor", word_list_file)
	assert decode_message("puppy", word_list_file) == "Can't decode word: puppy", "Test 4 failed. Output was %s" % decode_message("puppy", word_list_file) 

	print("Decoding tests passed - well done")

'''
The main function here just calls both test functions one after the other. 
You do not need to modify this.
Note that running this code without any changes will produce an error- this is *not* a mistake in the script. 
If you've understood and completed the lab exercises, you should be able to see why this error occurs
and what you need to do to fix it.
'''

def main():
	test_caesar_cipher()
	test_decode_message()


main()

