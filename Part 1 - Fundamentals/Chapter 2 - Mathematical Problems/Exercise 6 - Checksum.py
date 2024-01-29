

def calc_checksum(digits: str) -> int:
    n = len(digits)
    nx = 1
    sum = 0
    while(nx <= n):
        sum += nx * int(digits[nx - 1])
        nx += 1
    return sum % 10


if __name__ == "__main__":
    values = ["11111", "87654321"]
    for x in values:
        print(calc_checksum(x))
