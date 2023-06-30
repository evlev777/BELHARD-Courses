# Дан список содержащий словари, в каждом словаре
# может быть или не быть ключ price. Значение ключа,
# при его наличии, является число (int, float).
# Необходимо рассчитать среднее значение price среди словарей у которых есть данный ключ.

data_list = [
    {'item': 'Book', 'price': 1.7},
    {'item': 'Coca-Cola'},
    {'item': 'Latte', 'price': 3.9},
    {'item': 'Cappuccino'},
    {'item': 'Ball', 'price': 100},
    {'item': 'Doner', 'price': 10},
    {'item': 'Doner', 'price': 100}
]

def average_value_list(user_list):
    price_sum = 0
    count_key = 0

    for item_data_list in user_list:
        if item_data_list.get('price'):
            count_key += 1
            price_sum += item_data_list.get('price', 0)
        else:
            continue

    return price_sum / count_key

print('Среднее значение:', average_value_list(data_list), sep=' ')

