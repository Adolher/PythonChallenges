

def fib_rec(n: int) -> int:
    if n <= 0:
        return None
    elif n == 1 or n == 2:
        return 1
    else:
        return fib_rec(n-1) + fib_rec(n-2)

def fib_it(n: int) -> int:
    if n <= 0:
        return None
    f = [0, 0]
    for x in range(1, n+1):
        if x == 1:
            f[1] = 1
        else:
            f[0], f[1] = f[1], f[0] + f[1]
    return f[1]


if __name__ == "__main__":
    values = [1, 2, 3, 4, 5, 6, 7, 8]

    for x in values:
        print(fib_rec(x), end=" ")
    print()
    for x in values:
        print(fib_it(x), end=" ")
