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


class current_acct(Bank_Account):
    def __init__(self, Acct_no, Acct_name, over_draft):
        Bank_Account.__init__(self, Acct_no, Acct_name)
        self.over_draft = over_draft

    def display_current_acct_details(self):
        print("The over draft value of account is:", self.over_draft)


class fixed_deposit_acct(Bank_Account):
    def __init__(self, Acct_no, Acct_name, dep_amount):
        Bank_Account.__init__(self, Acct_no, Acct_name)
        self.dep_amount = dep_amount

    def display_deposite_amount(self):
        print("The deposite amount is", self.dep_amount)


a = Bank_Account(605674839, "Udhaya")
a.bank_details()
a.display_sav_acct_details()
a.display_current_acct_details()
a.display_deposite_amount()
