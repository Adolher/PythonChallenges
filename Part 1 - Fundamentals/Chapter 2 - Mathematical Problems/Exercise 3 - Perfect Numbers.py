

def calc_perfect_numbers(max_exclusive: int) -> list:
    perfect_numbers = []
    for number in range(1, max_exclusive):
        real_divisors = []
        sum = 0
        for n in range(1, (number//2)+1):
            if not number % n:
                real_divisors.append(n)
                sum += n
        if sum == number:
            perfect_numbers.append(number)
    return perfect_numbers

if __name__ == "__main__":
    values = [1000, 10000]
    for x in values:
        print(calc_perfect_numbers(x))

