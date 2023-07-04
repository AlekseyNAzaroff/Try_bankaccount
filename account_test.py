import bankaccount


def main():
    start_bal = float(input('Введите свой начальный остаток: '))

    saving = bankaccount.BankAccount(start_bal)

    pay = float(input('Сколько внести на счет? '))
    print('Вношу эту сумму на счет')
    saving.deposit(pay)

    print(saving)

    cash = float(input('Какую сумму вы хотите снять? '))
    print('Снимаю эту сумму со счета')
    saving.get_money(cash)
    print(saving)


if __name__ == '__main__':
    main()
