

def count_digits(value: int) -> int:
    if value < 10:
        return 1
    else:
        return count_digits(value//10) + 1

def calc_sum_of_digits(value: int) -> int:
    if value < 10:
        return value % 10
    else:
        return calc_sum_of_digits(value // 10) + value % 10


if __name__ == "__main__":
    values = [1234, 1234567]

    for x in values:
        print(f"{x}\t{count_digits(x)}\t{calc_sum_of_digits(x)}")
