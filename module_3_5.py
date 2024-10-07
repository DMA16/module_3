def get_multiplied_digits(number: int):
    str_number = str(number)

    first = int(str_number[0])

    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return int(str_number[0])

print(get_multiplied_digits(205035))
