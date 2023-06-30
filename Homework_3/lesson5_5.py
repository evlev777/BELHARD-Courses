# Вводится число N, необходимо вывести N чисел Фибоначчи

def fib(n):
    a = 0
    b = 1
    for _ in range(n):
        a, b = b, a + b
    return a

print(fib(int(input('Enter a number: '))))
