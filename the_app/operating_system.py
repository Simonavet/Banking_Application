from the_app.functions import *

account1 = Bank_account('Jessy Smith', 'EUR12345')
account2 = Bank_account('John Wick', 'EUR67890')

account1.generate_pin()
print(f'Enter your PIN: '), account1.account_activation(pin=int(input()))
print(f'Enter the amount that you want to supply: '), account1.account_supply(amount=int(input()))
account1.card_payment(100)
account1.balance_query()

account2.generate_pin()
print(f'Enter your PIN: '), account2.account_activation(pin=int(input()))
print(f'Enter the amount that you want to supply: '), account2.account_supply(amount=int(input()))
print(f'Enter the amount you want to pay: '), account2.card_payment(amount=int(input()))
account2.balance_query()