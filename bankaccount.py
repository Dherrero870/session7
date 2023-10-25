class Bankaccount:
    def __init__(self,account_number,current_balance = 0):
        self.account_number = account_number
        self.balance = current_balance
    def get_account_number(self):
        return self.account_number
    def add_funds (self,funds):
        self.balance = self.balance + funds
    def get_balance (self):
        return self.balance
bank_account = Bankaccount("ES9999999999999999999999")
bank_account.add_funds (-800)
bank_account.add_funds (3000)
"""
print (f"La cuenta con IBAN: {bank_account.get_account_number()} tiene {bank_account.get_balance()}€ en su cuenta.")
"""