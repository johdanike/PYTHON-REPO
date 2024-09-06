from decimal import Decimal

class Account:

    #constructor
    def __init__(self, name: str, pin: str, balance: Decimal = 0.00):
        self.name = name.upper()
        self.pin = pin
        self.balance = balance


    #method
    def deposit(self, amount):
        if amount < Decimal('0.00'):
            raise ValueError(f'{amount} is not a valid amount.')
        self.balance = self.balance + amount
        ...

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError(f'{amount} is greater than account balance.')
        self.balance = self.balance - amount




#account1.deposit()
