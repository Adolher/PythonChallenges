

def to_binary(n: int) -> str:
    if n == 0:
        return ""
    else:
        return to_binary(n//2) + "0" if n%2 == 0 else  to_binary(n//2) + "1"

def to_octal(n: int) -> str:
    if n == 0:
        return ""
    else:
        return to_octal(n//8) + str(n%8)

def to_hex(n: int) -> str:
    hex = {10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}
    if n == 0:
        return ""
    elif n%16 < 10:
        return to_hex(n//16) + str(n%16)
    else:
        return to_hex(n//16) + hex[n%16]

if __name__ == "__main__":
    values = [5, 7, 8, 15, 22, 42, 77, 256]
    func = [int, to_binary, to_octal, to_hex]

    for f in func:
        for x in values:
            print(f(x), end="\t")
        print()
