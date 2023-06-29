n = int(input('Какое кол-во чисел нужно вывести: '))
m = int(input('Введите кртаность: '))
k = int(input('Больше какого числа: '))

count = 0

while count < n:
    if k % m == 0:
        print(k)
        count += 1
    k += 1

