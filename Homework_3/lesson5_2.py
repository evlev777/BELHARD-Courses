
while True:
    num1 = int(input('Первое число: '))
    operation = input('Операция: ').replace(' ', '')
    num2 = int(input('Первое число: '))

    if operation == '+':
        print(f'{num1} {operation} {num2}', num1 + num2, sep=' = ')
    elif operation == '-':
        print(f'{num1} {operation} {num2}', num1 - num2, sep=' = ')
    elif operation == '*':
        print(f'{num1} {operation} {num2}', num1 * num2, sep=' = ')
    elif operation == '/':
        print(f'{num1} {operation} {num2}', num1 / num2, sep=' = ')

    if input('Введите n для выхода: ').lower() == 'n':
        break

