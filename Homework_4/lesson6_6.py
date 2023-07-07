# Дан список рандомных чисел, необходимо отсортировать его в виде, сначала
# четные, потом нечётные


from random import randint
lst = [randint(0, 100) for i in range(10)]

def custom_sort(user_list):
    return sorted(user_list, key=lambda item: item % 2)

res = custom_sort(lst)

print(res)

