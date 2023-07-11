import accounts


def main():
    print('Введите данные о сберегательном счете: ')
    acct_num = input('Номер счета: ')
    int_rate = float(input('Процентная ставка: '))
    balance = float(input('Остаток: '))

    saving = accounts.SavingAccount(acct_num, int_rate, balance)

    print('Введите данные о счете CD')
    acct_num = input('Номер счета: ')
    int_rate = float(input('Процентная ставка: '))
    balance = float(input('Остаток: '))
    maturity_input = input('Дата погашения: ')

    cd = accounts.CD(acct_num, int_rate, balance, maturity_input)

    print('Вот введенные вами данные:')
    print('Сберегательный счет:')
    print(f'Номер счета: {saving.get_account_num()}')
    print(f'Процентная ставка: {saving.get_int_rate()}')
    print(f'Остаток: {saving.get_bal()}')
    print()
    print('Счет депозитного сертификата (CD):')
    print(f'Номер счета: {cd.get_account_num()}')
    print(f'Процентная ставка: {cd.get_int_rate()}')
    print(f'Остаток: {cd.get_bal()}')
    print(f'Дата погашения: {cd.get_maturity_date()}')
    print()

if __name__ == '__main__':
    main()