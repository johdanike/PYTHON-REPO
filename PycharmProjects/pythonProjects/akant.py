from bankfunc import Account


account1 = Account('Chidinma', "0000")
account2 = Account('Stanley', "1111")

print(account1.name)
print(account1.balance)
account1.deposit(10000)
print(account1.balance)
account1.withdraw(1000)
print(account1.balance)
