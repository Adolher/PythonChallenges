

def number_as_text(n: int) -> str:
    value_to_text = ""
    while n != 0:
        remainder = n % 10
        if remainder == 0:
            value_to_text += "ZERO "
        if remainder == 1:
            value_to_text += "ONE "
        if remainder == 2:
            value_to_text += "TWO "
        if remainder == 3:
            value_to_text += "THREE "
        if remainder == 4:
            value_to_text += "FOUR "
        if remainder == 5:
            value_to_text += "FIVE "
        if remainder == 6:
            value_to_text += "SIX "
        if remainder == 7:
            value_to_text += "SEVEN "
        if remainder == 8:
            value_to_text += "EIGHT "
        if remainder == 9:
            value_to_text += "NINE "
        n = n // 10
    x = value_to_text.split(" ")
    x.reverse()
    value_to_text = " ".join(x)
    return value_to_text.strip()

if __name__ == "__main__":
    values = [7, 42, 24680, 13579]
    for x in values:
        print(number_as_text(x))