# TODO Заполнить список степенями числа 2 (от 2^1 до 2^n).

n = int(input('Enter pow for 2: '))

user_list = [2 ** i for i in range(1, n + 1)]

print(user_list)