# Дан список чисел, необходимо для каждого элемента посчитать сумму его
# соседей, для крайних чисел одним из соседей является число с противоположной
# стороны списка

from random import randint
lst = [randint(0, 100) for i in range(10)]
def neigbours_sum(user_list):
    sub_list = []
    for i in range(len(user_list)):
        if i == (len(user_list) - 1):
            sub_list.append(user_list[i - 1] + user_list[0])
            break

        sub_list.append(user_list[i - 1] + user_list[i + 1])
    return sub_list

res = neigbours_sum(lst)

print(lst, res, sep='\n')