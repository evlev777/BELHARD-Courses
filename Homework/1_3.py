#Пользователь вводит Имя, Возраст и Город, сформировать приветственное сообщение путем форматирования 3-мя способами
user_name = input('Введите имя:')
user_age = int(input('Введите возраст:'))
user_country = input('Введите город:')

print('%-формирование:', 'Добро пожаловать %s в %s. Ваш возраст %d' % (user_name,user_country,user_age))
print('Функция format:', 'Добро пожаловать {} в {}. Ваш возраст {}'.format(user_name,user_country,user_age))
print('f-формирование:', f'Добро пожаловать {user_name} в {user_country}. Ваш возраст {user_age}')