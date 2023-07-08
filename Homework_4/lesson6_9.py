# Дан словарь словарей, ключ внешнего словаря - id пользователя, значение -
# словарь с данными о пользователе (имя, фамилия, телефон, почта), вывести
# имена тех, у кого не указана почта (нет ключа email или значение этого ключа -
# пустая строка)

data = {
    '1': {
        'name': 'Alex',
        'lastname': 'Petro',
        'phone': 1111111,
        'email': 'alex@gmail.com'
    },
    '2': {
        'name': 'Rone',
        'lastname': 'Petro',
        'phone': 22222
    },
    '3': {
        'name': 'Harry',
        'lastname': 'Petro',
        'phone': 33333333,
        'email': 'alex@gmail.com'
    },
    '4': {
        'name': 'Germiona',
        'lastname': 'Petro',
        'phone': 4444444,
        'email': ''
    }
}

def sort_by_email(user_dict):
    sub_list = []
    for user_id, user_data in user_dict.items():
        if 'email' not in user_data or user_data['email'] == '':
            sub_list.append(user_data.get('name'))
    return sub_list

res = sort_by_email(data)

print(res)