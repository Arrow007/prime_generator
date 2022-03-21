# Prime Generator
# n^2 - n + 41 = Prime?
import math

num_values = 500


def calculate():
    result = []

    for n in range(num_values):
        result.append((n ** 2) - n + 41)

    return result


def is_prime(result):
    primes = []

    for i in result:
        if i <= 1:
            primes.append(0)

        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                primes.append(0)

        primes.append(1)

    return primes


def print_all(calculated_values, prime_values):
    print()
    print('{:7}'.format("VALUE #"), '{:11}'.format("CALCULATION"), '{:6}'.format("PRIME?"), sep="\t\t\t")
    count = 0

    for i in range(num_values):
        count += 1
        print('{:7}'.format(count), '{:11}'.format(calculate()[i]), '{:6}'.format(is_prime(calculate())[i]),
              sep="\t\t\t")


def print_prime(calculated_values, prime_values):
    print()
    print('{:7}'.format("VALUE #"), '{:11}'.format("CALCULATION"), '{:6}'.format("PRIME?"), sep="\t\t\t")
    count = 0

    for i in range(num_values):
        count += 1
        if is_prime(calculate())[i]:
            print('{:7}'.format(count), '{:11}'.format(calculate()[i]), '{:6}'.format(is_prime(calculate())[i]),
                  sep="\t\t\t")


def print_non_prime(calculated_values, prime_values):
    print()
    print('{:7}'.format("VALUE #"), '{:11}'.format("CALCULATION"), '{:6}'.format("PRIME?"), sep="\t\t\t")
    count = 0

    for i in range(num_values):
        count += 1
        if not is_prime(calculate())[i]:
            print('{:7}'.format(count), '{:11}'.format(calculate()[i]), '{:6}'.format(is_prime(calculate())[i]),
                  sep="\t\t\t")


print_all(calculate(), is_prime(calculate()))
print_prime(calculate(), is_prime(calculate()))
print_non_prime(calculate(), is_prime(calculate()))
