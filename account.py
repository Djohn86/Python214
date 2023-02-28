class Account:
    rate_usd = 0.013
    rate_euro = 0.011
    suffix = 'RUB'
    suffix_usd = 'USD'
    suffix_eur = "EUR"
    k = 0.03

    def __init__(self, num, surname, percent, value=0):
        self.num = num
        self.surname = surname
        self.percent = percent
        self.value = value
        print(f'Счет #{self.num} принадлежащий {self.surname} был открыт')
        print('*' * 50)

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_euro = rate

    @staticmethod
    def convert(value, rate):
        return value * rate

    def convert_to_usd(self):
        usd_val = Account.convert(self.value, Account.rate_usd)
        print(f'Состояние счета: {usd_val} {Account.suffix_usd}')

    def convert_to_eur(self):
        eur_val = Account.convert(self.value, Account.rate_euro)
        print(f'Состояние счета: {eur_val} {Account.suffix_eur}')

    def print_balance(self):
        print(f'Текущий баланс {self.value} {Account.suffix}')

    def edit_owner(self, surname):
        self.surname = surname

    def add_percent(self):
        self.value += self.value * self.percent
        print('Проценты начислены!')
        self.print_balance()

    def withdraw_money(self, val):
        if (val + 100) > self.value or val + val * Account.k > self.value:
            print(f'К сожалению у вас нет {val} {Account.suffix} c учетом комиссии')
        else:
            if val <= 100:
                self.value -= (val + 100)
                print(f'{val} {Account.suffix} было успешно снято')
                print(f'Комиссия: 100 {Account.suffix}')
            else:
                self.value -= (val + val * Account.k)
                print(f'{val} {Account.suffix} было успешно снято')
                print(f'Комиссия: {val * Account.k}  {Account.suffix}')
        self.print_balance()

    def add_money(self, val):
        self.value += val
        print(f'{val}{Account.suffix} было успешно добавлено')
        self.print_balance()

    def print_info(self):
        print('Информация о счете')
        print('-' * 20)
        print(f'#{self.num}')
        print(f'Владелец: {self.surname}')
        self.print_balance()
        print(f'Проценты: {self.percent}')
        print(f'Комиссия при снятии: {Account.k}%\nНо не менее 100 {Account.suffix}')
        print('-' * 20)

    def __del__(self):
        print('=' * 80)
        print(f"Счет #{self.num} принадлежащий {self.surname} был закрыт")


acc = Account('123456', 'Долгих', 0.03, 1000)
acc.print_info()
acc.convert_to_usd()
acc.convert_to_eur()
acc.set_usd_rate(2)
acc.convert_to_usd()
acc.set_eur_rate(0.4)
acc.convert_to_eur()
acc.edit_owner("Дюма")
acc.print_info()
print()
acc.add_percent()
print()
acc.withdraw_money(100)
print()
acc.withdraw_money(10000)
print()
acc.add_money(4000)
print()
acc.withdraw_money(2750)

