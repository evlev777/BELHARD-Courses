# Вывести четные числа от 2 до N по 5 в строку

num = int(input('Введите конченое число: '))
sub_str = ''

for i in range(2, num + 1, 2):
    sub_str += str(i) + ' '
    if i % 5 == 0:
        sub_str += '\n'

print(sub_str)