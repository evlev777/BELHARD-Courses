# Вводится число, необходимо подсчитать его факториал

def count_factorial(num):
    factorial = 1

    if num < 0:
        factorial = 'Введено отрицательное число'
        return factorial

    for i in range(1, num + 1):
        factorial *= i
    return factorial



print(count_factorial(int(input('Enter a number: '))))
