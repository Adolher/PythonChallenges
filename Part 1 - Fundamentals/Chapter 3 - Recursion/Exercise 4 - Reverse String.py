

def reverse_string(text: str) -> str:
    if len(text) == 1:
        return text[0]
    else:
        return text[-1] + reverse_string(text[:-1])


if __name__ == "__main__":
    values = ["A", "ABC", "abcdefghi"]

    for x in values:
        print(reverse_string(x))
