class Auto:

    def __init__(self, model, year, factory, power, color, cost):
        self.model = model
        self.year = year
        self.factory = factory
        self.power = power
        self.color = color
        self.cost = cost

    def print_info(self):
        print('  Характеристики автомобиля  '.center(50, '*'))
        print(f"Название модели: {self.model}\nГод выпуска: {self.year}\nпроизводитель: {self.factory}\n"
              f"Мощность двигателя: {self.power}\nЦвет машины: {self.color}\nЦена: {self.cost} ")
        print('='*50)

    def set_model(self, data1):
        self.model = data1

    def get_model(self):
        return self.model

    def set_year(self, data1):
        self.year = data1

    def get_year(self):
        return self.year

    def set_factory(self, data1):
        self.factory = data1

    def get_factory(self):
        return self.factory

    def set_power(self, data1):
        self.power = data1

    def get_power(self):
        return self.power

    def set_color(self, data1):
        self.color = data1

    def get_color(self):
        return self.color

    def set_cost(self, data1):
        self.cost = data1

    def get_cost(self):
        return self.cost


a1 = Auto('X7 M50i', '2021', 'BMW', '530 л. с.', 'white', '10790000')
a1.print_info()
a1.set_model('GTS Sport')
a1.set_year('2022')
a1.set_factory('Porsche')
a1.set_power('480 л. с.')
a1.set_color('silver')
a1.set_cost('11000000')
a1.print_info()
print(a1.get_model())
print(a1.get_year())
print(a1.get_factory())
print(a1.get_power())
print(a1.get_color())
print(a1.get_cost())
