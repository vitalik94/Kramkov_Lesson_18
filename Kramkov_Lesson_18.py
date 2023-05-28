#ДЗ на понедельник (Ivanov_Lesson_18.py)
# Создайте класс BankAccount, который представляет банковский счет.
# У класса есть приватные свойства __account_number (номер счета) и __balance (баланс).
# Инициализатор __init__ используется для инициализации номера счета и начального баланса.
#
# Методы get_account_number и get_balance предоставляют доступ
# к приватным свойствам __account_number и __balance соответственно.
# Методы deposit и withdraw позволяют пополнять и снимать деньги со счета,
# при этом проверяя валидность операции (достаточно ли средств, корректно ли введена сумма для снятия).
#
# В основной части кода мы создаем экземпляр класса BankAccount с номером счета "123456789"
# и начальным балансом 1000. Затем мы используем методы для получения номера счета и баланса,
# а также для пополнения и снятия средств. Выводятся результаты операций.

class BankAccount:
    __account_number = 'unknown'
    __balance = None

    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def get_account_number(self):
        print(f'Номер счета {self.__account_number}')

    def get_balance(self):
        print(f'Баланс {self.__balance}')

    def deposit(self, sumMoney):
        if isinstance(sumMoney, (int, float)) and sumMoney > 0:
            self.__balance += sumMoney
        else:
            print(f'Некорректно введена сумма {sumMoney, type(sumMoney)}')

    def withdraw(self, sumMoney):
        if self.__balance > 0 and isinstance(sumMoney, (int, float)) and 0 < sumMoney <= self.__balance:
            self.__balance -= sumMoney
        else:
            print(f'Некорректно введена сумма {sumMoney, type(sumMoney)} или недостаточно средств на счету {self.__balance}')


account = BankAccount('123456789', 1000)
account.get_account_number()
account.get_balance()
account.deposit(100.0)
account.get_balance()
account.withdraw(250)
account.get_balance()
account.deposit('1000')
account.deposit(-1000)
account.withdraw(-1000)
account.withdraw(2000)
account.withdraw(850)
account.get_balance()
account.withdraw(0)
account.withdraw(0.5)
