

def calc(m: int, n: int) -> int:
    return ((n * m // 2) % 7)

def calc_sum_and_count_all_numbers_div_by_2_or_7(max_exclusive: int) -> int:
    d2, d7, sum = 0,0,0
    for x in range(1, max_exclusive):
        if not x % 2 or not x % 7:
            if not x % 2:
                d2 += 1
            elif not x % 7:
                d7 +=1
            sum += x
    return (d2 + d7), sum

def is_even(x: int) -> bool:
    return False if x % 2 else True
def is_odd(x: int) -> bool:
    return True if x % 2 else False


if __name__ == "__main__":
    values = [(6,7), (5,5)]
    for x in values:
        n,m = x
        print("result = " + str(calc(n,m)))
    
    print()
    
    values = [3, 8, 15]
    for x in values:
        count, sum = calc_sum_and_count_all_numbers_div_by_2_or_7(x)
        print("count = {}\nsum = {}".format(count, sum))

    print()

    values = [1, 2, 3, 4]
    for x in values:
        if is_even(x):
            print(f"{x} is even")
        if is_odd(x):
            print(f"{x} is odd")
