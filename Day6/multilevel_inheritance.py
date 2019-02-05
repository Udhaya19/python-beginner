class Bank_Account:
    def __init__(self, Acct_no, Acct_name):
        self.Acct_no = Acct_no
        self.Acct_name = Acct_name

    def bank_details(self):
        print("The user account number:", self.Acct_no)
        print("The user name:", self.Acct_name)


class saving_acct(Bank_Account):
    def __init__(self, Acct_no, Acct_name, interest):
        Bank_Account.__init__(self, Acct_no, Acct_name)
        self.interest = interest

    def display_sav_acct_details(self):
        print("The interest of account is:", self.interest)


class amount_withdraw(saving_acct):
    def __init__(self, Acct_no, Acct_name, interest, amount):
        saving_acct.__init__(self, Acct_no, Acct_name, interest)
        self.amount = amount

    def display_withdraw_amount(self):
        print("The withdraw amount is:", self.amount)
print("multilevel_inheritance")
w=amount_withdraw(60758473,"udhaya",4,500)
w.display_withdraw_amount()

print("------------------------------")
print("single_inheritance")
s=saving_acct(60567483,"keerthi",5)
s.display_sav_acct_details()