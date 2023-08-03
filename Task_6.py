# Напишите программу банкомат. Начальная сумма равна нулю. Допустимые действия: пополнить, снять, выйти.
# Сумма пополнения и снятия кратны 50 у.е. Процент за снятие - 1,5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции поплнения или снятия начислятся проценты - 3%. Нельзя снять больше чем на счете.
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной. Любое действие выводит сумму денег.

class Bank:
    sum = 0
    operations_count = 0
    WITHDROW_INTEREST = 0.015
    MIN_WITHDROW_INTEREST_SUM = 30
    MAX_WITHDROW_INTEREST_SUM = 600
    BONUS_PERCENTS = 0.03
    RICH_LIMIT = 5000000
    RICH_TAX = 0.1

    def deposit(self, sum: int):
        self.checkRichness()

        if (sum % 50 != 0):
            return print('Можно вносить только суммы кратные 50')
        
        self.sum += sum

        self.checkOperationsCount()
        self.displaySum()

    def withdrow(self, sum: int):
        self.checkRichness()

        if (sum % 50 != 0):
            return print('Можно снимать только суммы кратные 50')
        
        withdrow_interest = sum * self.WITHDROW_INTEREST

        if (withdrow_interest < self.MIN_WITHDROW_INTEREST_SUM):
            withdrow_interest = self.MIN_WITHDROW_INTEREST_SUM

        if (withdrow_interest > self.MAX_WITHDROW_INTEREST_SUM):
            withdrow_interest = self.MAX_WITHDROW_INTEREST_SUM
        
        if (sum + withdrow_interest > self.sum):
            return print('На вашем счету нет такой суммы')
        
        self.sum -= sum + withdrow_interest

        self.displaySum()

    def checkOperationsCount(self):
        self.operations_count += 1
        if self.operations_count % 3 == 0:
            self.sum *= 1 + self.BONUS_PERCENTS

    def checkRichness(self):
        if (self.sum > self.RICH_LIMIT):
            self.sum -= self.sum * self.RICH_TAX

    def displaySum(self):
        print(f"Сумма на вашем счету: {self.sum}")

    def exit(self):
        print(f"До свидания, приходите еще. Сумма на вашем счету: {self.sum}")
        exit()


bank = Bank()

bank.deposit(50)
bank.deposit(50)
bank.deposit(50)
bank.withdrow(99)
bank.withdrow(100)
bank.deposit(5000000)
bank.withdrow(50)
bank.exit()