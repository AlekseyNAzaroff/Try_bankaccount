class BankAccount: #дебетовый счет
    def __init__(self, bal):
        self.__balance = bal

    def deposit(self, amount):
        self.__balance += amount

    def get_money(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print('Ошибка: средств недостаточно')

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f'Остаток составляет: {self.__balance: ,.2f}$'


