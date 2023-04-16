def decor(title):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f' {title} '.center(50, '='))
            output = func(*args, **kwargs)
            print('*' * 50)
            return output
        return wrap
    return wrapper


class MainInterface:
    @decor(' Ввод пользовательских данных ')
    def user_answer(self):
        print('Действия с фильмами:\n'
              '1 - добавление фильма\n'
              '2 - каталог фильмов\n'
              '3 - просмотр определенного фильма\n'
              '4 - удаление фильма\n'
              'q = выход из программы\n')
        var_user = input('Выберите действие: ')
        return var_user

    @decor(' Введите информацию о фильме ')
    def add_new_film(self):
        dir_film = {
            'название фильма': None,
            "жанр": None,
            "режиссёр": None,
            "год выпуска": None,
            "длительность": None,
            "студия": None,
            "актеры": None
        }
        for key in dir_film:
            dir_film[key] = input(f'Введите {key}: ')
        return dir_film

    @decor(' Каталог фильмов ')
    def show_film(self, films):
        for i, film in enumerate(films, start=1):
            print(f'{i}.{film}')

    @decor('Поиск фильма')
    def get_film(self):
        single_film = input('Введите название фильма: ')
        return single_film

    @decor("Просмотр фильма")
    def view_film(self, data_film):
        for key in data_film:
            print(f'{key}  - {data_film[key]}')

    @decor(" Ошибка ")
    def show_error(self, er_film):
        print(f'Фильма с названием {er_film} нет в каталоге')

    @decor(' Удаление статьи ')
    def view_remove_film(self, title):
        print(f'Фильм с названием {title} удален')

    @decor(' Ошибка выбора ')
    def error_enter(self, ent_user):
        print(f'{ent_user} нет такого варианта действий')




