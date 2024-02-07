

def sum_rec(values: list) -> int:
    if len(values) == 0:
        return 0
    elif len(values) == 1:
        return values[0]
    else:
        return values[-1] + sum_rec(values[:-1])
    

if __name__ == "__main__":
    values = [[1, 2, 3], [1, 2, 3, -7]]

    for x in values:
        print(sum_rec(x))
