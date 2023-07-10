# Дан список содержащий в себе различные типы данных, отфильтровать таким
# образом, чтобы остались только строки, использование дополнительного списка
# незаконно

# print(list(filter(lambda x: isinstance(x, str), [1, 'ssd', 3.14, 'qweqwe', True, 'zxcxzcvz', ['a', 'b'], 'tgb'])))

data = [1, 'ssd', 3.14, 'qweqwe', True, 'zxcxzcvz', ['a', 'b'], 'tgb']

def filter_by_str(user_list):

    for i in range(len(user_list) - 1, -1, -1):
        if not isinstance(user_list[i], str):
            del user_list[i]

    return user_list


res = filter_by_str(data)

print(res)
