#Пользователь вводит 3 числа, найти среднее арифмитическое с точность 3

first_number = int(input('Введите первое число:'))
second_number = int(input('Введите второе число:'))
third_number = int(input('Введите третье число:'))

print('Среднее арифметическое трех чисел равно:' , round((first_number + second_number + third_number)/3, 3))