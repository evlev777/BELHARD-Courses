# Дан список чисел и на вход поступает число N, необходимо сместить список на
# указанное число, пример: [1,2,3,4,5,6,7] N=3 ответ: [5,6,7,1,2,3,4]


def list_shift(user_list, user_shift):
    for i in range(user_shift):
        user_list.insert(0, user_list.pop())
    return user_list

res = list_shift([1,2,3,4,5,6,7], 3)

print(res)