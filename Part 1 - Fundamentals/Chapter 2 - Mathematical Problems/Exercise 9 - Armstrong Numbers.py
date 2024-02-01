

def calc_armstrong_numbers(a:int, b:int, c:int) -> list:
    for x in range(1,10):
        for y in range(1,10):
            for z in range(1,10):
                n = x*100 + y*10 + z
                m = pow(x,a) + pow(y,b) + pow(z,c)
                if n == m:
                    yield n


if __name__ == "__main__":
    l = calc_armstrong_numbers(3, 3, 3)
    for x in l:
        print(x)
    
    print()
    l = calc_armstrong_numbers(1, 2, 3)
    for x in l:
        print(x)
    
    print()
    l = calc_armstrong_numbers(3, 2, 1)
    for x in l:
        print(x)