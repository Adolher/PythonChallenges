

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

if __name__ == "__main__":
    values = [15, 25, 50]
    for x in values:
        print(calc_primes_up_to(x))
