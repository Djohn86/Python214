import json

data = {}


def load_data(func):
    def wrap(filename):
        try:
            data = json.load(open(filename))
        except FileNotFoundError:
            data = {}
        func(filename)
        print("Файл сохранен")

    return wrap


class CountryCapital:
    def __init__(self, country, capital):
        self.country = country
        self.capital = capital
        data[self.country] = self.capital

    def __str__(self):
        return f"{self.country}: {self.capital}"

    @staticmethod
    def load(filename):
        try:
            data1 = json.load(open(filename))
        except FileNotFoundError:
            data1 = {}
        finally:
            return data1

    @staticmethod
    @load_data
    def add_country(file_name):
        new_country = input('Введите название страны: ')
        new_capital = input('Введите название столицы: ')

        data = CountryCapital.load(file_name)

        data[new_country] = new_capital

        with open(file_name, 'w') as f:
            json.dump(data, f, indent=2)

    @staticmethod
    @load_data
    def delete_country(file_name):
        del_country = input('Введите название страны: ')

        data1 = CountryCapital.load(file_name)

        if del_country in data1:
            del data1[del_country]

            with open(file_name, 'w') as f:
                json.dump(data1, f, indent=2)
        else:
            print("Такой страны в базе нет")

    @staticmethod
    @load_data
    def search_data(file_name):

        country = input('Введите название страны: ')
        data1 = CountryCapital.load(file_name)

        if country in data1:
            print(f"Страна {country} столица {data1[country]} есть в словаре")
        else:
            print(f"Страны {country} нет в словаре")

    @staticmethod
    @load_data
    def edit_data(file_name):
        country = input('Введите страну для корректировки: ')
        new_capital = input('Введите новое название столицы: ')


        data1 = CountryCapital.load(file_name)

        if country in data1:
            data1[country] = new_capital
            with open(file_name, 'w') as f:
                json.dump(data1, f, indent=2)
        else:
            print("Такой страны в базе нет")

    @staticmethod
    def load_from_file(file_name):
        with open(file_name) as f:
            print(json.load(f))


file = 'list_capital.json'
index = ""
while True:
    index = input('Выбор действия:\n1 - добавление данных\n'
                  '2 - удаление данных\n3 - поиск данных\n'
                  '4 - редактирование данных\n5 - просмотр данных\n'
                  '6 - завершение работы\nВвод: ')
    if index == "1":
        CountryCapital.add_country(file)
    elif index == "2":
        CountryCapital.delete_country(file)
    elif index == "3":
        CountryCapital.search_data(file)
    elif index == "4":
        CountryCapital.edit_data(file)
    elif index == "5":
        CountryCapital.load_from_file(file)
    elif index == "6":
        break
    else:
        print("Введен некорректный номер")