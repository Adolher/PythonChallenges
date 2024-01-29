

def from_roman_numbers(roman_number: str) -> int:
    base_digits = {"I": 1, "X": 10, "C": 100, "M": 1000}
    sub_digits = {"V": 5, "L": 50, "D": 500}
    digits = {}
    digits.update(base_digits)
    digits.update(sub_digits)
    sorted_digits = list(digits.values())
    sorted_digits.sort()
    number = 0
    step = False

    for d in base_digits.keys():
        if d*4 in roman_number:
            return None
        
    for d in sub_digits.keys():
        if d*2 in roman_number:
            return None
        
    def check_substraction_syntax(x: str, y: str) -> bool:
        x = sorted_digits.index(base_digits[x])
        y = sorted_digits.index(digits[y])
        if y > x+2:
            return False
        return True

    for x in range(len(roman_number)):
        if step:
            step = False
        elif x+1 != len(roman_number) and digits[roman_number[x]] < digits[roman_number[x+1]]:
            if check_substraction_syntax(roman_number[x], roman_number[x+1]):
                number += (digits[roman_number[x+1]] - digits[roman_number[x]])
                step = True
            else:
                return None
        else:
            number += digits[roman_number[x]]
    
    return number


if __name__ == "__main__":
    values = ["XVII", "CDXLIV", "MCMLXXI", "MMXX", "IC", "XXXX", "MMMCMXCIX"]

    for x in values:
        print(f"{x} -> ", end="")
        print(from_roman_numbers(x))
        print()
