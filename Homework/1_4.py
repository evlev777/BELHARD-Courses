#Пользователь вводит 3 числа, сказать сколько из них положительных и сколько отрицательных

first_number = int(input('Введите первое число:'))
second_number = int(input('Введите второе число:'))
third_number = int(input('Введите третье число:'))

positive_count = (first_number > 0) + (second_number > 0) + (third_number > 0)
negative_count = (first_number < 0) + (second_number < 0) + (third_number < 0)

print('Количество положительных чисел:', positive_count)
print('Количество отрицательных чисел:', negative_count)