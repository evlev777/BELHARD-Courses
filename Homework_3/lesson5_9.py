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
    sub_list = []

    for item_list in user_list:
        if item_list['category_id'] == 1:
            del item_list
            continue
        elif item_list['category_id'] == 2:
            item_list['price'] -= item_list['price'] * 0.05

        sub_list.append(item_list)

    return sub_list

print(del_item_dict(data_list))

