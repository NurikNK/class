"""
Создайте класс BankAccount, который представляет банковский счет, c атрибутами экземпляра:
accountNumber (числовой тип), name (имя владельца счета строкового типа), balance.
Создайте конструктор с параметрами: accountNumber, name, balance.
Создайте метод Deposit(), который управляет действиями по пополнению счета.
Создайте метод Withdrawal(), который управляет действиями по снятию средств.
Создайте метод bankFees() для применения банковской комиссии в размере 5% от баланса счета.
Создайте метод display() для отображения деталей счета.
Приведите примеры использования.
"""


class BankAccount:

    def __init__(self, account_number, name):
        self.account_number = account_number
        self.name = name
        self.balance = 0
        self._status = True

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        if status == 0:
            self._status = False
        else:
            self._status = True

    def Deposit(self, money):
        self.balance += money
        return f'Now, your balance is ${self.balance}.'

    def bank_fees(self, money):
        return money * 0.05

    def Withdrawal(self, money):
        self.balance -= money + self.bank_fees(money)
        return f'Now, your balance is ${self.balance}.'

    def display(self):
        return self.balance


card1 = BankAccount(213124, 'kfc')
card1.status = None
print(card1.status)



"""
Создайте класс WashingMachine, конструктор которого имеет
параметры powder (порошок), conditioner (ополаскиватель). По
умолчанию значения количества порошка и ополаскивателя в
машинке будут равны: powder = 1000 (гр), conditioner = 1000 (мл).
Добавьте метод wash_clothes, который будет принимать
параметры powder, conditioner. Пусть эти данные вводит
пользователь. В самом начале проверьте, хватит ли вам
количества ингредиентов. Если его хватит для стирки, то вычтите
использованное количество ингредиентов, но не напрямую, а с
помощью приватных методов __subtract_ powder, __subtract_
conditioner. Помимо этого пусть метод wash_clothes распечатает
на экран “Процесс стирки завершен!“. Если же ингредиентов не
хватит, то распечатайте, какого именно ингредиента
(ингредиентов) не хватает и сколько нужно пополнить запасов.
То есть, должны вывести сообщение вида “Пополните запасы
порошка на 500 гр! Пополните запасы ополаскивателя на 100
мл!“."""

class WashingMachine:


    def __init__(self, powder=1000, conditioner=1000):
        self.powder = powder
        self.conditioner = conditioner

    def __subtract_powder(self, powder):
        self.powder -= powder

    def __subtract_conditioner(self, conditioner):
        self.conditioner -= conditioner

    def wash_clothes(self):
        powder = int(input("Введите расходуемое кол-во порошка в гр:"))
        conditioner=int(input("Введите расходуемое кол-во ополаскивателя в мл:"))
        if self.powder < powder and self.conditioner < conditioner:
            return f'Процесс стрики завершен!\n' \
                   f'Осталось {self.__subtract_conditioner(conditioner)}\n'\
                   f'Осталось и {self.__subtract_powder(powder)}'


            self.__subtract_powder(powder)
            print("Остаток порошка в гр", self.powder)
            self.__subtract_conditioner(conditioner)
            print("Остаток ополоскивателя в мл", self.conditioner)
            return






p = int(input())
c = int(input())
a = WashingMachine(p, c)
