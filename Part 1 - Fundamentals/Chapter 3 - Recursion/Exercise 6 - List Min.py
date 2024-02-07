from sys import maxsize


def min_rec(values: list) -> int:
    if len(values) == 0:
        return maxsize
    elif len(values) == 1:
        return values[0]
    else:
        l1 = min_rec(values[:len(values)//2])
        l2 = min_rec(values[(len(values)//2):])
        return l1 if l1 < l2 else l2

if __name__ == "__main__":
    values = [[7, 2, 1, 9, 7, 1], [11, 2, 33, 44, 55, 6, 7], [1, 2, 3, -7]]

    for x in values:
        print(min_rec(x))
