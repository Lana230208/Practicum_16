class Client:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.balance = 0
        # когда создаём клиента, у него нулевой балланс

    def set_balance(self, value):
        self.balance = value

    def print_info(self):
        print('Клиент "{} {}". Баланс: {} руб'.format(self.name, self.surname, self.balance))


c = Client("Иван", "Петров")
c.set_balance(50)
c.print_info()
