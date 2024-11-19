lower_limit = ''
while not lower_limit.isdigit():
    lower_limit = input("Please enter a lower limit")

lower_limit = int(lower_limit)

upper_limit = ''
while not upper_limit.isdigit():
    upper_limit = input("Please enter an upper limit")

upper_limit= int(upper_limit)

primes = []
for num in range(lower_limit, upper_limit + 1):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)

print("Prime between",lower_limit, "and", upper_limit, "are:", primes)


