# Написать функцию перевода десятичного числа в двоичное и обратно, без
# использования функции int

def decimal_to_bin(num):
    sub_str = ''

    while num > 0:
        sub_str = str(num % 2) + sub_str
        num //= 2

    return sub_str

def bin_to_decimal(bin_num):
    dec_num = 0

    for i in range(0, len(bin_num)):
        dec_num += int(bin_num[i]) * (2 ** (len(bin_num) - i - 1))

    return dec_num


res1 = decimal_to_bin(15)
res2 = bin_to_decimal(res1)

print(res1, res2, sep=' = ')

