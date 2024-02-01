from math import sqrt


def pythagoras(min: int, max: int) -> list:
    for a in range(min, max+1):
        for b in range(a, max+1):
            c = sqrt(pow(a,2) + pow(b,2))
            if c > max:
                break
            else:
                yield (a,b,c)
                if a == b:
                    continue
                yield (b,a,c)


def a2b2_equ_c2d2(min: int, max: int) -> list:
    for a in range(min, max+1):
        for b in range(a, max+1):
            a2b2 = pow(a,2) + pow(b,2)
            for c in range(min, max+1):
                for d in range(c, max+1):
                    c2d2 = pow(c,2) + pow(d,2)

                    if a2b2 == c2d2:
                        yield ((a, b), (c, d))
                        if a != b:
                            yield ((a, b), (d, c))
                        if c != d:
                            yield ((b, a), (d, c))
                        if a != b != c != d:
                            yield ((b, a), (c, d))



if __name__ == "__main__":
    l = list(pythagoras(1, 100))
    l.sort()

    for t in l:
        print(f"a = {t[0]}\tb = {t[1]}\tc = {t[2]:.4}")

    l = list(a2b2_equ_c2d2(1, 5))
    l.sort()

    for t in l:
        print(f"a = {t[0][0]}\tb = {t[0][1]}\tc = {t[1][0]}\td = {t[1][1]}\t\t {pow(t[0][0],2) + pow(t[0][1],2)} == {pow(t[1][0],2) + pow(t[1][1],2)}")

