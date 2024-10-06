def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


#1
print_params(b = 25)
print_params(c = [1,2,3])

#2
values_list = [54.32, 'Строка' , False]
values_dict = {'a': True, 'b': 34.3, 'c': 'Ща бы пиццы :/'}
print_params(*values_list)
print_params(**values_dict)

#3
values_list_2 = [666, "999"]
print_params(*values_list_2, 42)