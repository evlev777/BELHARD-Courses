# Без использования collections, написать программу, которая будет
# создавать словарь для подсчитывания количества вхождений каждой
# буквы в текст введенный с клавиатуры

text = input('Enter the text: ')

count_dict = {}

for letters in text:
    if letters in count_dict:
        count_dict[letters] += 1
    else:
        count_dict[letters] = 1

print(count_dict)
