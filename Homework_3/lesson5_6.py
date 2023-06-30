# Вводится число, необходимо проверить является ли оно простым

def is_simple(num):
    count = 0

    for i in range(2, num // 2 + 1):
        if num % i == 0:
            count += 1

    if count <= 0:
        return 'Число простое'
    else:
        return 'Число не является простым'

print(is_simple(int(input('Введите число: '))))
