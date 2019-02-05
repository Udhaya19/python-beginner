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


print("single_inheritance")
s = saving_acct(60567483, "keerthi", 5)
s.bank_details()
s.display_sav_acct_details()
