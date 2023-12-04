"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""


def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError("The value must be a positive integer , increase your number")

    list = []
    current_value_being_checked = 2  # Start with the first prime number

    while len(list) < number_of_primes:
        number_is_prime = True
        for factor in range(2, int(current_value_being_checked**0.5) + 1):
            if current_value_being_checked % factor == 0:
                number_is_prime = False
                break

        if number_is_prime:
            list.append(current_value_being_checked)

        current_value_being_checked += 1

    return list
