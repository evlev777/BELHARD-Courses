#Пользователь вводит предложение, заменить все пробелы на "-" 2-мя способами

user_str = input('Введите строку: ')
print('Функция replace():', user_str.replace(' ','-'))
print('Функции split() и join():','-'.join(user_str.split(' ')))