from bankaccount import Bankaccount
class Savingsaccount(Bankaccount):
    def __init__(self, account_number, current_balance = 0):
        super().__init__(account_number, current_balance)
        self.interest_rate = 5
    def interests_generated(self,months):
        interest = self.balance * self.interest_rate / 100 *months
        return interest