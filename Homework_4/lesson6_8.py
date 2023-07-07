# Дан словарь, ключ - Название страны, значение - список городов, на вход
# поступает город, необходимо сказать из какой он страны

def search_country(city):
    country_dict = {
        'Belarus': ['MINSK', 'GOMEL', 'GRODNO', 'BREST', 'MOGILEV', 'VITEBSK'],
        'Russia': ['MOSKOW', 'SAINT-PETERBURG', 'KAZAN', 'VLADIVOSTOK'],
        'USA': ['WASHINGTON', 'CAROLINA', 'MIAMI', 'FLORIDA', 'NEW-YORK']
    }

    for cities_list in country_dict:
        if city.upper() in country_dict[cities_list]:
            return cities_list
    else:
        return 'Такого города нет'




res = search_country(input('Enter the city: '))

print(res)