

def is_prime(x: int) -> bool:
    prime = False
    for n in range(2, x+1):
        if x % n == 0 and n != x:
            break
        elif n == x:
            prime = True
    return prime


def calc_prime_pairs(max_value: int) -> int:
    twins = {}
    cousins = {}
    sexies = {}
    for number in range(2, max_value+1):
        
        if is_prime(number):
            if is_prime(number+2):
                twins.update({number:number+2})
            if is_prime(number+4):
                cousins.update({number:number+4})
            if is_prime(number+6):
                sexies.update({number:number+6})
    return twins, cousins, sexies

if __name__ == "__main__":
    values = calc_prime_pairs(50)
    for x in values:
        print(x)
