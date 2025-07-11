import csv


def caesar_cipher(text, shift):
    """Task 1: Caesar cipher
    - This special type of comment is called a **docstring**.
    - Docstrings are usually used to describe what a function does.
    - Write your code for implementing the Caesar cipher below.
    """

    text_ascii = [ord(char) for char in text]
    ord_a = ord("a")  # ASCII value of "a"
    shift_ascii = [(char - ord_a + shift) % 26 + ord_a for char in text_ascii]

    # Convert the shifted values back to characters and join
    return "".join([chr(char) for char in shift_ascii])


def test_caesar_cipher():
    """This is a test function for your code.
    - It will run automatically when you run the script.
    - Do not modify it.
    - To pass this assignment, your code must pass all the tests.
    """

    # The assert statement will raise an error if the expression
    # contained within it does not evaluate to True
    assert caesar_cipher("a", 1) == "b", "Test 1 failed"
    assert caesar_cipher("a", 2) == "c", "Test 2 failed"
    assert caesar_cipher("z", 1) == "a", "Test 3 failed"
    assert caesar_cipher("a", -1) == "z", "Test 4 failed"
    assert caesar_cipher("hello", 3) == "khoor", "Test 5 failed"
    assert caesar_cipher("khoor", -3) == "hello", "Test 6 failed"

    print("Encoding tests passed - great job!")

    return None


def decode_message(message, word_list_filepath="word_list.txt"):
    """Task 2: Decoding
    - Write your code below for decoding a message when we don't know the shift.
    - You are given a list of words that the message may be composed of.
    - Your code should work by *brute force*: it should check all possible shifts until it finds a match.
    """

    with open(word_list_filepath, "r") as file:
        reader = csv.reader(file)
        word_list = [row[0] for row in reader]

    message_words = message.split()
    decoded_words = []

    for word in message_words:
        # Check if word consists of lowercase letters only
        if not (word.isalpha() and word.islower()):
            return "Invalid character in message"

        for shift in range(26):
            shift_word = caesar_cipher(word, -shift)

            # If a valid shift is found, append decoded word
            if shift_word in word_list:
                decoded_words.append(shift_word)
                break
            # If no valid shift is found, return error message
            elif shift == 25:
                return f"Can't decode word: {word}"

    # Join the decoded words into a single string
    return " ".join(decoded_words)


def test_decode_message():
    """This is a test function for task 2.
    - It will run automatically when you run the script.
    - Do not modify it.
    - To pass this assignment, your code must pass all the tests.
    """

    word_list = "word_list.txt"

    result1 = decode_message("khoor", word_list)
    condition1 = result1 == "hello"
    assert condition1, "Test 1 failed. Output was %s" % result1

    result2 = decode_message("Khoor", word_list)
    condition2 = result2 == "Invalid character in message"
    assert condition2, "Test 2 failed. Output was %s" % result2

    result3 = decode_message("khoor khoor", word_list)
    condition3 = result3 == "hello hello"
    assert condition3, "Test 3 failed. Output was %s" % result3

    result4 = decode_message("puppy", word_list)
    condition4 = result4 == "Can't decode word: puppy"
    assert condition4, "Test 4 failed. Output was %s" % result4

    print("Decoding tests passed - well done!")

    return None


def main():
    """The main function here just calls both test functions one after the other.

    - You do not need to modify this.
    - Note that running this code without any changes will produce an error: this is *not* a mistake in the script.
    - If you've understood and completed the lab exercises, you should be able to see why this error occurs.
    and what you need to do to fix it.
    """

    test_caesar_cipher()
    test_decode_message()


# Everything above this line should only contain function definitions.
# Below this line is where the code will be executed.

main()
