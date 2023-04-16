import pickle
import os.path


class Catalog:
    def __init__(self, tittle, genre, producer, age, duration, studio, actors):
        self.tittle = tittle
        self.genre = genre
        self.producer = producer
        self.age = age
        self.duration = duration
        self.studio = studio
        self.actors = actors

    def __str__(self):
        return f'{self.tittle} ({self.genre})'


class Data:
    def __init__(self):
        self.save_fail = 'film_catalog.txt'
        self.database = self.load_cf()

    def add_data(self, films):
        k = Catalog(*films.values())
        self.database[k.tittle] = k

    def get_catalog(self):
        return self.database.values()

    def get_t_film(self, enter_user):
        token_film = self.database[enter_user]
        dir_film = {
            'название фильма': token_film.tittle,
            "жанр": token_film.genre,
            "режиссёр": token_film.producer,
            "год выпуска": token_film.age,
            "длительность": token_film.duration,
            "студия": token_film.studio,
            "актеры": token_film.actors
        }

        return dir_film

    def remove_film(self, r_user):
        return self.database.pop(r_user)

    def load_cf(self):
        if os.path.exists(self.save_fail):
            with open(self.save_fail, 'rb') as f:
                return pickle.load(f)
        else:
            return  dict()

    def save_data(self):
        with open(self.save_fail, 'wb') as f:
            pickle.dump(self.database, f)


