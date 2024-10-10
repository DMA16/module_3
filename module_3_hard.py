data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def total_sum(set_of_values):
    sum = 0

    if isinstance(set_of_values, dict):
        set_of_values = set_of_values.items()


    for val in set_of_values:

        if isinstance(val, str):
            sum += len(val)
            continue

        if isinstance(val, int):
            sum += val
            continue

        sum += total_sum(val)

    return sum


print(total_sum(data_structure))