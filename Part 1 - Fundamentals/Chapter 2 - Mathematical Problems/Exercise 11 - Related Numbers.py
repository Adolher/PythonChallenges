

def calc_friends(max_exclusive: int) -> list:
    friends = set()
    pairs = []

    def divisors(value: int) -> list:
        divs = []
        for x in range(1, (value // 2) + 1):
            if value % x == 0:
                divs.append(x)
        return divs
    
    def sum(values: list) -> int:
        sum = 0
        while len(values) > 0:
            sum += values.pop(0)
        
        return sum
    
    for x in range(1, max_exclusive):
        pair = (x, sum(divisors(x)))
        pairs.append(pair)
        if (pair[1], pair[0]) in pairs and pair[0] != pair[1]:
            friends.add((pair, (pair[1], pair[0])))

    return friends

if __name__ == "__main__":
    print(calc_friends(1222))
