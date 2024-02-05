

def calc_primes_up_to(max_value: int) -> int:
    primes = []
    for number in range(2, max_value+1):
        prime = False
        for n in range(2, number+1):
            if number % n == 0 and n != number:
                break
            elif n == number:
                prime = True
        if prime:
            primes.append(number)
    return primes


def calc_prime_factors(value: int) -> list:
    primes = calc_primes_up_to(value)
    prime_factors = []

    while value != 1:
        for prime in primes:
            if value % prime == 0:
                prime_factors.append(prime)
                value /= prime
                break

    return prime_factors


if __name__ == "__main__":
    values = [8, 14, 42, 1155, 2222]
    for x in values:
        print(calc_prime_factors(x))
