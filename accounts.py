class SavingAccount:
    def __init__(self, account_num, int_rate, bal):
        self.__account_num = account_num
        self.__int_rate = int_rate
        self.__bal = bal

    def set_account_num(self, account_num):
        self.__account_num = account_num

    def set_int_rate(self, int_rate):
        self.__int_rate = int_rate

    def set_bal(self, bal):
        self.__bal = bal

    def get_account_num(self):
        return self.__account_num

    def get_int_rate(self):
        return self.__int_rate

    def get_bal(self):
        return self.__bal

    def __str__(self):
        return f'Номер счета: {self.__account_num}\n' \
               f'Процентная ставка: {self.__int_rate}\n' \
               f'Остаток счета: {self.__bal}'


class CD(SavingAccount):
    def __init__(self, account_num, int_rate, bal, mat_date):
        SavingAccount.__init__(self, account_num, int_rate, bal)
        self.__maturity_date = mat_date

    def set_maturity_date(self, mat_date):
        self.__maturity_dete = mat_date

    def get_maturity_date(self):
        return self.__maturity_date

    def __str__(self):
        return f'{SavingAccount.__str__(self)}\n' \
               f'{self.__maturity_dete}'
