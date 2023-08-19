"""
min - минимальное значение
max - максимальное значение
min < max
На вход программе будет подано:

Первая строка: строка из двух чисел, разделённых пробелом: min, max
Вторая строка: строка из произвольного количества элементов, разделённых пробелом - содержимое исходного списка

Вывести список, в котором каждое значение соответствует значению из исходного массива,
но если значение в исходном массиве меньше min, то в новом массиве оно должно быть заменено на min,
а если больше max, то заменить его нужно, но на значение max.
"""

def modify_list_values(min_val, max_val, values):
    modified_values = []

    for value in values:
        if value < min_val:
            modified_values.append(min_val)
        elif value > max_val:
            modified_values.append(max_val)
        else:
            modified_values.append(value)

    return modified_values


min_val, max_val = map(int, input().split())
values = list(map(int, input().split()))

modified_list = modify_list_values(min_val, max_val, values)
print(*modified_list)
