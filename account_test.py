import bankaccount


def main():
    start_bal = float(input('Введите свой начальный остаток: '))

    saving = bankaccount.BankAccount(start_bal)

    pay = float(input('Сколько внести на счет? '))
    print(f'Вношу на счет {pay:,.2f}$')
    saving.deposit(pay)
    print(f'Сейчас на вашем счете {saving.get_balance():,.2f}$')

    cash = float(input('Какую сумму вы хотите снять? '))
    saving.get_money(cash)
    print(f'Остаток на вашем счете {saving.get_balance():,.2f}$')


if __name__ == '__main__':
    main()
