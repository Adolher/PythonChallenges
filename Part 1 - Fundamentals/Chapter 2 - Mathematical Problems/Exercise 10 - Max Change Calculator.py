from itertools import combinations


def calc_max_possible_change(values: tuple) -> int:
    possible_values = set()

    for x in range(len(values)+1):
        combination = list(combinations(values, x))
        if len(combination[0]) > 0:
            for value in combination:
                sum = 0
                for v in value:
                    sum += v
                    possible_values.add(sum)

    print(possible_values, end="\t")
    return max(possible_values)


if __name__ == "__main__":
    values = [(1, ), (1, 1), (1, 5), (1, 2, 4), (1, 2, 3, 7), (1, 1, 1, 1, 5, 10, 20, 50)]

    for value in values:
        print(calc_max_possible_change(value))
