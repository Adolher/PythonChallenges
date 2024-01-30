

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


def to_roman_number(value: int) -> str:
    roman = {1:{1:"I", 5:"V", 10:"X"}, 10:{1:"X", 5:"L", 10:"C"}, 100:{1:"C", 5:"D", 10:"M"}, 1000:{1:"M"}}
    roman_number = []
    index = 1
    if not 0 < value < 4000:
        return None
    
    def add_one(index: int, number: str, digit: int) -> (str, int):
        number += roman[index][1]
        digit -= 1
        return number, digit
    
    def sub_one(index: int, number: str, digit: int) -> (str, int):
        number = roman[index][1] + number
        digit += 1
        return number, digit
    
    while(value > 0):
        digit = value % 10
        roman_digit = ""
        while(digit != 0):
            if digit == -1:
                roman_digit, digit = sub_one(index, roman_digit, digit)
            elif digit <= 3:
                roman_digit, digit = add_one(index, roman_digit, digit)
            elif digit <= 8:
                if not roman[index][5] in roman_digit:
                    roman_digit = roman[index][5]
                    digit -= 5
            else:
                if not roman[index][10] in roman_digit:
                    roman_digit = roman[index][10]
                    digit -= 10
        
        roman_number.append(roman_digit)
        index *= 10
        value //= 10

    roman_number.reverse()
    
    return "".join(roman_number)


if __name__ == "__main__":
    values = ["XVII", "CDXLIV", "MCMLXXI", "MMXX", "MMMCMXCIX", "LXXVII"]

    for x in values:
        print(f"{x} -> ", end="")
        print(from_roman_numbers(x), end = " -> ")
        print(to_roman_number(from_roman_numbers(x)))
