from random import randrange

class Bank_account:

    def __init__(self, accountHolder, iban):
        self.accountHolder = accountHolder
        self.iban = iban
        self.balance = 0
        self.active = False
        self.pin = randrange(1111, 9999, 1)

    def hello(self):
        print(f'Hello {self.accountHolder}')

    def balance_query(self):
        print(f'Account holder: {self.accountHolder}')
        print(f'IBAN: {self.iban}')
        print(f'Balance: {self.balance}')
        print(f'Active account: {self.active}')
        print('------------------------------------------')

    def generate_pin(self):
        pin = self.pin
        print(f'Your PIN is {pin}')

    def account_activation(self, pin):
        self.hello()
        if pin == self.pin:
            print(f'Your account has been activated')
            self.active = True
        else:
            print(f'Wrong PIN. Your account has not been activated')

    def account_supply(self, amount):
        self.hello()
        self.balance += amount
        print(f'You deposited the amount of: {amount} EURO')
        print(f'Now the balance is {self.balance} EURO')

    def card_payment(self, amount):
        self.hello()
        if amount <= self.balance:
            self.balance -= amount
            print(f'You spent the amount of: {amount} EURO')
            print(f'Now the balance is {self.balance} EURO')
        else:
            print(f'Insufficient funds')



