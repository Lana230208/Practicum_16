class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Guest(Person):
    def __init__(self, name, surname, city, status):
        super().__init__(name, surname)
        self.city = city
        self.status = status

    def print_info(self):
        print('{} {}, г.{}, статус "{}"'.format(self.name, self.surname, self.city, self.status))


g = Guest("Иван", "Петров", "Москва", "Наставник")
g.print_info()
