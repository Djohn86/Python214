class UserInterface:
    def wait_user_answer(self):
        print(" Ввод пользовательских данных ".center(50, '='))
        print('Действия со статьями:\n ')
        print('1 - создание статьи\n'
              '2- просмотр статей\n'
              '3 - просмотр определенной статьи\n'
              '4 - удаление статьи\n'
              'q - выход из программы\n ')
        user_name = input('Выберите вариант действия: ')
        print('=' * 50)
        return user_name

    def add_user_article(self):
        dict_article = {
            'название': None,
            "автор": None,
            "количество страниц": None,
            "описание": None
        }
        print(' Создание статьи '.center(50, '='))
        for key in dict_article:
            dict_article[key] = input(f'Введите {key} статьи: ')
        print('=' * 50)
        return dict_article

    def show_all_articles(self, articles):
        print(' Список статей '.center(50, '='))
        for ind, article in enumerate(articles, start=1):
            print(f'{ind}. {article}')
        print('=' * 50)

