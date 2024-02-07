

def gcd(a:int, b:int) -> int:
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
    
def gcd_it(a:int, b:int) -> int:
    while b != 0:
        a, b = b, a%b
    return a

def lcm(a:int, b:int) -> int:
    return int(a*b / gcd(a,b))


if __name__ == "__main__":
    values = [(42, 7), (42, 28), (42, 14)]

    for x in values:
        print(gcd(x[0], x[1]), end=" ")

    print()
    values = [(42, 7), (42, 28), (42, 14)]

    for x in values:
        print(gcd_it(x[0], x[1]), end=" ")

    print()
    values = [(2, 7), (7, 14), (42, 14)]

    for x in values:
        print(lcm(x[0], x[1]), end=" ")
