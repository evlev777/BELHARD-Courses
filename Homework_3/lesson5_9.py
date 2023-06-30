# Дан список словарей, каждый словарь имеет ключи: category_id, title, price.
# Значение ключа category_id является целое положительное число, значением ключа name - str,
# а значение ключа price - float.
# Те словари, у которых ключ category_id = 1, необходимо удалить, а те у которых category_id = 2,
# необходимо уменьшить price на 5%. Остальные словари оставляем без изменений.

data_list = [
    {'category_id': 1, 'title': 'book', 'price': 100},
    {'category_id': 2, 'title': 'book', 'price': 100},
    {'category_id': 4, 'title': 'book', 'price': 100},
    {'category_id': 3, 'title': 'book', 'price': 100},
    {'category_id': 2, 'title': 'book', 'price': 100},
    {'category_id': 1, 'title': 'book', 'price': 100}
]

def del_item_dict(user_list):

    for i in range(len(user_list) - 1, -1, -1):
        if user_list[i].get('category_id') == 1:
            del user_list[i]
        elif user_list[i].get('category_id') == 2:
            user_list[i].get('price', 0) * 0.95
        else:
            continue

    return user_list

print(del_item_dict(data_list))