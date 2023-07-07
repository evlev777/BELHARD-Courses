# Дан список чисел, необходимо его развернуть без использования метода revese и
# функции reversed, а так же дополнительного списка и среза

def custom_reverse(user_list):
    for i in range(len(user_list) // 2):
        user_list[i], user_list[len(user_list) - i - 1] = user_list[len(user_list) - i - 1], user_list[i]
    return user_list

res = custom_reverse([1, 2, 3, 4, 5, 6, 7])

print(res)