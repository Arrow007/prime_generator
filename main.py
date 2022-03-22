# Prime Generator
# n^2 - n + 41 = Prime?
import math
import os

print("This program generates prime values based on the formula n^2 - n + 41. It will then return the calculated "
      "values and whether or not they are prime.")
print("Below, specify the value of n you would like the program to generate up to.")
num_values = int(input("n = "))


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
    # print()
    # print("All Values")
    # print()
    # print("n =", num_values)
    # print(is_prime(calculate()).count(1), "/", num_values, " Prime (",
    #       '{:.2f}'.format((is_prime(calculate()).count(1) / num_values) * 100), "%)", sep="")
    # print("------------------------------------------")
    # print('{:7}'.format("VALUE #"), '{:11}'.format("CALCULATION"), '{:6}'.format("PRIME?"), sep="\t\t\t")

    export_all = open(f"C:\\Users\\{os.getlogin()}\\Desktop\\PG-{num_values}-All.txt", "w")
    export_all.write("All Values\n\n")
    export_all.write("n = " + str(num_values) + "\n")
    export_all.write(str(is_prime(calculate()).count(1)) + "/" + str(num_values) + " Prime (" +
                     str('{:.2f}'.format((is_prime(calculate()).count(1) / num_values) * 100)) + "%)" + "\n")
    export_all.write("--------------------------------------------------------------\n")
    export_all.write(
        '{:7}'.format("VALUE #") + "\t\t\t" + '{:11}'.format("CALCULATION") + "\t\t\t" + '{:6}'.format("PRIME?") + "\n")

    count = 0

    for i in range(num_values):
        count += 1
        # print('{:7}'.format(count), '{:11}'.format(calculate()[i]), '{:6}'.format(is_prime(calculate())[i]),
        #       sep="\t\t\t")
        export_all.write('{:7}'.format(count) + "\t\t\t" + '{:11}'.format(calculate()[i]) + "\t\t\t" + '{:6}'.format(
            is_prime(calculate())[i]) + "\n")

    export_all.close()


def print_prime(calculated_values, prime_values):
    # print()
    # print("Only Prime Values")
    # print("------------------------------------------")
    # print('{:7}'.format("VALUE #"), '{:11}'.format("CALCULATION"), '{:6}'.format("PRIME?"), sep="\t\t\t")

    export_prime = open(f"C:\\Users\\{os.getlogin()}\\Desktop\\PG-{num_values}-Prime.txt", "w")
    export_prime.write("Only Prime Values\n\n")
    export_prime.write("--------------------------------------------------------------\n")
    export_prime.write(
        '{:7}'.format("VALUE #") + "\t\t\t" + '{:11}'.format("CALCULATION") + "\t\t\t" + '{:6}'.format("PRIME?") + "\n")

    count = 0

    for i in range(num_values):
        count += 1
        if is_prime(calculate())[i]:
            # print('{:7}'.format(count), '{:11}'.format(calculate()[i]), '{:6}'.format(is_prime(calculate())[i]),
            #       sep="\t\t\t")
            export_prime.write(
                '{:7}'.format(count) + "\t\t\t" + '{:11}'.format(calculate()[i]) + "\t\t\t" + '{:6}'.format(
                    is_prime(calculate())[i]) + "\n")

    export_prime.close()


def print_non_prime(calculated_values, prime_values):
    # print()
    # print("Only Non-Prime Values")
    # print("------------------------------------------")
    # print('{:7}'.format("VALUE #"), '{:11}'.format("CALCULATION"), '{:6}'.format("PRIME?"), sep="\t\t\t")

    export_non_prime = open(f"C:\\Users\\{os.getlogin()}\\Desktop\\PG-{num_values}-Non_Prime.txt", "w")
    export_non_prime.write("Only Prime Values\n\n")
    export_non_prime.write("--------------------------------------------------------------\n")
    export_non_prime.write(
        '{:7}'.format("VALUE #") + "\t\t\t" + '{:11}'.format("CALCULATION") + "\t\t\t" + '{:6}'.format("PRIME?") + "\n")

    count = 0

    for i in range(num_values):
        count += 1
        if not is_prime(calculate())[i]:
            # print('{:7}'.format(count), '{:11}'.format(calculate()[i]), '{:6}'.format(is_prime(calculate())[i]),
            #       sep="\t\t\t")
            export_non_prime.write(
                '{:7}'.format(count) + "\t\t\t" + '{:11}'.format(calculate()[i]) + "\t\t\t" + '{:6}'.format(
                    is_prime(calculate())[i]) + "\n")

    export_non_prime.close()


print_all(calculate(), is_prime(calculate()))
print_prime(calculate(), is_prime(calculate()))
print_non_prime(calculate(), is_prime(calculate()))
