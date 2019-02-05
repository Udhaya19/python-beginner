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


class loan_details(saving_acct, current_acct):
    def __init__(self, Acct_no, Acct_name, interest, over_draft, emi):
        saving_acct.__init__(self, Acct_no, Acct_name, interest)
        current_acct.__init__(self, Acct_no, Acct_name, over_draft)
        self.emi = emi

    def display_loan_details(self):
        print("The EMI details:", self.emi)

print("HYbrid inheritance")
l = loan_details(60567483, "udhaya", 4, 7, 1500)
l.bank_details()
l.display_sav_acct_details()
l.display_current_acct_details()
l.display_loan_details()
