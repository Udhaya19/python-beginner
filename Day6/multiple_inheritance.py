class Saving_Acct():
    def __init__(self, Acct_no, Acct_name, interest):
        self.Acct_no=Acct_no
        self.Acct_name=Acct_name
        self.interest = interest

    def display_sav_acct_details(self):
        print("The interest of account is:", self.interest)


class Current_Acct():
    def __init__(self, Acct_no, Acct_name, over_draft):
        self.Acct_no=Acct_no
        self.Acct_name=Acct_name
        self.over_draft = over_draft

    def display_current_acct_details(self):
        print("The over draft value of account is:", self.over_draft)


class Loan_Details(Saving_Acct, Current_Acct):
    def __init__(self, Acct_no, Acct_name, interest, over_draft, emi):
        Saving_Acct.__init__(self, Acct_no, Acct_name, interest)
        Current_Acct.__init__(self, Acct_no, Acct_name, over_draft)
        self.emi = emi

    def display_loan_details(self):
        print("The EMI details:", self.emi)

l=Loan_Details(605874485, "udhaya",4,6,150 )
l.display_sav_acct_details()
l.display_current_acct_details()