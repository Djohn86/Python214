from view import MainInterface
from model import Data


class Controller:
    def __init__(self):
        self.model = Data()
        self.interface = MainInterface()

    def run(self):
        menu = None
        while menu != 'q':
            menu = self.interface.user_answer()
            self.check_menu(menu)

    def check_menu(self, muser):
        if muser == '1':
            add_film = self.interface.add_new_film()
            self.model.add_data(add_film)

        elif muser == '2':
            catalog = self.model.get_catalog()
            self.interface.show_film(catalog)

        elif muser == '3':
            u_film = self.interface.get_film()
            try:
                t_film = self.model.get_t_film(u_film)
            except KeyError:
                self.interface.show_error(u_film)
            else:
                self.interface.view_film(t_film)

        elif muser == '4':
            u_film = self.interface.get_film()
            try:
                r_film = self.model.remove_film(u_film)
            except KeyError:
                self.interface.show_error(u_film)
            else:
                self.interface.view_remove_film(u_film)

        elif muser == 'q':
            self.model.save_data()
        else:
            self.interface.error_enter(muser)

