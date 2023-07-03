# Возьмите задачу о банкомате из семинара 2.
# Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

def start_view():
    print("\nДоступные действия: \n* Пополнить \n* Снять \n* Выйти")
    try:
        action = input("Выберите действие: ").lower()
        return action
    except:
        print("Неверный ввод. Программа будет перезапущена\n")


def deposit():
    print_balance()
    amount = int(input("Введите сумму для пополнения (сумма должна быть кратна 50 у.е.): "))
    if amount % 50 != 0:
        print("Сумма пополнения должна быть кратна 50 у.е.")
    else:
        return amount


def removal():
    print_balance()
    amount = int(input("Введите сумму для снятия (сумма должна быть кратна 50 у.е.): "))
    if amount % 50 != 0:
        print("Сумма снятия должна быть кратна 50 у.е.")
        removal()
    if amount < 30:
        amount += 30
    elif amount > 600:
        amount += 600
    else:
        amount *= globals()['PERCENT_REMOVAL']
    return amount


def print_balance():
    print(f"Ваш баланс равен: {'%.2f' % globals()['balance']} у.е.")


def tax():
    if globals()['balance'] > wealth_tax_threshold:
        globals()['balance'] -= balance * 0.1


PERCENT_REMOVAL = 1.015
PERCENT_CONTRIBUTION = 1.03
balance = 0
transaction_count = 0
wealth_tax_threshold = 5_000_000


def atm():
    start = True
    while start:
        action = start_view()
        try:
            if action == 'пополнить':
                tax()
                globals()['balance'] += deposit()
                globals()['transaction_count'] += 1
                if globals()['transaction_count'] % 3 == 0:
                    globals()['balance'] *= PERCENT_CONTRIBUTION
                print_balance()
            elif action == 'снять':
                tax()
                removal_count = removal()
                if removal_count > globals()['balance']:
                    print('Недостаточно денег на счету для выполнения операции')
                    continue
                globals()['balance'] -= removal()
                globals()['transaction_count'] += 1
                if globals()['transaction_count'] % 3 == 0:
                    globals()['balance'] *= PERCENT_CONTRIBUTION
                print_balance()
            elif action == 'выйти':
                print('Работа прекращена')
                start = False
        except:
            atm()


atm()
