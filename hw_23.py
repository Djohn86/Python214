class Student:

    def __init__(self, name):
        self.name = name
        self.teh = self.Notebook()

    def vis(self):
        print(self.name, '=>', end=' ')

    class Notebook:

        def __init__(self):
            self.model = 'HP'
            self.proc = 'i7'
            self.mem = '16'

        def display(self):
            print(f'{self.model}, {self.proc}, {self.mem}')


s1 = Student('Roman')
t1 = s1.teh
s1.vis()
t1.display()
s2 = Student('Vladimir')
t2 = s2.teh
s2.vis()
t2.display()



