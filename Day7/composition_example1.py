class Salary:
    def __init__(self, pay):
        self.pay = pay

    def get_total(self):
        print(self.pay * 12)


class Employee:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus
        self.obj_salary = Salary(self.pay)

    def annual_salary(self):

        print("Total: ",str(self.obj_salary.get_total() + self.bonus))


emp = Employee(200, 50)
emp.annual_salary()
