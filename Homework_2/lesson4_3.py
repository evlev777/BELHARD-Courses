# Заполнить словарь где ключами будут выступать числа от 0 до n, а
# значениями вложенный словарь с ключами "name" и "email", а значения
# для этих ключей будут браться с клавиатуры


user_dict = {i: {'name': input(f'Enter {i} user name: '), 'email': input(f'Enter {i} user email: ')}
             for i in range(int(input('Enter a number: ')))}

print(user_dict)
