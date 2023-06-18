#Пользователь вводит 3 числа, сказать сколько из них положительных и сколько отрицательных

list_number = [int(input('Введите число:')) for i in range(3)]

count = 0
for num in list_number:
    if num < 0:
        count += 1

print('Количество положительных чисел:',len(list_number) - count)
print('Количество отрицательных чисел:',count)