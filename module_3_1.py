import random
import string as s
from random import randint
from re import search


call = 0


def count_call():
    global call
    call += 1


def string_info(string: str):
    count_call()
    return (len(string), string.upper(), string.lower())


def is_contains(string: str, list_to_search: list[str]):
    count_call()
    return string.upper() in [elem.upper() for elem in list_to_search]


def generate_text():
    letters = s.ascii_letters
    return ''.join(random.choice(letters) for j in range(randint(1, 15)))


def arbitrary_function_call():
    for i in range(randint(1, 10)):
        result_string_info = string_info(
            generate_text()
        )

        print(result_string_info)

        list_to_search = []

        for i_str in range(randint(1, 5)):
            list_to_search.append(generate_text())

        result_is_contains = is_contains(
            generate_text() if bool(randint(0, 1)) else list_to_search[
                randint(0, len(list_to_search) - 1)
            ],
            list_to_search
        )

        print(result_is_contains)

    print("\n", call)

arbitrary_function_call()