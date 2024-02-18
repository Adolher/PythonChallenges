

def is_power_of_2(n: int) -> bool:
    if n % 2 == 0:
        if n // 2 == 1:
            return True
        else:
            return is_power_of_2(n//2)
    else:
        return False
    

def power_of(n: int, x: int) -> int:
    if x == 0:
        return 1
    else:
        return n * power_of(n, x-1)
    

def power_of_it(n: int, x: int) -> int:
    if x == 0:
        return 1
    result = 1
    while x > 0:
        result *= n
        x -= 1
    return result


if __name__ == "__main__":
    values = [2, 10, 16]

    for x in values:
        print(f"x: {x}\t{is_power_of_2(x)}")
    
    values = [(2, 2), (2, 8), (4, 4)]

    for x in values:
        print(f" {x[0]}^{x[1]} = {power_of(x[0], x[1])}\t| {power_of_it(x[0], x[1])}")