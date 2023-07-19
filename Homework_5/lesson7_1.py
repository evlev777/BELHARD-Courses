# TODO Написать класс ConfigParser, конструктор класса принимает строку в формате:
#  text = '''[Section1]key1=value1key2=value2[Section2]key3=value3key4=value4'''
#
#  TODO написать метод класса parse, который будет вызываться в конструкторе, данный метод
#  принимает данную строку и преобразовывает в словарь словарей
#  результат метода после вызова в конструкторе, помещается в атрибут объекта datadata = {
#     'Section1': {
#         'key1': 'value1',
#         'key2': 'value2',    },
#     'Section2': {
#         'key3': 'value3',
#         # 'key4': 'value4'    }
# }

class ConfigParser:

    def __init__(self, text: str) -> None:
        self.data = self.loads(text)

    @classmethod
    def loads(cls, text: str) -> dict[str, dict[str, str]]:
        lines = [line for line in text.split('\n') if line]
        data = {}
        current_section = ''
        for line in lines:
            if line.startswith('[') and line.endswith(']'):
                current_section = line[1:-1]
                data[current_section] = {}
            else:
                key, value = line.split('=')
                data[current_section][key] = value
        return data

    def has_section(self, section: str) -> bool:
        return section in self.data

    def has_param(self, section: str, key: str) -> bool:
        try:
            return key in self.data[section]
        except KeyError:
            raise ValueError

    def add_section(self, section: str) -> None:
        if self.has_section(section):
            raise ValueError
        self.data[section] = {}

    def add_param(self, section: str, key: str, value: str) -> None:

        if not self.has_section(section):
            raise ValueError

        self.data[section][key] = value

    def del_section(self, section: str) -> None:
        del self.data[section]

    def del_param(self, section: str, key: str) -> None:

        if not self.has_section(section):
            raise ValueError
        elif not key in self.data[section]:
            self.add_param(section, key, None)

        del self.data[section][key]

    def dumps(self) -> str:
        list_data = []

        for i, j in self.data.items():
            list_data.append(f'[{i}]')
            for k, l in j.items():
                list_data.append(f'{k}={l}')

        return '\n'.join(list_data)





res = ConfigParser('''
[Section1]
key1=value1
key2=value2
[Section2]
key3=value3
key4=value4
''')




print(res.loads('''
[Section1]
key1=value1
key2=value2
[Section2]
key3=value3
key4=value4
key5=value5_1
'''))

print(res.add_param('Section2', 'key5', 'value5'))
print(res.add_section('Section3'))
print(res.data)
print(res.del_section('Section3'))
print(res.del_param('Section2', 'key6'))

print(res.data)
print(res.dumps())
