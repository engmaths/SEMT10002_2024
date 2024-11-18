def get_limit(prompt):

    limit = ''
    while not limit.isdigit():
        limit = input(prompt)

    limit = int(limit)

    return limit 

def is_number_prime(number):

    is_prime = True

    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True

def find_primes(lower_limit, upper_limit):

    primes = []

    for number in range(lower_limit, upper_limit+1):
        is_prime = is_number_prime(number)

        if is_prime:
            primes.append(number)

    return primes

def main():

    lower_limit = get_limit("Please enter a lower limit")
    upper_limit = get_limit("Please enter an upper_limit")

    primes = find_primes(lower_limit, upper_limit)

    print("Prime between",lower_limit, "and", upper_limit, "are:", primes)

main()